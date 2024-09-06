import random
from time import *


class Question:
    def __init__(self, question_text, answer_1, answer_2, answer_3, answer_4, correct_answer):
        self.question_text = question_text
        self.answers = ["Answers:", answer_1, answer_2, answer_3, answer_4]
        self.correct_answer = correct_answer
        
class Player:
    def __init__(self):
        self.current_saved_spot = 0
        self.fifty_lifeline_used = False
        self.audience_lifeline_used = False
        self.friend_lifeline_used = False



def main():
    player = Player()
    
    list_of_questions_1 = []
    list_of_questions_2 = []
    list_of_questions_3 = []
    list_of_questions_4 = []
    with open(r"C:\Users\nicos\Documents\Programmierung\Lernen\project\questions_pool.csv") as file:
        
        for line in file:
            if line.startswith("Question_Text"):
                continue
            row = line.rstrip().split(",")
            
            match row[6]:
                case "1":
                    list_of_questions_1.append(row)
                case "2":
                    list_of_questions_2.append(row)
                case "3":
                    list_of_questions_3.append(row)
                case "4":
                    list_of_questions_4.append(row)
    
    
    List_of_QuestionsO = []
    for _ in range(5):
        List_of_QuestionsO.append(get_Question_Object(list_of_questions_1, List_of_QuestionsO))
    for _ in range(5):
        List_of_QuestionsO.append(get_Question_Object(list_of_questions_2, List_of_QuestionsO))
    for _ in range(4):
        List_of_QuestionsO.append(get_Question_Object(list_of_questions_3, List_of_QuestionsO))
    List_of_QuestionsO.append(get_Question_Object(list_of_questions_4, List_of_QuestionsO))
    
    
            
    
    
    
    
    print(""" 
    Hello and welcome to WHO WANTS TO BE A MILLIONAIRE?
    
    The sometimes difficult, but always fun quiz show, where you can win
    up to a million pounds. But nobody said, it's going to be easy.
    You have to guess (or at best know) 15 answers correctly to get the full price.
    Nobody is that smart, so you've got 3 different lifelines.
    - You've got the 50:50 lifeline, which hides two wrong answers.
    - You've got the ask-the-audience lifeline, where the audience guesses the answer.
    - And you've got the phone-a-friend lifeline, where you can call a friend and ask for help.
    
    When you're ready to start, click the Enter-Button.
         """)
    if input("") == "":
        print("Let's go!\n")
        
        counter = 0
        for question in List_of_QuestionsO:
            counter = counter + 1
            if counter == 6:
                player.current_saved_spot = 5
                print(f"\nYou have reached a save spot of {get_money_value(5)}!\n")
            if counter == 11:
                player.current_saved_spot = 10
                print(f"\nYou have reached a save spot of {get_money_value(10)}!\n")
            ask_question(question, player, counter)
    
        print("")
        print("CONGRATULATIONS!!! YOU HAVE WON ONE MILLON POUNDS!\n")
        input("Click to exit")
        exit()
               
            
  
        
    else:
        main()


def get_Question_Object(list, list_of_objects):
    selected = random.choice(list)
    selected_question = Question(selected[0].replace('"', ''), selected[1], selected[2], selected[3], selected[4], selected[5])
    while selected_question.question_text in [question.question_text for question in list_of_objects]:
        selected = random.choice(list)
        selected_question = Question(selected[0].replace('"', ''), selected[1], selected[2], selected[3], selected[4], selected[5])  
    return selected_question

def get_money_value(question_number):
    match question_number:
        case 0:
            return "£0"
        case 1:
            return "£100"
        case 2:
            return "£200"
        case 3:
            return "£300"
        case 4:
            return "£500"
        case 5:
            return "£1,000"
        case 6:
            return "£2,000"
        case 7:
            return "£4,000"
        case 8:
            return "£8,000"
        case 9:
            return "£16,000"
        case 10:
            return "£32,000"
        case 11:
            return "64,000"
        case 12:
            return "£125,000"
        case 13:
            return "£250,000"
        case 14:
            return "£500,000"
        case 15:
            return "£1 Million"


def ask_question(question, player, counter):
    
    
    print(f"The {get_money_value(counter)} question:\n")
    print(f"{question.question_text}\n")
    
    print(f"1 - {question.answers[1]}\n")
    print(f"2 - {question.answers[2]}\n")
    print(f"3 - {question.answers[3]}\n")
    print(f"4 - {question.answers[4]}\n")
    
    print(f"Current milestone: {get_money_value(player.current_saved_spot)}")
    
    print("Available lifelines:")
    if player.fifty_lifeline_used == False:
        print("a - 50:50-lifeline")
    if player.audience_lifeline_used == False:
        print("b - ask-the-audience lifeline")
    if player.friend_lifeline_used == False:
        print("c - phone-a-friend-lifeline\n")
    if player.friend_lifeline_used and player.audience_lifeline_used and player.fifty_lifeline_used:
        print("No lifeline left.")
    
    answer = input(f"Type number of correct answer, or type exit to walk away with {get_money_value(counter - 1)}, or choose an available lifeline: ")
    if answer == question.correct_answer:
        print("")
        print("And that is...\n")
        sleep(3)
        print("Correct!\n")
        sleep(2)
        print("Next question:")
        
        
    elif answer == "exit":
        print(f"You won {get_money_value(counter - 1)}!")
        input("Click Enter to exit")
        exit()
    elif answer == "a":
        if player.fifty_lifeline_used:
            print("lifeline not available")
            ask_question(question, player, counter)
        else:
            fifty_lifeline(question, player)
            ask_question(question, player, counter)
    elif answer == "b":
        if player.audience_lifeline_used:
            print("lifeline not available")
            ask_question(question, player, counter)
        else:
            audience_lifeline(question, player)
            ask_question(question, player, counter)
    elif answer == "c":
        if player.friend_lifeline_used:
            print("lifeline not available\n")
            ask_question(question, player, counter)
        else:
            friend_lifeline(question, player)
            ask_question(question, player, counter)
            
    else:
        print("")
        print("And that is...\n")
        sleep(3)
        print("Wrong! :(\n")
        if input(f"You won {get_money_value(player.current_saved_spot)}. Click a to play again or enter to exit: ") == "a":
            main()
        else:
            exit()

def fifty_lifeline(question, player):
    list = [x for x in range(1,5) if str(x) != question.correct_answer]
    selected = random.choices(list, k=2)
    question.answers[selected[0]] = ""
    question.answers[selected[1]] = ""
    player.fifty_lifeline_used = True

def audience_lifeline(question, player):
    print("Waiting for the audience...")
    sleep(5)
    audience_number = 10
    guesses = [0, 0, 0, 0]
    list = [x for x in range(1,5) if str(x) != question.correct_answer]
    for x in range(audience_number):
        if random.random() < 0.4:
            guesses[int(question.correct_answer) - 1] = guesses[int(question.correct_answer) - 1] + 1
        else:
            x = random.choice(list)
            guesses[x-1] = guesses[x-1] + 1
            
    print(f"\nThe audience says the following:\n 1 - {guesses[0]/audience_number}% \n 2 - {guesses[1]/audience_number}% \n 3 - {guesses[2]/audience_number}% \n 4 - {guesses[3]/audience_number}%\n")
    sleep(3)
    player.audience_lifeline_used = True
   
        

def friend_lifeline(question, player):
    print("\n Calling... ")
    sleep(2)
    print("\n Calling...")
    sleep(2)
    print("\n Calling...")
    sleep(2)
    
    
    list = [x for x in range(1,5) if str(x) != question.correct_answer]
    if random.random() < 0.7:
        selected = question.correct_answer
    else:
        selected = random.choice(list)
    print(f"\n Hello, here is Mike. I would say the correct answer is Number {selected}, but I'm not sure.\n")
    sleep(4)
    player.friend_lifeline_used = True


main()
input("Click to exit.")