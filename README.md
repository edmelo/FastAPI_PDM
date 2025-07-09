# Cidade Saudável API

Esta é uma API desenvolvida com FastAPI para gerenciar recursos de uma aplicação de saúde comunitária, incluindo agendamentos, eventos, serviços de saúde e recursos comunitários.

## Tecnologias Utilizadas
- Python 3.11+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- PyJWT
- python-multipart

## Estrutura do Projeto
```
backend/
│   requirements.txt
└───app/
    │   main.py
    └───routes/
            __init__.py
            appointments.py
            community.py
            events.py
            health_services.py
            resources.py
            routes.py
```

## Instalação
1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd backend
   ```
2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Executando a API
Execute o servidor de desenvolvimento com Uvicorn:
```bash
uvicorn app.main:app --reload
```
Acesse a documentação automática em: [http://localhost:8000/docs](http://localhost:8000/docs)

## Estrutura das Rotas
- `/appointments` — Gerenciamento de agendamentos
- `/community` — Recursos da comunidade
- `/events` — Eventos comunitários
- `/health_services` — Serviços de saúde
- `/resources` — Recursos diversos

## Autenticação
A autenticação é baseada em JWT. Consulte as rotas protegidas para detalhes de uso.

## Contribuição
Pull requests são bem-vindos! Para grandes mudanças, abra uma issue primeiro para discutir o que você gostaria de modificar.

## Licença
Este projeto está sob a licença MIT.

