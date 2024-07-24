import streamlit as st
from pages import homepage, company, company_detail
from utils.data_loader import load_data

def main():
    st.set_page_config(page_title="Procurement Dashboard", page_icon="📊", layout="wide")
    
    # Load data
    companies_df, projects_df = load_data()
    
    # Get the current page from the URL
    page = st.experimental_get_query_params().get("page", ["home"])[0]
    company_id = st.experimental_get_query_params().get("id", [None])[0]

    # Sidebar for navigation
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", ['Homepage', 'Company Search'])

    if selection == 'Homepage':
        page = "home"
    elif selection == 'Company Search':
        page = "search"

    # Route to the appropriate page
    if page == "home":
        homepage.show(companies_df, projects_df)
    elif page == "search":
        company.show(companies_df, projects_df)
    elif page == "company" and company_id:
        company_detail.show(companies_df, projects_df, company_id)
    else:
        st.error("Page not found")

if __name__ == "__main__":
    main()