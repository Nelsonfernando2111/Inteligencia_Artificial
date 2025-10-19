import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1️⃣ Carregar o dataset (certifica-te que o nome do ficheiro está correto)
data = pd.read_csv("diabetes.csv")

# 2️⃣ Separar features (X) e o rótulo (y)
# No dataset Pima Indians, a coluna alvo é geralmente "Outcome"
X = data.drop(columns=["Outcome"])
y = data["Outcome"]

# 3️⃣ Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Criar e treinar o modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# 5️⃣ Avaliar o modelo
y_pred = modelo.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {acc:.2f}")

# 6️⃣ Guardar o modelo
joblib.dump(modelo, "modelo_diabetes.pkl")
print("Modelo salvo como 'modelo_diabetes.pkl'")
