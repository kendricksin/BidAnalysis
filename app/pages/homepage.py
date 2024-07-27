import streamlit as st
import plotly.express as px
from utils.visualiazations import create_thailand_bubble_map
from utils.province_mapping import province_to_coordinates

def show(companies_df, projects_df):
    st.title('Procurement Dashboard - Homepage')

    # Summary statistics
    st.header('Summary Statistics')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Companies", len(companies_df))
    with col2:
        st.metric("Total Projects", len(projects_df))
    with col3:
        st.metric("Total Project Value", f"${projects_df['project_money'].astype(float).sum():,.0f}")

    # Top 10 companies by project count
    st.subheader('Top 10 Companies by Project Count')
    top_companies = projects_df['winner'].value_counts().head(10)
    fig = px.bar(top_companies, x=top_companies.index, y=top_companies.values)
    st.plotly_chart(fig)

    # Project distribution by province (bubble map)
    st.subheader('Project Distribution by Province')
    province_distribution = projects_df['province'].value_counts().reset_index()
    province_distribution.columns = ['province', 'count']
    
    # Map province names to coordinates
    province_distribution['lat'] = province_distribution['province'].map(lambda x: province_to_coordinates.get(x, {}).get('lat'))
    province_distribution['lon'] = province_distribution['province'].map(lambda x: province_to_coordinates.get(x, {}).get('lon'))
    
    # Remove rows with missing coordinates
    province_distribution = province_distribution.dropna(subset=['lat', 'lon'])
    
    fig = create_thailand_bubble_map(province_distribution, 'lat', 'lon', 'count', 'Project Count by Province')
    st.plotly_chart(fig)

    # Project distribution by department
    st.subheader('Project Distribution by Department')
    dept_distribution = projects_df['dept_name'].value_counts().head(10)
    fig = px.pie(dept_distribution, values=dept_distribution.values, names=dept_distribution.index)
    st.plotly_chart(fig)

    # Project value distribution
    st.subheader('Project Value Distribution')
    fig = px.histogram(projects_df, x='project_money', nbins=50, log_y=True)
    fig.update_xaxes(title='Project Value')
    fig.update_yaxes(title='Count (log scale)')
    st.plotly_chart(fig)
