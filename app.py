from flask import Flask,render_template, request
import pickle
import numpy as np

model=pickle.load(open("model.pkl", "rb"))

app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    #values= [int(x) for x in request.form.values()]
    ram = int(request.form.get("ram"))
    rom = int(request.form.get("rom"))
    ss = float(request.form.get("size"))
    pc = int(request.form.get("rear"))
    fc = int(request.form.get("front"))
    battery = int(request.form.get("battery"))
    values=[ram,rom,ss,pc,fc,battery]
    final=np.array(values)
    prediction=model.predict(final.reshape(1,-1))
    output=round(prediction[0],2)
    return render_template("index.html", send_value= f"Expected price of the mobile with above mentioned specification is {output}")

if __name__== '__main__':
    app.run(debug=True)

