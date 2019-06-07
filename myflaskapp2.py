from flask import Flask
app = Flask(__name__)

@app.route('/alpha')
def alpha():
    return "ok"

@app.route('/beta')
def beta():
    return "This is the beta version"

if __name__=='__main__':
    app.run(debug=True)
