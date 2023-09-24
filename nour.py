import streamlit as st
import pandas as pd
import plotly.express as px

# Load the healthcare data from CSV
url = "https://raw.githubusercontent.com/your_username/your_repository/your_branch/healthcare-dataset-stroke-data-2.csv"
df = pd.read_csv(url)

# Streamlit app title
st.title("Healthcare Data Visualization")

# Filter the data based on conditions
st.sidebar.header("Filter Data")
age_range = st.sidebar.slider("Select Age Range", int(df['age'].min()), int(df['age'].max()), (int(df['age'].min()), int(df['age'].max())))
filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]

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

# Scatterplot Matrix
st.subheader("Scatterplot Matrix")
numerical_columns = ['age', 'avg_glucose_level', 'bmi']
fig_scatter_matrix = px.scatter_matrix(filtered_df, dimensions=numerical_columns, color='hypertension',
                                       title='Scatterplot Matrix Hypertension for Hypertension',
                                       labels={col: col for col in numerical_columns})
st.plotly_chart(fig_scatter_matrix)

# Sunburst Chart
st.subheader("Sunburst Chart: Relationship between Smoking Status, Gender, and Stroke")
fig_sunburst = px.sunburst(filtered_df, path=['smoking_status', 'gender'], values='stroke',
                           title='Sunburst Chart: Relationship between Smoking Status, Gender, and Stroke',
                           color_continuous_scale='Viridis',
                           labels={'smoking_status': 'Smoking Status', 'gender': 'Gender', 'stroke': 'Stroke'})
st.plotly_chart(fig_sunburst)

# Animated Bar Chart
st.subheader("Animated Bar Chart: Strokes Over Age")
fig_bar = px.bar(filtered_df, x='age', y='stroke', title='Animated Bar Chart: Strokes Over Age',
                  labels={'age': 'Age', 'stroke': 'Stroke'},
                  animation_frame='age',
                  range_x=[int(df['age'].min()), int(df['age'].max())],
                  range_y=[0, 1],
                  color='stroke',
                  color_discrete_map={0: 'blue', 1: 'red'},
                  text='stroke')
st.plotly_chart(fig_bar)
