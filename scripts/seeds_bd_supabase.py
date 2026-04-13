import random
from datetime import datetime, timedelta
from supabase import create_client, Client

url = "https://aueqjdxchrfbrgeepsnd.supabase.co"
key = "sb_publishable_w59JO2FJ6xp0Rl8OaUwXRA_FIo1m9V8" 
supabase: Client = create_client(url, key)

# Lista das tabelas para busca e dicionario para armazenar a tabela e seus IDs
tabelas = ["maquinas", "talhoes"]
dados_tabela = {}

def buscar_dados(tabelas):
    for i in tabelas:
        try:
            # Realiza a consulta pedindo apenas essa coluna dinâmica
            nome_coluna_id = f"id_{i}"
            response = supabase.table(i).select(nome_coluna_id).execute()
                        
            # Extrai apenas os IDs brutos para uma lista limpa
            ids_extraidos = [reg[nome_coluna_id] for reg in response.data]
            
            # Guarda no dicionário usando o nome da tabela como chave
            dados_tabela[i] = ids_extraidos
                
            print(f"Sucesso! {len(ids_extraidos)} IDs obtidos da tabela: {i}")
            
        except Exception as e:
            print(f"Erro ao buscar dados: {e}")

# Executa a função
buscar_dados(tabelas)


def gerar_dados_completos():
    anos = [2023, 2024, 2025]
    
    for ano in anos:
        print(f"Processando Safra {ano}...")
        
        # Período de colheita no MT (Janeiro a Março)
        data_atual = datetime(ano, 1, 1)
        data_fim = datetime(ano, 3, 30)
        
        while data_atual <= data_fim:
            # 1. Seleciona Maquina e Talhão do dia
            m_id = random.choice(dados_tabela["maquinas"])
            t_id = random.choice(dados_tabela["talhoes"])
            
            # 2. Simula 10 pontos de telemetria e sensores para este dia
            lote_telemetria = []
            lote_sensores = []
            peso_dia = 0
            
            for h in range(10):
                momento = data_atual + timedelta(hours=h + 8) # Das 08h às 18h
                
                # Variáveis com padrão lógico
                umidade_solo = random.uniform(15, 30)
                velocidade = random.uniform(5, 10)
                
                # LÓGICA DE NEGÓCIO: Se solo é ID 2 ou 5 (Argiloso nas fotos), gasta mais
                fator_solo = 1.3 if t_id in [2, 5] else 1.0
                consumo = (velocidade * 2.5 * fator_solo) + (umidade_solo * 0.2)
                
                lote_telemetria.append({
                    "maquina_id": m_id,
                    "timestamp": momento.isoformat(),
                    "consumo_h": round(consumo, 2),
                    "velocidade_kmh": round(velocidade, 2),
                    "umidade_grao": round(random.uniform(12, 18), 2),
                    "latitude": -12.5 + random.uniform(-0.01, 0.01),
                    "longitude": -55.5 + random.uniform(-0.01, 0.01),
                    "talhoes_id": t_id
                })
                
                lote_sensores.append({
                    "talhoes_id": t_id,
                    "timestamp": momento.isoformat(),
                    "umidade_percent": round(umidade_solo, 2)
                })
                
                peso_dia += random.uniform(500, 800) # Kg colhidos nessa hora

            # Inserindo no Banco
            supabase.table("telemetria_maquinas").insert(lote_telemetria).execute()
            supabase.table("sensores_solo").insert(lote_sensores).execute()
            
            # 3. Gera registro de Colheita (Resumo do dia/talhão)
            supabase.table("colheitas").insert({
                "talhoes_id": t_id,
                "safra": ano,
                "peso_kg": round(peso_dia, 2),
                "maquinas_id": m_id
            }).execute()

            data_atual += timedelta(days=1)

    print("--- BASE DE DADOS POPULADA COM SUCESSO ---")

gerar_dados_completos()