import os
from package_trader.collect_dates import collect_dates
from package_trader.process import process
from package_trader.model import train_and_evaluate_model
from package_trader.forecast import forecast_price

def main(ticker="PETR4.SA"):
    """
    Função principal que executa todo o processo de coleta, pré-processamento, 
    treinamento do modelo e geração de previsões, a partir de um ticker fornecido.
    
    Parâmetros:
        ticker (str): Código do ativo (ex: 'PETR4.SA'). O padrão é 'PETR4.SA'.
    """
    # Executar a coleta de dados
    print("\n📥 Coletando dados...")
    collect_dates(ticker=ticker)

    # Executar o pré-processamento
    print("\n🔄 Pré-processando os dados...")
    process()

    # Treinar o modelo
    print("\n🤖 Treinando o modelo...")
    train_and_evaluate_model()

    # Gera a previsão
    print("\n📊 Gerando previsões...")
    forecast_price(ticker=ticker)

    print("\n✅ Processo concluído com sucesso!")
