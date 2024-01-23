def codsoft_chatbot(question, bot_name="CodSoft AI"):
    queries = {
        "hello": f"Hi there! I'm {bot_name}. How can I help you?",
        "how are you": f"I'm just a computer program, but thanks for asking!",
        "bye": f"Goodbye! Have a great day!",
        "what's your name": f"I'm {bot_name}. Nice to meet you!",
        "who created you": f"I was created by a talented developer at CodSoft.",
        "tell me a joke": f"Why don't scientists trust atoms? Because they make up everything!",
        "default": f"I'm not sure how to respond to that. Can you ask me something else?"
    }

    question = question.lower()

    if question in queries:
        return queries[question]
    else:
        return queries["default"]


bot_name = "CodSoft AI"
print(f"{bot_name}: Hello! I'm {bot_name}, your friendly chatbot.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print(f"{bot_name}: Goodbye!")
        break
    response = codsoft_chatbot(user_input, bot_name)
    print(f"{bot_name}: {response}")
