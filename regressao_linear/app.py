from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Carregar modelo treinado
with open('trained_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    prediction = None
    try:
        # Capturar valores do formulário
        area = float(request.form['area'])
        quartos = int(request.form['quartos'])
        banheiro = int(request.form['banheiro'])
        idade = int(request.form['idade'])

        # Criar array para previsão
        X_new = np.array([[area, quartos, banheiro, idade]])
        prediction = model.predict(X_new)[0]

    except Exception as e:
        prediction = f"Erro: {str(e)}"

    return render_template('index.html', prediction=round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True)
