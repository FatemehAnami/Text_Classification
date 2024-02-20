import os
from Text_Classification.logging import logger
from transformers import AutoTokenizer
import datasets
import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from Text_Classification.entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config = DataTransformationConfig) -> None:
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
    
    def tokenize_and_encode_data(self, data, max_len: int = 256):
        
        label_dict = {'negative': 0 , 'neutral': 1, 'positive': 2}
        # Tokenize the text
        tokenized_inputs = self.tokenizer(data['text'],
                                    truncation=True,
                                    padding='max_length',
                                    max_length=max_len,
                                    return_tensors='pt')

        # Convert labels to integers and create a tensor
        labels = torch.tensor([label_dict[label] for label in data["labels"]])
        tokenized_inputs['labels'] = labels
        return tokenized_inputs

    def create_dataset(self, dataset):
        dataset_dict = {}
        dataset_dict['text'] = dataset['text']
        dataset_dict['labels'] = dataset['sentiment']
        return datasets.Dataset.from_dict(dataset_dict)
    
    def load_transform_data(self):
        # Load train and test data
        train = pd.read_csv(os.path.join(self.config.data_path, "train.csv"), 
                            encoding="ISO-8859-1", usecols=["text", 'sentiment'])
        logger.info("The train data loaded from csv files")
        test  = pd.read_csv(os.path.join(self.config.data_path,"test.csv"), 
                            encoding="ISO-8859-1", usecols=["text", 'sentiment'])
        logger.info("The test data loaded from csv files")
        
        # drop null value 
        train.dropna(inplace= True)
        test.dropna(inplace= True)
        logger.info("The null valuse drop from datasets")
        
        # split train data to train and validation 
        train , val = train_test_split(train , test_size = 0.2, random_state = 42)
        
        
        # transform pandas dataframe to torch dataset
        train_dataset = self.create_dataset(train)
        val_dataset = self.create_dataset(val)
        test_dataset = self.create_dataset(test)

        # convert data to dctionary 
        train_dataset = train_dataset.map(self.tokenize_and_encode_data, batched=True)
        logger.info("The Train data load and transformed successfully.")
        val_dataset = val_dataset.map(self.tokenize_and_encode_data, batched=True)
        logger.info("The Validation data load and transformed successfully.")
        test_dataset = test_dataset.map(self.tokenize_and_encode_data, batched=True)
        logger.info("The Test data load and transformed successfully.")

        # save data
        train_dataset.save_to_disk(os.path.join(self.config.root_dir,"train"))
        val_dataset.save_to_disk(os.path.join(self.config.root_dir,"val"))
        test_dataset.save_to_disk(os.path.join(self.config.root_dir,"test"))
