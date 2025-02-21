# Predição de Obesidade com Naive Bayes

## Visão Geral

Este projeto visa construir um classificador binário para prever se um paciente é obeso ou não com base em um conjunto de dados de um estudo sobre obesidade. A previsão é feita utilizando o algoritmo **Naive Bayes** e considera hábitos de saúde, condições físicas e informações complementares, sem incluir peso e altura.

## Objetivo do Projeto

A clínica de endocrinologia deseja validar se esse conjunto de dados pode ser usado para prever a obesidade de seus pacientes a partir das respostas de um formulário similar ao do estudo.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas para Análise de Dados**: Pandas, NumPy, Sweetviz, Statsmodels
- **Visualização de Dados**: Matplotlib, Seaborn, Plotly
- **Machine Learning**: Scikit-learn (Naive Bayes, Label Encoding, OneHot Encoding, Feature Selection, Pipeline, Train-Test Split)
- **Otimização de Hiperparâmetros**: Optuna
- **Salvamento do Modelo**: Joblib

## Passos Realizados

### 1. Exploração e Processamento dos Dados

- Análise exploratória utilizando **Sweetviz** para sumarizar estatísticas descritivas.
- Análise da distribuição da variável-alvo e de variáveis categóricas.
- Conversão de variáveis categóricas para valores numéricos usando **LabelEncoder** e **OneHotEncoder**.
- Testes estatísticos para verificar a independência das variáveis (teste qui-quadrado).

### 2. Construção do Modelo Baseline

- Utilização do classificador **Gaussian Naive Bayes**.
- Divisão dos dados em **treino (80%)** e **teste (20%)**.
- Construção de um pipeline de transformação dos dados.

### 3. Seleção de Features

- Uso do **SelectKBest** para selecionar as melhores features com base no teste qui-quadrado.
- Treinamento de um novo modelo **Gaussian Naive Bayes** apenas com as features mais relevantes.

### 4. Otimização de Hiperparâmetros

- Uso do **Optuna** para otimizar a quantidade de features selecionadas (valores de *k* no SelectKBest).
- Testes com vários valores de *k* para maximizar a métrica de **recall**.

### 5. Avaliação do Modelo

- **Matriz de confusão** e **relatório de classificação** para avaliar o desempenho do modelo.
- Comparativo entre o modelo baseline e o modelo otimizado.

### 6. Salvamento do Modelo

- Modelo treinado salvo com **joblib** para uso futuro.

## Como Executar o Projeto

1. Clone o repositório
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script de treinamento do modelo:
   ```bash
   python myobesitymodel.py
   ```
4. Utilize o modelo treinado para previsões futuras carregando-o com:
   ```python
   import joblib
   modelo = joblib.load('modelo_obesity.pkl')
   ```

