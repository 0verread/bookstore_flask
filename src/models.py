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

<<<<<<< HEAD
	def __init__(self, id, title, author, quantity):
		self.id = id
=======
	def __init__(self, title, author, quantity):
>>>>>>> week-2
		self.title = title
		self.author = author
		self.quantity = quantity

<<<<<<< HEAD
	@property
	def serialize(self):
=======
	def to_json(self):
>>>>>>> week-2
		return {"title": self.title, "author": self.author, "quantity": self.quantity}
	