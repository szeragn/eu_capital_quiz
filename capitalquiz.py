import random
from european_countries import european_countries
import time

játék = input("Üdvözöllek, kezdődhet a kvíz? (igen/nem) ").lower().strip()

if játék != "igen":
    print("Talán legközelebb, szia!")
    quit()
else:
    print("Felkészülni...")
    time.sleep(0.5)
    print()

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, country, capital):
        print("---------------------------------------------------")
        print(f"Mi a fővárosa a következő országnak: {country}?")
        print()
        options = list(self.questions.values())
        options.remove(capital)
        options = options[:3]  # Choose three random wrong options
        options.append(capital)
        options = random.sample(options, len(options))  # Shuffle the options

        for i, option in enumerate(options):
            print(f"{i+1}. {option}") 

        print()    

        user_choice = input("A válaszod (1/2/3/4): ")
        time.sleep(0.03)
        print()

        if user_choice.isdigit() and 1 <= int(user_choice) <= 4:
            if options[int(user_choice) - 1] == capital:
                print("Helyes! \U0001F601 ")
                self.score += 1
            else:
                print("Helytelen! \U0001F612 ")
                print(f"A helyes válasz ez volt: {capital}")
        else:
            print("Helytelen érték. Jön a következő kérdés.")

        print()

    def run_quiz(self, num_questions=20):
        questions = random.sample(list(self.questions.items()), num_questions)

        for country, capital in questions:
            self.ask_question(country, capital)

        print("---------------------------------------------------------")
        print(f"A kvíz végére értél! Gratulálok, az eredményed {self.score}/{(num_questions)}.")
        print("---------------------------------------------------------")


quiz = Quiz(european_countries) 
quiz.run_quiz(num_questions=20)
