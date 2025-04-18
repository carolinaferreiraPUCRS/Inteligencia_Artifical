import random

a = 1255
c = 4164
m = 1048576576
Xn = 5000

def congruenciaLinear(x):
    return (a*x + c) % m

def next_rand():
    global Xn
    Xn = congruenciaLinear(Xn)
    return Xn

def next_float():  # Entre 0 e 1
    return next_rand() / m

def my_shuffle(lst):
    lst_copy = lst[:]
    for i in range(len(lst_copy) - 1, 0, -1):
        j = next_rand() % (i + 1)
        lst_copy[i], lst_copy[j] = lst_copy[j], lst_copy[i]
    return lst_copy

def my_choice(seq):
    idx = next_rand() % len(seq)
    return seq[idx]


# Verificações
def check_winner(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
        [0, 4, 8], [2, 4, 6]              # diagonais
    ]
    return any(all(board[i] == player for i in pattern) for pattern in win_patterns)

def is_tie(board):
    return -1 not in board and not check_winner(board, 1) and not check_winner(board, 0)

def is_valid_hasgame(board):
    x_count = board.count(1)
    o_count = board.count(0)
    return abs(x_count - o_count) <= 1 and not check_winner(board, 1) and not check_winner(board, 0)

# Geradores
def generate_tie_samples(n):
    results = set()
    while len(results) < n:
        board = [1]*5 + [0]*4
        board = my_shuffle(board)
        if is_tie(board):
            results.add(tuple(board))
    return [list(b) + ['tie'] for b in results]

def generate_hasgame_samples(n):
    results = set()
    try:
        while len(results) < n:
            x = random.randint(0, 5)
            o = random.randint(0, 5)
            if abs(x - o) > 1 or x + o > 8:  # no espaço para continuar
                continue
            board = [1]*x + [0]*o + [-1]*(9 - x - o)
            board = my_shuffle(board)
            if is_valid_hasgame(board):
                results.add(tuple(board))  
    except KeyboardInterrupt:
        print("Geração interrompida pelo usuário.")
        print(results)
        print(f"Total de tabuleiros válidos: {len(results)}")
        return [list(b) + ['hasgame'] for b in results]
    finally:
        return [list(b) + ['hasgame'] for b in results]



# Geração
# tie_samples = generate_tie_samples(32)
hasgame_samples = generate_hasgame_samples(2000)
# all_data = tie_samples + hasgame_samples

# Visualização dos primeiros exemplos
# for row in tie_samples[:5] + hasgame_samples[:5]:
#     print(",".join(map(str, row)))
    
with open("tic_tac_toe_balanced_hasgame_samples.txt", "w") as f:
    for row in hasgame_samples:
        linha = ",".join(map(str, row))
        f.write(linha + "\n")