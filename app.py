import streamlit as st
import pandas as pd
import joblib

style = f"""
<style>
    .appview-container .main .block-container{{
        max-width: 70%;
    }}
</style>
"""

st.markdown(style, unsafe_allow_html=True)


# imagen
from PIL import Image
image = ('maraton.jpg')
st.image(image,width=660)


# titulo

st.header("Predicción de maratón")


col1, col2 = st.columns(2)
# categoria
with col1:
    st.subheader("Categoría")
    categoria = st.selectbox("Selecciona categoría : ", ('MAM', 'M45', 'M40', 'M50', 'M55', 'WAM'))
# Km4week
with col2:
    st.subheader("Km mensuales corridos")
    recorrido = st.number_input ("Introduce total de Km corridos el mes antes del maratón :", min_value=0.0)

col1, col2 = st.columns(2)
with col1:
# sp4week
    st.subheader("Velocidad media Km mensuales")
    velocidad = st.number_input (" Introduce velocidad media de Km corridos el mes antes del maratón : ", min_value=0.0)
# CrossTraining
with col2:
    st.subheader("¿ Haces ciclismo ?")
    ciclismo = st.number_input (" Introduce horas de ciclismo realizadas durante el mes", min_value=0.0)
# Wall21
st.subheader("Tiempo media maratón")
media = st.number_input("Introdduce tu tiempo en media maraton(decimal) ", min_value=0.0)



# boton
if st.button("Predicción"):
    
    # Unpickle classifier
    clf = joblib.load("maraton_model.pkl")
    
    # datos entradas
    maraton = pd.DataFrame([[categoria, recorrido, velocidad, ciclismo, media ]], 
                     columns = ["Category", "km4week", "sp4week", "CrossTraining", "Wall21"])
    maraton['Category'].replace(['MAM', 'M45', 'M40', 'M50', 'M55', 'WAM'], [1., 2., 3., 4., 5., 6.], inplace=True)

    
    # prediccion
    prediction = clf.predict(maraton)[0]
    
    # salida
    st.text(f"El tiempo decimal final para el maratón será:  {prediction}")