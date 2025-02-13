import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
import base64

# Set Streamlit page configuration
st.set_page_config(page_title="Employee Clustering System", page_icon=":busts_in_silhouette:", layout="wide")

# Set a custom background image (optional)
def add_bg_from_url(image_url):
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url({image_url});
             background-size: cover;
             background-attachment: fixed;
             background-repeat: no-repeat;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url('https://vratatech.com/assets/images/amg-companies/companies-3.jpg')  # Replace with your image URL

st.title('Employee Clustering System')
st.markdown("---")

# Upload file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.sidebar.header("Input Parameters")
    num_teams = st.sidebar.number_input("Number of Teams", min_value=1, value=5)
    skills_required = st.sidebar.text_input("Skills Required (comma-separated)")

    if st.sidebar.button('Cluster Employees'):
        # Filter employees based on required skills
        required_skills = [skill.strip().lower() for skill in skills_required.split(',')]
        df['Skills_lower'] = df['Skills'].str.lower()
        df_filtered = df[df['Skills_lower'].apply(lambda x: any(skill in x for skill in required_skills))]

        if df_filtered.empty:
            st.write("No employees found with the specified skills.")
        else:
            # Remove 'Skills_lower' column as it is no longer needed
            df_filtered = df_filtered.drop(columns=['Skills_lower'])

            # Preprocess data
            df_encoded = pd.get_dummies(df_filtered[['Skills', 'preferences', 'Job Role']])
            scaler = StandardScaler()
            scaled_features = scaler.fit_transform(df_encoded)

            # Fit K-Means model
            kmeans = KMeans(n_clusters=num_teams, random_state=42)
            df_filtered['Team'] = kmeans.fit_predict(scaled_features)
            
            # Display results
            st.write(df_filtered.head())

            # Visualization
            st.write(f"Clustered into {num_teams} teams:")
            for team in range(num_teams):
                st.write(f"### Team {team+1}")
                team_members = df_filtered[df_filtered['Team'] == team]
                st.write(team_members[['Name', 'Job Role', 'Skills', 'preferences']])

                # Plot the team members using Plotly with custom colors
                if not team_members.empty:
                    fig = px.bar(team_members, x='Job Role', y='Name', color='Job Role', orientation='h',
                         title=f'Team {team+1} Members by Job Role',
                         color_discrete_sequence=px.colors.qualitative.Pastel)
                    st.plotly_chart(fig)


            # Additional Visualization: Skill Distribution
            st.markdown("### Skill Distribution Across Teams")
            if not df_filtered.empty:
                skill_dist = df_filtered[['Skills', 'Team']].groupby('Skills').count().reset_index()
                fig_dist = px.pie(skill_dist, names='Skills', values='Team', title='Skills Distribution Across All Teams',
                                  color_discrete_sequence=px.colors.qualitative.Pastel)
                st.plotly_chart(fig_dist)

