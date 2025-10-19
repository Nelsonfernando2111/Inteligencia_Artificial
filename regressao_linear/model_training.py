# train_model.py
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

# Caminho para os dados e modelo
DATA_PATH = 'house_data.csv'
MODEL_PATH = 'trained_model.pkl'

# Carregar dataset
df = pd.read_csv(DATA_PATH)

# Features e target
X = df[['area', 'quartos', 'banheiro', 'idade']]
y = df['preco']

# Treinar modelo
model = LinearRegression()
model.fit(X, y)

# Salvar modelo
with open(MODEL_PATH, 'wb') as f:
    pickle.dump(model, f)


import pickle

with open('trained_model.pkl', 'rb') as f:
    model = pickle.load(f)

print("Modelo treinado e salvo com sucesso!")
