import time
import random
from rapidfuzz import fuzz, process


def traditional_chatbot():
    print("Chatbot: Hi! I'm a traditional chatbot. Type 'exit' to quit.")

    intents = {
        "greeting": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon"],
        "farewell": ["bye", "goodbye", "see you", "take care"],
        "status": ["how are you", "how's it going", "what's up"],
        "joke": ["tell me a joke", "make me laugh","say something funny"],
        "weather": ["what is the weather like", "how is the weather", "is it sunny outside"],
        "food": ["do you like pizza", "what is your favorite food", "do you eat"]
    }

    greetings = [
        "Hi there!", "Hello!", 
        "Hey! How can I assist you?", 
        "Greetings! How can I help?", 
        "Good to see you!"
    ]

    farewells = [
        "Goodbye! Have a nice day!",
        "See you later! Take care!",
        "Bye! Hope to chat with you again!",
        "Farewell! Stay safe!",
        "Take care! Have a great day!"
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
        "farewell": farewells,
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

        if user_input == "exit":
            print("Chatbot: Bye!")
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

        # Find the closest match using RapidFuzz
        match_result = process.extractOne(user_input, intent_phrases.keys(), scorer=fuzz.ratio)
        match, similarity = match_result[0], match_result[1]

        if similarity >= 80:  # Threshold for considering a match
            matched_intent = intent_phrases[match]  # Get the intent for the matched phrase
            response = random.choice(responses[matched_intent])  # Choose a random response from the intent
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: Sorry, I didn't understand that.")

        
traditional_chatbot()


