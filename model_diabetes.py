import numpy as np
import joblib
import streamlit as st

# Carregar modelo
model = joblib.load("model.pkl")

def diabetes_prediction(input_data):
    input_data = np.asarray(input_data).reshape(1, -1)
    prediction = model.predict(input_data)

    if prediction[0] == 0:
        return 'A pessoa não é diabética'
    else:
        return 'A pessoa é diabética'

def main():
    st.title("🩺 Predição de Diabetes")

    st.subheader("Insira os dados do paciente:")

    gravidezes = st.number_input('Número de gestações', min_value=0, max_value=20, step=1)
    glicose = st.number_input('Glicose (mg/dL)', min_value=0, max_value=200)
    pressao = st.number_input('Pressão arterial (mmHg)', min_value=0, max_value=140)
    espessura_pele = st.number_input('Espessura da pele (mm)', min_value=0, max_value=100)
    insulina = st.number_input('Insulina (µU/mL)', min_value=0, max_value=900)
    imc = st.number_input('IMC (kg/m²)', min_value=0.0, max_value=70.0)
    historico = st.number_input('Histórico familiar (Diabetes Pedigree Function)', min_value=0.0, max_value=3.0)
    idade = st.number_input('Idade', min_value=1, max_value=120)

    if st.button('🔍 Resultado'):
        dados = [
            gravidezes,
            glicose,
            pressao,
            espessura_pele,
            insulina,
            imc,
            historico,
            idade
        ]

        resultado = diabetes_prediction(dados)

        if "não" in resultado:
            st.success(resultado)
        else:
            st.error(resultado)

if __name__ == '__main__':
    main()
