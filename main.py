import time
from datetime import datetime
import random
from rapidfuzz import fuzz, process
from textblob import TextBlob

def traditional_chatbot():
    print(
        "Chatbot: Choose an option:\n"
        " 1. Know about me\n"
        " 2. Order pizza\n"
        " 3. Guessing game (chatbot guesses)\n"
        " 4. Guessing game (you guess)\n"
        " 5. Exit"
    )

    state = None
    order_details = {}

    intents = {
        "greeting": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon"],
        "status": ["how are you", "how's it going", "what's up"],
        "joke": ["tell me a joke", "make me laugh", "say something funny"],
        "weather": ["what is the weather like", "how is the weather", "is it sunny outside"],
        "food": ["do you like pizza", "what is your favorite food", "do you eat"],
        "exit": ["bye", "goodbye", "exit", "quit", "5"],
        "emotion_happy": ["happy", "glad", "joyful", "excited", "wonderful", "great"],
        "emotion_sad": ["sad", "unhappy", "depressed", "down", "upset", "terrible"]
    }

    responses = {
        "greeting": [
            f"Hi there! {greeting()}",
            f"Hello! {greeting()}",
            f"Hey! {greeting()} How can I assist you?",
            "Greetings! How can I help?",
            f"{greeting()} Good to see you!",
        ],
        "status": [
            "I'm doing great, thank you! How about you?",
            "All systems are running smoothly. How can I help you?",
            "I'm just a program, but I'm feeling good! How are you?",
        ],
        "joke": [
            "Why don't skeletons fight each other? They don't have the guts!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call cheese that isn't yours? Nacho cheese!",
        ],
        "weather": [
            "I can't check live weather, but I hope it's sunny where you are!",
            "I'm not connected to a weather service, but it's always a good day to chat!",
        ],
        "food": [
            "I don't eat, but if I could, I'd definitely try pizza. It sounds amazing!",
            "Food is not my thing, but pizza seems to be a popular choice among humans.",
        ],
    }

    faqs = {
        "what can you do?": "I can answer basic questions, provide general information, and assist with common tasks.",
        "how do i exit the chat?": "You can exit the chat anytime by typing 'bye' or choosing option 5.",
        "what if you don't understand my question?": "If I don't understand your question, try rephrasing it.",
    }

    # Flatten intent phrases for fuzzy matching
    intent_phrases = {phrase: intent for intent, phrases in intents.items() for phrase in phrases}

    def detect_emotion(text):
        """Detect emotion from text using keyword matching"""
        text_words = set(text.lower().split())
        
        # Check for explicit emotion statements
        if "i am" in text.lower() or "i'm" in text.lower():
            for word in intents["emotion_happy"]:
                if word in text_words:
                    return "positive"
            for word in intents["emotion_sad"]:
                if word in text_words:
                    return "negative"
        
        # Check for single emotion words
        for word in text_words:
            if word in intents["emotion_happy"]:
                return "positive"
            if word in intents["emotion_sad"]:
                return "negative"
                
        return None

    while True:
        user_input = input("You: ").strip().lower()

        # Handle exit first
        if any(exit_word in user_input for exit_word in intents["exit"]):
            print("Chatbot: Was this conversation helpful? (yes/no)")
            feedback = input("You: ").strip().lower()
            if feedback.lower() in ["y", "yes"]:
                print("Chatbot: Thanks for your feedback!")
            else:
                print("Chatbot: I'll try to improve next time!")
            break

        # Handle emotion with improved detection
        emotion = detect_emotion(user_input)
        if emotion == "positive":
            print("Chatbot: I see you're feeling good! 😊 How can I assist you?")
            continue
        elif emotion == "negative":
            print("Chatbot: I'm sorry to hear that you're feeling down. 😞 How can I help?")
            continue

        # Handle fuzzy intent matching for greetings
        match_result = process.extractOne(user_input, intent_phrases.keys(), scorer=fuzz.ratio)
        if match_result and match_result[1] >= 70:
            intent = intent_phrases[match_result[0]]
            if intent == "greeting":
                print(f"Chatbot: {random.choice(responses['greeting'])}")
                continue

        # Handle "Know about me"
        if "1" in user_input or "what is your name?" in user_input:
            print("Chatbot: Hey, I'm your friendly chatbot! What's your name?")
            name = input("You: ").strip()
            print(f"Chatbot: Nice to meet you, {name}!")
            continue

        # Handle guessing games
        if "3" in user_input:
            chatbot_guesses()
            continue
        if "4" in user_input:
            user_guesses()
            continue

        # Handle pizza ordering
        if state is None and ("2" in user_input or "order pizza" in user_input):
            print("Chatbot: Great! What toppings would you like?")
            state = "order_pizza"
            continue
        if state == "order_pizza":
            order_details["toppings"] = user_input
            print(f"Chatbot: Got it. You want {user_input} toppings. What size would you like? (small, medium, large)")
            state = "order_size"
            continue
        if state == "order_size":
            if user_input in ["small", "medium", "large"]:
                order_details["size"] = user_input
                print(f"Chatbot: A {order_details['size']} pizza with {order_details['toppings']} toppings. Is that correct? (yes/no)")
                state = "confirm_order"
            else:
                print("Chatbot: Please choose a valid size: small, medium, or large.")
            continue
        if state == "confirm_order":
            if user_input == "yes":
                print(f"Chatbot: Great! Your {order_details['size']} pizza with {order_details['toppings']} toppings is on its way!")
                state = None
            elif user_input == "no":
                print("Chatbot: Sorry about that. Let's start over. What toppings would you like?")
                state = "order_pizza"
            else:
                print("Chatbot: Please respond with 'yes' or 'no'.")
            continue

        # Fallback for unrecognized inputs
        print("Chatbot: Sorry, I didn't understand that. Could you please clarify?")

def greeting():
    """Dynamic greeting based on the time of day."""
    hour = datetime.now().hour
    if hour < 12:
        return "Good Morning"
    elif hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"

def chatbot_guesses():
    """Guessing game where the chatbot guesses the number."""
    print("Chatbot: Think of a number between 1 and 100, and I'll guess it!")
    low, high = 1, 100
    feedback = ""
    while feedback != "c":
        guess = random.randint(low, high)
        print(f"Chatbot: Is it {guess}? (H = too high, L = too low, C = correct)")
        feedback = input("You: ").strip().lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Chatbot: Yay! I guessed your number {guess} correctly!")

def user_guesses():
    """Guessing game where the user guesses the number."""
    print("Chatbot: I'm thinking of a number between 1 and 100. Try to guess it!")
    number = random.randint(1, 100)
    while True:
        try:
            guess = int(input("You: "))
            if guess < number:
                print("Chatbot: Too low. Try again!")
            elif guess > number:
                print("Chatbot: Too high. Try again!")
            else:
                print(f"Chatbot: Congratulations! You guessed the number {number}!")
                break
        except ValueError:
            print("Chatbot: Please enter a valid number.")

if __name__ == "__main__":
    traditional_chatbot()