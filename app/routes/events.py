from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    titulo: str
    descricao: str
    data: str

router = APIRouter()

@router.get("/", response_model=List[Event])
def listar_eventos():
    return [
        Event(id=1, titulo="Palestra sobre Autismo", descricao="Evento especial", data="2025-06-10"),
        Event(id=2, titulo="Workshop de Nutrição", descricao="Saúde e bem-estar", data="2025-06-15")
    ]

@router.get("/{event_id}", response_model=Event)
def detalhes_evento(event_id: int):
    return Event(id=event_id, titulo="Exemplo", descricao="Descrição", data="2025-06-20")

@router.post("/register")
def registrar_usuario_evento():
    return {"message": "Usuário registrado no evento"}

