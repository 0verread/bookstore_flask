from flask_sqlalchemy import SQLAlchemy

from . import db

class BooksModel(db.Model):
	"""
	Defines the Books model
	"""
	__tablename__ = "books"
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80), nullable=False)
	author = db.Column(db.String(225), nullable=False)
	quantity = db.Column(db.Integer)

	def __init__(self, title, author, quantity):
		self.title = title
		self.author = author
		self.quantity = quantity

	def to_json(self):
		return {"title": self.title, "author": self.author, "quantity": self.quantity}
	