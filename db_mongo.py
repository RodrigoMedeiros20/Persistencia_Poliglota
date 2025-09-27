from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['restaurantes_db']
collection = db['locais']

def adicionar_restaurante(nome, cozinha_id, bairro_id, latitude, longitude):
    """Adiciona um novo restaurante à coleção do MongoDB."""
    documento = {
        "nome_local": nome,
        "cozinha_id": cozinha_id,
        "bairro_id": bairro_id,
        "coordenadas": {
            "latitude": latitude,
            "longitude": longitude
        }
    }
    collection.insert_one(documento)

def get_todos_restaurantes():
    """Retorna uma lista de todos os restaurantes cadastrados."""
    return list(collection.find({}, {'_id': 0}))