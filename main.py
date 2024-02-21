from Text_Classification.logging import logger
from Text_Classification.pipeline.Step01_data_ingestion import DataIngestionTrainingPipeline
from Text_Classification.pipeline.Step02_data_validation import DataValidationTrainingPipeline
from Text_Classification.pipeline.Step03_data_transformation import DataTransformationTrainingPipeline
from Text_Classification.pipeline.Step04_model_trainer import ModelTrainerTrainingPipeline
from Text_Classification.pipeline.Step05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"---------- Stage {STAGE_NAME} started ----------")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"---------- Stage {STAGE_NAME} Completed Successfully.---------")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation"
try:
    logger.info(f"---------- Stage {STAGE_NAME} started ----------")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"---------- Stage {STAGE_NAME} Completed Successfully.---------")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation"
try:
    logger.info(f"---------- Stage {STAGE_NAME} started ----------")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"---------- Stage {STAGE_NAME} Completed Successfully.---------")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer"
try:
    logger.info(f"---------- Stage {STAGE_NAME} started ----------")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f"---------- Stage {STAGE_NAME} Completed Successfully.---------")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation"
try:
    logger.info(f"---------- Stage {STAGE_NAME} started ----------")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f"---------- Stage {STAGE_NAME} Completed Successfully.---------")
except Exception as e:
    logger.exception(e)
    raise e