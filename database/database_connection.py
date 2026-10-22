from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text

load_dotenv(override=True)

database_url = os.getenv("dburl")
if database_url is None:
    raise ValueError()

engine = create_engine(database_url, connect_args={"ssl": {}})
def connect_db()->bool:
    with engine.connect() as connection:
        try:
            connection.execute(text("select 1"))
            return True
        except Exception as e:
            print(e)
            return False

