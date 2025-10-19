from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Carregar o modelo treinado
modelo = joblib.load("modelo_diabetes.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prever", methods=["POST"])
def prever():
    # Capturar os valores do formulário
    Pregnancies = float(request.form["Pregnancies"])
    Glucose = float(request.form["Glucose"])
    BloodPressure = float(request.form["BloodPressure"])
    SkinThickness = float(request.form["SkinThickness"])
    Insulin = float(request.form["Insulin"])
    BMI = float(request.form["BMI"])
    DiabetesPedigreeFunction = float(request.form["DiabetesPedigreeFunction"])
    Age = float(request.form["Age"])

    # Montar o array com os valores
    dados = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                       Insulin, BMI, DiabetesPedigreeFunction, Age]])

    # Fazer previsão
    previsao = modelo.predict(dados)[0]

    # Converter resultado
    resultado = "Sem Diabetes" if previsao == 0 else "Com Diabetes"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
