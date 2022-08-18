from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    print('Hello!')
    return 'Hello!'

@app.route('/get', methods=['GET'])
def get_req():
    print('Get!')
    params = {}
    name = request.args['name']
    if name is not None:
        params['name'] = name
        print('params=', params)
        response = requests.get("http://192.168.3.10/api.wsgi/get", params=params)
        result = response.json()
    else:
        response = 'params=None'

    print('result=', result)
    return result

@app.route('/post', methods=['POST'])
def post_req():
    print('Post!')
    params = {}
    name = request.form['name']
    age = request.form['age']
    if (name is not None or age is not None):
        params['name'] = name
        params['age'] = age
        print('params=', params)
        response = requests.post("http://192.168.3.10/api.wsgi/post", json=params)
        result = response.json()
        # 文字列の場合
        #result = response.text
    else:
        result = 'params=None'

    print('result=', result)
    return result

if __name__ == '__main__':
    app.run(debug=True)
