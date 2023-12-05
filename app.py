from flask import Flask, jsonify, make_response, request, abort
from flask_sqlalchemy import SQLAlchemy
import os

from src.models import BooksModel
from src import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.app_context().push()

db.init_app(app)
db.create_all()

@app.route('/books', methods=['GET'])
def get_all_books():
	try:
		books = BooksModel.query.all()
		return make_response(jsonify([book.to_json() for book in books]), 200)
	except Exception as e:
		return make_response(jsonify({'message': 'error getting Books', 'error': e}), 500)


@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
	book = BooksModel.query.filter_by(id=id).first()
	if book is None:
		abort(400)
	return jsonify(book.to_json())

@app.route('/books', methods=['POST'])
def create_book_record():
	book = BooksModel(
		title = request.json["title"],
		author = request.json["author"],
		quantity = request.json["quantity"]
		)
	db.session.add(book)
	db.session.commit()
	return jsonify({"message": "Book details added"}) 



if __name__ == '__main__':
	app.run(DEBUG=True)


