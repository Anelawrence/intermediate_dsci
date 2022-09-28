import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:bulldog11@localhost:5432/demo_db", pool_recycle=-1)
db_engine = engine.connect()
print("engine created successfully")

def query_db(query: str, db_conn: sqlalchemy.engine.base.Connection) -> pd.DataFrame:
    df = pd.read_sql(query, db_conn)
    print(df)
    return df

query_db("SELECT * FROM courses LIMIT 10", db_engine)

db_engine.close()
