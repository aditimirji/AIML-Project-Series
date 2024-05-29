
user_name = None
    
def greet_user():
    return "Hello! How can I help you today?"

def get_response(user_input):
    global user_name
    responses = {
        "how are you": "I'm a chatbot, so I don't have feelings, but thanks for asking!",
        "what is your name": "I'm ChatBot, your virtual assistant.",
        "what can you do": "I can answer your questions and chat with you!",
        "yes, i do": "Please go ahead and ask whatever you want.",
        "good": "Nice hearing that!",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
        "bye": "Goodbye! Have a great day!"
    }
    
    # Check if the user input includes their name
    if user_input.lower().startswith("my name is"):
        user_name = user_input[11:].strip()
        return f"Nice to meet you, {user_name}!"
    
    # Provide a personalized response if the user's name is known
    if user_name:
        return responses.get(user_input.lower(), f"I'm not sure how to respond to that, {user_name}. Can you ask something else?")
    else:
        return responses.get(user_input.lower(), "I'm not sure how to respond to that. Can you ask something else?")
conversation_history = {}

def remember_context(user_input, user_id):
    if user_id not in conversation_history:
        conversation_history[user_id] = []
    conversation_history[user_id].append(user_input)

def get_previous_context(user_id):
    return conversation_history.get(user_id, [])

def ask_questions():
    questions = [
        " ",
        "What is your name?",
        "How are you feeling today?",
        "Do you have any questions for me?"
    ]
    return questions

def chatbot():
    user_id = 1  # In a real scenario, this could be a session ID or user identifier
    print(greet_user())
    
    for question in ask_questions():
        print(question)
        user_input = input("Your response: ")
        remember_context(user_input, user_id)
        print(get_response(user_input))
        
    while True:
        user_input = input("You: ")
        remember_context(user_input, user_id)
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"ChatBot: {response}")

# Run the chatbot
chatbot()