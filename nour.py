import streamlit as st
import pandas as pd
import plotly.express as px

# Load the healthcare data from CSV
df = pd.read_csv("stroke_data.csv")

# Streamlit app title
st.title("Healthcare Data Visualization")

# Filter the data based on conditions
st.sidebar.header("Filter Data")

# Gender Dropdown
gender_options = ['All'] + df['gender'].unique().tolist()
selected_gender = st.sidebar.selectbox("Select Gender", gender_options)

# Age Slider
age_range = st.sidebar.slider("Select Age Range", int(df['age'].min()), int(df['age'].max()), (int(df['age'].min()), int(df['age'].max())))

# Hypertension Dropdown
hypertension_options = ['All'] + df['hypertension'].unique().astype(str).tolist()
selected_hypertension = st.sidebar.selectbox("Select Hypertension", hypertension_options)

# Heart Disease Dropdown
heart_disease_options = ['All'] + df['heart_disease'].unique().astype(str).tolist()
selected_heart_disease = st.sidebar.selectbox("Select Heart Disease", heart_disease_options)

# Married Dropdown
ever_married_options = ['All'] + df['ever_married'].unique().tolist()
selected_ever_married = st.sidebar.selectbox("Select Marital Status", ever_married_options)

# Work Type Dropdown
work_type_options = ['All'] + df['work_type'].unique().tolist()
selected_work_type = st.sidebar.selectbox("Select Work Type", work_type_options)

# Residence Type Dropdown
residence_type_options = ['All'] + df['Residence_type'].unique().tolist()
selected_residence_type = st.sidebar.selectbox("Select Residence Type", residence_type_options)

# Smoking Status Dropdown
smoking_status_options = ['All'] + df['smoking_status'].unique().tolist()
selected_smoking_status = st.sidebar.selectbox("Select Smoking Status", smoking_status_options)

# Apply filters
filtered_df = df[
    ((df['gender'] == selected_gender) | (selected_gender == 'All')) &
    ((df['age'] >= age_range[0]) & (df['age'] <= age_range[1])) &
    ((df['hypertension'].astype(str) == selected_hypertension) | (selected_hypertension == 'All')) &
    ((df['heart_disease'].astype(str) == selected_heart_disease) | (selected_heart_disease == 'All')) &
    ((df['ever_married'] == selected_ever_married) | (selected_ever_married == 'All')) &
    ((df['work_type'] == selected_work_type) | (selected_work_type == 'All')) &
    ((df['Residence_type'] == selected_residence_type) | (selected_residence_type == 'All')) &
    ((df['smoking_status'] == selected_smoking_status) | (selected_smoking_status == 'All'))
]

# Box Plot
st.subheader("Box Plot of BMI by Smoking Status")
fig_box = px.box(filtered_df, x='smoking_status', y='bmi', color='smoking_status',
                 title='Box Plot of BMI by Smoking Status',
                 labels={'smoking_status': 'Smoking Status', 'bmi': 'BMI'},
                 color_discrete_map={'formerly smoked': 'blue', 'never smoked': 'green', 'smokes': 'red', 'Unknown': 'gray'})
st.plotly_chart(fig_box)

# Violin Plot
st.subheader("Violin Plot of Average Glucose Level by Marital Status")
fig_violin = px.violin(filtered_df, x='ever_married', y='avg_glucose_level', box=True,
                      title='Violin Plot of Average Glucose Level by Marital Status',
                      labels={'ever_married': 'Marital Status', 'avg_glucose_level': 'Average Glucose Level'})
st.plotly_chart(fig_violin)
