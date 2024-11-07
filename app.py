import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Custom CSS for styling
st.markdown("""
    <style>
    .reportview-container {
        background-color: #1e1e1e; /* Darker grey background */
        color: #ffffff; /* White text color */
    }
    .sidebar .sidebar-content {
        background-color: #242424; /* Darker grey sidebar */
    }
    .css-18e3th9 {
        background-color: #333333; /* Darker grey for the main header area */
    }
    .stButton > button {
        background-color: #00bfae; /* Teal button */
        color: white;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton > button:hover {
        background-color: #009b8f; /* Darker teal on hover */
    }
    .title {
        font-size: 36px;
        color: #ffffff;
        text-align: center;
        padding: 20px;
        font-weight: bold;
    }
    .vit-banner {
    font-size: 48px; /* Larger font size for VIT */
    color: #ffffff; /* White text color */
    text-align: center;
    padding: 20px;
    background-color: #222222; /* Slightly lighter grey background for the VIT banner */
    border-radius: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    font-family: 'Arial', sans-serif;

    /* Add blue border effect to the text */
    text-shadow: 
        -2px -2px 0 #00bfff,  /* Top-left blue shadow */
         2px -2px 0 #00bfff,  /* Top-right blue shadow */
        -2px  2px 0 #00bfff,  /* Bottom-left blue shadow */
         2px  2px 0 #00bfff;  /* Bottom-right blue shadow */
}

    .about-us {
        font-size: 18px;
        color: #ffffff;
        padding: 20px;
        text-align: center;
        background-color: #333333;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stTextInput input {
        border-radius: 8px;
        padding: 10px;
        border: 1px solid #444444;
        background-color: #2e2e2e;
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for navigation
with st.sidebar:
    st.title("Menu->")
    selected = option_menu('What do you want to predict??',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'About Us'],
                           icons=['activity', 'heart', 'person', 'info'],
                           default_index=0,
                           styles={
                               "container": {"padding": "5!important", "background-color": "#242424"},
                               "icon": {"color": "white", "font-size": "20px"},
                               "nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "#333333"},
                               "nav-link-selected": {"background-color": "#555555"},
                           })

# Display VIT separately on the frontend
st.markdown('<div class="vit-banner">PredictEase</div>', unsafe_allow_html=True)

# About Us Section
if selected == 'About Us':
    st.title('About Us')
    st.markdown("""
        <div class="about-us">
            <p><strong>PredictEase</strong> is an advanced predictive analytics application designed to provide accurate predictions for various health conditions. By leveraging machine learning models, PredictEase helps users assess the likelihood of diabetes, heart disease, and Parkinson's disease based on their input data.</p>
            <p>This project aims to offer a user-friendly interface that integrates powerful prediction models in a single platform, making health assessments more accessible and reliable. This is our project-1 for Vellore Institute of Technology.</p>
            <p><strong>Creators:</strong><br>
            1. Shubham Nijhawan<br>
            2. Manit Gera<br>
            3. Aditya Aryan</p>
        </div>
    """, unsafe_allow_html=True)

# Function to convert inputs to numeric values safely
def safe_float_input(input_value, default_value=0.0):
    try:
        return float(input_value)
    except ValueError:
        return default_value

# Diabetes Prediction with Advice and Precautions
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using SVM')
    
    # User inputs
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = safe_float_input(st.text_input('No. of Pregnancies?'))
    with col2:
        Glucose = safe_float_input(st.text_input('Glucose Level?'))
    with col3:
        BloodPressure = safe_float_input(st.text_input('Blood Pressure?'))
    with col1:
        SkinThickness = safe_float_input(st.text_input('Skin Thickness?'))
    with col2:
        Insulin = safe_float_input(st.text_input('Insulin?'))
    with col3:
        BMI = safe_float_input(st.text_input('BMI?'))
    with col1:
        DiabetesPedigreeFunction = safe_float_input(st.text_input('Diabetes Pedigree Function value?'))
    with col2:
        Age = safe_float_input(st.text_input('Age?'))
    
    diab_diagnosis = ''
    diab_advice = ''  # Variable for advice based on diagnosis
    
    # Prediction
    if st.button('Diabetes Test Result'):
        try:
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic :( 🤧'
                diab_advice = """
                    **Advice-:**
                    - Maintain a healthy and balanced diet rich in fiber, low in refined carbs and sugar.
                    - Regularly monitor your blood sugar levels.
                    - Incorporate at least 30 minutes of physical activity daily.
                    - Take prescribed medications and insulin, if required.
                    - Regular medical checkups and keeping stress levels in check are important.
                    - Sleep is important!!
                """
            else:
                diab_diagnosis = 'The person is not diabetic :) 😁'
                diab_advice = """
                    ***Tips-(Prevention is better than cure :)***
                    - Continue eating a balanced diet.
                    - Stay physically active with regular exercise.
                    - Avoid smoking and manage stress effectively.
                    - Maintain a healthy weight and get body tests occassionly done.
                    - Sleep is important!!
                """
        except Exception as e:
            diab_diagnosis = f"Error in prediction: {str(e)}"
            diab_advice = ''
    
    st.success(diab_diagnosis)
    st.markdown(diab_advice)

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using Logistic Regression')

    # User inputs
    col1, col2, col3 = st.columns(3)

    with col1:
        age = safe_float_input(st.text_input('Age?'))
    with col2:
        sex = safe_float_input(st.text_input('Sex?'))
    with col3:
        cp = safe_float_input(st.text_input('Chest Pain types?'))
    with col1:
        trestbps = safe_float_input(st.text_input('Resting Blood Pressure?'))
    with col2:
        chol = safe_float_input(st.text_input('Serum Cholestoral in mg/dl?'))
    with col3:
        fbs = safe_float_input(st.text_input('Fasting Blood Sugar > 120 mg/dl?'))
    with col1:
        restecg = safe_float_input(st.text_input('Resting Electrocardiographic results?'))
    with col2:
        thalach = safe_float_input(st.text_input('Maximum Heart Rate achieved?'))
    with col3:
        exang = safe_float_input(st.text_input('Exercise Induced Angina?'))
    with col1:
        oldpeak = safe_float_input(st.text_input('ST depression induced by exercise relative to rest?'))
    with col2:
        slope = safe_float_input(st.text_input('Slope of the peak exercise ST segment?'))
    with col3:
        ca = safe_float_input(st.text_input('Major vessels colored by flourosopy?'))
    with col1:
        thal = safe_float_input(st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect'))

    heart_diagnosis = ''
    
    # Prediction
    if st.button('Heart Disease Test Result'):
        try:
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has heart disease :('
            else:
                heart_diagnosis = 'The person does not have heart disease :)'
        except Exception as e:
            heart_diagnosis = f"Error in prediction: {str(e)}"
    
    st.success(heart_diagnosis)

# Parkinson's Prediction
if selected == 'Parkinsons Prediction':
    st.title('Parkinson\'s Disease Prediction using XGBoost')
    
    # User inputs
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fo = safe_float_input(st.text_input('MDVP:Fo(Hz)'))
    with col2:
        fhi = safe_float_input(st.text_input('MDVP:Fhi(Hz)'))
    with col3:
        flo = safe_float_input(st.text_input('MDVP:Flo(Hz)'))
    with col1:
        jitter_percent = safe_float_input(st.text_input('Jitter(%)'))
    with col2:
        jitter_abs = safe_float_input(st.text_input('Jitter(Abs)'))
    with col3:
        rap = safe_float_input(st.text_input('MDVP:RAP'))
    with col1:
        ppq = safe_float_input(st.text_input('MDVP:PPQ'))
    with col2:
        ddp = safe_float_input(st.text_input('Jitter:DDP'))
    with col3:
        shimmer = safe_float_input(st.text_input('Shimmer'))
    with col1:
        shimmer_db = safe_float_input(st.text_input('Shimmer(dB)'))
    with col2:
        apq3 = safe_float_input(st.text_input('APQ3'))
    with col3:
        apq5 = safe_float_input(st.text_input('APQ5'))
    with col1:
        apq = safe_float_input(st.text_input('APQ'))
    with col2:
        dda = safe_float_input(st.text_input('DDA'))
    with col3:
        nhr = safe_float_input(st.text_input('NHR'))
    with col1:
        hnr = safe_float_input(st.text_input('HNR'))

    parkinsons_diagnosis = ''
    
    # Prediction
    if st.button("Parkinson's Test Result"):
        try:
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr]])
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease :("
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease :)"
        except Exception as e:
            parkinsons_diagnosis = f"Error in prediction: {str(e)}"
    
    st.success(parkinsons_diagnosis)
