from flask import Flask

app = Flask(__name__)
visitCount = 0

@app.route('/')
def hello_world():
    return f'Hello, World! This page has been visited {visitCount} times'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)