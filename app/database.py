from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, text, select


#use pathlib for robust cadence.db
engine = create_engine("sqlite:///cadence.db", echo=True)# cadence.db will be created?


class Base(DeclarativeBase):
    pass



Session = sessionmaker(bind=engine, expire_on_commit=False)
session = Session()
Base.metadata.create_all(engine)