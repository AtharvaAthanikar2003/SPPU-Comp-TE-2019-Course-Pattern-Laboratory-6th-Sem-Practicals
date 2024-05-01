#AI 5th Lab
import time
class Chatbot:
    def __init__(self):
        self.user_name = None
        self.user_age = None
        self.user_job = None
        self.user_hobbies = None
    def greet(self):
        print("🤖 Hello, I'm your friendly Chatbot - AI-Saathi ! 🤖")
        time.sleep(1)        
    def get_user_info(self):
        self.user_name = input("🤖 What's your name? ")
        print(f"🤖 Nice to meet you, {self.user_name}!")
        time.sleep(1)        
        self.user_age = int(input("🤖 How old are you? "))
        self.categorize_age()
        time.sleep(1)       
        self.user_job = input("🤖 What do you do for a living? ")
        self.describe_job()
        time.sleep(1)        
        self.user_hobbies = input("🤖 What are your hobbies? ")
        time.sleep(1)       
        print("🤖 Thanks for sharing! Let's move on.")
        time.sleep(1)        
    def categorize_age(self):
        if 18 <= self.user_age <= 25:
            print("🤖 Ah, you're in the prime of your youth!")
        elif 26 <= self.user_age <= 40:
            print("🤖 You're in the midst of your professional life!")
        elif self.user_age > 40:
            print("🤖 You've gathered a wealth of experience!")
        else:
            print("🤖 You're young and full of potential!")       
    def describe_job(self):
        print(f"🤖 {self.user_job} sounds like an interesting profession!")
    def remind_lunch_or_dinner(self):
        response = input("🤖 Have you had your lunch/dinner? (yes/no) ").lower()
        if response == "yes":
            print("🤖 Great! Make sure to stay hydrated and take breaks.")
        else:
            print("🤖 Take a break and have a nutritious meal. Your health is important!")
def main():
    chatbot = Chatbot()
    chatbot.greet()
    chatbot.get_user_info()
    chatbot.remind_lunch_or_dinner()
if __name__ == "__main__":
    main()