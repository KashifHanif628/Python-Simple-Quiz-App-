import streamlit as st # to show the data on streamlit UI.
import random # for the randomly selection of question
import time # for the timer

st.title("🎯 Quiz Application")

# Initialize points in session state if not set
if "points" not in st.session_state:
    st.session_state.points = 0  # ⭐ پوائنٹس اسٹارٹ میں 0 ہوں گے

# ✅ to display the earned points of user on correct answers.
st.write(f"🏆 Your Total Points: **{st.session_state.points}**")

# first we will make a list of question, second will be option and third will be answers.
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
        "answer": "Islamabad",
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": [
            "Allama Iqbal",
            "Liaquat Ali Khan",
            "Muhammad Ali Jinnah",
            "Benazir Bhutto",
        ],
        "answer": "Muhammad Ali Jinnah",
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu",
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee",
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
        "answer": "Karachi",
    },
    {
        "question": "Who is the winner of ICC CHampions Trophy of 2017 ?",
        "options": ["India", "Australia", "Pakistan", "New-Zealand"],
        "answer": "Pakistan",
    },
    {
        "question": "Who is the Currently President of Pakistan ?",
        "options": ["Bilawal Bhutto", "Molana Fazlur-e-hman", "Shahbaz Sharif", "Asif Ali Zardari"],
        "answer": "Asif Ali Zardari",
    },
    {
        "question": "Which is the National Game of Pakistan ?",
        "options": ["Tennis", "Hockey", "Cricket", "Football"],
        "answer": "Hockey",
    },
    {
        "question": "In which year Pakistan won the Cricket World Cup ?",
        "options": ["1992", "2000", "2003", "1985"],
        "answer": "1992",
    },
    {
        "question": "In which month Pakistan was becom the Nuclear power?",
        "options": ["December 2001", "May 1998", "August 1947", "Dont Know"],
        "answer": "May 1998",
    },
]

# Session Estate
# it means it will store the current state of your browser and will not restart from the begining.
# Session estate will choos randomly question from the above and store in the our browser memory.

if "current_question" not in st.session_state: # session estate will store the question through 
    st.session_state.current_question = random.choice(questions) # random.choice in the current_question variable

# Get the current question from session state
# make a variabl of question & it is = st.session_state.current_question
question = st.session_state.current_question

# then call this question varibal in sub header dynamically and in the bracket[question] is our every question keyword. 
# Display the question
st.subheader(question["question"])

# Create radio buttons for the options
# radio function will show our option on the streamlit UI.
# another create variabl of selected option
selected_option = st.radio("Choose your answer", question["options"], key="answer") # answer key user here to get the answer from the user and want to match from our dictionary.


# Submit button for the checking answer
# if user press the button of submit answer
if st.button("Submit Answer"):
    # check if the answer is correct or selected option is equal to question answer
    if selected_option == question["answer"]:
        # then print the msg of st.success
        st.success("✅ Correct!")
        st.balloons()
        st.write("🎉 Congratulations! You have earned **1 Point**")
        st.session_state.points += 1  # ⭐ 1 to update and add the point
    else:
        # if not then show the below msg with the correct answer.
        st.error("❌ Incorrect! the correct answer is " + question["answer"])
        st.write("😞 Sorry! You lost **1 Point**")
        if st.session_state.points > 0:  # ⭐ for points dont go in negative figure
            st.session_state.points -= 1

 # ✅ to show the updated points of every given answers
    st.write(f"📊 Updated Points: **{st.session_state.points}**")
  
    # Wait for 3 seconds before showing the next question
    time.sleep(4)

    # Select a new random question
    # this will help to randomly select the question again.
    st.session_state.current_question = random.choice(questions)

    # Rerun the app to display the next question 
    # with this key word the app will show the next question display on UI.
    st.rerun()
