from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:example@172.17.0.1:3306/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']

    return render_template('index.html', name=name, comment=comment)

@app.route('/page/<place>')
def page(place):
    return '<h1>You are on the '+ place +' page!</h1>'

@app.route('/home', methods=['GET', 'POST'])
def home():
    return '<h1>You are on the home page!</h1>'

@app.route('/template')
def template():
    links = ['https://docker-curriculum.com','https://www.youtube.com/watch?v=Qw9zlE3t8Ko','https://flask.palletsprojects.com']
    return render_template('example.html', myvar=' Flask example', links=links)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
