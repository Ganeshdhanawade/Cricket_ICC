from src.components import data_ingestion,data_transformation,model_trainer

##call the data engestion
obj = data_ingestion.DataIngestion()
train_data, test_data = obj.initiate_data_ingestion()

##transform the dataset
data_transformation =  data_transformation.DataTransformation()
train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)

##model training and show the result
modeltrainer = model_trainer.ModelTrainer()
print(modeltrainer.initiate_model_trainer(train_arr,test_arr))