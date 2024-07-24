import pandas as pd
from sqlalchemy import create_engine
from app.config.settings import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

def load_data():
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}', 
                           client_encoding='utf8')
    
    companies_df = pd.read_sql_table('companies', engine)
    projects_df = pd.read_sql_table('gov_procurement', engine)
    
    return companies_df, projects_df