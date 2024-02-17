import os
import urllib.request as request
import zipfile
from pathlib import Path
from Text_Classification.logging import logger
from Text_Classification.utils.common import get_size, create_directories
from Text_Classification.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config = DataIngestionConfig) -> None:
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file                
            )
            logger.info(f"{filename} downloaded! with following info:\n{headers}")
        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file))}")
            
    
    def extract_zip_file(self) -> None:
        """
        Extract the zip file into given folder 
        This function returns None
        """
        try:
            
            unzip_path = self.config.unzip_dir
            create_directories([unzip_path])
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"data unzip successfully in {self.config.unzip_dir}.")
        except Exception as e :
            logger.info(f"Some error occure during unzipping data, error is {str(e)}.")
