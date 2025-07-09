from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

class Route(BaseModel):
    id: int
    nome: str
    dificuldade: str
    distancia_km: float

class Review(BaseModel):
    id: int
    route_id: int
    texto: str

router = APIRouter()

@router.get("/", response_model=List[Route])
def listar_rotas():
    return [
        Route(id=1, nome="Trilha do Parque", dificuldade="Fácil", distancia_km=3.5),
        Route(id=2, nome="Ciclovia Central", dificuldade="Média", distancia_km=7.2)
    ]

@router.get("/{route_id}", response_model=Route)
def detalhes_rota(route_id: int):
    return Route(id=route_id, nome="Exemplo", dificuldade="Fácil", distancia_km=5.0)

@router.post("/")
def criar_rota():
    return {"message": "Rota criada"}

@router.get("/{route_id}/reviews", response_model=List[Review])
def listar_reviews(route_id: int):
    return [Review(id=1, route_id=route_id, texto="Ótima rota!")]

@router.post("/reviews")
def adicionar_review():
    return {"message": "Avaliação adicionada"}

