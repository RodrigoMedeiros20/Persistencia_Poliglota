from geopy.distance import geodesic

def calcular_distancia(ponto1, ponto2):
    """Calcula a distância em km entre duas coordenadas (lat, lon)."""
    return geodesic(ponto1, ponto2).km

def encontrar_restaurantes_proximos(lat_usuario, lon_usuario, raio_km, restaurantes):
    """
    Filtra uma lista de restaurantes, retornando apenas os que estão dentro do raio
    a partir da localização do usuário.
    """
    ponto_usuario = (lat_usuario, lon_usuario)
    restaurantes_proximos = []

    for restaurante in restaurantes:
        coords = restaurante.get("coordenadas", {})
        lat_restaurante = coords.get("latitude")
        lon_restaurante = coords.get("longitude")

        if lat_restaurante is not None and lon_restaurante is not None:
            ponto_restaurante = (lat_restaurante, lon_restaurante)
            distancia = calcular_distancia(ponto_usuario, ponto_restaurante)

            if distancia <= raio_km:
                restaurante['distancia_km'] = round(distancia, 2)
                restaurantes_proximos.append(restaurante)

    restaurantes_proximos.sort(key=lambda r: r['distancia_km'])
    
    return restaurantes_proximos