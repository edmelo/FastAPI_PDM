from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AppointmentCreate(BaseModel):
    title: str
    description: Optional[str] = None
    date: str  # ISO format: "2024-01-15T10:30:00"
    location: Optional[str] = None
    patientName: str
    doctorName: Optional[str] = None

class Appointment(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    date: str
    location: Optional[str] = None
    patientName: str
    doctorName: Optional[str] = None
    status: str = "scheduled"
    createdAt: str = datetime.now().isoformat()

class Professional(BaseModel):
    id: int
    name: str
    specialty: str
    location: Optional[str] = None

router = APIRouter()

# Dados de exemplo
sample_appointments = [
    Appointment(
        id=1,
        title="Consulta de Fisioterapia",
        description="Sessão de fisioterapia para reabilitação",
        date="2025-01-15T09:00:00",
        location="Centro de Reabilitação",
        patientName="Maria Silva",
        doctorName="Dra. Ana Santos",
        status="scheduled"
    ),
    Appointment(
        id=2,
        title="Consulta Nutricional",
        description="Avaliação nutricional e planejamento dietético",
        date="2025-01-16T14:30:00",
        location="Clínica de Nutrição",
        patientName="João Oliveira",
        doctorName="Dr. Carlos Mendes",
        status="confirmed"
    )
]

sample_professionals = [
    Professional(id=1, name="Dra. Ana Santos", specialty="Fisioterapia", location="Centro de Reabilitação"),
    Professional(id=2, name="Dr. Carlos Mendes", specialty="Nutrição", location="Clínica de Nutrição"),
    Professional(id=3, name="Dr. Pedro Lima", specialty="Cardiologia", location="Hospital Municipal")
]

@router.get("/", response_model=List[Appointment])
def listar_agendamentos():
    return sample_appointments

@router.get("/{appointment_id}", response_model=Appointment)
def obter_agendamento(appointment_id: int):
    for appointment in sample_appointments:
        if appointment.id == appointment_id:
            return appointment
    return Appointment(
        id=appointment_id,
        title="Agendamento não encontrado",
        date="2025-01-01T00:00:00",
        patientName="N/A",
        status="not_found"
    )

@router.post("/", response_model=Appointment)
def criar_agendamento(appointment_data: AppointmentCreate):
    new_id = max([a.id for a in sample_appointments]) + 1 if sample_appointments else 1
    new_appointment = Appointment(
        id=new_id,
        title=appointment_data.title,
        description=appointment_data.description,
        date=appointment_data.date,
        location=appointment_data.location,
        patientName=appointment_data.patientName,
        doctorName=appointment_data.doctorName,
        status="scheduled"
    )
    sample_appointments.append(new_appointment)
    return new_appointment

@router.put("/{appointment_id}", response_model=Appointment)
def atualizar_agendamento(appointment_id: int, appointment_data: AppointmentCreate):
    for i, appointment in enumerate(sample_appointments):
        if appointment.id == appointment_id:
            updated_appointment = Appointment(
                id=appointment_id,
                title=appointment_data.title,
                description=appointment_data.description,
                date=appointment_data.date,
                location=appointment_data.location,
                patientName=appointment_data.patientName,
                doctorName=appointment_data.doctorName,
                status=appointment.status,
                createdAt=appointment.createdAt
            )
            sample_appointments[i] = updated_appointment
            return updated_appointment
    return obter_agendamento(appointment_id)

@router.delete("/{appointment_id}")
def deletar_agendamento(appointment_id: int):
    global sample_appointments
    sample_appointments = [a for a in sample_appointments if a.id != appointment_id]
    return {"message": "Agendamento deletado com sucesso"}

@router.get("/professionals", response_model=List[Professional])
def listar_profissionais():
    return sample_professionals

@router.get("/time-slots")
def listar_horarios():
    return ["09:00", "10:00", "11:00", "14:00", "15:00", "16:00"]
