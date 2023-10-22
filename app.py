from flask import Flask, render_template , request ,  jsonify

app = Flask(__name__)

@app.route('/')
def index():
    initial_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    return render_template('index.html', initial_position=initial_position)

@app.route('/make_move', methods=['POST'])
def make_move():
    data = request.get_json()
    move = data.get('move')

    # Process the move and update the game state
    # Example: game.make_move(move)

    # Return a response to the client
    print(move)
    response_data = {'move': move}
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True, port=8081)