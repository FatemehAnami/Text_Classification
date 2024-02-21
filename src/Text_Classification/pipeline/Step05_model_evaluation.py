from Text_Classification.logging import logger
from Text_Classification.config.configuration import ConfigurationManager
from Text_Classification.components.model_evaluation import ModelEvaluation


class ModelEvaluationTrainingPipeline():
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()



