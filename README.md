# 🚜 Projeto End-to-End: Telemetria e Inteligência no Agronegócio

Este projeto demonstra a construção de um ecossistema de dados completo, desde a modelagem de um banco de dados relacional na nuvem até a entrega de um dashboard estratégico para tomada de decisão no campo.

<img width="1797" height="1016" alt="image" src="https://github.com/user-attachments/assets/5a438d11-e036-40fc-a4a3-abe85933799c" />


## 🚀 O Desafio
O objetivo foi criar uma solução que simulasse o monitoramento de uma frota agrícola, permitindo analisar o consumo de combustível e a eficiência operacional em diferentes cenários de solo e safra.

## 🛠️ Etapas de Desenvolvimento

### 1. Modelagem e Infraestrutura (Supabase)
- Estruturação do banco de dados relacional utilizando **PostgreSQL** hospedado no **Supabase**.
- Criação e normalização de tabelas: `maquinas`, `talhoes`, `colheitas`, `sensores_solo` e `telemetria_maquina`.
- Implementação de chaves primárias (PK) e estrangeiras (FK) para garantir a integridade referencial.

<img width="888" height="688" alt="image" src="https://github.com/user-attachments/assets/7f1836b5-1bb5-4338-b040-078d9e83aed2" />


### 2. Engenharia de Dados e Simulação (Python)
Um dos maiores diferenciais técnicos deste projeto foi o desenvolvimento de um script Python para geração de massa de dados sintéticos (+2.700 linhas) com **lógica de negócio aplicada**:
- **Consumo Inteligente:** O script correlaciona o tipo de solo (ex: argiloso vs. arenoso) com o esforço mecânico, resultando em variações realistas de consumo de combustível.
- **Ingestão Automática:** Integração direta com a API do Supabase para o carregamento automatizado dos dados.

### 3. Conexão e Troubleshooting (Power BI)
A etapa de conexão exigiu resoluções de problemas de infraestrutura e segurança:
- **Resolução de Conectividade:** Superação de erros de *"Host não conhecido"* e instabilidades de certificado SSL/Criptografia.

### 4. Visualização e Business Intelligence
Desenvolvimento de um **Overview de Negócio** focado em responder perguntas estratégicas:
- Qual a média de consumo por tipo de solo?
- Como está a produção de cada talhão?
- Qual o desempenho e consumo das máquinas em cada talhão?
- Desempenho da Safra anual

## 📈 Resultados
O dashboard final permite ao gestor agrícola monitorar o desempenho da safra em tempo real, identificar padrões de desperdício e planejar a alocação de máquinas de acordo com o tipo de solo e umidade, otimizando diretamente o custo por hectare.

## 💻 Tecnologias Utilizadas
- **Banco de Dados:** PostgreSQL (Supabase)
- **Linguagens:** Python e SQL
- **BI:** Power BI (Power Query)

## 💡 Como visualizar
- **Scripts SQL:** Localizados na pasta `/sql` (Criação de estrutura).
- **Scripts Python:** Localizados na pasta `/scripts` (Geração de massa de dados).
- **Relatório:** O arquivo `.pbix` está disponível na pasta `/report`.

> **Observação:** Para rodar o projeto, é necessário popular previamente as tabelas de `Talhoes` e `Maquinas` antes de executar o script.
