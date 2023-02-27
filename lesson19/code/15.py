from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg2://postgres:1111@localhost/sqlalchemy_tuts")
session = Session(bind=engine)
