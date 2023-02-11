from flask import Flask, render_template, request, redirect, url_for #importing the FLASK and all the other methods
from flask_sqlalchemy import SQLAlchemy                             # using SQLAlchemy , we can also use SQLlite3 as well as CSV file 

app = Flask(__name__)
app.app_context().push()                                            #creating an appcontext playback which is a new feeature in flask to create the datbase

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'       #connecting to the SQLite which is known as database 'db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                    
db = SQLAlchemy(app)                                                #sepcifiing that all the methods and SQL will be optianied from app.py


class Todo(db.Model):                                               # to define the coloumns in the database
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route("/add", methods=["POST"])                                #this is to get the FORMs from the interface form is nothing but the text bar 
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:todo_id>")                                  # this is to notify that the status is updated to 1 which sets the id as 1 in the list
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")                                  #this route is to delete the certain objects in the list created by the form 
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route('/')                                                        # routing the render main component to basically use CURD operation on the
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


if __name__ == "__main__":                              # to run the database and also the application here we use db.create_all to create all the columns from the route but in the terminal we also specify it for an safer side of it 
    db.create_all()
    app.run(debug=True)