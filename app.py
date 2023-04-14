import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
import io
def happy(l1:float,l2:float):
        happiness = l1-l2
        if (happiness <= 100) and (happiness > 75):
            st.markdown("# Sei felicissimo!")
        elif (happiness <= 75) and (happiness > 50):
            st.markdown("# Sei proprio felice!")
        elif (happiness <= 50) and (happiness > 0):
            st.markdown("# Sei contento!")
        elif (happiness <= 0) and (happiness > -50):
            st.markdown("# Sei a posto!")
        elif (happiness <= -50) and (happiness > -75):
            st.markdown("# Sei Triste! :(")
        elif (happiness <= -75) and (happiness >= -100):
            st.markdown("# Sei GHISLY!")
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://marketplace.canva.com/EAFHm4JWsu8/1/0/1600w/canva-pink-landscape-desktop-wallpaper-HGxdJA_xIx0.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


def main():
    add_bg_from_url()
    st.header('Paper del cavolo')
    iris = load_iris()
    #Creazione del dataframe
    df = pd.DataFrame(data=iris.data,columns=iris.feature_names)
    #Aggiunta delle etichette di classe
    df['target']= iris.target
    #Cambio i nomi delle classi da valori a stringhe
    df['target']=df['target'].replace({0:"Setosa",1:"Versicolor",2:"Virginica"})
    st.markdown('# Il dataframe ottenuto')
    options = {"mostra 5 datapoint casuali": 0, "mostra solo i primi 5 datapoint":1, "mostra tutto":2}
    add_radio = st.radio(
        "Please choose an option",
        ["mostra 5 datapoint casuali", "mostra solo i primi 5 datapoint", "mostra tutto"])
    if options[add_radio] == 0:
        st.dataframe(df.sample(5))
        
    elif options[add_radio] == 1:
        st.dataframe(df.head())

    elif options[add_radio] == 2:
        st.dataframe(df)
    st.markdown('## Trovo le informazioni')
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
    st.markdown('## Uso il describe')
    st.dataframe(df.describe(include="all"))

    x1 = st.slider('Inserisci quanto sei felice', 0, 100, 25)
    x2 = st.slider('Inserisci quanto sei triste', 0, 100, 35)
    happy(x1,x2)
    

    
    # Using object notation



if __name__ == "__main__":
    main()

