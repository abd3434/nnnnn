import streamlit as st
import pandas as pd
import plotly.express as px

# Load the healthcare data from CSV
df = pd.read_csv("stroke_data.csv")

# Streamlit app title
st.title("Healthcare Data Visualization")

# Filter the data based on conditions
st.sidebar.header("Filter Data")

# Age Range Slider
age_range = st.sidebar.slider("Select Age Range", int(df['age'].min()), int(df['age'].max()), (int(df['age'].min()), int(df['age'].max())))

# Hypertension Checkbox
hypertension_checkbox = st.sidebar.checkbox("Hypertension", True)

# Heart Disease Checkbox
heart_disease_checkbox = st.sidebar.checkbox("Heart Disease", True)

# Dropdown for Work Type
work_type_options = ['All'] + df['work_type'].unique().tolist()
selected_work_type = st.sidebar.selectbox("Select Work Type", work_type_options)

# Gender Dropdown
gender_options = ['All', 'Male', 'Female']
selected_gender = st.sidebar.selectbox("Select Gender", gender_options)

# Apply filters
if selected_work_type == 'All' and selected_gender == 'All':
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1]) & 
                      (df['hypertension'] == int(hypertension_checkbox)) & 
                      (df['heart_disease'] == int(heart_disease_checkbox))]
elif selected_work_type == 'All':
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1]) & 
                      (df['hypertension'] == int(hypertension_checkbox)) & 
                      (df['heart_disease'] == int(heart_disease_checkbox)) & 
                      (df['gender'] == selected_gender)]
elif selected_gender == 'All':
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1]) & 
                      (df['hypertension'] == int(hypertension_checkbox)) & 
                      (df['heart_disease'] == int(heart_disease_checkbox)) & 
                      (df['work_type'] == selected_work_type)]
else:
    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1]) & 
                      (df['hypertension'] == int(hypertension_checkbox)) & 
                      (df['heart_disease'] == int(heart_disease_checkbox)) & 
                      (df['work_type'] == selected_work_type) & 
                      (df['gender'] == selected_gender)]

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

# Bar Chart with Range Slider for Glucose Level
st.subheader("Bar Chart: Strokes Over Glucose Level")
glucose_level_range = st.sidebar.slider("Select Glucose Level Range", float(df['avg_glucose_level'].min()), 
                                       float(df['avg_glucose_level'].max()), 
                                       (float(df['avg_glucose_level'].min()), float(df['avg_glucose_level'].max())))
glucose_filtered_df = df[(df['avg_glucose_level'] >= glucose_level_range[0]) & 
                         (df['avg_glucose_level'] <= glucose_level_range[1])]

fig_bar_glucose = px.bar(glucose_filtered_df, x='avg_glucose_level', y='stroke', 
                         title='Strokes Over Glucose Level',
                         labels={'avg_glucose_level': 'Average Glucose Level', 'stroke': 'Stroke'},
                         range_x=[float(df['avg_glucose_level'].min()), float(df['avg_glucose_level'].max())],
                         range_y=[0, 1],
                         color='stroke',
                         color_discrete_map={0: 'blue', 1: 'red'},
                         text='stroke')
st.plotly_chart(fig_bar_glucose)
