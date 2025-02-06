import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def process(X_train_file="X_train_scaled.csv", X_test_file="X_test_scaled.csv", 
            y_train_file="y_train.csv", y_test_file="y_test.csv", 
            X_train_output="X_train_scaled.csv", X_test_output="X_test_scaled.csv", 
            y_train_output="y_train.csv", y_test_output="y_test.csv"):
    """
    Processa os dados históricos para treinamento de modelos de machine learning.
    
    Parâmetros:
        X_train_file (str): Caminho para o arquivo CSV com os dados de treino.
        X_test_file (str): Caminho para o arquivo CSV com os dados de teste.
        y_train_file (str): Caminho para o arquivo CSV com os valores de treino.
        y_test_file (str): Caminho para o arquivo CSV com os valores de teste.
        X_train_output (str): Caminho para salvar os dados de treino processados.
        X_test_output (str): Caminho para salvar os dados de teste processados.
        y_train_output (str): Caminho para salvar os valores de treino processados.
        y_test_output (str): Caminho para salvar os valores de teste processados.
    
    Retorna:
        None
    """
    try:
        # Carregar os dados brutos
        dados = pd.read_csv("dados_brutos.csv", index_col="Date", parse_dates=True)

        # Remover valores ausentes
        dados = dados.dropna()

        # Criar médias móveis
        dados["MM_20"] = dados["Close"].rolling(window=20).mean()
        dados["MM_50"] = dados["Close"].rolling(window=50).mean()

        # Remover as linhas onde as médias móveis não têm valor (geralmente as primeiras 49 ou 19 linhas)
        dados = dados.dropna(subset=["MM_20", "MM_50"])

        # Dividir em variáveis de entrada (X) e saída (y)
        X = dados[["MM_20", "MM_50"]]  # Usando médias móveis como features
        y = dados["Close"]  # Variável alvo

        # Dividir em treino e teste (80% treino, 20% teste)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

        # Normalizar os dados
        scaler = MinMaxScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Salvar os dados processados
        pd.DataFrame(X_train_scaled, columns=["MM_20", "MM_50"]).to_csv(X_train_output)
        pd.DataFrame(X_test_scaled, columns=["MM_20", "MM_50"]).to_csv(X_test_output)
        pd.DataFrame(y_train, columns=["Close"]).to_csv(y_train_output)
        pd.DataFrame(y_test, columns=["Close"]).to_csv(y_test_output)

        print("✅ Dados pré-processados e salvos com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao processar os dados: {e}")
