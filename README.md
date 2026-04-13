🚜 Projeto End-to-End: Telemetria e Inteligência no Agronegócio
Este projeto demonstra a construção de um ecossistema de dados completo, desde a modelagem de um banco de dados relacional na nuvem até a entrega de um dashboard estratégico para tomada de decisão no campo.

🚀 O Desafio
O objetivo foi criar uma solução que simulasse o monitoramento de uma frota agrícola, permitindo analisar o consumo de combustível e a eficiência operacional em diferentes cenários de solo e safra.

🛠️ Etapas de Desenvolvimento
1. Modelagem e Infraestrutura (Supabase)
Estruturação do banco de dados relacional utilizando PostgreSQL no Supabase.

Criação de tabelas para maquinas, talhoes, colheitas e telemetria.

Definição de chaves primárias e estrangeiras para garantir a integridade dos dados.

2. Engenharia de Dados e Simulação (Python)
Um dos maiores desafios foi desenvolver um script em Python que não gerasse apenas dados aleatórios, mas que seguisse uma lógica de negócio:

Geração de +2.700 linhas de dados sintéticos.

Lógica implementada: O script correlaciona o tipo de solo (ex: argiloso vs. arenoso) com o esforço da máquina, resultando em variações realistas de consumo de combustível.

Utilização de bibliotecas como pandas e integração direta com a API do Supabase para ingestão dos dados.

3. Conexão e Troubleshooting (Power BI)
A etapa de conexão apresentou desafios técnicos que exigiram soluções criativas:

Superação de Bloqueios: Resolução de erros de "Host não conhecido" e problemas de certificado SSL/Criptografia na conexão direta.

Consumo via API REST: Implementação de conexão via Web API com cabeçalhos de autenticação (apikey e Bearer Token) para contornar limitações de drivers locais (Npgsql).

Tratamento de Erros: Resolução de inconsistências de autenticação anônima e cabeçalhos no Power Query.

4. Visualização e Business Intelligence
Desenvolvimento de um Overview de Negócio focado em responder:

Qual a média de consumo por tipo de solo?

Como a eficiência das máquinas varia entre as safras?

Quais talhões apresentam os maiores custos operacionais?

📈 Resultados
O dashboard final permite que um gestor agrícola identifique padrões de desperdício e planeje melhor a alocação de máquinas de acordo com a umidade e o tipo de solo, otimizando o custo por hectare.

💻 Tecnologias Utilizadas
Banco de Dados: PostgreSQL (Supabase)

Linguagem: Python (Pandas, Supabase-py)

BI: Power BI (Power Query, DAX)

💡 Como visualizar
Os scripts SQL de criação das tabelas estão na pasta /sql.

O script Python de geração de massa de dados está em /scripts.

O arquivo .pbix está disponível para download na pasta /report.
