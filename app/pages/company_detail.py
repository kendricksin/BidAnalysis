import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from scipy import stats

def show(companies_df, projects_df, company_id):
    company_data = companies_df[companies_df['organization_id'] == company_id].iloc[0]
    company_name = company_data['name_english']
    
    st.title(f'Company Details: {company_name}')

    company_projects = projects_df[projects_df['winner_tin'] == company_id].copy()
    company_projects['project_money'] = pd.to_numeric(company_projects['project_money'], errors='coerce')

    # Calculate total projects and total value
    total_projects = len(company_projects)
    total_value = company_projects['project_money'].sum()

    # Display key metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Projects", f"{total_projects:,}")
    col2.metric("Total Project Value", f"${total_value:,.2f}")
    col3.metric("Avg Project Value", f"${total_value/total_projects:,.2f}" if total_projects > 0 else "$0")

    # Project budget distribution
    st.subheader('Project Budget Distribution')
    if not company_projects.empty:
        fig = px.histogram(company_projects, x='project_money', nbins=30, height=300)
        
        # Calculate normal distribution
        mean = company_projects['project_money'].mean()
        std = company_projects['project_money'].std()
        x = np.linspace(company_projects['project_money'].min(), company_projects['project_money'].max(), 100)
        y = stats.norm.pdf(x, mean, std)
        
        # Scale the normal distribution to match the histogram
        y_scaled = y * (len(company_projects) * (company_projects['project_money'].max() - company_projects['project_money'].min()) / 30)
        
        # Add normal distribution curve
        fig.add_trace(go.Scatter(x=x, y=y_scaled, mode='lines', name='Normal Distribution'))
        
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No project data available.")

    # Add more visualizations and data as needed...

    # List of past projects won
    st.subheader('Top Projects Won (by value)')
    if not company_projects.empty:
        top_projects = company_projects.sort_values('project_money', ascending=False).head(10)
        top_projects['project_money'] = top_projects['project_money'].apply(lambda x: f"${x:,.2f}")
        top_projects['announce_date'] = pd.to_datetime(top_projects['announce_date']).dt.strftime('%Y-%m-%d')
        st.dataframe(top_projects[['project_name', 'project_money', 'announce_date', 'dept_name', 'province']], height=400)
    else:
        st.write("No project data available.")