import math
import random
import numpy as np

# Make empty board
class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None


    def init_board():
        return [" " for _ in range(9)]

    # Print out board
    def print_board(self):
        print("-------------")
        for i in range(3):
            row = "| "
            for j in range(3):
                row += self.board[i*3 + j] + " | "
            print(row)
            print("-------------")

    # Get empty cells with no values
    def get_empty_cells(self):
        return [i for i in range(len(self.board)) if self.board[i] == " "]

    # Check for wins
    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                return self.board[i]
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return self.board[i]
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[2]
        # Check for tie game
        if " " not in self.board:
            return "Tie"
        # Game is still in progress
        return None

    # Check who won
    def evaluate(self, ai_player, human_player):
        winner = self.check_winner()
        if winner == ai_player:
            return 1
        elif winner == human_player:
            return -1
        else:
            return 0

# Minimax
game = TicTacToe()

def minimax(board, depth, is_maximizing, ai_player, human_player):
    score = game.evaluate(board, ai_player, human_player)
    if score != 0:
        return score
    if depth == 5:
        return 0
    
    if is_maximizing:
        best_score = float('-inf')
        for cell in game.get_empty_cells(board):
            new_board = board.copy()
            new_board[cell] = ai_player
            score = minimax(new_board, depth+1, False, ai_player, human_player)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for cell in game.get_empty_cells(board):
            new_board = board.copy()
            new_board[cell] = human_player
            score = minimax(new_board, depth+1, True, ai_player, human_player)
            best_score = min(best_score, score)
        return best_score

# Minimax with alphabeta
def alphabeta(board, depth, alpha, beta, is_maximizing, ai_player, human_player):
    score = game.evaluate(ai_player, human_player)
    if score != 0:
        return score
    if depth == 5:
        return 0
    
    if is_maximizing:
        best_score = float('-inf')
        for cell in game.get_empty_cells():
            new_board = board.copy()
            new_board[cell] = ai_player
            score = alphabeta(new_board, depth+1, alpha, beta, False, ai_player, human_player)
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for cell in game.get_empty_cells():
            new_board = board.copy()
            new_board[cell] = human_player
            score = alphabeta(new_board, depth+1, alpha, beta, True, ai_player, human_player)
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

# AI move. This selects a move using Minimax or Alphabeta
def ai_move(board, ai_player, human_player, AI):
    best_score = float('-inf')
    best_move = None
    for cell in game.get_empty_cells():
        new_board = board.copy()
        new_board[cell] = ai_player
        if (AI == 1):
            score = minimax(new_board, 0, float('-inf'), float('inf'), False, ai_player, human_player)
        else:
            score = alphabeta(new_board, 0, float('-inf'), float('inf'), False, ai_player, human_player)
        if score > best_score:
            best_score = score
            best_move = cell
    return best_move

# Get user's move
def get_player_move(board, player):
    while True:
        try:
            cell = int(input(f"{player}'s turn. Enter a number from 1-9: ")) - 1
            if cell in game.get_empty_cells():
                return cell
            else:
                print("That cell is not empty. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

# Initialize Game
def play_game():
    board = game.board
    game.print_board()
    ai_player = "O"
    human_player = "X"
    current_player = ai_player

    while True:
        if current_player == ai_player:
            print("AI's turn.")
            cell = ai_move(board, ai_player, human_player, AI)
        else:
            cell = get_player_move(board, human_player)
        board[cell] = current_player
        game.print_board()
        winner = game.check_winner()
        if winner is not None:
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(f"{winner} won the game!")
            break
        if current_player == ai_player:
            current_player = human_player
        else:
            current_player = ai_player

# Choose AI
AI = input("Choose method (using number): \n1. MiniMax\n2. Alpha Beta Pruning\n")
play_game()


# This code implements the game of tic tac toe and uses two search algorithms to choose the best move for the AI player. The two search algorithms used are minimax and alpha-beta pruning. The minimax algorithm searches through all possible moves and scores each move based on how likely it is to lead to a win for the AI player. The algorithm then selects the move with the highest score. The alpha-beta pruning algorithm is similar to minimax, but it tries to eliminate some of the branches that are guaranteed to be less optimal than others. This makes the alpha-beta pruning algorithm faster than the minimax algorithm in some cases.

# The game is played on a 3x3 grid, with two players taking turns placing their marks (either "X" or "O") on the board. The game ends when one player has three marks in a row (horizontally, vertically, or diagonally) or when the board is full and there is no winner (a tie game). The program keeps track of the current state of the board, the AI player's mark, and the human player's mark. The program alternates between letting the AI player choose a move and letting the human player choose a move. When it is the AI player's turn, it selects the best move using either the minimax or alpha-beta pruning algorithm. When it is the human player's turn, it prompts the user to input a number corresponding to the cell on the board where they would like to place their mark.

