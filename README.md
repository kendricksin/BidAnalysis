Just install requirements.txt and use streamlit run app/main.py

app runs on a postgres database with following structure:

bid_db=# \d companies
                        Table "public.companies"
       Column       |       Type       | Collation | Nullable | Default
--------------------+------------------+-----------+----------+---------
 organization_id    | text             |           | not null |
 name_english       | text             |           |          |
 type               | text             |           |          |
 registration_date  | date             |           |          |
 status             | text             |           |          |
 objective_code     | text             |           |          |
 objective_english  | text             |           |          |
 registered_capital | double precision |           |          |
 province           | text             |           |          |
Indexes:
    "companies_pkey" PRIMARY KEY, btree (organization_id)

bid_db=# \d gov_procurement
                   Table "public.gov_procurement"
           Column           | Type | Collation | Nullable | Default
----------------------------+------+-----------+----------+---------
 project_id                 | text |           | not null |
 project_type_name          | text |           |          |
 project_name               | text |           |          |
 dept_name                  | text |           |          |
 province                   | text |           |          |
 contract_no                | text |           |          |
 dept_sub_name              | text |           |          |
 purchase_method_group_name | text |           |          |
 district                   | text |           |          |
 winner                     | text |           |          |
 price_build                | text |           |          |
 project_status             | text |           |          |
 contract_date              | text |           |          |
 budget_year                | text |           |          |
 subdistrict                | text |           |          |
 purchase_method_name       | text |           |          |
 announce_date              | text |           |          |
 sum_price_agree            | text |           |          |
 winner_tin                 | text |           |          |
 status                     | text |           |          |
 price_agree                | text |           |          |
 contract_finish_date       | text |           |          |
 transaction_date           | text |           |          |
 project_money              | text |           |          |
 geom                       | text |           |          |
Indexes:
    "gov_procurement_pkey" PRIMARY KEY, btree (project_id)