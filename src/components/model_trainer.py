import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from dataclasses import dataclass

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

from src.utils import save_object
from src.logger import logging
from src.exception import CustomException

from data_ingestion import *
from data_transformation import *

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self) -> None:
        self.model_trainer_config = ModelTrainerConfig()


    def initiate_model_trainer(self,train_arr,test_arr,preprocessor_path = None):
        try:
            logging.info("Split train and test")
            x_train, y_train, x_test, y_test =(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            model = RandomForestRegressor(max_depth=36)
            model.fit(x_train,y_train)
            logging.info("model selected for use and fitted on the data.")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=model
            )

            logging.info("model pickle file save.")

            y_pred = model.predict(x_test)
            score = r2_score(y_test,y_pred)*100
            return score
        
        except Exception as e:
            CustomException(e,sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation =  DataTransformation()
    train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)
    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))