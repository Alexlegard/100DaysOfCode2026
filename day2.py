# Today, I was doing some simple logic for starting a new chess game.
# Thankfully the only state that needs to be reset is board and selected_square.
# And the html form calls the python function new_game directly, no JS needed.
# it's just that simple....


@app.route('/new_game', methods=['POST'])
def new_game():
    global board, selected_square
    board = chess.Board()
    selected_square = None
    return redirect(url_for('index'))