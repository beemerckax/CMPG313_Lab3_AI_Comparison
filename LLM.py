def modern_ai_chat():
    print("Modern AI Chatbot")
    print("Type 'quit' to stop.")
    
    user_name = "Boikanyo"
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Bot: Goodbye!")
            break
        
        # Simulated LLM contextual response based on your screenshots
        if "stressed" in user_input.lower() or "exams" in user_input.lower():
            print(f"Bot: It's very common to feel overwhelmed during exam season, {user_name}.")
            print("For your CMPG 313 module, try to focus on one task at a time.")
            print("Prioritizing rest will actually help your brain retain the coding logic")
            print("and AI concepts better. Don't forget to take breaks!")
        else:
            print("Bot: I understand. How else can I assist you with your studies today?")

if __name__ == "__main__":
    modern_ai_chat()
