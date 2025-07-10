from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class HealthServiceCreate(BaseModel):
    name: str
    description: Optional[str] = None
    type: str
    address: Optional[str] = None
    phone: Optional[str] = None
    hours: Optional[str] = None

class HealthService(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    type: str
    address: Optional[str] = None
    phone: Optional[str] = None
    hours: Optional[str] = None
    createdAt: str = datetime.now().isoformat()

router = APIRouter()

# Dados de exemplo
sample_health_services = [
    HealthService(
        id=1,
        name="Academia Municipal",
        description="Academia pública com equipamentos modernos",
        type="academia",
        address="Rua Central, 123 - Centro",
        phone="(11) 3333-4444",
        hours="06:00 - 22:00"
    ),
    HealthService(
        id=2,
        name="Clínica FisioVida",
        description="Clínica especializada em fisioterapia e reabilitação",
        type="fisioterapia",
        address="Av. Saúde, 456 - Bairro Norte",
        phone="(11) 5555-6666",
        hours="08:00 - 18:00"
    ),
    HealthService(
        id=3,
        name="UBS São João",
        description="Unidade Básica de Saúde com atendimento geral",
        type="posto_saude",
        address="Rua das Flores, 789 - São João",
        phone="(11) 7777-8888",
        hours="07:00 - 17:00"
    ),
    HealthService(
        id=4,
        name="Centro de Especialidades",
        description="Centro médico com diversas especialidades",
        type="clinica",
        address="Av. Principal, 321 - Centro",
        phone="(11) 9999-0000",
        hours="08:00 - 20:00"
    )
]

@router.get("/", response_model=List[HealthService])
def listar_servicos():
    return sample_health_services

@router.get("/{service_id}", response_model=HealthService)
def detalhes_servico(service_id: int):
    for service in sample_health_services:
        if service.id == service_id:
            return service
    return HealthService(
        id=service_id,
        name="Serviço não encontrado",
        type="unknown",
        address="N/A",
        description="Este serviço não existe"
    )

@router.post("/", response_model=HealthService)
def criar_servico(service_data: HealthServiceCreate):
    new_id = max([s.id for s in sample_health_services]) + 1 if sample_health_services else 1
    new_service = HealthService(
        id=new_id,
        name=service_data.name,
        description=service_data.description,
        type=service_data.type,
        address=service_data.address,
        phone=service_data.phone,
        hours=service_data.hours
    )
    sample_health_services.append(new_service)
    return new_service
