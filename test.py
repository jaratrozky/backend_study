from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/resume')
@app.route('/')
def hello_world():
    return render_template('resume.html')


if __name__ == "__main__":
    app.run(debug=True)