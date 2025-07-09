from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

class Professional(BaseModel):
    id: int
    nome: str
    especialidade: str

class Appointment(BaseModel):
    id: int
    user_id: int
    professional_id: int
    horario: str

router = APIRouter()

@router.get("/professionals", response_model=List[Professional])
def listar_profissionais():
    return [
        Professional(id=1, nome="Dra. Ana", especialidade="Fisioterapia"),
        Professional(id=2, nome="Dr. João", especialidade="Nutrição")
    ]

@router.get("/time-slots")
def listar_horarios():
    return ["09:00", "10:00", "11:00"]

@router.post("/")
def criar_agendamento(agendamento: Appointment):
    return agendamento

@router.get("/user/{user_id}")
def listar_agendamentos_usuario(user_id: int):
    return []

@router.put("/{appointment_id}/cancel")
def cancelar_agendamento(appointment_id: int):
    return {"message": "Agendamento cancelado"}

