import pickle
import numpy as np

# In this file the saved steps for the model are loaded from the notebook and the prediction is done

def load_model_and_encoders():
    # Load model from pickled file
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data["model"], data["le_country"], data["le_education"]

def predict_salary(country, education, experience, model, le_country, le_education):
    # Encoding
    country_enc = le_country.transform([country])[0]
    education_enc = le_education.transform([education])[0]
    # Array creation
    input_data = np.array([[country_enc, education_enc, experience]])
    salary_pred = model.predict(input_data)
    return salary_pred
