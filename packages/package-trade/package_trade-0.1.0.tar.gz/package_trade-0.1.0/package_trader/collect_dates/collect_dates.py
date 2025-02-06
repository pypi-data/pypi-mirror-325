import yfinance as yf
import pandas as pd
from datetime import datetime
import os

def collect_dates(ticker="PETR4.SA", start_date="2020-01-01", output_file="dados_brutos.csv"):
    """
    Coleta dados históricos de uma ação usando o yfinance e salva em um arquivo CSV.
    
    Parâmetros:
        ticker (str): Código do ativo (ex: 'PETR4.SA'). O padrão é 'PETR4.SA'.
        start_date (str): Data de início no formato 'YYYY-MM-DD'.
        output_file (str): Nome do arquivo CSV para salvar os dados.
    
    Retorna:
        pandas.DataFrame: DataFrame com os dados coletados
    """
    try:
        # Verificar se o ticker é válido
        print(f"🔄 Coletando dados para {ticker} de {start_date} até {datetime.today().strftime('%Y-%m-%d')}...")
        dados = yf.download(ticker, start=start_date, end=datetime.today().strftime('%Y-%m-%d'))

        # Se o download falhar (ticker inválido), usar o padrão
        if dados.empty:
            print(f"⚠️ Ticker '{ticker}' inválido ou não encontrado. Usando o ticker padrão 'PETR4.SA'.")
            dados = yf.download("PETR4.SA", start=start_date, end=datetime.today().strftime('%Y-%m-%d'))
            ticker = "PETR4.SA"
        
        # Aplanar o MultiIndex, se existir
        if isinstance(dados.columns, pd.MultiIndex):
            dados.columns = dados.columns.get_level_values(0)
        
        # Resetar o índice para garantir que 'Date' esteja como coluna
        dados.reset_index(inplace=True)
        
        # Adicionar 'Adj Close' se não existir
        if "Adj Close" not in dados.columns:
            dados["Adj Close"] = dados["Close"]
        
        # Renomear as colunas para garantir consistência
        if len(dados.columns) == 7:
            dados.columns = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
            
            # Salvar o arquivo no diretório atual
            current_directory = os.getcwd()  # Obtém o diretório atual
            output_path = os.path.join(current_directory, output_file)  # Define o caminho completo
            dados.to_csv(output_path, index=False)  # Salva o arquivo no diretório atual
            print(f"✅ Dados coletados e salvos em '{output_path}'")
        else:
            print(f"⚠️ O número de colunas não corresponde a 7. O DataFrame tem {len(dados.columns)} colunas.")
            print("🔍 Colunas atuais:", dados.columns)
        
        return dados
    except Exception as e:
        print(f"❌ Erro ao coletar os dados: {e}")
        return None
