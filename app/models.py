from app.database import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import create_engine, DateTime, Integer, String, Float, ForeignKey
from typing import Optional
from datetime import datetime


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    fullname: Mapped[str] = mapped_column(String(100))
    nickname: Mapped[Optional[str]] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(200))
    niche: Mapped[Optional[str]] = mapped_column(String(150))
    brand_profile: Mapped[str] = mapped_column(String)
    key_values: Mapped[Optional[str]] = mapped_column(String)
    target_audience: Mapped[Optional[str]] = mapped_column(String)
    services: Mapped[Optional[str]] = mapped_column(String)
    specialty: Mapped[Optional[str]] = mapped_column(String)
    typical_topics: Mapped[Optional[str]] = mapped_column(String)
    content_length: Mapped[Optional[int]]
    preferred_formats: Mapped[Optional[str]] = mapped_column(String)
    #drafts = Mapped[list["drafts"]]= relationship("Draft") 
    '''client = session.query(Client).first()
    print(client.drafts)  
    # gives you all Draft rows where client_id == this client's id'''

class Draft(Base):
    __tablename__ = "drafts"

    id: Mapped[int] = mapped_column(primary_key=True)  
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(String)
    format: Mapped[str] = mapped_column(String(50))
    created_at:  Mapped[datetime] = mapped_column(DateTime, default="datetime.utcnow" )
    voice_score:  Mapped[Optional[float]] #= mapped_column(float) 
    notes:  Mapped[Optional[str]] = mapped_column(String)
    status: Mapped[Optional[str]] = mapped_column(String(20))
