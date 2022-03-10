from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '50f523de6093f0e9e867718821ac020b70a9316977812a1f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)