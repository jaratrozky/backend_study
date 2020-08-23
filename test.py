from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/resume')
@app.route('/')
def showResume():
    return render_template('resume.html')

@app.route('/about')
def showAbout():
    return render_template('about.html')

@app.route('/interests')
def showInterests():
    return render_template('interests.html')


if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 1488)