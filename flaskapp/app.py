from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello There!!!!!!!!!!</h1>'

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
