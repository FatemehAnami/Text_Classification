from Text_Classification.logging import logger
from Text_Classification.config.configuration import ConfigurationManager
from Text_Classification.components.data_transformation import DataTransformation


class DataTransformationTrainingPipeline():
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.load_transform_data()



