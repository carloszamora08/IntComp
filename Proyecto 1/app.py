import streamlit as st
import pandas as pd
import joblib

model = joblib.load("modelo_harrypotter.joblib")

st.set_page_config(page_title="Hogwarts Sorting Hat", page_icon="🧙")

st.title("🧙 Hogwarts Sorting Hat Test")
st.write("Adjust your traits and discover your Hogwarts House!")

st.divider()

famous_characters = {
    "Gryffindor": [
        "Harry Potter",
        "Hermione Granger",
        "Ron Weasley",
        "Albus Dumbledore"
    ],
    "Slytherin": [
        "Draco Malfoy",
        "Severus Snape",
        "Tom Riddle (Voldemort)",
        "Bellatrix Lestrange"
    ],
    "Ravenclaw": [
        "Luna Lovegood",
        "Cho Chang",
        "Filius Flitwick",
        "Gilderoy Lockhart"
    ],
    "Hufflepuff": [
        "Cedric Diggory",
        "Nymphadora Tonks",
        "Newt Scamander",
        "Pomona Sprout"
    ]
}

bravery = st.slider("Bravery", 0, 10, 5)
intelligence = st.slider("Intelligence", 0, 10, 5)
loyalty = st.slider("Loyalty", 0, 10, 5)
ambition = st.slider("Ambition", 0, 10, 5)
dark_arts = st.slider("Dark Arts Knowledge", 0, 10, 5)
quidditch = st.slider("Quidditch Skills", 0, 10, 5)
dueling = st.slider("Dueling Skills", 0, 10, 5)
creativity = st.slider("Creativity", 0, 10, 5)

blood_status = st.selectbox(
    "Blood Status",
    ["Pure-blood", "Half-blood", "Muggle-born"]
)

if st.button("Reveal My House 🪄"):

    new_student = pd.DataFrame([{
        "Bravery": bravery,
        "Intelligence": intelligence,
        "Loyalty": loyalty,
        "Ambition": ambition,
        "Dark_Arts_Knowledge": dark_arts,
        "Quidditch_Skills": quidditch,
        "Dueling_Skills": dueling,
        "Creativity": creativity,
        "Blood_Status": blood_status
    }])

    prediction = model.predict(new_student)[0]
    probabilities = model.predict_proba(new_student)[0]
    classes = model.classes_

    st.success(f"🎉 You belong to: {prediction}!")

    st.write("### 🏆 Famous Members of Your House")
    
    for character in famous_characters.get(prediction, []):
        st.write(f"✨ {character}")

    st.write("### 📊 Confidence:")
    for house, prob in zip(classes, probabilities):
        st.write(f"{house}: {prob:.2%}")

    house_colors = {
    "Gryffindor": "#7F0909",
    "Slytherin": "#0D6217",
    "Ravenclaw": "#0E1A40",
    "Hufflepuff": "#EEE117"
    }

    color = house_colors.get(prediction, "#FFFFFF")

    st.markdown(
        f"<h2 style='color:{color};'>Welcome to {prediction}!</h2>",
        unsafe_allow_html=True
    )