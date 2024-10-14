from sqlalchemy import create_engine,engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




sqlite_url = f"sqlite:///./product.db"#properlocation 
engine = create_engine(sqlite_url, connect_args= {"check_same_thread": False})
SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()