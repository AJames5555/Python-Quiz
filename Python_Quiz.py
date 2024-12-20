
from random import uniform




question_dict = {
    1: "What was the name of the Bronze Age civilization which grew up on and around the island of Crete in the Mediterranean?",
    2: "Saint Petersburg, Stockholm, Helsinki and Riga are all cities situated on which sea?",
    3: "Which film has the following as its last line - 'I do wish we could chat longer, but... I'm having an old friend for dinner. Bye.'",
    4: "Shirley Crabtree Jr was a huge presence on the UK wrestling scene under what name?",
    5: "What was the Manhattan Project?",
    6:"In which city is the famous Edvard Eriksen statute, The Little Mermaid?",
    7: "Which book by Ray Bradbury starts with the words  - 'It was a pleasure to burn.'", 
    8: "What is the capital city of Canada?",
    9: "Which actress wrote the first series of Killing Eve and was the creator and writer of Fleabag?",
    10: "In 1953 Edmund Hillary was the first man to reach the summit of Everest along with which other person?"
}

multichoice_dict1 = {
    1: "Mycenaean",
    2: "Black Sea",
    3: "Silence of the Lambs",
    4: "Fit Finlay",
    5: "The expansion of the New York Subway",
    6: "Oslo",
    7: "Firefly",
    8: "Ottawa",
    9: "Phoebe Waller-Bridge",
    10: "Norbert Talwar"
}

multichoice_dict2 = {
    1: "Minoan",
    2: "Balkan Sea",
    3: "Se7en",
    4: "Dynamite Kid",
    5: "The construction of the Empire State Building",
    6: "Helsinki",
    7: "FAHRENHEIT 451",
    8: "Toronto",
    9: "Emma Watson",
    10: "Tenzing Norgay"
}

multichoice_dict3 = {
    1: "Hittite",
    2: "Baltic Sea",
    3: "Hannibal",
    4: "Big Daddy",
    5: "The development of the Atomic Bomb", 
    6: "Copenhagen",
    7: "Catch-22",
    8: "Vancouver",
    9: "Emilia Clarke",
    10: "Adesh Maheshwari"
}


answers_dict = {
    1: "Minoan",
    2: "Baltic Sea",
    3: "Silence of the Lambs",
    4: "Big Daddy",
    5: "The development of the Atomic Bomb", 
    6: "Copenhagen",
    7: "FAHRENHEIT 451",
    8: "Ottawa",
    9: "Phoebe Waller-Bridge",
    10: "Tenzing Norgay"
}


def quiz_func(score, x, asked_questions):
    available_questions = [num for num in range(1,11) if num not in asked_questions]
    question_num= available_questions[round(uniform(0, len(available_questions) - 1))]

    question = question_dict.get(question_num)
    answer = answers_dict.get(question_num)
    choice1 = multichoice_dict1.get(question_num)
    choice2= multichoice_dict2.get(question_num)
    choice3= multichoice_dict3.get(question_num)

    this_question_num = x

    print(f'Question {this_question_num}')
    print(question)
    print(choice1)
    print(choice2)
    print(choice3)
    user_answer=input("Please write the correct answer ")
    if user_answer == answer:
        print("Correct answer. Good job")
        score += 1

    else:
        print("Incorrect Answer. Better luck next time")
    

    asked_questions.append(question_num)
    return score



def welcome_message():
    print("Welcome to the quiz. Are you ready?")
    quiz_start=input("Start quiz? ").lower()
    if quiz_start in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup']:
        score = 0
        i = 1
        x = 1
        asked_questions = []
        while i <= 10: 
            score = quiz_func(score, x, asked_questions)
            i += 1
            x += 1
        print(f"Your final score is: {score}")
    else:
        print("Thanks for stopping by. Have a great day.")

welcome_message()





