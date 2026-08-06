from pydantic import BaseModel, ConfigDict 
from datetime import datetime


#Pydantic Schemas
class ClientAPIResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    fullname: str
    nickname: str # = name?
    description: str
    niche: str
    brand_profile: str 
    key_values: str
    target_audience: str
    services: str
    specialty: str
    typical_topics: str
    content_length: str
    preferred_formats: str


class GetClientAPIResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    fullname: str
    nickname: str # = name?
    description: str
    niche: str
    brand_profile: str 
    key_values: str
    target_audience: str
    services: str
    specialty: str
    typical_topics: str
    content_length: str
    preferred_formats: str



class GetDraftAPIResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    client_id: int   
    title: str
    content: str
    format: str 
    created_at: datetime
    voice_score: float
    notes: str
    status: str 