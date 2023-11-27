from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

from src.models import BooksModel
from src import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookstoredb.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.app_context().push()

db.init_app(app)
db.create_all()

@app.route('/books', methods=['GET'])
def get_all_books():
	try:
		books = BooksModel.query.all()
		return make_response(jsonify([book.serialize for book in books]), 200)
	except Exception as e:
		return make_response(jsonify({'message': 'error getting Books', 'error': e}), 500)


if __name__ == '__main__':
	app.run(DEBUG=True)


