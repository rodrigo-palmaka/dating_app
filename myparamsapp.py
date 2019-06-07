from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/input')
def render():
    if 'filename' in request.args:
        myfilename = request.args.get('filename')
        return render_template(myfilename)
    else:
        return "No input file specified"

if __name__=='__main__':
    app.run(debug=True)
