from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="sqlite:///./database.db"
db_engine=create_engine(DATABASE_URL)
db_session=sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
Base=declarative_base()




