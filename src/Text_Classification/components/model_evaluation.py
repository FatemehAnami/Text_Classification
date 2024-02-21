from transformers import AutoModelForSequenceClassification, AutoTokenizer
from datasets import load_from_disk 
from transformers import pipeline
from transformers.pipelines.pt_utils import KeyDataset
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import torch
import pandas as pd
from Text_Classification.logging import logger
from tqdm import tqdm
from Text_Classification.entity import ModelEvaluationConfig

class ModelEvaluation:

    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate(self, max_length = 256):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        test_dataset = load_from_disk(self.config.data_path)
        pipe = pipeline("sentiment-analysis", 
                        model = AutoModelForSequenceClassification.from_pretrained(self.config.model_path).to(device), 
                        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path))
       
        # predict labels of test dataset
        y_preds = []
        labels = {"negative": 0, "neutral": 1 , "positive" : 2}
        logger.info("Start predicting on test dataset.....")
        output = pipe(KeyDataset(test_dataset, "text"), batch_size=8, truncation=True, max_length = max_length) 
        for out in output:
           y_preds.append(labels[out['label']])
        logger.info("Prediction on test dataset feinished successfully.")
        # calculate metrices
        #print(y_preds)
        #print(test_dataset['labels'])
        acc = accuracy_score(test_dataset['labels'], y_preds)
        pre = precision_score(test_dataset['labels'], y_preds, average= 'weighted')
        recall = recall_score(test_dataset['labels'], y_preds, average= 'weighted')
        f1 = f1_score(test_dataset['labels'], y_preds, average= 'weighted')
        logger.info("Evaluation metrics calculated successfully.")

        # create output of evaluation
        results = {"accuracy" : acc, "Precision" : pre, "Recall": recall, "F1_Score": f1}
        df = pd.DataFrame(results, index = ['Twitter'])
        df.to_csv(self.config.metrics_file_name, index = False)
