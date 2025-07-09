from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

class ForumPost(BaseModel):
    id: int
    titulo: str
    conteudo: str

class Comment(BaseModel):
    id: int
    post_id: int
    texto: str

class ChatRoom(BaseModel):
    id: int
    nome: str

class ChatMessage(BaseModel):
    id: int
    room_id: int
    texto: str

router = APIRouter()

@router.get("/forums", response_model=List[ForumPost])
def listar_foruns():
    return [
        ForumPost(id=1, titulo="Grupo Autismo", conteudo="Discussão sobre autismo"),
        ForumPost(id=2, titulo="Ciclistas", conteudo="Rotas e dicas")
    ]

@router.get("/forums/{post_id}", response_model=ForumPost)
def detalhes_forum(post_id: int):
    return ForumPost(id=post_id, titulo="Exemplo", conteudo="Conteúdo exemplo")

@router.post("/forums")
def criar_forum():
    return {"message": "Post criado"}

@router.get("/forums/{post_id}/comments", response_model=List[Comment])
def listar_comentarios(post_id: int):
    return [Comment(id=1, post_id=post_id, texto="Comentário exemplo")]

@router.post("/comments")
def adicionar_comentario():
    return {"message": "Comentário adicionado"}

@router.get("/chat/rooms", response_model=List[ChatRoom])
def listar_salas():
    return [ChatRoom(id=1, nome="Sala 1"), ChatRoom(id=2, nome="Sala 2")]

@router.get("/chat/rooms/{room_id}/messages", response_model=List[ChatMessage])
def listar_mensagens(room_id: int):
    return [ChatMessage(id=1, room_id=room_id, texto="Mensagem exemplo")]

@router.post("/chat/messages")
def enviar_mensagem():
    return {"message": "Mensagem enviada"}

