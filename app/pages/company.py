import streamlit as st
from fuzzywuzzy import process

def fuzzy_search(query, companies_df, limit=5):
    if not query:
        return []
    
    choices = companies_df['organization_id'].tolist() + companies_df['name_english'].tolist()
    results = process.extract(query, choices, limit=limit)
    
    unique_results = []
    seen = set()
    for result in results:
        if result[0] not in seen:
            unique_results.append(result[0])
            seen.add(result[0])
    
    return unique_results

def show(companies_df, projects_df):
    st.title('Company Search')

    search_query = st.text_input('Enter company name or ID')

    company_name_to_id = dict(zip(companies_df['name_english'], companies_df['organization_id']))
    company_id_to_name = dict(zip(companies_df['organization_id'], companies_df['name_english']))

    suggestions = fuzzy_search(search_query, companies_df)

    if suggestions:
        selected_item = st.selectbox("Select a company:", suggestions, key="company_select")
        if selected_item in company_id_to_name:
            selected_company_id = selected_item
            selected_company_name = company_id_to_name[selected_item]
        else:
            selected_company_name = selected_item
            selected_company_id = company_name_to_id[selected_item]

        if st.button(f"View details for {selected_company_name}"):
            st.experimental_set_query_params(page="company", id=selected_company_id)
            st.experimental_rerun()
    else:
        st.write("No matches found. Please try a different search term.")

    st.write("You can also access company details directly by using the URL format: `localhost:8501/?page=company&id=COMPANY_ID`")