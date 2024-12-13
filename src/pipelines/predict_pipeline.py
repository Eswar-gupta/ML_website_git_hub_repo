import sys
import pandas as pd
import os
from src.exception import CustomException
from src.utils import load_object


"""
This is How the predict pipeline will be working

So in app.py using Flask and request etc... we exctracted the requried input data in form of text and numbers and then they are using "from src.pipeline.predict_pipeline import CustomData,PredictPipeline"

then when features are passed as a data we all ready converted the ColoumTranformer class who parameter and vraible are previously described in data_traformation.py into a .pkl file called preproceser
so now we use that same class to convert this data into binnary complete numerical data 

This numerical data is then passed to the best_model that was discovered during the model training process as the best_model along with its peratmeter is converted into a .pkl file so we use that to rain and prodoce the result


"""


class PredictPipeline:
    def __init__(self):
        pass


    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprosser.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
