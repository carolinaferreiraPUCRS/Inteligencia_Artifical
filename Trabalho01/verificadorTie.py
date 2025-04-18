import random

# Pré-calcula as combinações vencedoras uma vez só
COMBINACOES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
    [0, 4, 8], [2, 4, 6]              # Diagonais
]

def venceu(tab, jogador):
    return any(all(tab[i] == jogador for i in c) for c in COMBINACOES)

def empate(tab):
    # Assume que o tabuleiro está cheio
    return not venceu(tab, 0) and not venceu(tab, 1)

def gerar_tabuleiro_completo():
    jogadas = [1]*5 + [0]*4
    random.shuffle(jogadas)
    return jogadas

# Geração dos empates únicos
def gerar_ties_unicos(n=100):
    empates_unicos = set()
    lista_de_ties = [
        [1, 1, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 1, 1, 1, 0, 1],
        [0, 1, 1, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 1, 0, 1, 0],
        [1, 0, 0, 0, 1, 1, 1, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 1],
        [0, 1, 1, 1, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 1, 1, 0, 0],
        [1, 1, 0, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0, 1, 1],
        [0, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 1, 0, 1],
    ]



    # Adiciona os tabuleiros de empate ao conjunto
    
    try:
        # Gere tabuleiros até atingir o limite
        for tabuleiro in lista_de_ties:
            # empates_unicos.add(tuple(tabuleiro))
             if empate(tabuleiro):
                empates_unicos.add(tuple(tabuleiro))
        # while len(empates_unicos) < n:
        #     tab = gerar_tabuleiro_completo()
        #     if empate(tab):
        #         empates_unicos.add(tuple(tab))
        print("Geração interrompida pelo usuário.")
        print(empates_unicos)
        print(f"Total de tabuleiros válidos: {len(empates_unicos)}")
       
    except KeyboardInterrupt:
        print("Geração interrompida pelo usuário.")
        print(empates_unicos)
        print(f"Total de tabuleiros válidos: {len(empates_unicos)}")
    finally:
        return [list(t) for t in empates_unicos]
   
    
import pandas as pd

ties = gerar_ties_unicos(100)
df = pd.DataFrame(ties)
df['resultado'] = 'tie'
df.to_csv('empates_verificados.csv', index=False, header=False)
