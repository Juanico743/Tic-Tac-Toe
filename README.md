# Hi to Everyone
I just wrote my very first Tkinter code in Python!  It's such an exciting milestone for me! I have to admit, it's a bit messy, but I poured my heart and soul into it. I hope you like it despite its imperfections!

# Tic Tac Toe Game with GUI using Tkinter

This repository contains a simple implementation of the classic Tic Tac Toe game with a graphical user interface (GUI) using the Tkinter library in Python. The game features two players taking turns to place their marks ('X' and 'O') on a 3x3 grid until a player wins by forming a line of three consecutive marks, or the game ends in a draw.

## Features

- **GUI Interface**: Built using Tkinter, the game provides a visually appealing and interactive interface.
- **Player Turns**: Players alternate turns, with visual feedback on the current player's move.
- **Scoring System**: Keeps track of the scores for both players, updating after each round.
- **Game Status Indicators**: Displays whether the game is won, drawn, or ongoing.

## How to Run

To run the game, ensure you have Python installed on your machine. Execute the script, and the game window will appear. Players can take turns by clicking on the available grid positions.

## How to Play

1. Click the "START" button to begin the game.
2. Players take turns clicking on an empty grid position to place their mark.
3. The game announces the winner when a player forms a line of three marks.
4. In case of a draw, the game indicates a tie.
5. Click "NEXT" to start a new round or "QUIT" to exit the game.

## Customization

- **Player Symbols**: The default symbols are 'X' and 'O', but you can customize them.
```Python
self.player1 = "X"
self.player2 = "O"
```
- **Player Colors**: Customize player colors for a personalized touch.
  You can choose a color by visiting this website: `https://g.co/kgs/RYqC8L`
```Python
self.player1_color = "#6E66fA"
self.player2_color = "#FA6678"
self.draw_color = "#7D7D7D"
self.win_color = "#52FA87"
```

Feel free to explore the code and adapt it to your preferences. Enjoy playing Tic Tac Toe with friends or use it as a starting point for your Tkinter-based game projects!

