from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers import aluno
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código de inicialização da API
    logger.info("API Iniciada")
    
    yield  # reprenta ação do tempo de vida da aplicação
    
    # Código de finalização da API
    logger.info("API Finalizada")

# Crio o objeto da API
app = FastAPI(lifespan=lifespan)

# # Evento de inicialização da aplicação (Old way)
# @app.on_event("startup")
# def startup_event():
#     logger.info("Aplicação iniciada com sucesso!")

# # Evento de encerramento da aplicação (Old way)
# @app.on_event("shutdown")
# def shutdown_event():
#     logger.info("Aplicação encerrada!")

app.include_router(aluno.router, prefix="/buscar-aluno", tags=["Aluno"])

# app.include_router(aluno.router, prefix="/buscar-endereco-aluno", tags=["Aluno"])