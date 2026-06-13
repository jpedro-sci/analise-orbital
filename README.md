# Projeto: Análise de Asteroides (NEOs)

**Disciplina:** Introdução à Ciência de Dados  
**Instituição:** UFPB (Universidade Federal da Paraíba)

---

## Equipe
* **João Pedro da Silva Araújo**
* **Brenda Letícia do N. Dias** * **Alonso da Costa Sousa Araújo**
* **Pedro Lucas Moreira Rolim**

---

## Qual é a ideia do projeto?
Esse é o nosso trabalho para a disciplina. A ideia principal aqui é pegar dados reais de asteroides que cruzam a órbita da Terra (a NASA chama de NEOs) e tentar achar padrões neles.

Em vez de só fazer gráficos básicos, o nosso objetivo final é pegar todo esse histórico de 10 anos e jogar num algoritmo chamado **K-Means**. Como ele agrupa as coisas sozinho (sem a gente dar as respostas), queremos ver se a IA consegue descobrir quem são os asteroides mais perigosos, os maiores, ou os mais rápidos, só olhando pra matemática da coisa.

---

## Como a gente pegou esses dados?
Pra não usar planilhas prontas (tipo do Kaggle) que já vêm mastigadas, a gente resolveu ir direto na fonte e puxar tudo da NASA, automatizando pelo código:

1. **Fonte:** Usamos a API pública oficial deles, chamada NeoWs.
2. **Problema do Limite:** A API da NASA trava se você pedir muitos dias de uma vez (limite de segurança é de 7 em 7 dias).
3. **Nossa Solução:** Pra resolver isso de um jeito legal, a gente montou um script em Python usando as bibliotecas `requests` e `datetime`. O código faz um loop que vai avançando de semana em semana e baixando tudo sozinho, montando um histórico gigante de 10 anos em poucos minutos.
4. **Limpando a sujeira:** O arquivo que a NASA devolve (JSON) vem com muita informação inútil para o objetivo do nosso projeto. Então o próprio script já filtra isso na hora, pega só os números que importam, joga num DataFrame do Pandas e salva um arquivo `.csv` limpinho pra gente usar.

---

## O que tem no nosso arquivo? 
Nosso arquivo final gerou essas colunas abaixo. Aqui vai a explicação do que cada uma significa na prática:

* **`id`**
  * *O que é:* O código único de registro do asteroide lá no sistema da NASA.
  * *Exemplo:* `2465633`
* **`nome`**
  * *O que é:* O nome oficial ou a numeração que os astrônomos deram pra rocha.
  * *Exemplo:* `465633 (2009 JR5)`
* **`diametro_min_m`**
  * *O que é:* O menor tamanho estimado do asteroide (em metros).
  * *Exemplo:* `152.9`
* **`diametro_max_m`**
  * *O que é:* O tamanho máximo que ele pode ter (em metros).
  * *Exemplo:* `341.9`
* **`velocidade_km_s`**
  * *O que é:* A velocidade dele quando passou pertinho da Terra (em km/s).
  * *Exemplo:* `18.53`
* **`distancia_km`**
  * *O que é:* A distância mínima que ele passou do nosso planeta (em km).
  * *Exemplo:* `5230000.5`
* **`ameaca`**
  * *O que é:* Um valor True ou False dizendo se a NASA acha que ele é um perigo pra Terra ou não.
  * *Exemplo:* `True`

---

## O arquivo final:
O nosso arquivo `asteroides_10_anos.csv` com todos os dados coletados e tratados tá salvo lá no nosso Drive da equipe. O professor e os colegas podem baixar direto por aqui:

* [🔗 Link pra pasta no Google Drive](https://drive.google.com/drive/folders/1wqkNRG8OlB1cgBnf8aDBQHlKuL2HjB7x?usp=sharing)

---

## O que a gente tá usando?
* **Linguagem:** Python
* **Pra Coletar:** `requests`, `JSON`
* **Pra Analisar os Dados:** `pandas`, `numpy`, `matplotlib`, `seaborn`
