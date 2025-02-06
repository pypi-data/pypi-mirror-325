import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
from sklearn.preprocessing import MinMaxScaler

def train_and_evaluate_model(X_train_file="X_train_scaled.csv", X_test_file="X_test_scaled.csv", 
                             y_train_file="y_train.csv", y_test_file="y_test.csv", 
                             model_output="modelo_regressao.pkl", scaler_output="scaler.pkl"):
    """
    Treina um modelo de regressão linear e avalia o desempenho.
    
    Parâmetros:
        X_train_file (str): Caminho para o arquivo CSV com os dados de treino (padrão: "X_train_scaled.csv").
        X_test_file (str): Caminho para o arquivo CSV com os dados de teste (padrão: "X_test_scaled.csv").
        y_train_file (str): Caminho para o arquivo CSV com os valores de treino (padrão: "y_train.csv").
        y_test_file (str): Caminho para o arquivo CSV com os valores de teste (padrão: "y_test.csv").
        model_output (str): Caminho para salvar o modelo treinado (padrão: "modelo_regressao.pkl").
        scaler_output (str): Caminho para salvar o scaler (padrão: "scaler.pkl").
    
    Retorna:
        None
    """
    try:
        # Carregar os dados pré-processados
        X_train_scaled = pd.read_csv(X_train_file, index_col=0)
        X_test_scaled = pd.read_csv(X_test_file, index_col=0)
        y_train = pd.read_csv(y_train_file, index_col=0)
        y_test = pd.read_csv(y_test_file, index_col=0)

        # Criar e treinar o modelo de regressão linear
        modelo = LinearRegression()
        modelo.fit(X_train_scaled, y_train)

        # Avaliação do modelo
        mae = mean_absolute_error(y_test, modelo.predict(X_test_scaled))
        rmse = np.sqrt(mean_squared_error(y_test, modelo.predict(X_test_scaled)))

        print(f"✅ Modelo treinado!")
        print(f"📊 Erro Médio Absoluto (MAE): {mae:.4f}")
        print(f"📉 Raiz do Erro Quadrático Médio (RMSE): {rmse:.4f}")

        # Criar e salvar o scaler
        scaler = MinMaxScaler()
        scaler.fit(X_train_scaled)  # Ajuste do scaler nos dados de treino
        joblib.dump(scaler, scaler_output)

        # Salvar o modelo treinado
        joblib.dump(modelo, model_output)

        print(f"✅ Modelo e scaler salvos como '{model_output}' e '{scaler_output}'")
    except Exception as e:
        print(f"❌ Erro ao treinar o modelo: {e}")
