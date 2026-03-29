import nltk
from nltk.chat.util import Chat, reflections

# Modified rules for Lab 3
pairs = [
    [
        r"My name is (.*)",
        ["I am not interested in names.", "Names don't matter to me."]
    ],
    [
        r"I feel (.*)",
        ["Do you often feel %1?", "Why do you feel %1?"]
    ],
    [
        r"Because (.*)",
        ["Is that the real reason?", "What other reasons might there be?"]
    ],
    [
        r"quit",
        ["Goodbye.", "Have a nice day."]
    ],
    [
        r"(.*) (exams|stressed|tired)",
        ["It sounds like you are under a lot of pressure. Have you tried resting?", "Focus on one task at a time."]
    ],
    [
        r"(.*)",
        ["Please tell me more.", "Can you elaborate on that?"]
    ]
]

def eliza_chat():
    print("ELIZA Chatbot")
    print("Type 'quit' to stop.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    eliza_chat()
