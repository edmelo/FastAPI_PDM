from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

class Resource(BaseModel):
    id: int
    nome: str
    tipo: str

class AutismProfessional(BaseModel):
    id: int
    nome: str
    especialidade: str

class QuietHour(BaseModel):
    id: int
    local: str
    horario: str

class Facility(BaseModel):
    id: int
    nome: str
    tipo: str

router = APIRouter()

@router.get("/", response_model=List[Resource])
def listar_recursos():
    return [
        Resource(id=1, nome="Profissionais Autismo", tipo="especialista"),
        Resource(id=2, nome="Academia Acessível", tipo="acessibilidade")
    ]

@router.get("/{resource_id}", response_model=Resource)
def detalhes_recurso(resource_id: int):
    return Resource(id=resource_id, nome="Exemplo", tipo="especialista")

@router.post("/")
def criar_recurso():
    return {"message": "Recurso criado"}

@router.post("/rate")
def avaliar_recurso():
    return {"message": "Recurso avaliado"}

@router.get("/autism/professionals", response_model=List[AutismProfessional])
def listar_profissionais_autismo():
    return [AutismProfessional(id=1, nome="Dra. Clara", especialidade="Psicologia"), AutismProfessional(id=2, nome="Dr. Paulo", especialidade="Fonoaudiologia")]

@router.get("/autism/quiet-hours", response_model=List[QuietHour])
def listar_horarios_tranquilos():
    return [QuietHour(id=1, local="Academia Municipal", horario="14:00-16:00")]

@router.get("/accessibility/facilities", response_model=List[Facility])
def listar_instalacoes_acessiveis():
    return [Facility(id=1, nome="Parque Central", tipo="parque"), Facility(id=2, nome="Ginásio Inclusivo", tipo="ginásio")]

