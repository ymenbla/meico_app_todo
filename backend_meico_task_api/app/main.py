from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from fastapi.openapi.utils import get_openapi
from app.routers.auth_router import auth
from app.routers.task_router import task

from app.config.db import Base, engine
from app.config.settings import settings

app = FastAPI(title="App Meico ToDo")

origins = [
    "http://localhost:4200",   # Angular local
    # "http://localhost:3000",   # React local
    # "https://tu-dominio.com",  # Producción
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # Dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],        # Métodos permitidos: GET, POST, PUT, DELETE...
    allow_headers=["*"],        # Headers permitidos: Authorization, Content-Type...
)

Base.metadata.create_all(bind=engine)

app.include_router(auth, prefix=settings.PREFIX_API)
app.include_router(task, prefix=settings.PREFIX_API)

# Personalizar OpenAPI para que Swagger muestre "Authorize"
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="App Meico ToDo",
        version="1.0.0",
        description="API con JWT Auth usando email/password",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi