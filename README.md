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

O núcleo do projeto é a utilização de dois sistemas de banco de dados distintos para otimizar o armazenamento de diferentes tipos de dados:

* **SQLite**: Utilizado para armazenar dados altamente estruturados e relacionais, como Tipos de Cozinha e Bairros.
* **MongoDB**: Utilizado para armazenar documentos semiestruturados no formato JSON, ideais para dados flexíveis como os detalhes dos restaurantes, que incluem coordenadas geográficas aninhadas.

O fluxo de dados para o usuário final envolve a geocodificação do endereço fornecido, seguida por uma consulta de geoprocessamento que calcula a distância de cada restaurante (armazenado no MongoDB) até o ponto do usuário. Os resultados são então enriquecidos com dados do SQLite (nomes das cozinhas e bairros) antes de serem exibidos.

## 🛠️ Tecnologias Utilizadas

O projeto foi construído com as seguintes tecnologias:

* **Backend:** Python 3.10+
* **Interface Web:** Streamlit
* **Banco de Dados Relacional:** SQLite3
* **Banco de Dados NoSQL:** MongoDB (com a biblioteca PyMongo)
* **Geoprocessamento:** Geopy
* **Mapas Interativos:** Folium
* **Manipulação de Dados:** Pandas

## 📁 Estrutura do Projeto

A aplicação é estruturada como um projeto multi-páginas do Streamlit, uma evolução da estrutura sugerida na proposta acadêmica:

```bash
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
```


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