import time
from datetime import datetime
import random
from rapidfuzz import fuzz, process


def traditional_chatbot():
    print("Chatbot: Hi! I'm a traditional chatbot. Type 'bye' to quit.")

    #conversation state
    state = None  # Tracks the current state
    order_details = {}  # To store pizza order details

    intents = {
        "greeting": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon"],
        "status": ["how are you", "how's it going", "what's up"],
        "joke": ["tell me a joke", "make me laugh","say something funny"],
        "weather": ["what is the weather like", "how is the weather", "is it sunny outside"],
        "food": ["do you like pizza", "what is your favorite food", "do you eat"]
    }
    hour = datetime.now().hour
    if hour < 12:
        g = "Good Morning"
    elif hour < 18:
        g = "Good afternoon!"
    else:
        g ="Good evening!"

    greetings = [
        f"Hi there! {g}", f"Hello! {g}", 
        f"Hey! {g} How can I assist you?", 
        "Greetings! How can I help?", 
        f"{g} Good to see you!"
    ]

    status_responses = [
        "I'm doing great, thank you! How about you?",
        "All systems are running smoothly. How can I help you?",
        "I'm just a program, but I'm feeling good! How are you?",
        "Doing well! Let me know what you need.",
        "Feeling helpful today! What can I assist you with?"
    ]

    jokes = [
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don’t scientists trust atoms? Because they make up everything!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "What do you get if you cross a snowman with a vampire? Frostbite!"
    ]
    weather_responses = [
        "I can’t check live weather, but I hope it’s sunny where you are!",
        "I’m not connected to a weather service, but it’s always a good day to chat!",
        "Sorry, I don’t know the weather right now. Maybe check your local forecast?",
        "Weather? It’s always nice and warm in my circuits!",
        "I’m not sure, but I hope it’s not raining on your parade!"
    ]
    food_responses = [
        "I don’t eat, but if I could, I’d definitely try pizza. It sounds amazing!",
        "Food is not my thing, but pizza seems to be a popular choice among humans.",
        "I can’t taste, but I’ve heard great things about chocolate cake too!",
        "I’m a fan of virtual food… like data bytes!",
        "I don’t eat, but if I did, pizza with extra cheese sounds delightful!"
    ]

    responses = {
        "greeting": greetings,
        "status": status_responses,
        "joke": jokes,
        "weather": weather_responses,
        "food": food_responses
    }


    faqs = {
        "what can you do?": "I can answer basic questions, provide general information, and assist with common tasks. How can I help you today?",
        "how do i exit the chat?": "You can exit the chat anytime by typing 'exit'.",
        "what if you don’t understand my question?": "If I don’t understand your question, I’ll let you know. You can try rephrasing it, and I’ll do my best to help!",
        "is this chatbot available 24/7?": "Yes, I’m always available to chat with you!",
        "can you handle specific tasks or advanced queries?": "I’m a traditional chatbot with limited capabilities. If you need advanced help, you might need a more specialized chatbot or human assistance."
    }

    intent_phrases = {phrase: intent for intent, phrases in intents.items() for phrase in phrases}

    while True:
        user_input = input("You: ").strip().lower()

        match_result = process.extractOne(user_input, intent_phrases.keys(), scorer=fuzz.ratio)
        match, similarity = match_result[0], match_result[1]

        if user_input == "bye":
            print("Chatbot: Was this conversation helpful? (yes/no)")
            user_input = input("You: ").strip().lower()
            if user_input == "yes":
                print("Chatbot: Thanks for your feedback!")
            else:
                print("Chatbot: I'm sorry, tell me what's your problem, I’ll do my best to help!")
                user_input = input("You: ").strip().lower()
                print("chatbot: I'll improve next time, Thanks for your feedback!")

            break

        if user_input == "faq":
            print("Chatbot: Here are some frequently asked questions:")
            for question in faqs.keys(): 
                print(f"- {question}")
            continue         
        
        if user_input in faqs:
            print(f"Chatbot: {faqs[user_input]}")
            continue
            
        if user_input == "what is your name?":
            print("Hey I'm your chatbot, What is your name?")
            name = input("You: ")
            print(f"Chatbot: Hey, {name}!")
            continue

        if user_input == "time":
            print(f"The current time is {time.strftime('%H:%M:%S')}.")
            continue
        if user_input == "date":
            print(f"Today's date is: {time.strftime('%Y-%m-%d')}")
            continue

        # Handle user input based on the state
        if state is None:  # General state
            if "order pizza" in user_input or "i want pizza" in user_input or "pizza" in user_input:
                print("Chatbot: Great! What toppings would you like?")
                state = "order_pizza"  # Transition to pizza ordering state
                continue
        if similarity >= 50:  # Threshold for considering a match
            matched_intent = intent_phrases[match]  # Get the intent for the matched phrase
            response = random.choice(responses[matched_intent])  # Choose a random response from the intent
            print(f"Chatbot: {response}")

        elif state == "order_pizza":  # Pizza toppings state
            order_details["toppings"] = user_input
            print(f"Chatbot: Got it. You want {user_input} toppings. What size would you like? (small, medium, large)")
            state = "order_size"  # Transition to size selection state

        elif state == "order_size":  # Pizza size state
            if user_input in ["small", "medium", "large"]:
                order_details["size"] = user_input
                print(f"Chatbot: A {user_input} pizza with {order_details['toppings']} toppings. Is that correct? (yes/no)")
                state = "confirm_order"  # Transition to confirmation state
            else:
                print("Chatbot: Please choose a valid size: small, medium, or large.")

        elif state == "confirm_order":  # Order confirmation state
            if user_input == "yes":
                print(f"Chatbot: Great! Your {order_details['size']} pizza with {order_details['toppings']} toppings is on its way!")
                state = None  # Reset state for a new conversation
            elif user_input == "no":
                print("Chatbot: Sorry about that. Let's start over. What toppings would you like?")
                state = "order_pizza"  # Restart order flow

        else:
            print("Chatbot: Sorry, I didn't understand that.")

        
traditional_chatbot()


