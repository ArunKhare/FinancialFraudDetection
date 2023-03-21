from src.frauddetection.entity.config_entity import DataIngestionConfig
from src.exception import FraudException
from src.logger import logging
import shutil
import sys, os
import pandas as pd
import tarfile
from src.frauddetection.entity.artifact_entity import DataIngestionArtifact
from sklearn.model_selection import train_test_split
from zipfile import ZipFile

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info("{=*20} Data ingestion start{=*20}")
            self.data_ingestion_config = data_ingestion_config
            
        except Exception as e:
            raise FraudException(e, sys) from e

  
    def download_payment_data(self,) -> str:
        try:
            #extraction remote url to download dataset
            download_dataset_link = self.data_ingestion_config.dataset_download_url

            #folder location to download file
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir
            
            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)
            
            os.makedirs(tgz_download_dir,exist_ok=True)

            base_filename = "online-payments-fraud-detection-dataset.zip"

            tgz_file_path = os.path.join(tgz_download_dir, base_filename)

            logging.info(f"Downloading file from :[{download_dataset_link}] into :[{tgz_file_path}]")
            if not os.path.exists(tgz_file_path):
                os.system('cmd /c "kaggle datasets download -d rupakroy/online-payments-fraud-detection-dataset"')
                shutil.copy("online-payments-fraud-detection-dataset.zip",tgz_download_dir)
                logging.info(f"Download file from :[{download_dataset_link}] into [{tgz_file_path}]")
            else:
                logging.info(f"dataset file already exist")
            logging.info(f"File :[{tgz_file_path}] has been downloaded successfully.")
            return tgz_file_path

        except Exception as e:
            raise FraudException(e,sys) from e

    def extract_tgz_file(self,tgz_file_path:str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir,exist_ok=True)

            logging.info(f"Extracting tgz file: [{tgz_file_path}] into dir: [{raw_data_dir}]")
            # with tarfile.open(tgz_file_path) as payments_tgz_file_obj:
            #     payments_tgz_file_obj.extractall(path=raw_data_dir)
            with ZipFile(tgz_file_path,'r') as zobj:
                zobj.extractall(path=raw_data_dir)
            
            logging.info(f"Extraction completed")

        except Exception as e:
            raise FraudException(e,sys) from e
    
    def split_data_as_train_test(self) -> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            file_name = os.listdir(raw_data_dir)[0]

            payments_filepath = os.path.join(raw_data_dir,file_name)


            logging.info(f"Reading csv file: [{payments_filepath}]")
            payment_data_frame = pd.read_csv(payments_filepath)

            training_set, test_set = train_test_split(payment_data_frame, test_size=0.33, random_state=42)

        
            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,
                                            file_name)

            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,
                                        file_name)
            
            if train_file_path is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
                logging.info(f"Exporting training datset to file: [{train_file_path}]")
                training_set.to_csv(train_file_path,index=False)

            if test_file_path is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok= True)
                logging.info(f"Exporting test dataset to file: [{test_file_path}]")
                test_set.to_csv(test_file_path,index=False)
            

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                test_file_path=test_file_path,
                                is_ingested=True,
                                message=f"Data ingestion completed successfully."
                                )
            logging.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact

        except Exception as e:
            raise FraudException(e,sys) from e

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            tgz_file_path =  self.download_payment_data()
            self.extract_tgz_file(tgz_file_path=tgz_file_path)
            return self.split_data_as_train_test()
        except Exception as e:
            raise FraudException(e,sys) from e
    
    def __del__(self):
        logging.info(f"{'>>'*20}Data Ingestion log completed.{'<<'*20} \n\n")