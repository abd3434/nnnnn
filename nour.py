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

filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1]) & 
                  (df['hypertension'] == int(hypertension_checkbox)) & 
                  (df['heart_disease'] == int(heart_disease_checkbox))]

# Display the filtered data
st.write("Filtered Data:")
st.write(filtered_df)

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

# Dropdown for Work Type
work_type_options = ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked']
selected_work_type = st.sidebar.selectbox("Select Work Type", work_type_options)
work_type_filtered_df = filtered_df[filtered_df['work_type'] == selected_work_type]

# Pie Chart
st.subheader(f"Pie Chart: Distribution of Stroke for {selected_work_type} Work Type")
fig_pie = px.pie(work_type_filtered_df, names='stroke', title=f"Distribution of Stroke for {selected_work_type} Work Type")
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
