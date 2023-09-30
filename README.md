# Define a function to handle user input and provide responses
def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define predefined rules and responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    elif "how are you" in user_input:
        return "I'm just a computer program, but I'm here to help. What can I do for you?"

    elif "what is your name" in user_input:
        return "I'm a simple chatbot."

    elif "goodbye" in user_input or "bye" in user_input:
        return "Goodbye! Feel free to return if you have more questions."

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

# Main loop to interact with the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
