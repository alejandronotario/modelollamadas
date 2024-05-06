import os
from flask import render_template
from wtforms import Form, StringField
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = ''
client = OpenAI()

class InputForm(Form):
    texto = StringField(default="no se ha introducido texto")

def compute(texto):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": "Sentiment analysis of the following text: {}".format(texto)}
      ]
    )
    prediction = response.choices[0].message.content
    return render_template("result_template.html", prediction=prediction)	