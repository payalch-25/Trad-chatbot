import time
from datetime import datetime
import random
from rapidfuzz import fuzz, process

def traditional_chatbot():
    print(
        "Chatbot: Choose an option:\n"
        " 1. Know about me\n"
        " 2. Order pizza\n"
        " 3. Guessing game (chatbot guesses)\n"
        " 4. Guessing game (you guess)\n"
        " 5. Exit"
    )

    state = None  # Tracks the current conversation state
    order_details = {}  # Stores pizza order details

    intents = {
        "greeting": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon"],
        "status": ["how are you", "how's it going", "what's up"],
        "joke": ["tell me a joke", "make me laugh", "say something funny"],
        "weather": ["what is the weather like", "how is the weather", "is it sunny outside"],
        "food": ["do you like pizza", "what is your favorite food", "do you eat"],
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
            "Why don’t skeletons fight each other? They don’t have the guts!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call cheese that isn't yours? Nacho cheese!",
        ],
        "weather": [
            "I can’t check live weather, but I hope it’s sunny where you are!",
            "I’m not connected to a weather service, but it’s always a good day to chat!",
        ],
        "food": [
            "I don’t eat, but if I could, I’d definitely try pizza. It sounds amazing!",
            "Food is not my thing, but pizza seems to be a popular choice among humans.",
        ],
    }

    faqs = {
        "what can you do?": "I can answer basic questions, provide general information, and assist with common tasks.",
        "how do i exit the chat?": "You can exit the chat anytime by typing 'bye' or choosing option 5.",
        "what if you don’t understand my question?": "If I don’t understand your question, try rephrasing it.",
    }

    # Flatten intent phrases for fuzzy matching
    intent_phrases = {phrase: intent for intent, phrases in intents.items() for phrase in phrases}

    while True:
        user_input = input("You: ").strip().lower()

        # Handle exit
        if "bye" in user_input or "5" in user_input:
            print("Chatbot: Was this conversation helpful? (yes/no)")
            feedback = input("You: ").strip().lower()
            print("Chatbot: Thanks for your feedback!" if feedback == "yes" else "Chatbot: I'll try to improve next time!")
            break

        # Handle FAQs
        if user_input == "faq":
            print("Chatbot: Here are some frequently asked questions:")
            for question in faqs.keys():
                print(f"- {question}")
            continue
        if user_input in faqs:
            print(f"Chatbot: {faqs[user_input]}")
            continue

        # Handle fuzzy intent matching
        match_result = process.extractOne(user_input, intent_phrases.keys(), scorer=fuzz.ratio)
        if match_result and match_result[1] >= 50:  # Match confidence threshold
            intent = intent_phrases[match_result[0]]
            print(f"Chatbot: {random.choice(responses[intent])}")
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
                print(f"Chatbot: A {user_input} pizza with {order_details['toppings']} toppings. Is that correct? (yes/no)")
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


# Helper Functions
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
    guess = 0
    while guess != number:
        guess = int(input("You: "))
        if guess < number:
            print("Chatbot: Too low. Try again!")
        elif guess > number:
            print("Chatbot: Too high. Try again!")
    print(f"Chatbot: Congratulations! You guessed the number {number}!")

# Run the chatbot
traditional_chatbot()