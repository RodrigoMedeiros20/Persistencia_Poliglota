# 🍽️ Onde Comer? - Projeto de Persistência Poliglota

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-orange?style=for-the-badge&logo=streamlit)
![MongoDB](https://img.shields.io/badge/MongoDB-4.4%2B-green?style=for-the-badge&logo=mongodb)
![SQLite](https://img.shields.io/badge/SQLite-3-darkblue?style=for-the-badge&logo=sqlite)

Este projeto é uma aplicação web desenvolvida em Python com Streamlit que demonstra o conceito de **Persistência Poliglota** e **Geoprocessamento**. A aplicação funciona como um buscador de restaurantes, permitindo que usuários encontrem locais próximos a um endereço e que administradores gerenciem os dados dos estabelecimentos.

O projeto foi desenvolvido como uma solução prática para a proposta acadêmica de "Persistência Poliglota com MongoDB + SQLite e Geo-Processamento".

## 🚀 Funcionalidades Principais

* **Busca por Proximidade:** Usuários podem inserir um endereço e um raio em quilômetros para encontrar restaurantes na região.
* **Visualização em Mapa:** Os resultados da busca são exibidos em uma tabela e plotados em um mapa interativo com nomes e detalhes.
* **Persistência Poliglota:** Utiliza SQLite para dados estruturados (Cozinhas, Bairros) e MongoDB para dados semiestruturados (Restaurantes).
* **Painel Administrativo:** Uma página separada e protegida para administradores, onde é possível cadastrar novos tipos de cozinha, bairros e restaurantes.
* **Geocodificação:** Converte endereços de texto em coordenadas geográficas (latitude e longitude) para o cadastro e a busca.

## 🏛️ Arquitetura e Como Funciona

[cite_start]O núcleo do projeto é a utilização de dois sistemas de banco de dados distintos para otimizar o armazenamento de diferentes tipos de dados[cite: 3]:

* [cite_start]**SQLite**: Utilizado para armazenar dados altamente estruturados e relacionais, como Tipos de Cozinha e Bairros[cite: 8].
* [cite_start]**MongoDB**: Utilizado para armazenar documentos semiestruturados no formato JSON, ideais para dados flexíveis como os detalhes dos restaurantes, que incluem coordenadas geográficas aninhadas[cite: 12, 13].

[cite_start]O fluxo de dados para o usuário final envolve a geocodificação do endereço fornecido, seguida por uma consulta de geoprocessamento que calcula a distância de cada restaurante (armazenado no MongoDB) até o ponto do usuário[cite: 28, 29, 31]. [cite_start]Os resultados são então enriquecidos com dados do SQLite (nomes das cozinhas e bairros) antes de serem exibidos[cite: 31].

## 🛠️ Tecnologias Utilizadas

[cite_start]O projeto foi construído com as seguintes tecnologias [cite: 48-55]:

* [cite_start]**Backend:** Python 3.10+ [cite: 49]
* [cite_start]**Interface Web:** Streamlit [cite: 50]
* [cite_start]**Banco de Dados Relacional:** SQLite3 [cite: 51]
* [cite_start]**Banco de Dados NoSQL:** MongoDB (com a biblioteca PyMongo) [cite: 52]
* [cite_start]**Geoprocessamento:** Geopy [cite: 53]
* [cite_start]**Mapas Interativos:** Folium [cite: 54]
* [cite_start]**Manipulação de Dados:** Pandas [cite: 55]

## 📁 Estrutura do Projeto

[cite_start]A aplicação é estruturada como um projeto multi-páginas do Streamlit, uma evolução da estrutura sugerida na proposta acadêmica[cite: 46]:

app_restaurante/
├── 📄 Home.py                 # Página principal para o usuário
├── 📄 db_mongo.py             # Funções de interação com o MongoDB
├── 📄 db_sqlite.py            # Funções de interação com o SQLite
├── 📄 geoprocessamento.py     # Funções de cálculo de distância
├── 📄 requirements.txt        # Dependências do projeto
├── 📁 .streamlit/
│   └── 📄 config.toml         # Arquivo de tema do Streamlit
└── 📁 pages/
└── 📄 1_Painel_Admin.py   # Página do painel administrativo


## 🚀 Como Usar e Executar o Projeto

Siga os passos abaixo para executar a aplicação localmente.

### Pré-requisitos

* Python 3.10 ou superior
* MongoDB Community Server instalado e o serviço em execução.

### Instalação

1.  Clone este repositório (ou simplesmente crie os arquivos como descrito).
2.  Navegue até a pasta raiz do projeto (`app_restaurante/`).
3.  Crie um ambiente virtual (recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```
4.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Executando a Aplicação

1.  Certifique-se de que seu serviço do MongoDB está ativo.
2.  Delete o arquivo `jantares.db` (se existir de uma execução anterior) para garantir que o banco de dados SQLite seja criado com a estrutura mais recente.
3.  No terminal, a partir da pasta raiz do projeto, execute:
    ```bash
    streamlit run Home.py
    ```
A aplicação será aberta no seu navegador. Você poderá navegar entre a página principal e o painel administrativo pela barra lateral.