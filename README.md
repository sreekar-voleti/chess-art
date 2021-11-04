# Chess Art

## Concept

This code uses a chess game's Portable Game Notation (PGN) to produce move-diagrams as shown below (produced from [Viswanathan Anand's 1997 brilliancy against Joel Laurier in Biel](https://www.youtube.com/watch?v=Sw4EtXkFx6Q)):

![](example_images/ViswanathanAnand_vs_JoelLautier_1997.png)

It is written in Python 3, using the `chess` package.

## Prerequisites and Installation

You need Python's `chess` package, so before running the scripts in this repository, make sure to type in any of the following commands in your command line/powershell:

`pip install chess`

`pip3 install chess`

Unfortunately, this package is not part of Anaconda's registry of packages so `conda` won't work here.

After you have the `chess` package set up, clone this repository into a directory of your choice using

`git clone https://github.com/sreekar-voleti/chess-art.git`

## Usage

1. Download the PGN (.pgn file) for any game you want to turn into art (I have only tried this with games from lichess and chess.com but in principle any valid PGN file should work), and place it in the `chess-art/PGNFiles/` directory.

2. Go into `inputs.py` and change the `file_name` to the name of the PGN file (just the name of the file, no need for any directory specification), and set the `white_colour`, `black_colour` and `background_colour` to colours of your choice from [this list](https://matplotlib.org/stable/gallery/color/named_colors.html).

3. Run `chessplot.py` from the command line using either of the following

    `python chessplot.py`

    `python3 chessplot.py`

    The .png file containing the image should appear in the `chess-art/ImageFiles/` directory.

4. Show your friends this cool new PGN art at the bar and the library!
