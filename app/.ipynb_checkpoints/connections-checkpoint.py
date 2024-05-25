from sqlalchemy import create_engine

def get_connection():
    return  create_engine("postgresql+psycopg2://postgres:ThWicz2409@personal.cxe0iuo8g20s.us-east-1.rds.amazonaws.com:5432/postgres")