import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Function to convert inputs to numeric values safely
def safe_float_input(input_value, default_value=0.0):
    try:
        return float(input_value)
    except ValueError:
        return default_value

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using SVM')
    
    # User inputs
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = safe_float_input(st.text_input('Number of Pregnancies'))
    with col2:
        Glucose = safe_float_input(st.text_input('Glucose Level'))
    with col3:
        BloodPressure = safe_float_input(st.text_input('Blood Pressure value'))
    with col1:
        SkinThickness = safe_float_input(st.text_input('Skin Thickness value'))
    with col2:
        Insulin = safe_float_input(st.text_input('Insulin Level'))
    with col3:
        BMI = safe_float_input(st.text_input('BMI value'))
    with col1:
        DiabetesPedigreeFunction = safe_float_input(st.text_input('Diabetes Pedigree Function value'))
    with col2:
        Age = safe_float_input(st.text_input('Age of the Person'))
    
    diab_diagnosis = ''
    
    # Prediction
    if st.button('Diabetes Test Result'):
        try:
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        except Exception as e:
            diab_diagnosis = f"Error in prediction: {str(e)}"
        
    st.success(diab_diagnosis)

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using Logistic Regression')

    # User inputs
    col1, col2, col3 = st.columns(3)

    with col1:
        age = safe_float_input(st.text_input('Age'))
    with col2:
        sex = safe_float_input(st.text_input('Sex'))
    with col3:
        cp = safe_float_input(st.text_input('Chest Pain types'))
    with col1:
        trestbps = safe_float_input(st.text_input('Resting Blood Pressure'))
    with col2:
        chol = safe_float_input(st.text_input('Serum Cholestoral in mg/dl'))
    with col3:
        fbs = safe_float_input(st.text_input('Fasting Blood Sugar > 120 mg/dl'))
    with col1:
        restecg = safe_float_input(st.text_input('Resting Electrocardiographic results'))
    with col2:
        thalach = safe_float_input(st.text_input('Maximum Heart Rate achieved'))
    with col3:
        exang = safe_float_input(st.text_input('Exercise Induced Angina'))
    with col1:
        oldpeak = safe_float_input(st.text_input('ST depression induced by exercise'))
    with col2:
        slope = safe_float_input(st.text_input('Slope of the peak exercise ST segment'))
    with col3:
        ca = safe_float_input(st.text_input('Major vessels colored by flourosopy'))
    with col1:
        thal = safe_float_input(st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect'))

    heart_diagnosis = ''

    # Prediction
    if st.button('Heart Disease Test Result'):
        try:
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        except Exception as e:
            heart_diagnosis = f"Error in prediction: {str(e)}"

    st.success(heart_diagnosis)

# Parkinson's Prediction
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using SVM")

    # User inputs
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = safe_float_input(st.text_input('MDVP:Fo(Hz)'))
    with col2:
        fhi = safe_float_input(st.text_input('MDVP:Fhi(Hz)'))
    with col3:
        flo = safe_float_input(st.text_input('MDVP:Flo(Hz)'))
    with col4:
        Jitter_percent = safe_float_input(st.text_input('MDVP:Jitter(%)'))
    with col5:
        Jitter_Abs = safe_float_input(st.text_input('MDVP:Jitter(Abs)'))
    with col1:
        RAP = safe_float_input(st.text_input('MDVP:RAP'))
    with col2:
        PPQ = safe_float_input(st.text_input('MDVP:PPQ'))
    with col3:
        DDP = safe_float_input(st.text_input('Jitter:DDP'))
    with col4:
        Shimmer = safe_float_input(st.text_input('MDVP:Shimmer'))
    with col5:
        Shimmer_dB = safe_float_input(st.text_input('MDVP:Shimmer(dB)'))
    with col1:
        APQ3 = safe_float_input(st.text_input('Shimmer:APQ3'))
    with col2:
        APQ5 = safe_float_input(st.text_input('Shimmer:APQ5'))
    with col3:
        APQ = safe_float_input(st.text_input('MDVP:APQ'))
    with col4:
        DDA = safe_float_input(st.text_input('Shimmer:DDA'))
    with col5:
        NHR = safe_float_input(st.text_input('NHR'))
    with col1:
        HNR = safe_float_input(st.text_input('HNR'))
    with col2:
        RPDE = safe_float_input(st.text_input('RPDE'))
    with col3:
        DFA = safe_float_input(st.text_input('DFA'))
    with col4:
        spread1 = safe_float_input(st.text_input('Spread1'))
    with col5:
        spread2 = safe_float_input(st.text_input('Spread2'))
    with col1:
        D2 = safe_float_input(st.text_input('D2'))
    with col2:
        PPE = safe_float_input(st.text_input('PPE'))

    parkinsons_diagnosis = ''

    # Prediction
    if st.button("Parkinson's Test Result"):
        try:
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
        except Exception as e:
            parkinsons_diagnosis = f"Error in prediction: {str(e)}"

    st.success(parkinsons_diagnosis)
