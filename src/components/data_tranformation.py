"""
- What this file is doing 
This has mainly 1 classes - DataTramformation(The other class DataTramformationConfig is nothing but provideds paths and path related thing it will deal)

DataTramformationConfig
- get_data_tramformation_obj()
    After performing eda on our data we came to know what are the numerical and catagorical(that is non-numerical) features and we know what are input and output features clearly
    So For training model we need a black box
                                  ________________
    input_data(a data farame) -->| Black box      | --> The new traformed data
    This black box is coloum tranformer -->self explainer it tranform the data in the coloums
        so to tranform it ask to thing as input num_pipeline,cat_pipelines that is we need to give input how to deal with this data
    
        Numerical data undergoes the following
            1) imputer - if any data is missing it replace with the medina there
            2)standard scalar adjust the mean to 0 and standard deviation to 1
        catorical data
            1)inputer
            2)One Hot encoding
            3)standard scalar - with mean false

        and finally this fuction return this black box containg this Coloum tranformer

- intitiate the data tranformation
    Hear we take the input data frame and divide it into 
        1 - train,test
        2 - input,output features
        and give only input features in both train and test and then concatenate the tranformed features which are also in numpy array foramt to the output feature

save_obj - So we written a utils function to save objects in genral
So .pkl is file foramt that classes in bit stream 

It's not just class being stored there all the parameters it learned like median etc... so that we no need compute them agin for this class
The advatages are it takes less space and can be easily reloded as python and can be used else where also

even in next time we are going to convert the model that we create also into a.pkl file
                                                                  ----------------

"""
import numpy as np
import pandas as pd
import os
import sys
from src.logger import logging
from dataclasses import dataclass

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler


from src.logger import logging
from src.exception import CustomException
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprosser_obj_file_path = os.path.join("artifacts","preprosser.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )

            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)

                ]


            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformation_object()

            target_column_name="math_score"
            numerical_columns = ["writing_score", "reading_score"]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path=self.data_transformation_config.preprosser_obj_file_path,
                obj=preprocessing_obj 
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprosser_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)