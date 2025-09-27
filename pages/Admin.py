import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim

from db_sqlite import get_todas_cozinhas, adicionar_cozinha, get_todos_bairros, adicionar_bairro
from db_mongo import adicionar_restaurante

st.set_page_config(page_title="Painel Admin", page_icon="🛠️")

if 'center_admin' not in st.session_state:
    st.session_state.center_admin = [-7.1200, -34.8800]
if 'marker_admin' not in st.session_state:
    st.session_state.marker_admin = [None, None]

st.title("🛠️ Painel Administrativo")
st.markdown("Gerencie os dados da aplicação.")

col1, col2 = st.columns(2)
with col1:
    with st.expander("➕ Adicionar Novo Tipo de Cozinha"):
        novo_tipo_cozinha = st.text_input("Nome do tipo de cozinha")
        if st.button("Salvar Cozinha"):
            if novo_tipo_cozinha and adicionar_cozinha(novo_tipo_cozinha):
                st.success(f"Cozinha '{novo_tipo_cozinha}' adicionada!")
            else:
                st.error("Erro ao adicionar cozinha.")

with col2:
    with st.expander("🏘️ Adicionar Novo Bairro"):
        novo_bairro = st.text_input("Nome do Bairro")
        if st.button("Salvar Bairro"):
            if novo_bairro and adicionar_bairro(novo_bairro):
                st.success(f"Bairro '{novo_bairro}' adicionado!")
            else:
                st.error("Erro ao adicionar bairro.")

st.markdown("---")
st.header("🏪 Adicionar Novo Restaurante")

with st.form(key="add_restaurante_form"):
    nome_restaurante = st.text_input("Nome do Restaurante")
    
    opcoes_cozinhas = get_todas_cozinhas()
    map_cozinhas = {nome: id for id, nome in opcoes_cozinhas}
    cozinha_selecionada = st.selectbox("Tipo de Cozinha", options=map_cozinhas.keys())

    opcoes_bairros = get_todos_bairros()
    map_bairros = {nome: id for id, nome in opcoes_bairros}
    bairro_selecionado = st.selectbox("Bairro", options=map_bairros.keys())

    endereco_restaurante = st.text_input("Endereço Completo (Rua e Número)", placeholder="Ex: Rua das Acácias, 123")
    
    if st.form_submit_button("Verificar Endereço no Mapa"):
        endereco_completo = f"{endereco_restaurante}, {bairro_selecionado}"
        geolocator = Nominatim(user_agent="admin_panel_app")
        try:
            location = geolocator.geocode(endereco_completo)
            if location:
                st.session_state.center_admin = [location.latitude, location.longitude]
                st.session_state.marker_admin = [location.latitude, location.longitude]
                st.success("Endereço localizado no mapa abaixo!")
            else:
                st.session_state.marker_admin = [None, None]
                st.error("Endereço não encontrado.")
        except Exception:
            st.error("Erro ao processar o endereço.")

m = folium.Map(location=st.session_state.center_admin, zoom_start=16)
if st.session_state.marker_admin[0] is not None:
    folium.Marker(st.session_state.marker_admin, tooltip="Local do Restaurante").add_to(m)
map_data = st_folium(m, width=700, height=400)

if map_data and map_data['last_clicked']:
    st.session_state.marker_admin = [map_data['last_clicked']['lat'], map_data['last_clicked']['lng']]
    st.info(f"Posição ajustada no mapa para: {st.session_state.marker_admin}")

if st.button("Salvar Restaurante no Banco de Dados"):
    lat, lon = st.session_state.marker_admin
    if not all([nome_restaurante, cozinha_selecionada, bairro_selecionado, lat, lon]):
        st.warning("Preencha todos os campos e verifique o endereço no mapa.")
    else:
        cozinha_id = map_cozinhas[cozinha_selecionada]
        bairro_id = map_bairros[bairro_selecionado]
        adicionar_restaurante(nome_restaurante, cozinha_id, bairro_id, lat, lon)
        st.success(f"Restaurante '{nome_restaurante}' salvo com sucesso!")
        st.session_state.marker_admin = [None, None]