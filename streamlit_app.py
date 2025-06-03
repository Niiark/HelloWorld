import streamlit as st
import pandas as pd

st.title("Programme Sportif Hebdomadaire")

jours = [
    "Lundi",
    "Mardi",
    "Mercredi",
    "Jeudi",
    "Vendredi",
    "Samedi",
    "Dimanche",
]

if "schedule" not in st.session_state:
    st.session_state.schedule = {jour: [] for jour in jours}
if "progress" not in st.session_state:
    st.session_state.progress = []

st.sidebar.header("Ajouter une séance")
jour = st.sidebar.selectbox("Jour de la semaine", jours)
exercices = st.sidebar.text_input("Exercices (séparés par des virgules)")
if st.sidebar.button("Ajouter au programme"):
    if exercices:
        st.session_state.schedule[jour].extend(
            [e.strip() for e in exercices.split(",") if e.strip()]
        )

st.header("Mon Programme")
for jour in jours:
    st.subheader(jour)
    exos = st.session_state.schedule[jour]
    if exos:
        for exo in exos:
            st.write("-", exo)
    else:
        st.write("Repos")

st.header("Suivi des progrès")
col1, col2 = st.columns(2)
date = col1.date_input("Date")
performance = col2.number_input("Performance (kg, km, etc.)", min_value=0.0)
if st.button("Ajouter un progrès"):
    st.session_state.progress.append({"date": date, "performance": performance})

if st.session_state.progress:
    df = pd.DataFrame(st.session_state.progress)
    st.line_chart(df.set_index("date"))
    st.dataframe(df)
