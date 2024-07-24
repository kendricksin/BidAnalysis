import streamlit as st
import pandas as pd
import plotly.express as px
from fuzzywuzzy import process

def fuzzy_search(query, choices, limit=5):
    results = process.extract(query, choices, limit=limit)
    return [result[0] for result in results]

def show(companies_df, projects_df):
    st.title('Company Search')

    # Search bar
    search_query = st.text_input('Enter company name')

    if search_query:
        company_names = companies_df['name_english'].tolist()
        search_results = fuzzy_search(search_query, company_names)

        selected_company = st.selectbox('Select a company', search_results)

        if selected_company:
            st.subheader(f'Statistics for {selected_company}')

            # Get company data
            company_data = companies_df[companies_df['name_english'] == selected_company].iloc[0]
            company_projects = projects_df[projects_df['winner'] == selected_company]

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Projects", len(company_projects))
            with col2:
                st.metric("Total Project Value", f"${company_projects['project_money'].astype(float).sum():,.0f}")

            # Project budget distribution
            st.subheader('Project Budget Distribution')
            fig = px.histogram(company_projects, x='project_money', nbins=30)
            fig.update_xaxes(title='Project Value')
            fig.update_yaxes(title='Count')
            st.plotly_chart(fig)

            # Department distribution
            st.subheader('Department Distribution')
            dept_dist = company_projects['dept_name'].value_counts()
            fig = px.pie(dept_dist, values=dept_dist.values, names=dept_dist.index)
            st.plotly_chart(fig)

            # Province distribution
            st.subheader('Province Distribution')
            province_dist = company_projects['province'].value_counts()
            fig = px.pie(province_dist, values=province_dist.values, names=province_dist.index)
            st.plotly_chart(fig)

            # Project duration distribution
            st.subheader('Project Duration Distribution')
            company_projects['contract_date'] = pd.to_datetime(company_projects['contract_date'])
            company_projects['contract_finish_date'] = pd.to_datetime(company_projects['contract_finish_date'])
            company_projects['duration'] = (company_projects['contract_finish_date'] - company_projects['contract_date']).dt.days
            fig = px.histogram(company_projects, x='duration', nbins=30)
            fig.update_xaxes(title='Duration (days)')
            fig.update_yaxes(title='Count')
            st.plotly_chart(fig)