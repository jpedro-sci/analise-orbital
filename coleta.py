import requests
import pandas as pd
from datetime import datetime, timedelta
import time


# Chave de Acesso - Por gentileza não vazar a KEY

API_KEY = "NrsCRcMOs3XYwBTqGDXQt3Fjh2DS2FjK5NFcBfgE"
URL = "https://api.nasa.gov/neo/rest/v1/feed"

# Hoje até 10 anos atrás

data_fim = datetime.now()
data_inicio = data_fim - timedelta(days=10*365) # mais ou menos 3650 dias

data_atual = data_inicio
lista_asteroides = []

print(f"Iniciando extração: {data_inicio.strftime('%Y-%m-%d')} até {data_fim.strftime('%Y-%m-%d')}")


# De 7 em 7 dias

while data_atual < data_fim:
    # Calcula os próximos 7 dias (Limite máximo da API)
    proxima_data = data_atual + timedelta(days=7)
    
    if proxima_data > data_fim:
        proxima_data = data_fim

    start_str = data_atual.strftime('%Y-%m-%d')
    end_str = proxima_data.strftime('%Y-%m-%d')

    parametros = {
        "start_date": start_str,
        "end_date": end_str,
        "api_key": API_KEY
    }

    # Requisição
    resposta = requests.get(URL, params=parametros)
    
    # Valida
    if resposta.status_code == 200:
        dados_json = resposta.json()
        near_earth_objects = dados_json.get("near_earth_objects", {})
        
        # Mineração do JSON:
        for data, asteroides in near_earth_objects.items():
            for asteroide in asteroides:
                
                # Prevenção: pula o asteroide se não tiver dados de aproximação
                if not asteroide.get("close_approach_data"):
                    continue
                    
                dados_aprox = asteroide["close_approach_data"][0]
                
                lista_asteroides.append({
                    "id": asteroide["id"],
                    "nome": asteroide["name"],
                    "diametro_min_m": asteroide["estimated_diameter"]["meters"]["estimated_diameter_min"],
                    "diametro_max_m": asteroide["estimated_diameter"]["meters"]["estimated_diameter_max"],
                    "velocidade_km_s": float(dados_aprox["relative_velocity"]["kilometers_per_second"]),
                    "distancia_km": float(dados_aprox["miss_distance"]["kilometers"]),
                    "ameaca": asteroide["is_potentially_hazardous_asteroid"]
                })
        
        print(f"Coletado: {start_str} a {end_str}")
    else:
        print(f"Erro {resposta.status_code} no período {start_str} a {end_str}")

    # Avança o calendário para próxima semana
    data_atual = proxima_data + timedelta(days=1)
    
    # Pausa de 0.5 seg para não sobrecarregar
    time.sleep(0.5)


# Fechamento/Exportação

df_asteroides = pd.DataFrame(lista_asteroides)

df_asteroides = df_asteroides.drop_duplicates(subset=['id'])

# Exportando o arquivo
nome_arquivo = "asteroides_10_anos.csv"
df_asteroides.to_csv(nome_arquivo, index=False)

print(f"\nExtração Concluída! Total de {len(df_asteroides)} asteroides salvos em '{nome_arquivo}'.")