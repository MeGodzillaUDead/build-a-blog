from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:catfish@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = "catfish"

db = SQLAlchemy(app)

# database model classes to create tables from
class Blog(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50))
	body = db.Column(db.String(255))
	
	def __init__(self, title, body):
		self.title = title
		self.body = body
		
@app.route("/blog")
def blog():
	entries = Blog.query.all()
	
	return render_template("blog.html", entries=entries)
	
if __name__ == "__main__":
	app.run()
