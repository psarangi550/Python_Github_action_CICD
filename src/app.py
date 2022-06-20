from  flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, world!"

@app.route('/index')
def index():
    return "<h1>good Afternoon</h1>"

if __name__ == '__main__':
    app.run(debug=True)