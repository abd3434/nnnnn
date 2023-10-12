import streamlit as st
import pandas as pd
import plotly.express as px

# Load the healthcare data from CSV
df = pd.read_csv("stroke_data.csv")

# Streamlit app title
st.title("Stroke")

# Definition of Stroke
st.write("""
A stroke occurs when the blood supply to part of your brain is interrupted or reduced, preventing brain tissue from getting oxygen and nutrients. Brain cells begin to die in minutes.
""")

# Title and paragraph about Stroke
st.write("Stroke is a critical health condition that requires attention and understanding. It is a significant medical issue that impacts numerous individuals worldwide. Exploring and visualizing data related to stroke can provide insights into its prevalence, risk factors, and potential preventative measures.")

# Filter the data based on conditions
st.sidebar.header("Filter Data")

# [Original Dropdowns and Sliders for Filtering Here]

# Apply filters
filtered_df = df[
    ((df['gender'] == selected_gender) | (selected_gender == 'All')) &
    ((df['hypertension'].astype(str) == selected_hypertension) | (selected_hypertension == 'All')) &
    ((df['heart_disease'].astype(str) == selected_heart_disease) | (selected_heart_disease == 'All')) &
    ((df['ever_married'] == selected_ever_married) | (selected_ever_married == 'All')) &
    ((df['work_type'] == selected_work_type) | (selected_work_type == 'All')) &
    ((df['Residence_type'] == selected_residence_type) | (selected_residence_type == 'All')) &
    ((df['smoking_status'] == selected_smoking_status) | (selected_smoking_status == 'All')) &
    ((df['age'] >= age_range[0]) & (df['age'] <= age_range[1])) &
    ((df['avg_glucose_level'] >= avg_glucose_level_range[0]) & (df['avg_glucose_level'] <= avg_glucose_level_range[1])) &
    ((df['bmi'] >= bmi_range[0]) & (df['bmi'] <= bmi_range[1]))
]

# [Rest of the Visualization Code Remains the Same as the Enhanced Code]

# 3D Scatter Plot
st.subheader("3D Scatter Plot of Age, Glucose Level, and BMI")
fig_3d = px.scatter_3d(filtered_df, x='age', y='avg_glucose_level', z='bmi', color='stroke',
                        title='3D Scatter Plot of Age, Glucose Level, and BMI',
                        labels={'age': 'Age', 'avg_glucose_level': 'Average Glucose Level', 'bmi': 'BMI'},
                        color_discrete_map={0: 'blue', 1: 'red'})
st.plotly_chart(fig_3d)
st.write("""
This 3D scatter plot visualizes the relationship between age, average glucose level, and BMI. 
The distinction in colors indicates the presence (red) or absence (blue) of stroke. Observing any clusters or patterns can help identify potential risk factors.
""")

# Contour Plot
st.subheader("Contour Plot of Age vs. Average Glucose Level")
fig_contour = px.density_contour(filtered_df, x='age', y='avg_glucose_level', color='stroke',
                                 title='Contour Plot of Age vs. Average Glucose Level',
                                 labels={'age': 'Age', 'avg_glucose_level': 'Average Glucose Level'},
                                 color_discrete_map={0: 'blue', 1: 'red'})
st.plotly_chart(fig_contour)
st.write("""
The contour plot showcases the density of data points at various intersections of age and average glucose level. 
Darker regions indicate a higher concentration of individuals, providing insight into common age and glucose levels.
""")

# Pie Chart
st.subheader(f"Pie Chart: Distribution of Stroke for {selected_gender if selected_gender != 'All' else 'All Genders'}")
fig_pie = px.pie(filtered_df, names='stroke', title=f"Distribution of Stroke for {selected_gender if selected_gender != 'All' else 'All Genders'}")
st.plotly_chart(fig_pie)
st.write("""
This pie chart provides a clear representation of the proportion of individuals who have experienced a stroke based on the selected gender filter. 
It helps in understanding the gender-specific prevalence of stroke.
""")

# Bar Chart with Range Slider
st.subheader(f"Bar Chart: Average Glucose Level vs. BMI for Age {age_range[0]} - {age_range[1]}")
fig_bar = px.bar(filtered_df, x='avg_glucose_level', y='bmi', color='age', 
                 title=f"Average Glucose Level vs. BMI for Age {age_range[0]} - {age_range[1]}",
                 labels={'avg_glucose_level': 'Average Glucose Level', 'bmi': 'BMI'},
                 range_x=[float(df['avg_glucose_level'].min()), float(df['avg_glucose_level'].max())],
                 range_y=[float(df['bmi'].min()), float(df['bmi'].max())])
st.plotly_chart(fig_bar)
st.write("""
The bar chart visualizes the relationship between average glucose levels and BMI for individuals within the selected age range. 
The color gradient, representing age, provides an added dimension to analyze how age might be influencing these parameters.
""")

# Sunburst Chart
st.subheader("Sunburst Chart: Relationship between Smoking Status, Gender, and Stroke")
fig_sunburst = px.sunburst(filtered_df, path=['smoking_status', 'gender'], values='stroke',
                           title='Sunburst Chart: Relationship between Smoking Status, Gender, and Stroke',
                           color_continuous_scale='Viridis',
                           labels={'smoking_status': 'Smoking Status', 'gender': 'Gender', 'stroke': 'Stroke'})
st.plotly_chart(fig_sunburst)
st.write("""
The sunburst chart presents a hierarchical view of the relationship between smoking status, gender, and instances of stroke. 
It allows for a multi-level exploration of how these factors might interplay in the prevalence of stroke.
""")
