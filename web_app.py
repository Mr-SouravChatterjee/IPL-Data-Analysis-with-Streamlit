import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define plotting functions for each visualization
def plot_job_role_distribution(df):
    plt.figure(figsize=(7, 5))
    sns.countplot(y='Job Role', data=df, palette='pastel', order=df['Job Role'].value_counts().index, hue='Job Role', legend=False)
    plt.title('Job Role Distribution')
    plt.xlabel('Number of Employees')
    plt.ylabel('Job Role')
    st.pyplot(plt.gcf())
    plt.close()

def plot_performance_rating_distribution(df):
    plt.figure(figsize=(7, 5))
    sns.countplot(x='Performance Rating', data=df, palette='pastel', hue='Performance Rating', legend=False)
    plt.title('Distribution of Performance Ratings')
    plt.xlabel('Performance Rating')
    plt.ylabel('Number of Employees')
    st.pyplot(plt.gcf())
    plt.close()

def plot_job_roles_vs_performance(df):
    top_job_roles = df['Job Role'].value_counts().nlargest(5).index
    filtered_df = df[df['Job Role'].isin(top_job_roles)]
    plt.figure(figsize=(8, 6), facecolor='white')
    sns.countplot(x='Job Role', hue='Performance Rating', data=filtered_df, palette=['lightgreen', 'pink'])
    plt.title('Job Roles vs. Performance Rating')
    plt.xlabel('Job Role')
    plt.ylabel('Count of Employees')
    plt.xticks(rotation=45)
    plt.legend(title='Performance Rating')
    plt.tight_layout()
    st.pyplot(plt.gcf())
    plt.close()

def plot_top_job_roles_by_performance(df):
    plt.figure(figsize=(7, 5))
    avg_performance_by_role = df.groupby('Job Role')['Performance Rating'].mean().sort_values(ascending=False)
    sns.barplot(x=avg_performance_by_role.values, y=avg_performance_by_role.index, palette='pastel', hue=avg_performance_by_role.index, legend=False)
    plt.title('Top Job Roles by Average Performance Rating')
    plt.xlabel('Average Performance Rating')
    plt.ylabel('Job Role')
    st.pyplot(plt.gcf())
    plt.close()

def plot_gender_distribution(df):
    plt.figure(figsize=(7, 5))
    gender_counts = df['Gender'].value_counts()
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
    plt.title('Gender Distribution')
    st.pyplot(plt.gcf())
    plt.close()

def plot_gender_distribution_in_job_roles(df):
    plt.figure(figsize=(7, 5))
    sns.countplot(y='Job Role', hue='Gender', data=df, palette='pastel')
    plt.title('Gender Distribution Across Job Roles')
    plt.xlabel('Number of Employees')
    plt.ylabel('Job Role')
    st.pyplot(plt.gcf())
    plt.close()

def plot_gender_vs_performance_rating(df):
    plt.figure(figsize=(7, 5))
    sns.countplot(x='Gender', hue='Performance Rating', data=df, palette=['pink', 'violet'])
    plt.title('Gender vs. Performance Rating')
    plt.xlabel('Gender')
    plt.ylabel('Count of Employees')
    plt.legend(title='Performance Rating')
    plt.tight_layout()
    st.pyplot(plt.gcf())
    plt.close()

def plot_experience_distribution(df):
    plt.figure(figsize=(7, 5))
    sns.histplot(df['Experience'], kde=False, color='skyblue', bins=10)
    plt.title('Distribution of Experience')
    plt.xlabel('Years of Experience')
    plt.ylabel('Number of Employees')
    st.pyplot(plt.gcf())
    plt.close()

def plot_experience_vs_performance_rating(df):
    plt.figure(figsize=(7, 5))
    sns.boxplot(x='Performance Rating', y='Experience', data=df, palette='coolwarm', hue='Performance Rating', legend=False)
    plt.title('Experience vs. Performance Rating')
    plt.xlabel('Performance Rating')
    plt.ylabel('Years of Experience')
    st.pyplot(plt.gcf())
    plt.close()

def plot_performance_rating_by_yoe():
    experience_years = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    performance_rating_3 = [5, 10, 15, 20, 25, 30, 20, 10, 5, 3, 2]
    performance_rating_5 = [0, 2, 5, 10, 15, 20, 30, 25, 20, 15, 10]

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].bar(experience_years, performance_rating_3, color='lightcoral', alpha=0.7)
    axes[0].set_xticks(experience_years)
    axes[0].set_title("Distribution of Performance (PR-3) by YOE")
    axes[0].set_xlabel("Years of Experience")
    axes[0].set_ylabel("Counts")
    axes[0].grid(axis='y')

    axes[1].bar(experience_years, performance_rating_5, color='lightblue', alpha=0.7)
    axes[1].set_xticks(experience_years)
    axes[1].set_title("Distribution of Performance (PR-5) by YOE")
    axes[1].set_xlabel("Years of Experience")
    axes[1].set_ylabel("Counts")
    axes[1].grid(axis='y')

    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

def plot_top_skills(df):
    plt.figure(figsize=(7, 5))
    skills = df['Skills'].str.get_dummies(sep=' ').sum().sort_values(ascending=False).head(10)
    sns.barplot(x=skills.values, y=skills.index, palette='pastel', hue=skills.index, legend=False)
    plt.title('Top 10 Skill Distribution Among Employees')
    plt.xlabel('Number of Employees with Skill')
    plt.ylabel('Skills')
    st.pyplot(plt.gcf())
    plt.close()

# Streamlit app
st.set_page_config(page_icon=":bar_chart:", page_title="Comprehensive Employee Data Analysis")

st.title("Comprehensive Employee Data Analysis")
st.caption("This dashboard provides insights into various aspects of employee data. Use the sidebar to select and view specific visualizations.")

df = pd.read_excel('C:\Users\User\OneDrive\Desktop\final_processed_employee_data.xlsx')

st.sidebar.title("Visualizations")
visualization = st.sidebar.radio("Select a visualization:", 
                                 ["Home",  
                                  "Job Role Distribution", 
                                  "Performance Rating Distribution", 
                                  "Job Roles vs. Performance Rating", 
                                  "Top Job Roles by Performance Rating", 
                                  "Gender Distribution", 
                                  "Gender Distribution in Job Roles", 
                                  "Gender vs. Performance Rating", 
                                  "Experience Distribution", 
                                  "Experience vs. Performance Rating", 
                                  "Performance Rating by Years of Experience", 
                                  "Top 10 Skills"])

if visualization == "Home":
    st.subheader("Welcome to the Employee Data Analysis Dashboard")
    
    st.write("""
    This dashboard is designed to provide a comprehensive analysis of employee data,
    focusing on performance ratings, job roles, skills, gender distribution, and more.
    
    Use the sidebar to navigate through various visualizations and gain insights into the
    employee dataset. The visualizations help to identify key trends and patterns that 
    can inform decision-making and strategic planning.
    """)

    #st.video("https://videos.pexels.com/video-files/6774467/6774467-uhd_1440_2560_30fps.mp4")
    st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center;">
        <video width="800" height="400" controls>
            <source src="https://videos.pexels.com/video-files/6774467/6774467-uhd_1440_2560_30fps.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    <p style="text-align: center; font-size: 18px; margin-top: 10px;">Bought to you by: Zigma-3</p>

    """,
    unsafe_allow_html=True
)
    
    st.markdown("### Key Features:")
    st.markdown("- *Job Role Distribution*: Understand the spread of job roles across the company.")
    st.markdown("- *Performance Ratings*: Analyze performance ratings by various factors such as job roles and experience.")
    st.markdown("- *Skills Analysis*: Explore the top skills among employees.")
    st.markdown("- *Gender Distribution*: Review gender distribution in different job roles and performance ratings.")
    st.markdown("- *Experience Analysis*: Examine how experience impacts performance.")
    
if visualization == "Job Role Distribution":
    plot_job_role_distribution(df)
elif visualization == "Performance Rating Distribution":
    plot_performance_rating_distribution(df)
elif visualization == "Job Roles vs. Performance Rating":
    plot_job_roles_vs_performance(df)
elif visualization == "Top Job Roles by Performance Rating":
    plot_top_job_roles_by_performance(df)
elif visualization == "Gender Distribution":
    plot_gender_distribution(df)
elif visualization == "Gender Distribution in Job Roles":
    plot_gender_distribution_in_job_roles(df)
elif visualization == "Gender vs. Performance Rating":
    plot_gender_vs_performance_rating(df)
elif visualization == "Experience Distribution":
    plot_experience_distribution(df)
elif visualization == "Experience vs. Performance Rating":
    plot_experience_vs_performance_rating(df)
elif visualization == "Performance Rating by Years of Experience":
    plot_performance_rating_by_yoe()
elif visualization == "Top 10 Skills":
    plot_top_skills(df)