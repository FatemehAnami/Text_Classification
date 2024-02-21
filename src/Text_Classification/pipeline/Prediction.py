from Text_Classification.logging import logger
from Text_Classification.config.configuration import ConfigurationManager
from Text_Classification.components.model_evaluation import ModelEvaluation
from transformers import pipeline
from transformers import AutoTokenizer

class PredictionPipeline:
    def __init__(self) -> None:
        self.config = ConfigurationManager().get_model_evaluation_config()

    def prediction(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"max_length" : 256}
        
        pipe = pipeline("sentiment-analysis", 
                       model = self.config.model_path, 
                       tokenizer = tokenizer)

        output = pipe(text, **gen_kwargs)[0]['label']
        return output
