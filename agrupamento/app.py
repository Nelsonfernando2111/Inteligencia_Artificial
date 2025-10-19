from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

app = Flask(__name__)

CSV_FILE = "estudantes_dataset.csv"

# Carrega o dataset original
df_original = pd.read_csv(CSV_FILE)

def aplicar_kmeans(df, n_clusters=3):
    """
    Aplica K-Means em um dataframe e retorna um novo dataframe
    com a coluna 'Cluster' apenas em memória.
    """
    X = df[["Presenca", "NotaMedia", "Participacao", "TarefasEntregues"]].values
    X_scaled = StandardScaler().fit_transform(X)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df_result = df.copy()
    df_result["Cluster"] = kmeans.fit_predict(X_scaled)
    return df_result

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/agrupar', methods=['POST'])
def agrupar():
    """
    Retorna os últimos 5 estudantes do dataset original com clusters.
    """
    df_cluster = aplicar_kmeans(df_original)
    ultimos = df_cluster.tail(5).to_dict(orient="records")
    return jsonify(ultimos)

@app.route('/grafico', methods=['GET'])
def grafico():
    """
    Retorna todos os estudantes do dataset original com clusters.
    """
    df_cluster = aplicar_kmeans(df_original)
    return jsonify(df_cluster.to_dict(orient="records"))

@app.route('/adicionar', methods=['POST'])
def adicionar():
    """
    Adiciona temporariamente um estudante em memória e retorna
    os clusters para o gráfico, sem alterar o CSV original.
    """
    data = request.json
    novo = {
        "Nome": data['nome'],
        "Presenca": int(data['presenca']),
        "NotaMedia": int(data['nota']),
        "Participacao": int(data['participacao']),
        "TarefasEntregues": int(data['tarefas'])
    }

    # Cria um dataframe temporário com todos os dados + novo estudante
    df_temp = pd.concat([df_original, pd.DataFrame([novo])], ignore_index=True)

    # Aplica K-Means em memória
    df_cluster = aplicar_kmeans(df_temp)

    # Retorna apenas o novo estudante com cluster para visualização
    ultimo = df_cluster.iloc[[-1]].to_dict(orient="records")[0]
    return jsonify(ultimo)

if __name__ == '__main__':
    app.run(debug=True)
