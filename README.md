# 🚜 Dashboard de Telemetria e Eficiência Agrícola

Dashboard interativo desenvolvido para análise de performance de máquinas agrícolas, consumo de combustível e produtividade por safra/talhão.

## 🛠️ Desafios Técnicos Superados
Neste projeto, implementei soluções de engenharia de dados para conectar o Power BI a um banco de dados **Supabase (PostgreSQL)**:
- **Conexão via API REST:** Consumo de dados via endpoints JSON para garantir portabilidade.
- **Modelagem Star Schema:** Organização de tabelas Fato (Telemetria) e Dimensão (Talhões, Máquinas, Colheitas).
- **Tratamento de Ambiguidade:** Resolução de caminhos circulares no modelo de dados para garantir a integridade das médias por safra.

## 📊 Insights do Projeto
- Identificação de maior consumo em solos **Argilosos** (Talhões Norte/Oeste) vs **Arenosos**.
- Correlação entre umidade do solo e eficiência operacional.
- Média de consumo por safra ajustada via relacionamentos cruzados.

## 🚀 Tecnologias
- **Power BI** (DAX, Power Query)
- **Supabase / PostgreSQL**
- **Python** (Geração de massa de dados sintéticos)
