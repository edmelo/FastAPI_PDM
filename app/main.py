from fastapi import FastAPI
from app.routes import health_services, events, appointments, community, routes, resources

app = FastAPI(
    title="Cidade Saudável API",
    description="Backend do app Cidade Saudável",
    version="0.1.0"
)

app.include_router(health_services.router, prefix="/api/health-services", tags=["Serviços de Saúde"])
app.include_router(events.router, prefix="/api/events", tags=["Eventos"])
app.include_router(appointments.router, prefix="/api/appointments", tags=["Agendamentos"])
app.include_router(community.router, prefix="/api/community", tags=["Comunidade"])
app.include_router(routes.router, prefix="/api/routes", tags=["Rotas"])
app.include_router(resources.router, prefix="/api/resources", tags=["Recursos Especiais"])

