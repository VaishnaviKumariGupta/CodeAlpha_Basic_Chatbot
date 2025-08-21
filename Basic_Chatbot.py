def chatbot(user):
    user = user.lower()

    if user in ["hello", "hii"]:
        return "hello!"
    elif user in ["who are you"]:
        return "I am a basic Chatbot"
    elif user in ["how are you"]:
        return "I am fine. how about you?"
    elif user in ["bye", "byy", "by", "goodbye"]:
        return "Goodbye! Have a nice day."
    elif user in ["what is your name"]:
        return "I am a chatbot"
    else:
        return "Sorry! i didn't understand what you want to say."
    
print("Chatbot: enter hello to chat or bye to exit: ")

while(True):
    
    user = input("You: ").lower()
    print("Chatbot:",chatbot(user))

    if user in ["bye", "byy", "by", "goodbye"]:
        break

