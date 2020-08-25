from flask import Flask, render_template, request
from random import randint
import cmath
import markovify

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

@app.route('/test')
def showTest():
    price = randint(1, 50)
    return render_template('test.html', backend_price=price)

@app.route('/calc')
def calculate():
    a = request.args.get('a', 0)
    b = request.args.get('b', 0)
    c = request.args.get('c', 0)
    try:
        a=int(a);b=int(b);c=int(c)
    except:
        return 'Всё сломалось'    
    if a == 0:
        if b != 0:
            return render_template('calc.html',a=a,b=b,c=c,x1=-c/b)
        else:
            return render_template('calc.html',a=a,b=b,c=c)
    else:
        d = b**2 - 4*a*c # discriminant
        x1 = (-b + cmath.sqrt(d)) / (2*a)
        x2 = (-b - cmath.sqrt(d)) / (2*a)
        return render_template('calc.html',a=a,b=b,c=c,x1=x1,x2=x2)


@app.route('/anec')
def shutka():

    with open("corpus.txt") as f:
        text = f.read()

    text_model = markovify.Text(text)
    # print(text_model.make_sentence(init_state=('Заратустра','говорил')))
    return text_model.make_sentence()


if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0', port = 1488)
