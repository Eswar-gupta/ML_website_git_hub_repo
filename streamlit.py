import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipelines.predict_pipeline import CustomData, PredictPipeline

# Load your existing model and data preprocessor (if applicable)

st.title("Gayathri")  # Set the app title

# Define input fields for user interaction
gender = st.selectbox("Gender", ("male", "female"))
race_ethnicity = st.selectbox("Race/Ethnicity", ("group A", "group B", "group C", "group D", "group D"))
parental_level_of_education = st.selectbox(
    "Parental Level of Education", ("high school", "some college", "bachelor's degree", "master's degree", "associate's degree", "some high school")
)
lunch = st.selectbox("Lunch", ("standard", "free/feduced"))
test_preparation_course = st.selectbox("Lunch", ("none", "completed"))
reading_score = st.number_input("Reading Score",step = 1)
writing_score = st.number_input("Writing Score",step = 1)

# Create a custom function to handle prediction logic
def predict(data):
    # Preprocess data if needed
    scaler = StandardScaler()  # Example scaler (adjust based on your model)
    #data = scaler.fit_transform(data)

    # Create a CustomData object with user input
    data_obj = CustomData(
        gender=data[0],
        race_ethnicity=data[1],
        parental_level_of_education=data[2],
        lunch=data[3],
        test_preparation_course=data[4],
        reading_score=data[5],
        writing_score=data[6],
    )

    # Get data as DataFrame
    pred_df = data_obj.get_data_as_data_frame()

    # Load and use your prediction pipeline
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    return results[0]

# Combine user input into a list for prediction
user_data = [
    gender,
    race_ethnicity,
    parental_level_of_education,
    lunch,
    test_preparation_course,
    reading_score,
    writing_score,
]

# Trigger prediction only if the submit button is clicked
if st.button("Predict Result"):
    prediction = predict(user_data)
    st.write(f"Predicted Outcome: {prediction}")