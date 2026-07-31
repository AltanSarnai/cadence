from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine


#use pathlib for robust cadence.db
engine = create_engine("sqlite:///cadence.db", echo=True)# cadence.db will be created?


class Base(DeclarativeBase):
    pass
