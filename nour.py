import streamlit as st
import pandas as pd
import plotly.express as px

# Load the healthcare data from CSV
df = pd.read_csv("stroke_data.csv")

# Streamlit app title
st.title("Stroke")

# Title and paragraph about Stroke
st.write("""
Stroke is a critical health condition that requires attention and understanding. 
It is a significant medical issue that impacts numerous individuals worldwide. 
Exploring and visualizing data related to stroke can provide insights into its 
prevalence, risk factors, and potential preventative measures.
""")

# Brief Introduction to the Dataset
st.write("## About the Dataset")
st.write("""
The dataset provides insights into various factors related to strokes. 
It includes demographic information, health metrics, and lifestyle habits of individuals. 
By exploring this dataset, we can better understand the patterns and correlations 
between these factors and the occurrence of strokes.
""")

# Filter the data based on conditions
st.sidebar.header("Filter Data")

# Gender Dropdown
gender_options = ['All'] + df['gender'].unique().tolist()
selected_gender = st.sidebar.selectbox("Select Gender", gender_options)

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

# Age Slider
age_range = st.sidebar.slider("Select Age Range", int(df['age'].min()), int(df['age'].max()), (int(df['age'].min()), int(df['age'].max())))

# Average Glucose Level Slider
avg_glucose_level_range = st.sidebar.slider("Select Average Glucose Level Range", float(df['avg_glucose_level'].min()), 
                                            float(df['avg_glucose_level'].max()), 
                                            (float(df['avg_glucose_level'].min()), float(df['avg_glucose_level'].max())))

# BMI Slider
bmi_range = st.sidebar.slider("Select BMI Range", float(df['bmi'].min()), float(df['bmi'].max()), 
                              (float(df['bmi'].min()), float(df['bmi'].max())))

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

# 3D Scatter Plot
st.subheader("3D Scatter Plot of Age, Glucose Level, and BMI")
st.write("""
This 3D scatter plot visualizes the relationship between age, average glucose level, and BMI. 
Individuals with strokes are colored in red, while others are in blue. It helps in understanding 
how these three factors correlate with stroke incidences.
""")
fig_3d = px.scatter_3d(filtered_df, x='age', y='avg_glucose_level', z='bmi', color='stroke',
                       title='3D Scatter Plot of Age, Glucose Level, and BMI',
                       labels={'age': 'Age', 'avg_glucose_level': 'Average Glucose Level', 'bmi': 'BMI'},
                       color_discrete_map={0: 'blue', 1: 'red'})
st.plotly_chart(fig_3d)

# Contour Plot
st.subheader("Contour Plot of Age vs. Average Glucose Level")
st.write("""
The contour plot showcases the density of data points based on age and average glucose levels. 
The color coding indicates whether the individuals had strokes. It's instrumental in identifying 
regions of high risk.
""")
fig_contour = px.density_contour(filtered_df, x='age', y='avg_glucose_level', color='stroke',
                                 title='Contour Plot of Age vs. Average Glucose Level',
                                 labels={'age': 'Age', 'avg_glucose_level': 'Average Glucose Level'},
                                 color_discrete_map={0: 'blue', 1: 'red'})
st.plotly_chart(fig_contour)

# Pie Chart
st.subheader(f"Pie Chart: Distribution of Stroke for {selected_gender if selected_gender != 'All' else 'All Genders'}")
st.write(f"""
The pie chart presents the distribution of stroke cases for {selected_gender if selected_gender != 'All' else 'all genders'}. 
It provides a quick glance at the proportion of individuals affected by strokes.
""")
fig_pie = px.pie(filtered_df, names='stroke', title=f"Distribution of Stroke for {selected_gender if selected_gender != 'All' else 'All Genders'}")
st.plotly_chart(fig_pie)

# Bar Chart with Range Slider
st.subheader(f"Bar Chart: Average Glucose Level vs. BMI for Age {age_range[0]} - {age_range[1]}")
st.write("""
This bar chart displays the relationship between average glucose levels and BMI for the selected age range. 
The color gradient represents the age of individuals, allowing for deeper insights into age-related patterns.
""")
fig_bar = px.bar(filtered_df, x='avg_glucose_level', y='bmi', color='age', 
                 title=f"Average Glucose Level vs. BMI for Age {age_range[0]} - {age_range[1]}",
                 labels={'avg_glucose_level': 'Average Glucose Level', 'bmi': 'BMI'},
                 range_x=[float(df['avg_glucose_level'].min()), float(df['avg_glucose_level'].max())],
                 range_y=[float(df['bmi'].min()), float(df['bmi'].max())])
st.plotly_chart(fig_bar)

# Sunburst Chart
st.subheader("Sunburst Chart: Relationship between Smoking Status, Gender, and Stroke")
st.write("""
The Sunburst chart offers a hierarchical view of the data. It displays the relationship between 
smoking status, gender, and stroke occurrences, enabling users to identify patterns across these factors.
""")
fig_sunburst = px.sunburst(filtered_df, path=['smoking_status', 'gender'], values='stroke',
                           title='Sunburst Chart: Relationship between Smoking Status, Gender, and Stroke',
                           color_continuous_scale='Viridis',
                           labels={'smoking_status': 'Smoking Status', 'gender': 'Gender', 'stroke': 'Stroke'})
st.plotly_chart(fig_sunburst)
