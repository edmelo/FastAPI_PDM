from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class CommunityResourceCreate(BaseModel):
    name: str
    description: Optional[str] = None
    type: str
    address: Optional[str] = None
    contact: Optional[str] = None
    availability: Optional[str] = None

class CommunityResource(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    type: str
    address: Optional[str] = None
    contact: Optional[str] = None
    availability: Optional[str] = None
    createdAt: str = datetime.now().isoformat()

class ForumPost(BaseModel):
    id: int
    title: str
    content: str
    author: str
    created_at: str = datetime.now().isoformat()

class Comment(BaseModel):
    id: int
    post_id: int
    text: str
    author: str
    created_at: str = datetime.now().isoformat()

router = APIRouter()

# Dados de exemplo para recursos da comunidade
sample_community_resources = [
    CommunityResource(
        id=1,
        name="Grupo de Apoio ao Autismo",
        description="Grupo de famílias e cuidadores para apoio mútuo",
        type="grupo_apoio",
        address="Centro Comunitário - Rua das Palmeiras, 100",
        contact="grupoautismo@email.com",
        availability="Terças-feiras às 19h"
    ),
    CommunityResource(
        id=2,
        name="Clube de Ciclismo Saudável",
        description="Grupo para prática de ciclismo e atividades ao ar livre",
        type="atividade_fisica",
        address="Parque Municipal",
        contact="(11) 9999-1234",
        availability="Sábados às 8h e Domingos às 16h"
    ),
    CommunityResource(
        id=3,
        name="Horta Comunitária",
        description="Espaço para cultivo coletivo de alimentos orgânicos",
        type="agricultura_urbana",
        address="Rua Verde, 500 - Bairro Jardim",
        contact="horta.comunidade@email.com",
        availability="Diariamente das 6h às 18h"
    )
]

# Dados de exemplo para fórum
sample_forum_posts = [
    ForumPost(
        id=1,
        title="Dicas para famílias com autismo",
        content="Compartilho aqui algumas estratégias que têm funcionado bem em casa...",
        author="Maria Santos"
    ),
    ForumPost(
        id=2,
        title="Melhores rotas de ciclismo na cidade",
        content="Pessoal, vamos compartilhar as melhores rotas para pedalar com segurança...",
        author="João Pedalada"
    ),
    ForumPost(
        id=3,
        title="Receitas saudáveis da horta",
        content="Que tal trocarmos receitas usando os vegetais da nossa horta comunitária?",
        author="Ana Verde"
    )
]

@router.get("/", response_model=List[CommunityResource])
def listar_recursos_comunidade():
    return sample_community_resources

@router.get("/{resource_id}", response_model=CommunityResource)
def obter_recurso_comunidade(resource_id: int):
    for resource in sample_community_resources:
        if resource.id == resource_id:
            return resource
    return CommunityResource(
        id=resource_id,
        name="Recurso não encontrado",
        type="unknown",
        description="Este recurso não existe"
    )

@router.post("/", response_model=CommunityResource)
def criar_recurso_comunidade(resource_data: CommunityResourceCreate):
    new_id = max([r.id for r in sample_community_resources]) + 1 if sample_community_resources else 1
    new_resource = CommunityResource(
        id=new_id,
        name=resource_data.name,
        description=resource_data.description,
        type=resource_data.type,
        address=resource_data.address,
        contact=resource_data.contact,
        availability=resource_data.availability
    )
    sample_community_resources.append(new_resource)
    return new_resource

@router.get("/forums", response_model=List[ForumPost])
def listar_foruns():
    return sample_forum_posts

@router.get("/forums/{post_id}", response_model=ForumPost)
def obter_post_forum(post_id: int):
    for post in sample_forum_posts:
        if post.id == post_id:
            return post
    return ForumPost(
        id=post_id,
        title="Post não encontrado",
        content="Este post não existe",
        author="Sistema"
    )
