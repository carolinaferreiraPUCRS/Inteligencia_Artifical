def check_owin(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == 0:
            return True
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == 0:
            return True
    
    # Check diagonals
    if board[0] == board[4] == board[8] == 0:
        return True
    if board[2] == board[4] == board[6] == 0:
        return True
    
    return False

def is_board_full(board):
    return -1 not in board

def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    owin_count = 0
    tie_count = 0
    
    with open(output_file, 'w') as f:
        for line in lines:
            parts = line.strip().split(',')
            if parts[-1] == 'negative':
                board = [int(x) for x in parts[:-1]]
                if check_owin(board):
                    f.write(','.join(parts[:-1]) + ',owin\n')
                    owin_count += 1
                elif is_board_full(board):
                    f.write(','.join(parts[:-1]) + ',tie\n')
                    tie_count += 1
                else:
                    # This shouldn't happen if the data is correct
                    f.write(','.join(parts[:-1]) + ',unknown\n')
            else:
                f.write(line)
    
    print(f"Processed {len(lines)} lines")
    print(f"Found {owin_count} O wins")
    print(f"Found {tie_count} ties")

if __name__ == "__main__":
    input_file = "/Users/carolinaferreira/Downloads/tic+tac+toe+endgame/tic-tac-toe.data"
    output_file = "tic-tac-toe-separated.data"
    process_file(input_file, output_file) 