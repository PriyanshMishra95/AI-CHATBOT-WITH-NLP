import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I am an AI Chatbot created using Python and NLTK."]
    ],
    [
        r"how are you?",
        ["I am fine. Thank you!"]
    ],
    [
        r"who created you?",
        ["I was created for a CodTech Internship project."]
    ],
    [
        r"bye",
        ["Goodbye! Have a nice day."]
    ]
]

chatbot = Chat(pairs, reflections)

print("AI Chatbot Started")
print("Type 'bye' to exit")

chatbot.converse()