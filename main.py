from fastapi import FastAPI
from routers import aluno

# Crio o objeto da API
app = FastAPI()

app.include_router(aluno.router, prefix="/aluno", tags=["Aluno"])