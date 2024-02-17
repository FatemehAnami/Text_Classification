from Text_Classification.logging import logger
from Text_Classification.pipeline.Step01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"---------- Stage {STAGE_NAME} started ----------")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"---------- Stage {STAGE_NAME} Completed Successfully.---------")
except Exception as e:
    logger.exception(e)
    raise e
