# Connect Four

A simple Python class that implements a typical Connect Four game.
Included is also a sample console client for demonstaring the usage. 

### Example
```
import connect4

game = connect4.Game()

status, board = game.start()
print(board)

status, board = game.play(4) # player 1
print(board)
```
