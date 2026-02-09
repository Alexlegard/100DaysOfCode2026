# Today, I was setting up a new chess-related python app called python-chess-puzzles.
# Since I finished the other chess game, I needed to decide on what I wanted to continue
# to work on. I could have continued to work on the other game, and implemented chess.com
# features like move history, drag-and-drop movement, resigning, draw offers, etc.
# I decided I wanted to implement chess puzzles more, it simply has more flavour.

# Current progress:
# virtual environment set up
# one route that just renders an empty chessboard

# To do:
# Write an api, containing ten chess puzzles.

from flask import Flask, render_template, request, redirect, url_for, jsonify
import chess
import pdb
from dataclasses import dataclass

app = Flask(__name__)


@app.route('/') 
def index(): 
    return render_template('index.html', pieces=None, selected=None)


if __name__ == "__main__":
    app.run(debug=True)