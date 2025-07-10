from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Event(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    date: str
    location: Optional[str] = None
    organizer: str
    capacity: Optional[int] = None
    attendees: int = 0
    createdAt: str = datetime.now().isoformat()

class EventCreate(BaseModel):
    title: str
    description: Optional[str] = None
    date: str
    location: Optional[str] = None
    organizer: str
    capacity: Optional[int] = None

router = APIRouter()

# Dados de exemplo
sample_events = [
    Event(
        id=1,
        title="Palestra sobre Autismo",
        description="Evento especial sobre conscientização do autismo",
        date="2025-06-10T14:00:00",
        location="Centro Comunitário",
        organizer="Secretaria de Saúde",
        capacity=100,
        attendees=25
    ),
    Event(
        id=2,
        title="Workshop de Nutrição",
        description="Saúde e bem-estar através da alimentação",
        date="2025-06-15T09:00:00",
        location="Centro de Saúde Norte",
        organizer="Nutricionistas Voluntários",
        capacity=50,
        attendees=12
    ),
    Event(
        id=3,
        title="Caminhada Saudável",
        description="Atividade física para toda a família",
        date="2025-06-20T07:00:00",
        location="Parque Municipal",
        organizer="Educadores Físicos",
        capacity=200,
        attendees=85
    )
]

@router.get("/", response_model=List[Event])
def listar_eventos():
    return sample_events

@router.get("/{event_id}", response_model=Event)
def detalhes_evento(event_id: int):
    for event in sample_events:
        if event.id == event_id:
            return event
    return Event(
        id=event_id,
        title="Evento Não Encontrado",
        description="Este evento não existe",
        date="2025-01-01T00:00:00",
        organizer="Sistema",
        attendees=0
    )

@router.post("/", response_model=Event)
def criar_evento(event: EventCreate):
    new_id = max([e.id for e in sample_events]) + 1 if sample_events else 1
    new_event = Event(
        id=new_id,
        title=event.title,
        description=event.description,
        date=event.date,
        location=event.location,
        organizer=event.organizer,
        capacity=event.capacity,
        attendees=0
    )
    sample_events.append(new_event)
    return new_event

@router.post("/register")
def registrar_usuario_evento():
    return {"message": "Usuário registrado no evento"}
