# KalahaAI
Assignment 1 - Introduction to AI

## Prerequisites
Make sure you have the necessary packages installed. See requirements.txt, for which packages that is. 

## How to run
Simply open the [Run Notebook](./Run_Notebook.ipynb), and follow the instructions in there. 

**Alternatively**: <br>
Run main.py. Set Human = True if you want to play against the AI. When it's your turn, enter a number between 1-5 and
press enter after to make your move. 

## Files 
* **Agent.py** contains the implementation of the AI agent, that uses Minimax and Minimax with alpha-beta pruning 
* **Game.py** contains the Kalaha game implementation. Completely separate from AI implementation, to avoid any 
unfair advantages to the AI. 
* **main.py** contains the runner code for a game simulation. To try a game, run this file and observe the game in 
your terminal. 
* **AgentInspection.ipynb** contains various experiments. 
* **MCTS** is the folder, containing the implementation of MCTS. We model MCTS, with the two classes Node and State. 
 
