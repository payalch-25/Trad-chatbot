# Traditional Chatbot

A simple, interactive chatbot script implemented in Python. This chatbot provides various functionalities, including casual conversation, guessing games, and even pizza ordering! It uses natural language processing for intent recognition and dynamic responses.

## Features

- **Casual Conversation**: The chatbot can respond to greetings, jokes, weather inquiries, and emotional expressions.
- **Guessing Games**:
  - The chatbot guesses a number you're thinking of.
  - You guess the number the chatbot is thinking of.
- **Pizza Ordering**: Place a virtual pizza order by selecting toppings and size.
- **Dynamic Greeting**: Tailored greetings based on the current time of day.
- **Fuzzy Intent Matching**: Leverages the `rapidfuzz` library for flexible and robust intent detection.

## Technologies Used

- **Python**: The core programming language for the chatbot.
- **RapidFuzz**: For intent recognition through fuzzy string matching.
- **TextBlob**: For sentiment analysis and emotion detection.

## Getting Started

### Prerequisites

Ensure you have Python 3.7+ installed on your system. Additionally, install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/traditional-chatbot.git
   cd traditional-chatbot
   ```

2. Run the chatbot:
   ```bash
   python main.py
   ```

## Usage

1. Run the script.
2. Choose an option from the chatbot's menu:
   - Learn about the chatbot.
   - Order a pizza.
   - Play a guessing game.
3. Chat naturally! The chatbot can detect emotions and match intents to respond accordingly.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.