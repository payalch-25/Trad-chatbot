import streamlit as st
import random
from datetime import datetime
from rapidfuzz import fuzz, process
from textblob import TextBlob

def greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good Morning!"
    elif hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

def detect_emotion(text):
    happy_words = ["happy", "glad", "joyful", "excited", "wonderful", "great"]
    sad_words = ["sad", "unhappy", "depressed", "down", "upset", "terrible"]
    text_words = set(text.lower().split())
    if any(word in text_words for word in happy_words):
        return "positive"
    if any(word in text_words for word in sad_words):
        return "negative"
    return None

def chatbot_response(user_input):
    intents = {
        "greeting": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon"],
        "status": ["how are you", "how's it going", "what's up"],
        "joke": ["tell me a joke", "make me laugh", "say something funny"],
        "weather": ["what is the weather like", "how is the weather", "is it sunny outside"],
        "food": ["do you like pizza", "what is your favorite food", "do you eat"],
        "exit": ["bye", "goodbye", "exit", "quit"],
        "emotion_happy": ["happy", "glad", "joyful", "excited", "wonderful", "great"],
        "emotion_sad": ["sad", "unhappy", "depressed", "down", "upset", "terrible"]
    }
    responses = {
        "greeting": [f"Hi there! {greeting()}"],
        "status": ["I'm doing great, thank you! How about you?"],
        "joke": ["Why don't skeletons fight each other? They don't have the guts!"],
        "weather": ["I can't check live weather, but I hope it's sunny where you are!"],
        "food": ["I don't eat, but if I could, I'd definitely try pizza. It sounds amazing!"]
    }
    intent_phrases = {phrase: intent for intent, phrases in intents.items() for phrase in phrases}
    match_result = process.extractOne(user_input, intent_phrases.keys(), scorer=fuzz.ratio)
    if match_result and match_result[1] >= 60:
        intent = intent_phrases[match_result[0]]
        if intent in responses:
            return random.choice(responses[intent])
    emotion = detect_emotion(user_input)
    if emotion == "positive":
        return "I see you're feeling good! 😊 How can I assist you?"
    elif emotion == "negative":
        return "I'm sorry to hear that you're feeling down. 😞 How can I help?"
    return "I'm not sure I understand. Can you rephrase?"

def chatbot():
    st.title("Chatbot with Streamlit")
    st.write("Choose an option:")
    option = st.radio("", ["Know about me", "Order pizza", "Guessing game (chatbot guesses)", "Guessing game (you guess)", "Exit"])
    user_input = st.text_input("You:")
    if user_input:
        response = chatbot_response(user_input)
        st.text_area("Chatbot:", response, height=100, disabled=True)
    if option == "Order pizza":
        toppings = st.text_input("What toppings would you like?")
        size = st.selectbox("Choose a size", ["Small", "Medium", "Large"])
        if st.button("Confirm Order"):
            st.write(f"Your {size} pizza with {toppings} is on its way!")
    elif option == "Guessing game (chatbot guesses)":
        low, high = 1, 100
        feedback = ""
        while feedback != "Correct":
            guess = random.randint(low, high)
            feedback = st.selectbox(f"Is your number {guess}?", ["Too high", "Too low", "Correct"])
            if feedback == "Too high":
                high = guess - 1
            elif feedback == "Too low":
                low = guess + 1
        st.write(f"I guessed your number {guess} correctly!")
    elif option == "Guessing game (you guess)":
        number = random.randint(1, 100)
        guess = st.number_input("Guess the number:", min_value=1, max_value=100, step=1)
        if st.button("Submit Guess"):
            if guess < number:
                st.write("Too low. Try again!")
            elif guess > number:
                st.write("Too high. Try again!")
            else:
                st.write(f"Congratulations! You guessed the number {number}!")

if __name__ == "__main__":
    chatbot()
