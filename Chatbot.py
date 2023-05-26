import random

bot_name = "College Buddy"

knowledge_base = {
    "what is your name?": [f"My name is {bot_name}! Happy to help you with your College inquiries!"],
    "hello": [f"Hello, I'm {bot_name}! How can I assist you with your College inquiries?"],
    "what are the best colleges from pune?": ["COEP", "PICT", "VIT", "CUMMINS", "PCCOE"],
}

print("College Enquiry Rule-Based Chatbot")


def respond(user_input):
    if user_input in knowledge_base:
        responses = knowledge_base[user_input]
        for response in responses:
            print(response)
    else:
        print("Question is not present in the knowledge base!")
        answer = input(
            "Could you please enter the appropriate answer for the question: ")
        knowledge_base[user_input] = [answer]


while True:
    user_input = input("User: ").lower()
    respond(user_input)
