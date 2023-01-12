from Insurance.logger import logging
from Insurance.exception import InsuranceException
from Insurance.utils import get_collection_as_dataframe
import sys, os
from Insurance.entity.config_entity import DataIngestionConfig
from Insurance.entity import config_entity
from Insurance.components.data_ingestion import DataIngestion
from Insurance.components.data_validation import DataValidation

from Insurance.components.data_transformation import DataTransformation

#def test_logger_and_expection():
   # try:
       # logging.info("Starting the test_logger_and_exception")
        #result = 3/0
       # print(result)
       # logging.info("Stoping the test_logger_and_exception")
    #except Exception as e:
      #  logging.debug(str(e))
       # raise InsuranceException(e, sys)

if __name__=="__main__":
     try:
          #start_training_pipeline()
          #test_logger_and_expection()
       # get_collection_as_dataframe(database_name ="INSURANCE", collection_name = 'INSURANCE_PROJECT')
       training_pipeline_config = config_entity.TrainingPipelineConfig()
       
      #data ingestion
       data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
       print(data_ingestion_config.to_dict())
       data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
       data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
       
       # Data Validation
       data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
       data_validation = DataValidation(data_validation_config=data_validation_config,
                         data_ingestion_artifact=data_ingestion_artifact)
        
       data_validation_artifact = data_validation.initiate_data_validation()

      #Data Transformation

       data_transformation_config = config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)
       data_transformation = DataTransformation(data_transformation_config=data_transformation_config, 
       data_ingestion_artifact=data_ingestion_artifact)
       data_transformation_artifact = data_transformation.initiate_data_transformation()

      
     except Exception as e:
          print(e)