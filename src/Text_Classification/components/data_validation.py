import os
from Text_Classification.logging import logger
from Text_Classification.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config = DataValidationConfig) -> None:
        self.config = config
        
    def validate_all_files_exist(self) -> bool :
        try:
            validation_status = None
            all_files = os.listdir(os.path.join("artifacts" , "data_ingestion", "Data"))
            
            for file in all_files :
                if file.split('.')[0] not in self.config.ALL_REQUIRED_FILES :
                    validation_status = False
                else :
                    validation_status = True
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validatioon Status is: {validation_status}")
                logger.info(f"The validation status is: {validation_status} for file: {file}")
            return validation_status
        except Exception as e :
            logger.info(f"Some Error occure during running function 'validate_all_files_exist that is: {str(e)}")
            raise e