from flask import Flask, render_template, request
from sklearn.linear_model import LogisticRegression
import joblib

model = joblib.load("cropmo.pkl")


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        neitro = request.form["ni"]
        phosph = request.form["phs"]
        potas = request.form["pot"]
        tempa = request.form["temp"]
        humi = request.form["hum"]
        phv = request.form["ph"]
        rainfall = request.form["rai"]
        inputs = [
            float(neitro),
            float(phosph),
            float(potas),
            float(tempa),
            float(humi),
            float(phv),
            float(rainfall),
        ]
        res = model.predict([inputs])[0]
        return render_template("result.html",content = res )
if __name__ == "__main__":
    app.run()


   



