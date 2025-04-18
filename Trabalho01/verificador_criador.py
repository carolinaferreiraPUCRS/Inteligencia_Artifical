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
   
def gerar_vencedores(n=100):
    xwins = set()
    owins = set()
    try:
        
        while len(xwins) < n:
            tabuleiro = [1]*3 + [0]*4 + [-1]*2
            random.shuffle(tabuleiro)
            if venceu(tabuleiro, 1):
                tabuleiro.append('xwins')
                xwins.add(tuple(tabuleiro))
            elif venceu(tabuleiro, 0):
                tabuleiro.append('owins')
                owins.add(tuple(tabuleiro))
    except KeyboardInterrupt:
        print("Geração interrompida pelo usuário.")
        print(f"Total de vitórias X: {len(xwins)}")
        print(f"Total de vitórias O: {len(owins)}")
        return [list(x) + ['x'] for x in xwins] + [list(y) + ['o'] for y in owins]
    finally:
        print("Geração concluída.")
        return [x for x in xwins] + [y for y in owins]



# def verificador_hasGame(tabuleiro: list[int]) -> bool:
    
#     # x e o nao podem ter vencido e não tem mais -1 entao nao pode
#     return not venceu(tabuleiro, 1) and not venceu(tabuleiro, 0) and ( -1 not in tabuleiro and not empate(tabuleiro))

import pandas as pd

# ties = gerar_ties_unicos(100)
# df = pd.DataFrame(ties)
# df['resultado'] = 'tie'
# df.to_csv('empates.csv', index=False, header=False)

vencedores = gerar_vencedores(1000)
df = pd.DataFrame(vencedores)
df.to_csv('vitorias.csv', index=False, header=False)

# X_train = []
# y_train = [] 

# data = pd.read_csv('./tic_tac_toe_balanced_hasgame_samples.txt', sep=",", header=None)

# X = data.iloc[:, :9]
# Y = data.iloc[:, 9]

# hasGameVerificado = []

# for tabuleiro in X.values:
#     if verificador_hasGame(tabuleiro):
#         hasGameVerificado.append(tabuleiro)
# print(f"Total de tabuleiros válidos: {len(hasGameVerificado)}")
# print(hasGameVerificado)



