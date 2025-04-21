from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI(title="API IA - Jogo da Velha com múltiplos algoritmos")

# Caminhos dos modelos
MODELOS = {
    "arvore": "modelos/arvore.pkl",
    "mlp": "modelos/mlp.pkl",
    "knn": "modelos/knn.pkl",
    "svm": "modelos/svm.pkl"
}

modelos_carregados = {}

class RequisicaoEntrada(BaseModel):
    estado: list[int]  # 9 valores do tabuleiro
    algoritmo: str     # "arvore", "mlp", "knn", "svm"

@app.post("/prever/")
def prever_estado_jogo(requisicao: RequisicaoEntrada):
    if len(requisicao.estado) != 9:
        return {"erro": "O tabuleiro deve conter exatamente 9 posições."}
    
    if requisicao.algoritmo not in MODELOS:
        return {"erro": f"Algoritmo '{requisicao.algoritmo}' não suportado. Use: {list(MODELOS.keys())}"}

    if requisicao.algoritmo not in modelos_carregados:
        caminho = MODELOS[requisicao.algoritmo]
        if not os.path.exists(caminho):
            return {"erro": f"Arquivo do modelo '{requisicao.algoritmo}' não encontrado em: {caminho}"}
        modelos_carregados[requisicao.algoritmo] = joblib.load(caminho)

    modelo = modelos_carregados[requisicao.algoritmo]
    entrada = np.array(requisicao.estado).reshape(1, -1)
    predicao = modelo.predict(entrada)[0]

    return {
        "algoritmo_utilizado": requisicao.algoritmo,
        "estado_previsto": predicao
    }
