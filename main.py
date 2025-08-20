from fastapi import FastAPI
from routers import aluno
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Evento de inicialização da aplicação
@app.on_event("startup")
def startup_event():
    logger.info("Aplicação iniciada com sucesso!")

# Evento de encerramento da aplicação
@app.on_event("shutdown")
def shutdown_event():
    logger.info("Aplicação encerrada!")

# Crio o objeto da API
app = FastAPI()

app.include_router(aluno.router, prefix="/buscar-aluno", tags=["Aluno"])