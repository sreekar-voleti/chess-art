import numpy as np
import chess.pgn
import chess
from matplotlib import pyplot as plt
from inputs import file_name , white_colour , black_colour , background_colour , opacity_gradient , max_opacity , thickness

# Change this to the name of the PGN file you want to plot

# Open the game

pgn = open("PGNFiles/"+file_name)
game = chess.pgn.read_game(pgn)
board = game.board()

# This array will hold the long algebraic notation for the game

moves = []

# From the PGN we extract the Long Algebraic Notation for the game and put it into moves.
## Odd moves are white, Even moves are black

for move in game.mainline_moves():
    moves.append(move.uci())

# Dictionary for the squares to the array

files = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h']
ranks = ['1' , '2' , '3' , '4' , '5' , '6' , '7' , '8']

board_dict = {}

for i in range(8):
    for j in range(8):
        board_dict[files[i]+ranks[j]] = [i,j]

# This function takes an element from the array "moves" and gives 2 points b/w which to draw lines

def paths(move):
    return np.array([ board_dict[move[0:2]] , board_dict[move[2:4]] ] )

# Set of all initial points
x = []
# Set of all final points
y = []

for i in range(len(moves)):
    x.append(paths(moves[i])[0])
    y.append(paths(moves[i])[1])

# Colours for white and black
cols = [white_colour , black_colour]

# Plot a line between points a and b
def simpleplot( a , b , i , op ):
    x = [a[0] , b[0]]
    y = [a[1] , b[1]]
    plt.plot( x , y , color = cols[i%2] , alpha = op , linewidth = thickness , solid_capstyle = 'round')

fig = plt.figure()

ax = fig.add_subplot(111)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')
fig.set_facecolor(background_colour)

if opacity_gradient == "on":
    for i in range(len(moves)):
        simpleplot(x[i] , y[i] , i , (i+1)*max_opacity/len(moves))
elif opacity_gradient == "off":
    for i in range(len(moves)):
        simpleplot(x[i] , y[i] , i , max_opacity)

plt.savefig("ImageFiles/"+file_name[0:-4]+".png" , dpi = 800)
#plt.show()
