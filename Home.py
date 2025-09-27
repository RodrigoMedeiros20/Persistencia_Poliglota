import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import st_folium

from db_mongo import get_todos_restaurantes
from geoprocessamento import encontrar_restaurantes_proximos
from db_sqlite import get_cozinha_por_id, get_bairro_por_id

st.set_page_config(page_title="Onde Comer?", page_icon="🍽️", layout="centered")

st.markdown("""<style>.main-button > button {background-color: #1E90FF;color: white;font-weight: bold;}</style>""", unsafe_allow_html=True)

if 'search_results' not in st.session_state:
    st.session_state.search_results = None

st.title("🍽️ Onde Comer?")
st.markdown("Encontre os melhores restaurantes perto de você!")
st.markdown("---")

with st.form(key="busca_restaurantes"):
    endereco = st.text_input("📍 Informe seu endereço ou um ponto de referência", placeholder="Ex: Av. Epitácio Pessoa, João Pessoa, PB")
    raio = st.slider("Selecione o raio de busca (em km)", min_value=1, max_value=25, value=5)
    submit_button = st.form_submit_button(label="🔍 Encontrar Restaurantes Próximos")

if submit_button:
    st.session_state.search_results = None
    if not endereco:
        st.warning("Por favor, informe um endereço para a busca.")
    else:
        user_lat, user_lon = None, None
        with st.spinner("Verificando sua localização..."):
            geolocator = Nominatim(user_agent="onde_comer_app")
            try:
                location = geolocator.geocode(endereco)
                if location:
                    user_lat, user_lon = location.latitude, location.longitude
                    st.info(f"Endereço encontrado: {location.address}")
                else:
                    st.error("Endereço não encontrado. Tente ser mais específico."); st.stop()
            except Exception as e:
                st.error(f"Ocorreu um erro na busca pelo endereço: {e}"); st.stop()
        
        with st.spinner("Buscando restaurantes na região..."):
            todos_restaurantes = get_todos_restaurantes()
            restaurantes_encontrados = encontrar_restaurantes_proximos(user_lat, user_lon, raio, todos_restaurantes)
        
        if restaurantes_encontrados:
            dados_para_exibir = []
            for r in restaurantes_encontrados:
                dados_para_exibir.append({
                    "Nome": r['nome_local'],
                    "Cozinha": get_cozinha_por_id(r['cozinha_id']),
                    "Bairro": get_bairro_por_id(r['bairro_id']),
                    "Distância (km)": r['distancia_km'],
                    "latitude": r['coordenadas']['latitude'],
                    "longitude": r['coordenadas']['longitude']
                })
            df = pd.DataFrame(dados_para_exibir)
            st.session_state.search_results = {"df": df, "user_lat": user_lat, "user_lon": user_lon}
        else:
            st.warning("Nenhum restaurante encontrado neste raio. Tente aumentar a distância.")

if st.session_state.search_results is not None:
    results = st.session_state.search_results
    df = results["df"]
    user_lat, user_lon = results["user_lat"], results["user_lon"]

    st.success(f"🎉 Encontramos {len(df)} restaurante(s) para você!")
    
    st.dataframe(df[['Nome', 'Cozinha', 'Bairro', 'Distância (km)']], use_container_width=True)

    st.subheader("Visualização no Mapa")
    mapa_resultados = folium.Map(location=[user_lat, user_lon], zoom_start=14)
    folium.Marker([user_lat, user_lon], popup="Sua Localização", tooltip="Você está aqui", icon=folium.Icon(color="blue", icon="person")).add_to(mapa_resultados)
    for index, row in df.iterrows():
        popup_html = f"<b>{row['Nome']}</b><br>Cozinha: {row['Cozinha']}<br>Bairro: {row['Bairro']}<br>Distância: {row['Distância (km)']} km"
        folium.Marker([row['latitude'], row['longitude']], popup=folium.Popup(popup_html, max_width=200), tooltip=row['Nome']).add_to(mapa_resultados)
    st_folium(mapa_resultados, use_container_width=True)