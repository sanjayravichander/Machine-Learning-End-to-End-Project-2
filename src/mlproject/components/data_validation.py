from src.mlproject.logging import logger
from src.mlproject.entity.config_entity import DataValidationConfig
from pathlib import Path
import pandas as pd


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            # Read data from CSV
            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = set(data.columns)
            all_schema = set(self.config.all_schema.keys())

            # Create directory if it doesn't exist
            Path(self.config.root_dir).mkdir(parents=True, exist_ok=True)

            # Validate columns
            missing_columns = all_schema - all_columns
            extra_columns = all_columns - all_schema
            
            validation_status = len(missing_columns) == 0 and len(extra_columns) == 0

            # Write the validation status to the file
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation Status: {'Success' if validation_status else 'Failure'}\n")
                if missing_columns:
                    f.write(f"Missing Columns: {missing_columns}\n")
                if extra_columns:
                    f.write(f"Extra Columns: {extra_columns}\n")

            # Log the validation result
            logger.info(f"Validation status: {'Success' if validation_status else 'Failure'}")
            if missing_columns:
                logger.info(f"Missing Columns: {missing_columns}")
            if extra_columns:
                logger.info(f"Extra Columns: {extra_columns}")

            return validation_status

        except Exception as e:
            logger.error(f"An error occurred during data validation: {e}")
            raise e
