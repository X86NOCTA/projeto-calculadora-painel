import streamlit as st
import math

st.set_page_config(page_title="CALCULADORA DE PAINÉIS", layout="wide")

st.markdown("<h1 style='text-align:center;'>CALCULADORA DE PAINÉIS DE GEOMEMBRANA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>*ATENÇÃO! Utilize ponto (.) ao invés de vírgula (,)</p>", unsafe_allow_html=True)

# Entradas lado a lado
col1, col2, col3 = st.columns(3)
with col1:
    largura = st.text_input("Largura (m)")
with col2:
    comprimento = st.text_input("Comprimento (m)")
with col3:
    profundidade = st.text_input("Profundidade (m)")

st.markdown("---")

if st.button("Calcular"):
    try:
        valor1 = float(largura)
        valor2 = float(comprimento)
        valor3 = float(profundidade)

        valor_largura = (valor1 + 2) + (valor3 * 2)
        valor_comprimento = (valor2 + 2) + (valor3 * 2)
        perda_solda = 0.10

        materiais = {
            "PVC TRANÇADO BRANCO/CINZA 0,4MM": {"peso": 0.6, "bobina": 3.0, "preco": 25},
            "PVC PURO PRETO/PRETO 1MM": {"peso": 1.1, "bobina": 2.3, "preco": 57},
            "PVC TRANÇADO AZUL/AZUL 0,9MM": {"peso": 1.3, "bobina": 3.0, "preco": 68},
            "PVC TRANÇADO CINZA/CINZA 0.8MM": {"peso": 0.6, "bobina": 2.0, "preco": 50},
            "PEAD TRANÇADO VERDE/PRETO 0,75MM": {"peso": 0.45, "bobina": 4.2, "preco": 32},
            "PEAD TRANÇADO PRETO/PRETO 1MM": {"peso": 0.6, "bobina": 4.0, "preco": 40},
        }

        colunas = st.columns(3)
        i = 0

        for nome, dados in materiais.items():
            peso_especifico = dados["peso"]
            L_bobina = dados["bobina"]
            preco = dados["preco"]

            faixas = math.ceil(valor_largura / (L_bobina - perda_solda))
            largura_real = (faixas * L_bobina) - (perda_solda * (faixas - 1))
            comprimento_real = valor_comprimento
            valor_total_real = largura_real * comprimento_real

            peso_painel = peso_especifico * valor_total_real
            tempo_total_minutos = ((faixas - 1) * 2.5) * valor_comprimento
            horas = int(tempo_total_minutos // 60)
            minutos = int(tempo_total_minutos % 60)
            valor_total = preco * valor_total_real

            with colunas[i]:
                st.markdown(
                    f"""
                    <div style="border:2px solid #1E90FF; border-radius:10px; padding:15px; margin-bottom:20px;">
                        <h3 style="color:#00BFFF;">{nome}</h3>
                        <p><b>LARGURA:</b> {largura_real:.2f} m</p>
                        <p><b>COMPRIMENTO:</b> {comprimento_real:.2f} m</p>
                        <p><b>METRAGEM QUADRADA:</b> {valor_total_real:.2f} m²</p>
                        <p><b>PESO DO PAINEL:</b> {peso_painel:.2f} kg</p>
                        <p><b>VALOR ESTIMADO:</b> R$ {valor_total:.2f}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            i += 1
            if i >= 3:
                i = 0
                colunas = st.columns(3)

    except ValueError:
        st.error("Por favor, digite números válidos (use ponto).")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>© 2025 Brasil Piscis - Developed by Matheus Tartaglia</p>", unsafe_allow_html=True)



# coloquei esse comentario 