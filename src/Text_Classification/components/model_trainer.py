from Text_Classification.logging import logger
from transformers import Trainer, TrainingArguments
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers import EarlyStoppingCallback
from Text_Classification.entity import ModelTrainerConfig
from datasets import load_from_disk 
import torch
import os 

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def delete_ckpts(self):
        folders_list = os.listdir(self.config.root_dir)
        try:
            for folder in folders_list: 
                if folder.startswith("check") :
                    for file in os.path.join(self.config.root_dir , folder):
                        os.remove(os.path.join(self.config.root_dir , folder, file))
                    os.rmdir(os.path.join(self.config.root_dir , folder))
                else:
                    continue
        except Exception as e :
            logger.info(f"Some Error occure during deleting checkpoints: {str(e)}")        


    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model = AutoModelForSequenceClassification.from_pretrained(self.config.model_ckpt, 
                                                                   num_labels=self.config.num_labels)

        train_dataset = load_from_disk(os.path.join(self.config.data_path, "train"))
        val_dataset = load_from_disk(os.path.join(self.config.data_path, "val"))

        training_args = TrainingArguments(
            output_dir=self.config.root_dir,      
            num_train_epochs=self.config.num_train_epochs,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_eval_batch_size, 
            warmup_steps=self.config.warmup_steps,
            weight_decay=self.config.weight_decay,
            logging_dir=self.config.log_dir,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            load_best_model_at_end=self.config.load_best_model_at_end,
            save_steps=self.config.save_steps,
            seed=self.config.seed,
        )
        trainer = Trainer(
        model=model,
        tokenizer=tokenizer,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        callbacks = [EarlyStoppingCallback(3, 0.001)],
        )

        trainer.train()
    
        model.save_pretrained(os.path.join(self.config.root_dir, "model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))

        self.delete_ckpts()