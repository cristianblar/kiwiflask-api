from flask import Flask  # Flask package for web service
from flask.json import jsonify

from find_pivot import find_pivot  # The algorithm function

app = Flask(__name__)  # Flask object


@app.route('/api/check-array')
def hello():
    return jsonify({'message': 'Hello Flask world!'})


def main():
    app.run()


if __name__ == '__main__':
    main()
