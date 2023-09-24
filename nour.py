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
filtered_df = df[
    ((df['gender'] == selected_gender) | (selected_gender == 'All')) &
    ((df['age'] >= age_range[0]) & (df['age'] <= age_range[1])) &
    ((df['hypertension'].astype(str) == selected_hypertension) | (selected_hypertension == 'All')) &
    ((df['heart_disease'].astype(str) == selected_heart_disease) | (selected_heart_disease == 'All')) &
    ((df['ever_married'] == selected_ever_married) | (selected_ever_married == 'All')) &
    ((df['work_type'] == selected_work_type) | (selected_work_type == 'All')) &
    ((df['Residence_type'] == selected_residence_type) | (selected_residence_type == 'All')) &
    ((df['avg_glucose_level'] >= avg_glucose_level_range[0]) & (df['avg_glucose_level'] <= avg_glucose_level_range[1])) &
    ((df['bmi'] >= bmi_range[0]) & (df['bmi'] <= bmi_range[1])) &
    ((df['smoking_status'] == selected_smoking_status) | (selected_smoking_status == 'All'))
]

# 3D Scatter Plot
st.subheader("3D Scatter Plot of Age, Glucose Level, and BMI")
fig_3d = px.scatter_3d(filtered_df, x='age', y='avg_glucose_level', z='bmi', color='stroke',
                        title='3D Scatter Plot of Age, Glucose Level, and BMI',
                        labels={'age': 'Age', 'avg_glucose_level': 'Average Glucose Level', 'bmi': 'BMI'},
                        color_discrete_map={0: 'blue', 1: 'red'})
st.plotly_chart(fig_3d)

# Contour Plot
st.subheader("Contour Plot of Age vs. Average Glucose Level")
fig_contour = px.density_contour(filtered_df, x='age', y='avg_glucose_level', color='stroke',
                                 title='Contour Plot of Age vs. Average Glucose Level',
                                 labels={'age': 'Age', 'avg_glucose_level': 'Average Glucose Level'},
                                 color_discrete_map={0: 'blue', 1: 'red'})
st.plotly_chart(fig_contour)

# Pie Chart
st.subheader(f"Pie Chart: Distribution of Stroke for {selected_gender if selected_gender != 'All' else 'All Genders'}")
fig_pie = px.pie(filtered_df, names='stroke', title=f"Distribution of Stroke for {selected_gender if selected_gender != 'All' else 'All Genders'}")
st.plotly_chart(fig_pie)

# Bar Chart with Range Slider
st.subheader(f"Bar Chart: Average Glucose Level vs. BMI for Age {age_range[0]} - {age_range[1]}")
fig_bar = px.bar(filtered_df, x='avg_glucose_level', y='bmi', color='age', 
                 title=f"Average Glucose Level vs. BMI for Age {age_range[0]} - {age_range[1]}",
                 labels={'avg_glucose_level': 'Average Glucose Level', 'bmi': 'BMI'},
                 range_x=[float(df['avg_glucose_level'].min()), float(df['avg_glucose_level'].max())],
                 range_y=[float(df['bmi'].min()), float(df['bmi'].max())])
st.plotly_chart(fig_bar)

# Sunburst Chart
st.subheader("Sunburst Chart: Relationship between Smoking Status, Gender, and Stroke")
fig_sunburst = px.sunburst(filtered_df, path=['smoking_status', 'gender'], values='stroke',
                           title='Sunburst Chart: Relationship between Smoking Status, Gender, and Stroke',
                           color_continuous_scale='Viridis',
                           labels={'smoking_status': 'Smoking Status', 'gender': 'Gender', 'stroke': 'Stroke'})
st.plotly_chart(fig_sunburst)
