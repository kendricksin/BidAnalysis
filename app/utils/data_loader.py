import pandas as pd
from sqlalchemy import create_engine
from config.settings import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

def load_data():
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}', 
                           client_encoding='utf8')
    
    companies_df = pd.read_sql_table('companies', engine)
    projects_df = pd.read_sql_table('gov_procurement', engine)
    
    print(f"Loaded {len(companies_df)} companies and {len(projects_df)} projects")
    print(f"Companies columns: {companies_df.columns.tolist()}")
    print(f"Projects columns: {projects_df.columns.tolist()}")
    
    return companies_df, projects_df