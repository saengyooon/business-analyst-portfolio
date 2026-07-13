import random

def print_board(board):
    print("\n")
    for i in range(3):
        row = " | ".join(board[i*3:(i+1)*3])
        print(f" {row} ")
        if i < 2:
            print("---+---+---")
    print("\n")

def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_board_full(board):
    return all(cell != " " for cell in board)

def get_computer_move(board):
    available = [i for i, cell in enumerate(board) if cell == " "]
    return random.choice(available) if available else None

def play_game():
    board = [" " for _ in range(9)]
    current_player = "X"
    
    print("\n=== Крестики-нолики ===")
    print("Ячейки нумеруются слева направо, сверху вниз (0-8)")
    print_board([str(i) for i in range(9)])
    
    while True:
        if current_player == "X":
            while True:
                try:
                    move = int(input("Ваш ход (0-8): "))
                    if 0 <= move <= 8 and board[move] == " ":
                        break
                    print("Неверный ход, попробуйте снова")
                except ValueError:
                    print("Введите число от 0 до 8")
        else:
            move = get_computer_move(board)
            print(f"Компьютер ходит: {move}")
        
        board[move] = current_player
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"{'Вы' if current_player == 'X' else 'Компьютер'} победил!")
            break
        
        if is_board_full(board):
            print("Ничья!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    while True:
        play_game()
        again = input("Играть снова? (да/нет): ").lower()
        if again not in ["да", "yes", "y", "д"]:
            print("Спасибо за игру!")
            break
