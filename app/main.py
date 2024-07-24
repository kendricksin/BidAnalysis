import streamlit as st
from app.pages import homepage, company_search
from app.utils.data_loader import load_data

def main():
    st.set_page_config(page_title="Procurement Dashboard", page_icon="📊", layout="wide")
    
    # Load data
    companies_df, projects_df = load_data()
    
    # Sidebar for navigation
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", ['Homepage', 'Company Search'])

    if selection == 'Homepage':
        homepage.show(companies_df, projects_df)
    elif selection == 'Company Search':
        company_search.show(companies_df, projects_df)

if __name__ == "__main__":
    main()