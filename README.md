# Define predefined rules and responses
if "hello" in user_input or "hi" in user_input:
    return "Hello! How can I assist you today?"

elif "how are you" in user_input:
    return "I'm just a computer program . What can I do for you?"

elif "what is your name" in user_input:
    return "I'm a simple chatbot. im happy to help you"

elif "how can i learn to code" in user_input:
    return "search how to code on google"

elif "where can i get internship" in user_input:
    return "follow codsoft on linkedin."

elif "goodbye" in user_input or "bye" in user_input:
    return "Goodbye! have a great day."

else:
    return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"