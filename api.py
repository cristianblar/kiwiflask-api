from flask import Flask, request  # Flask package for web service
from flask.json import jsonify

from find_pivot import find_pivot  # The algorithm function

app = Flask(__name__)  # Flask object


@app.route('/api/check-array', methods=['POST'])
def receive_array():
    if not request.data:
        return jsonify({'error': 1, 'message': 'No array was received or was not sent properly'}), 400

    input_array = request.get_json(force=True).get('array')
    result = find_pivot(input_array)
    if result == -1:
        return jsonify({'error': 1, 'message': 'Bad request, please send a valid array'}), 400
    if result == -2:
        return jsonify({'error': 2, 'message': "The array cannot be separated in 2 parts that give the same sum result"}), 200
    return jsonify({'result': result}), 200


def main():
    app.run()


if __name__ == '__main__':
    main()
