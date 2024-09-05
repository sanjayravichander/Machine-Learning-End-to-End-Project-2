from mlproject.logging import logger
from src.mlproject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e
#logger.info("Welcome to our custom Logger")