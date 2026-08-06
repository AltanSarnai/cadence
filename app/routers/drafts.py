from fastapi import APIRouter
from app.models import Draft
from app.database import Session
from app.schemas import GetDraftAPIResponse
from pydantic import BaseModel
from sqlalchemy import select
from datetime import datetime, date #potential bug?


router = APIRouter(prefix="/api", tags=["drafts"])

class CreateDraft(BaseModel):

    #id: int
    client_id: int
    title: str
    content: str
    format: str
    created_at: str = date.today()
    voice_score: float
    notes: str
    status: str

class DraftResponse(BaseModel):
    id: int


class UpdateDraftRequest(BaseModel):

    #id: int = None
    #client_id: int = None
    title: str = None 
    content: str = None
    format: str = None
    created_at: datetime = None
    voice_score: float = None
    notes: str = None
    status: str = None    

#client_id is hardcoded from api call
@router.post("/drafts", response_model=DraftResponse)
def create_draft(request: CreateDraft):

    with Session.begin() as session:
        draft = Draft(
            client_id=request.client_id,
            title= request.title,
            content= request.content,
            format=request.format,
            created_at= date.today(),
            voice_score= request.voice_score,#float
            notes= request.notes,
            status= request.status 
        )
        session.add(draft)
        stmt = select(Draft).where(Draft.title == request.title )
        result = session.execute(stmt)
        id = result.scalars().first().id         

    return DraftResponse(id=id)


# Get Draft by ID
@router.get("/drafts/{id}", response_model=GetDraftAPIResponse)
def get_draft(id: int):
    with Session.begin() as session:
            draft = session.query(Draft).get(id)
    
    return draft


# As in update_clients all fields must be passed in
@router.put("/drafts/{id}", response_model=GetDraftAPIResponse)
def update_draft(id: int, request: UpdateDraftRequest):

    with Session.begin() as session:
        stmt = (session.query(Draft)
                .filter(Draft.id == id)
                .update(
                    {
                    Draft.title: request.title,
                    Draft.content: request.content,
                    Draft.format: request.format,
                    #Draft.created_at: date.today(), shouldnt be updated
                    #add a updated date?ß
                    Draft.voice_score: request.voice_score,
                    Draft.notes: request.notes,
                    Draft.status: request.status
                    }
                )
        )
        draft = session.query(Draft).get(id)

    return draft

                     
#Delete Draft by ID
@router.delete("/drafts/{id}")
def delete_draft(id: int):
    with Session.begin() as session:
        draft = session.query(Draft).get(id)
        title = draft.title
        session.delete(draft)

    return f"Successfully deleted draft: {title}"


