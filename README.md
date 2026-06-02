# Análise de Asteróides e Objetos Próximos a Terra (NEOs)

**Disciplina:** Introdução à Ciência de Dados  
**Instituição:** Universidade Federal da Paraíba (UFPB)

---

## Integrantes:
* **João Pedro da Silva Araújo**
* **Brenda Letícia do N. Dias** 
* **Alonso da Costa Sousa Araújo**
* **Pedro Lucas Moreira Rolim**

---

## Tema do Projeto
O projeto aplica conceitos de Ciência de Dados no campo da astronomia e defesa planetária. 

O objetivo principal é extrair, processar e analisar dados de milhares de asteroides classificados como *Near Earth Objects* (NEOs). A partir de características físicas e orbitais (como diâmetro máximo, velocidade relativa e distância de aproximação), utilizaremos o algoritmo de Aprendizado Não Supervisionado **K-Means** para descobrir padrões ocultos e agrupar esses objetos em perfis espaciais de risco e comportamento, indo além da simples análise descritiva.

---

## Abordagem de Coleta dos Dados
A coleta será realizada via código de forma automatizada:

1. **Fonte dos Dados:** Utilizaremos a [API pública NeoWs (Near Earth Object Web Service)](https://api.nasa.gov/) fornecida oficialmente pela NASA.
2. **Método de Extração:** Como a API possui um limite de requisição nativo (blocos máximos de 7 dias), desenvolvemos um script em Python utilizando as bibliotecas `requests` e `datetime`. 
3. **Pipeline (Loop Temporal):** O script executa um loop automatizado que itera sobre o calendário, solicitando dados de semana em semana até extrair um histórico massivo de 10 anos de registros orbitais.
4. **Tratamento Inicial:** O payload bruto em formato `.json` é filtrado "no voo" (in-memory) durante a extração, selecionando apenas as *features* matemáticas de interesse, e consolidado em um `DataFrame` do Pandas. O resultado final é exportado como um arquivo `.csv` limpo, pronto para a Análise Exploratória e o pipeline de Machine Learning.

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Coleta:** `requests`, `JSON`
* **Manipulação e Análise:** `pandas`, `numpy`, `matplotlib`, `seaborn`
* **Machine Learning:** `scikit-learn` (K-Means Clustering)
* **Visualização:** `streamlit` (Dashboard Interativo)
