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
hypertension_options = ['All'] + df['hypertension'].unique().tolist()
selected_hypertension = st.sidebar.selectbox("Select Hypertension", hypertension_options)

# Heart Disease Dropdown
heart_disease_options = ['All'] + df['heart_disease'].unique().tolist()
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

# Average Glucose Level Slider
avg_glucose_level_range = st.sidebar.slider("Select Average Glucose Level Range", float(df['avg_glucose_level'].min()), 
                                            float(df['avg_glucose_level'].max()), 
                                            (float(df['avg_glucose_level'].min()), float(df['avg_glucose_level'].max())))

# BMI Slider
bmi_range = st.sidebar.slider("Select BMI Range", float(df['bmi'].min()), float(df['bmi'].max()), 
                              (float(df['bmi'].min()), float(df['bmi'].max())))

# Smoking Status Dropdown
smoking_status_options = ['All'] + df['smoking_status'].unique().tolist()
selected_smoking_status = st.sidebar.selectbox("Select Smoking Status", smoking_status_options)

# Apply filters
filtered_df = df[(df['gender'] == selected_gender or selected_gender == 'All') &
                 (df['age'] >= age_range[0]) & (df['age'] <= age_range[1]) &
                 (df['hypertension'] == int(selected_hypertension) or selected_hypertension == 'All') &
                 (df['heart_disease'] == int(selected_heart_disease) or selected_heart_disease == 'All') &
                 (df['ever_married'] == selected_ever_married or selected_ever_married == 'All') &
                 (df['work_type'] == selected_work_type or selected_work_type == 'All') &
                 (df['Residence_type'] == selected_residence_type or selected_residence_type == 'All') &
                 (df['avg_glucose_level'] >= avg_glucose_level_range[0]) & (df['avg_glucose_level'] <= avg_glucose_level_range[1]) &
                 (df['bmi'] >= bmi_range[0]) & (df['bmi'] <= bmi_range[1]) &
                 (df['smoking_status'] == selected_smoking_status or selected_smoking_status == 'All')]

# Display the filtered data
st.write("Filtered Data")
st.write(filtered_df)

# 3D Scatter Plot
st.subheader("3D Scatter Plot of Age, Glucose Level, and BMI")
fig_3d = px.scatter_3d(filtered_df, x='age', y='avg_glucose_level', z='bmi', color='stroke',
                        title='3D Scatter Plot of Age, Glucose Level, and BMI',
                        labels={'age': 'Age', 'avg_glucose_level': 'Average Glucose Level', 'bmi': 'BMI'},
                        color_discrete_map={0: 'blue', 1: 'red'})
st.plotly_chart(fig_3d)
