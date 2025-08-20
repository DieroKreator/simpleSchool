# bibliotecas e frameworks
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
import logging

logger = logging.getLogger(__name__)

# crio o objeto do roteador
router = APIRouter()

# banco de dados simulado (fake)
alunos_db = {
    "joao@iterasys.com.br": {
        "nome": "João Cruz",
        "validade_assinatura": "2025-12-31",
        "endereco": {
            "rua": "Rua Carlos Antonio",
            "numero": 123,
            "bairro": "Itú",
            "cidade": "Floripa",
            "estado": "SC"
        }
    },
    "maria@iterasys.com.br": {
        "nome": "Maria Oliveira",
        "validade_assinatura": "2026-05-15",
        "endereco": {
            "rua": "Rua Puebla",
            "numero": 456,
            "bairro": "Pinheiro",
            "cidade": "São Paulo",
            "estado": "SP"
        }
    },
}

class AlunoRequest(BaseModel):
    email: EmailStr

@router.post("/")
def buscar_aluno(dados: AlunoRequest):
    aluno = alunos_db.get(dados.email)
    logger.info(f"Buscando aluno com email: {dados.email}")
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

# @app.post("/buscar-endereco-aluno")
# def buscar_endereco_aluno(dados: AlunoRequest):
#     aluno = alunos_db.get(dados.email)
#     if not aluno:
#         raise HTTPException(status_code=404, detail="Aluno não encontrado")
#     return {
#         "endereco": aluno["endereco"]
#     }
    
@router.get("/")
def buscar_aluno_get(email: EmailStr):
    aluno = alunos_db.get(email)
    logger.info(f"Buscando aluno com email: {dados.email}")
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno