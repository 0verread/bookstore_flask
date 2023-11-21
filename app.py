from flask import Flask, jsonify


app = Flask(__name__)

# 127.0.0.1:8080/hello


@app.route('/hello', methods=['GET'])
def hello():
	return "Hello world!"


books_data = [
	{"id": 1, "name": "War and Peace"},
	{"id": 2, "name": "Crime and Punishment"},
	{"id": 3, "name": "Anna Karenina"}
]


@app.route('/books', methods=['GET'])
def get_books():
	return jsonify(books_data)


