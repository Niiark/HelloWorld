import streamlit as st
import pandas as pd
from datetime import date

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

plan_defaut = {
    "Lundi": [
        {"name": "Jumping jacks (30 sec)", "done": False},
        {"name": "Burpees (30 sec)", "done": False},
        {"name": "Mountain climbers (30 sec)", "done": False},
        {"name": "Squats sautés (30 sec)", "done": False},
    ],
    "Mardi": [
        {"name": "Squats (45 sec)", "done": False},
        {"name": "Pompes (45 sec)", "done": False},
        {"name": "Planche (45 sec)", "done": False},
        {"name": "Fentes alternées (45 sec)", "done": False},
        {"name": "Gainage latéral (45 sec)", "done": False},
    ],
    "Mercredi": [
        {"name": "Jumping jacks (30 sec)", "done": False},
        {"name": "Burpees (30 sec)", "done": False},
        {"name": "Squats (45 sec)", "done": False},
        {"name": "Pompes (45 sec)", "done": False},
    ],
    "Jeudi": [],
    "Vendredi": [],
    "Samedi": [],
    "Dimanche": [],
}

if "schedule" not in st.session_state:
    st.session_state.schedule = plan_defaut
if "progress" not in st.session_state:
    st.session_state.progress = []

st.sidebar.header("Ajouter ou modifier une séance")
jour_select = st.sidebar.selectbox("Jour de la semaine", jours)
nouvel_exo = st.sidebar.text_input("Nouvel exercice", key="new_ex")
if st.sidebar.button("Ajouter au programme"):
    if nouvel_exo:
        st.session_state.schedule[jour_select].append({"name": nouvel_exo, "done": False})
        st.session_state.new_ex = ""

st.header("Mon Programme")
for jour in jours:
    st.subheader(jour)
    exos = st.session_state.schedule[jour]
    if exos:
        for i, exo in enumerate(exos):
            col1, col2 = st.columns([4, 1])
            name_key = f"{jour}_{i}_name"
            done_key = f"{jour}_{i}_done"
            new_name = col1.text_input("Exercice", value=exo["name"], key=name_key)
            done = col2.checkbox("Fait", value=exo.get("done", False), key=done_key)
            st.session_state.schedule[jour][i]["name"] = new_name
            if done and not exo.get("done", False):
                st.session_state.progress.append({"date": date.today(), "exercise": new_name})
            st.session_state.schedule[jour][i]["done"] = done
    else:
        st.write("Repos")

st.header("Suivi des exercices effectués")
if st.session_state.progress:
    df = pd.DataFrame(st.session_state.progress)
    st.dataframe(df)
