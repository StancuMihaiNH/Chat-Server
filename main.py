from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/hello')
def hello():
    return jsonify("'Hello, world!")


if __name__ == '__main__':
    app.run()
