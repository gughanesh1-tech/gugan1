import streamlit as st

st.title("🎮 My First Streamlit App")
st.write("Hello, Gugan!")
st.write("Welcome to my website.")
import streamlit as st

ANSWER = "light"

st.title("🟩 Wordle by Gugan")
st.write("Guess the 5-letter word. You have 5 chances!")

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

guess = st.text_input("Enter your guess:")

if st.button("Submit"):
    if len(guess) != 5:
        st.error("Please enter exactly 5 letters.")
    else:
        st.session_state.attempts += 1

        colors = []

        for i in range(5):
            if guess[i] == ANSWER[i]:
                colors.append("🟩")
            elif guess[i] in ANSWER:
                colors.append("🟨")
            else:
                colors.append("⬜")

        st.write(" ".join(colors))

        if guess == ANSWER:
            st.success("🎉 You won!")
        elif st.session_state.attempts >= 5:
            st.error(f"You lost! The word was {ANSWER}")
        else:
            st.write(f"Attempts left: {5 - st.session_state.attempts}")
