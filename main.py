import streamlit as st


txt = st.text_area("Medical Abstract", value="",height = 400) # Mostramos el área donde se copia el texto
pred = st.button("Predict") # Botón para predecir
