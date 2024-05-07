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
        {"role":"system","content":
          "This is an application to help call center employees"
          "Assistant takes inputs from users and determines its positive neutral and negative weights."
          "This weights are in 0-1 scale and their sum is 1."
          "Assistant must print the weights"
          "Assistant must print the input text"
          "Besides, if the negative weight is above 0.5, the Assistant must suggest a text in Spanish."
          "If the input text is a query te Assistant must suggest a solution in Spanish"},
        {"role": "user", "content": "{}".format(texto)}
      ]
    )
    prediction = response.choices[0].message.content
    return render_template("result_template.html", prediction=prediction)	