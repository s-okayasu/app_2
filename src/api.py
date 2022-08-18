from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
base_dir = os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
print(base_dir)
print(app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Text)
    def __init__(self, name, age):
        self.name = name
        self.age = age

@app.route('/')
def index():
    print('Hello!')
    return 'Hello!'

@app.route('/get', methods=['GET'])
def get_req():
    print('Get!')
    name = request.args['name']
    if name is not None:
        result = Users.query.filter_by(name = name).all()
        print('Select!')
    else:
        print('params=None')

    ages = []
    for i in range(len(result)):
        ages.append(result[i].age)

    print('result=', ages)
    return {'message': 'Select Success', 'result': ages}

@app.route('/post', methods=['POST'])
def post_req():
    print('Post!')
    req = request.json
    name = req['name']
    age = req['age']
    if (name is not None or age is not None):
        db.session.add(Users(name, age))
        db.session.commit()
        print('Insert!')
    else:
        print('params=None')

    return {'message': 'Insert Success', 'result': None}

if __name__ == '__main__':
    app.run()
