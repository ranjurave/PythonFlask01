from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config['SECRET_KEY']='random string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=100))
    city = db.Column(db.String(length=50))
    addr = db.Column(db.String(length=200))
    pin = db.Column(db.String(length=10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

@app.route('/')
def show_all():
    return render_template('show_all.html', students=students.query.all())

@app.route('/new', methods=['GET','POST'])
def new():
    if request.method=='POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            student = students(request.form['name'],
                               request.form['city'],
                               request.form['addr'],
                               request.form['pin'])
            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))

    return  render_template('new.html')

if(__name__=="__main__"):
    app.run(debug=True)