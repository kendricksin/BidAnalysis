import streamlit as st
from fuzzywuzzy import process
import pandas as pd

def fuzzy_search(query, companies_df, limit=5):
    if not query:
        return []
    
    # Ensure organization_id is treated as string and padded to 13 digits
    companies_df['organization_id'] = companies_df['organization_id'].astype(str).str.zfill(13)
    
    # Combine organization_id and name_english into a single string for searching
    choices = companies_df.apply(lambda row: f"({row['organization_id']}) {row['name_english']}", axis=1).tolist()
    results = process.extract(query, choices, limit=limit*2)  # Get more results initially
    
    # Filter results to only include those with 13-digit IDs
    valid_results = [result for result in results if len(result[0].split(')')[0].strip('(')) == 13]
    
    # Return unique results, limited to the original limit
    return list(dict.fromkeys(result[0] for result in valid_results))[:limit]

def show(companies_df, projects_df):
    st.title('Company Search')

    search_query = st.text_input('Enter company name or ID')

    suggestions = fuzzy_search(search_query, companies_df)

    if suggestions:
        selected_item = st.selectbox("Select a company:", suggestions, key="company_select")
        selected_company_id = selected_item.split(')')[0].strip('(')

        if st.button(f"View details for {selected_item}"):
            st.query_params["page"] = "company"
            st.query_params["id"] = selected_company_id
            st.rerun()
    else:
        st.write("No matches found. Please try a different search term.")

    st.write("You can also access company details directly by using the URL format: `?page=company&id=COMPANY_ID`")