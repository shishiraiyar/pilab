from flask import Flask
app = Flask(__name__)


count = 0
@app.route("/")
def home():
    global count
    count += 1
    return "Hello there. Visit count: " + str(count)

@app.route("/about")
def first():
    return "about"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)