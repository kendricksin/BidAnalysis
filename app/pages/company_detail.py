import streamlit as st
import pandas as pd
import plotly.express as px
from utils.visualiazations import create_bar_chart, create_pie_chart, create_histogram

def show(companies_df, projects_df, company_id):
    # Add a "Back to Search" button
    if st.button("Back to Search"):
        st.session_state.page = 'search'
        st.rerun()

    company_data = companies_df[companies_df['organization_id'] == company_id].iloc[0]
    company_name = company_data['name_english']
    company_thai = projects_df[projects_df['winner_tin'] == company_id]['winner'].iloc[0]
    st.title(f'Company Details: {company_thai}')

    # Additional company information
    st.subheader('Company Information')
    info_col1, info_col2 = st.columns(2)
    with info_col1:
        st.write(f"**Organization ID:** {company_data['organization_id']}")
        st.write(f"**Type:** {company_data['type']}")
        st.write(f"**Registration Date:** {company_data['registration_date']}")
    with info_col2:
        st.write(f"**Status:** {company_data['status']}")
        st.write(f"**Registered Capital:** ${company_data['registered_capital']:,.2f}")
        st.write(f"**Province:** {company_data['province']}")

    company_projects = projects_df[projects_df['winner_tin'] == company_id].copy()
    company_projects['project_money'] = pd.to_numeric(company_projects['project_money'], errors='coerce')
    company_projects['price_build'] = pd.to_numeric(company_projects['price_build'], errors='coerce')
    company_projects['price_agree'] = pd.to_numeric(company_projects['price_agree'], errors='coerce')

    # Calculate metrics
    total_projects = len(company_projects)
    total_value = company_projects['project_money'].sum()
    median_value = company_projects['project_money'].median()
    avg_value = company_projects['project_money'].mean()
    
    # Calculate average price cut
    company_projects['price_cut'] = (company_projects['price_build'] - company_projects['price_agree']) / company_projects['price_build']
    avg_price_cut = company_projects['price_cut'].mean() * 100  # Convert to percentage

    # Display key metrics
    col1, col2, col3, col4, col5 = st.columns([1,3,3,3,2])
    col1.metric("Total Projects", f"{total_projects:,}")
    col2.metric("Total Project Value", f"${total_value:,.2f}")
    col3.metric("Avg Project Value", f"${avg_value:,.2f}")
    col4.metric("Median Project Value", f"${median_value:,.2f}")
    col5.metric("Avg Price Cut", f"{avg_price_cut:.2f}%")

    # Create two columns for charts
    left_column, right_column = st.columns(2)

    with left_column:
        # Project budget distribution
        st.subheader('Project Budget Distribution')
        fig_budget = create_histogram(company_projects, 'project_money', 'Project Budget Distribution', nbins=30)
        st.plotly_chart(fig_budget, use_container_width=True)

        # Province distribution
        st.subheader('Project Distribution by Province')
        province_distribution = company_projects['province'].value_counts()
        fig_province = create_pie_chart(province_distribution, names=province_distribution.index, values=province_distribution.values, title='Projects by Province')
        st.plotly_chart(fig_province, use_container_width=True)

        # Project Type distribution
        st.subheader('Project Type Distribution')
        type_distribution = company_projects['project_type_name'].value_counts()
        fig_type = create_pie_chart(type_distribution, names=type_distribution.index, values=type_distribution.values, title='Projects by Type')
        st.plotly_chart(fig_type, use_container_width=True)

    with right_column:
        # Bid response time analysis
        st.subheader('Bid Response Time Analysis')
        company_projects['announce_date'] = pd.to_datetime(company_projects['announce_date'])
        company_projects['contract_date'] = pd.to_datetime(company_projects['contract_date'])
        company_projects['bid_response_time'] = (company_projects['contract_date'] - company_projects['announce_date']).dt.days
        fig_response_time = create_histogram(company_projects, 'bid_response_time', 'Bid Response Time (Days)', nbins=30)
        st.plotly_chart(fig_response_time, use_container_width=True)

        # Department distribution
        st.subheader('Project Distribution by Department')
        dept_distribution = company_projects['dept_name'].value_counts()
        fig_dept = create_pie_chart(dept_distribution, names=dept_distribution.index, values=dept_distribution.values, title='Projects by Department')
        st.plotly_chart(fig_dept, use_container_width=True)

        # Project FY distribution
        st.subheader('Project FY Distribution')
        FY_distribution = company_projects['budget_year'].value_counts()
        fig_FY = create_pie_chart(FY_distribution, names=FY_distribution.index, values=FY_distribution.values, title='Projects by FY')
        st.plotly_chart(fig_FY, use_container_width=True)

    # List of past projects won
    st.subheader('Top Projects Won (by value)')
    top_projects = company_projects.sort_values('project_money', ascending=False).head(10)
    top_projects['project_money'] = top_projects['project_money'].apply(lambda x: f"${x:,.2f}")
    top_projects['price_build'] = top_projects['price_build'].apply(lambda x: f"${x:,.2f}")
    top_projects['price_agree'] = top_projects['price_agree'].apply(lambda x: f"${x:,.2f}")
    top_projects['announce_date'] = top_projects['announce_date'].dt.strftime('%Y-%m-%d')
    top_projects['contract_date'] = top_projects['contract_date'].dt.strftime('%Y-%m-%d')
    
    # Custom CSS to reduce font size and allow text wrapping
    st.markdown("""
    <style>
    .dataframe {
        font-size: 0.7rem !important;
    }
    .dataframe td {
        white-space: normal !important;
        max-width: 200px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.dataframe(top_projects[[
        'project_name', 'project_money', 'price_build', 'price_agree', 
        'announce_date', 'contract_date', 'dept_name', 'province', 
        'project_type_name', 'purchase_method_name'
    ]], height=400, use_container_width=True)

