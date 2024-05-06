from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, make_response
from model import InputForm
from model import compute

app = Flask(__name__)

@app.route('/')
def welcome():
	return render_template('home_template.html')

@app.route('/predictor', methods=['GET', 'POST'])
def predictor():
    form = InputForm(request.form)
    if request.method == 'POST':
        result = compute(form.texto)
    else:
        result = None

    return render_template('prediction_template.html',
                           form=form, result=result)

    
    

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000,debug=True)
