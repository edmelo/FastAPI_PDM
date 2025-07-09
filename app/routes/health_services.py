from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

class HealthService(BaseModel):
    id: int
    nome: str
    tipo: str
    endereco: str
    preco: Optional[str] = None

router = APIRouter()

@router.get("/", response_model=List[HealthService])
def listar_servicos():
    return [
        HealthService(id=1, nome="Academia Municipal", tipo="academia", endereco="Rua A, 123", preco="Grátis"),
        HealthService(id=2, nome="Clínica FisioVida", tipo="fisioterapia", endereco="Av. B, 456", preco="R$ 80")
    ]

@router.get("/{service_id}", response_model=HealthService)
def detalhes_servico(service_id: int):
    return HealthService(id=service_id, nome="Exemplo", tipo="academia", endereco="Rua Exemplo, 1", preco="R$ 50")

