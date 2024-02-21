from Text_Classification.logging import logger
from Text_Classification.config.configuration import ConfigurationManager
from Text_Classification.components.model_trainer import ModelTrainer


class ModelTrainerTrainingPipeline():
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        #model_trainer.train()



