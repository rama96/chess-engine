from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    initial_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    return render_template('index.html', initial_position=initial_position)

if __name__ == '__main__':
    app.run(debug=True)