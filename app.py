from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, template_folder='templates',static_folder='static', static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    mail = request.form.get('mail')
    message = request.form.get('message')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
