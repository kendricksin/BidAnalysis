from fuzzywuzzy import process

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