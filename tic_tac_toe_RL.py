import random
import numpy as np

# Tic Tac Toe Class like last game
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        print('|---|---|---|')
        print('| ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2] + ' |')
        print('|---|---|---|')
        print('| ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5] + ' |')
        print('|---|---|---|')
        print('| ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8] + ' |')
        print('|---|---|---|')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([s == letter for s in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True

        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board()

    letter = 'X'
    while game.num_empty_squares() > 0 and not game.current_winner:
        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print("It's a tie!")
    return None

# Player classes (Human, Random for training and QLearning)
class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = str(int(input(self.letter + "'s turn. Input move (1-9): ")) - 1)
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val

class RandomAgent(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_moves())


class QLearningAgent(Player):
    def __init__(self, letter, alpha=0.5, discount=0.9, epsilon=0.1):
        super().__init__(letter)
        self.alpha = alpha
        self.discount = discount
        self.epsilon = epsilon
        self.q_table = {}

    def get_state(self, game):
        return str(game.board)

    def get_move(self, game):
        if random.uniform(0, 1) < self.epsilon:
            move = random.choice(game.available_moves())
        else:
            state = self.get_state(game)
            if state not in self.q_table:
                self.q_table[state] = np.zeros(9)
            move = np.argmax(self.q_table[state])

        return move

    def update(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(9)
        if next_state not in self.q_table:
            self.q_table[next_state] = np.zeros(9)

        old_value = self.q_table[state][action]
        next_max = np.max(self.q_table[next_state])

        new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.discount * next_max)
        self.q_table[state][action] = new_value

q_agent = QLearningAgent('O')
r_agent = RandomAgent('X')
t = TicTacToe()


# Training the QLearning AI
for i in range(10000):
    play(t, q_agent, r_agent, print_game=False)
    if i % 1000 == 0:
        print(f"Finished {i} training games")

# Playing Loop
while True:
    t = TicTacToe()
    human_agent = HumanPlayer('X')
    q_agent = QLearningAgent('O')
    winner = play(t, human_agent, q_agent)

    if winner == 'X':
        print("You win!")
    elif winner == 'O':
        print("You lose!")
    else:
        print("It's a tie!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
        break


