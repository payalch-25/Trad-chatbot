def traditional_chatbot():
    print("Chatbot: Hi! I'm a traditional chatbot. Type 'exit' to quit.")
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bunch of code, but I'm doing great!",
        "bye": "Goodbye! Have a nice day!"
    }
    
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Chatbot: Bye!")
            break
        response = responses.get(user_input, "Sorry, I didn't understand that.")
        print(f"Chatbot: {response}")

traditional_chatbot()