from flask import Flask
app = Flask(__name__)

@app.route('/')
def display():
    return "Pedru boiola"

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=3134)
