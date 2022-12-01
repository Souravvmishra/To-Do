from flask import Flask, render_template , request, redirect
from flask_sqlalchemy import SQLAlchemy, session
from sqlalchemy import func
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable=True)
    completed = db.Column(db.Boolean, default = False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"




@app.route('/')
def home():
    list = Todo.query.order_by(Todo.sno.desc()).all()
    print(list)
    return render_template("index.html", list = list)


@app.route('/add',methods = ["GET","POST"])
def add():
    if request.method == "POST": 
        item = Todo(title = request.form["title"])
        print(item)
        db.session.add(item)
        db.session.commit()
    return redirect("/")

@app.route('/completed/<int:n>')
def completd(n):
    item = Todo.query.filter_by(sno = n).first()
    item.completed = True
    db.session.commit()
    return redirect("/")


@app.route('/delete/<int:n>')
def delete(n):
    item = Todo.query.filter_by(sno = n).first()
    db.session.delete(item)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)