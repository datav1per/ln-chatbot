#chatbot
from textblob import TextBlob

#define intent and their corresponding responses based on keywords
intents = {
    "hours":{
        "keywords":["hours","open","close"],
        "response":"We are open from 9 AM to 5 PM, Monday to Friday."
        },
        "return":{
            "keywords":["refund","money back","return"],
            "response":"I'd be happy to help you with that. Let me transfer you to our customer service team."
        }
}

def get_response(message):
    #Convert message to lowercase for easier matching
    message = message.lower()
    #check if any of the keywords in the message match the keywords in the intents
    if any(word in message for word in intent_data["keywords"]):
    #return the corresponding response if a keyword matches
        return intent_data["response"]
    #analyze the sentiment of the message using textblob
        sentiment = TextBlob(message).sentiment.polarity
    #return a response based on the sentiment score
    return("That's so great to hear! I'm glad you're feeling positive.") if sentiment > 0 else ("I'm sorry to hear that you're feeling down. How can I help you?")

def chat():
    #Greet the user and prompt for input
    print("Chatbot: Hi, How can I help you today?")
    while (user_message := input("You: ").strip().lower())not in ["exit", "quit", "bye"]:
        print(f"\nChatbot: {get_response(user_message)}")
        #Get the response from the chatbot based on the user message
        
    #Thank the user for chatting and exit
    print("Chatbot: Thank you for chatting with me! Have a great day!")
#Run the chat function to start the chatbot
if __name__ == "__main__":
    chat() #start the chatbot