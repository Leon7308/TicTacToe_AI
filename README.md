### TicTacToe_AI

tic_tac_toe.py - Minimax and alpha beta  
tic_tac_toe_RL.py - Q-Learning

### Introduction

This project implements the game of Tic Tac Toe and uses two search algorithms and a reinforcement learning approach to choose the best move for the AI player. The two search algorithms used are minimax and alpha-beta pruning, and Q-Learning is used for Reinforcement Learning. The minimax algorithm searches through all possible moves and scores each move based on how likely it is to lead to a win for the AI player. The algorithm then selects the move with the highest score. The alpha-beta pruning algorithm is similar to minimax, but it tries to eliminate some of the branches that are guaranteed to be less optimal than others. This makes the alpha-beta pruning algorithm faster than the minimax algorithm in some cases but does not make a significant difference in our scenario.
The game is played on a 3x3 grid, with two players taking turns placing their marks (either "X" or "O") on the board. The game ends when one player has three marks in a row (horizontally, vertically, or diagonally) or when the board is full and there is no winner (a tie game). The program keeps track of the current state of the board, the AI player's mark, and the human player's mark. The program alternates between letting the AI player choose a move and letting the human player choose a move. When it is the AI player's turn, it selects the best move using either the minimax or alpha-beta pruning algorithm. When it is the human player's turn, it prompts the user to input a number corresponding to the cell on the board where they would like to place their mark.

### Approach

Minimax is a decision-making algorithm that is used to determine the optimal move for a player. It works by recursively searching through the game tree and assigning a score to each possible move. The algorithm then chooses the move with the highest score for the current player and the lowest score for the opponent. This ensures that the player will always choose the best possible move while minimizing the opponent’s chances of winning.
Alpha-beta pruning is an optimization technique used in conjunction with Minimax algorithm to reduce the number of nodes that are evaluated by the Minimax algorithm in its search tree. This allows us to search much faster and even go into deeper levels in the game tree.
Q-learning is a reinforcement learning algorithm that can be used to train an agent to play Tic Tac Toe. It works by assigning a reward value to each state-action pair and updating these values based on feedback from the environment. The agent then uses these values to choose its next move.

### Implementation (include difficulties)

For the implementation of the minimax/ alphabeta pruning, I used a TicTacToe class to have all the TicTacToe functions in order to make a working game. I then used ‘minimax’ and ‘alphabeta’ functions to evaluate the best possible move and returned it as the AI move. We use the evaluate function to get a best move where AI wins. 
 
The Q- Learning method is slightly different since it plays against a random agent and updates values before being ready to play. In tic_tac_toe_RL.py, I have used the same TicTacToe class but have also made a Player class to describe human, random and Q-Learning agents respectively. 
The Q-Learning agent is implemented as a subclass of the Player class, which has a method get_move(game) that returns the next move of the player. The get_move method of the Q-Learning agent is responsible for selecting the next move of the agent based on the current state of the game and the agent's Q-Table.
The Q-Table is a matrix where each row represents a state of the game, and each column represents an action that the agent can take. The entries of the Q-Table represent the expected reward that the agent will receive if it takes a particular action in a particular state.
During training, the Q-Learning agent plays against a Random Agent, which chooses moves randomly. The agent interacts with the environment and updates its Q-Table based on the rewards it receives for each action it takes.

The Q-Learning agent's get_move method first checks if the agent should explore or exploit based on the current value of the agent's exploration parameter, epsilon. If a random value between 0 and 1 is less than epsilon, the agent chooses a random move from the available moves of the game. Otherwise, the agent selects the move with the highest Q-Value for the current state of the game.
If the current state is not in the agent's Q-Table, the agent adds a new row to the table for the current state and initializes all entries to 0. If the current state is already in the agent's Q-Table, the agent selects the action with the highest Q-Value for that state.
After the agent selects its move, it returns the index of the chosen square to the game, which then makes the move. The game then calculates the reward of the move, which is 0 if the game is ongoing, 1 if the agent wins, and -1 if the agent loses. If the game ends, the Q-Learning agent updates its Q-Table based on the reward it received for each action it took during the game using the Q-Learning algorithm's update rule.At the end of the training phase, the Q-Learning agent should have a Q-Table that reflects the optimal action-selection policy for any given state of the game. The agent can then use this table to play the game optimally.

Problems – Both these approaches aren’t perfect. I failed to implement a better evaluation function for minimax which could potentially give much more optimal moves. The reinforcement learning model is also easy to beat with a few moves. Both methods could be updated for a more challenging AI.
Test Results and conclusion
The approaches make for a fun Tic Tac Toe opponent which make optimal moves. In the future, I would like to make a more conclusive evaluation function for minimax and make a UI using Tkinter for a more immersive experience.
 
### References
1.	TicTacToe source - https://geekflare.com/tic-tac-toe-python-code/
2.	QLearning - https://towardsdatascience.com/a-beginners-guide-to-q-learning-c3e2a30a653c 
3.	Minimax and alphabeta pruning - https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/ 

