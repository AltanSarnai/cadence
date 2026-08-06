from fastapi import APIRouter
from pydantic import BaseModel
from app.database import Session
from app.models import Client
from app.schemas import ClientAPIResponse, GetClientAPIResponse
from sqlalchemy import select, text, delete#,update

router = APIRouter(prefix="/api", tags=["clients"])

class CreateClientRequest(BaseModel):
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

class ClientResponse(BaseModel):
    id: int

class GetClientRequest(BaseModel):
    id: int

class UpdateClientRequest(BaseModel):
    name: str = None
    fullname: str = None
    nickname: str = None # = name?
    description: str = None
    niche: str = None
    brand_profile: str = None
    key_values: str = None
    target_audience: str = None
    services: str = None
    specialty: str = None
    typical_topics: str = None
    content_length: str = None
    preferred_formats: str = None


@router.post("/clients", response_model=ClientResponse)
def create_client(request: CreateClientRequest):
    with Session.begin() as session:
        new_client = Client(
            name=request.name,
            fullname=request.fullname,
            nickname=request.nickname,
            description=request.description,
            niche=request.niche,
            brand_profile=request.brand_profile,
            key_values=request.key_values,
            target_audience=request.target_audience,
            services=request.services,
            specialty=request.specialty,
            typical_topics=request.typical_topics,
            content_length=request.content_length,
            preferred_formats=request.preferred_formats
        )

        session.add(new_client)
        stmt = select(Client).where(Client.name == request.name )
        result = session.execute(stmt)
        id = result.scalars().first().id #return the newly created client id.

    return ClientResponse(id=id)


@router.get("/clients", response_model=list[ClientAPIResponse])
def get_all_clients():

    with Session.begin() as session:
        clients = session.query(Client).all() # all(): Return the results represented by this Query as a list

    return clients

@router.get("/clients/{id}", response_model=ClientAPIResponse)#reuse clientapiresponse
def get_client(id: int):
    with Session.begin() as session:
        client = session.query(Client).get(id)

    return client

#All fields must be sent.. think of using PATCH. to send just one=< to update
@router.put("/clients/{id}", response_model=ClientAPIResponse)
def update_client(id: int, request: UpdateClientRequest):
    with Session.begin() as session:
        stmt = (session.query(Client)
                .filter(Client.id == id)
                .update(
                    {
                    Client.name: request.name,
                    Client.fullname: request.fullname,
                    Client.nickname: request.nickname,
                    Client.description: request.description,
                    Client.niche: request.niche,
                    Client.brand_profile: request.brand_profile,                    
                    Client.key_values: request.key_values,
                    Client.target_audience: request.target_audience,
                    Client.services: request.services,
                    Client.specialty: request.specialty,
                    Client.typical_topics: request.typical_topics,
                    Client.content_length: request.content_length,
                    Client.preferred_formats: request.preferred_formats 
                    }
                )
        )
        client = session.query(Client).get(id)
    return client


@router.delete("/clients/{id}")
def update_client(id: int):
    with Session.begin() as session:
        stmt = delete(Client).where(Client.id == id)
        session.execute(stmt)
    success_message = f"\nClient with id= {id} deleted successfully.\n\n"
    return success_message
