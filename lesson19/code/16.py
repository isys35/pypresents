from sqlalchemy.orm import Session, sessionmaker

session = sessionmaker(bind=engine)
