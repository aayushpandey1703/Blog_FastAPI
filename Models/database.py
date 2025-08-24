from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="sqlite:///./database.db"
db_engine=create_engine(DATABASE_URL)
# for creating db session
db_session=sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
## for defining models
Base=declarative_base()

def get_db():
    try:
        db=db_session()
        yield db
    finally:
        db.close()





