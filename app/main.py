import streamlit as st
from pages import homepage, company, company_detail
from utils.data_loader import load_data
from utils.search import fuzzy_search

def initialize_session_state():
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    if 'company_id' not in st.session_state:
        st.session_state.company_id = None
    if 'search_query' not in st.session_state:
        st.session_state.search_query = ''
    if 'search_results' not in st.session_state:
        st.session_state.search_results = []

def main():
    st.set_page_config(page_title="Procurement Dashboard", page_icon="📊", layout="wide")
    
    initialize_session_state()
    
    # Load data
    companies_df, projects_df = load_data()
    
    # Sidebar for navigation
    st.sidebar.title('Navigation')
    if st.sidebar.button('Homepage'):
        st.session_state.page = 'home'
    if st.sidebar.button('Company Search'):
        st.session_state.page = 'search'

    # Persistent search bar in sidebar
    st.sidebar.title('Company Quick Search')
    search_query = st.sidebar.text_input('Enter company name or ID', key='persistent_search', value=st.session_state.search_query)
    if search_query != st.session_state.search_query:
        st.session_state.search_query = search_query
        st.session_state.search_results = fuzzy_search(search_query, companies_df)

    if st.session_state.search_results:
        selected_item = st.sidebar.selectbox("Select a company:", st.session_state.search_results, key="persistent_company_select")
        selected_company_id = selected_item.split(')')[0].strip('(')
        if st.sidebar.button(f"View details for {selected_item}"):
            st.session_state.page = 'company'
            st.session_state.company_id = selected_company_id

    # Route to the appropriate page
    if st.session_state.page == "home":
        homepage.show(companies_df, projects_df)
    elif st.session_state.page == "search":
        company.show(companies_df, projects_df)
    elif st.session_state.page == "company" and st.session_state.company_id:
        company_detail.show(companies_df, projects_df, st.session_state.company_id)
    else:
        st.error("Page not found")

    # Debug information
    st.sidebar.write("Debug Info:")
    st.sidebar.write(f"Current Page: {st.session_state.page}")
    st.sidebar.write(f"Company ID: {st.session_state.company_id}")

if __name__ == "__main__":
    main()