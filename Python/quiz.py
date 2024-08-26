import json

points = 0

def show_question(question):
    global points
    print()
    print(question["pytanie"])
    print("a:", question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"])
    print()
    
    answer = input("Podaj odpowiedź (a, b, c, d): ")

    if answer == question["prawidłowa_odpowiedź"]:
        points += 1
        
        print("Brawo! To prawidłowa odpowiedź. Masz już", points, "punktów")
    else:
        print("Niestety, to zła odpowiedź. Prawidłowa odpowiedź to:", question["prawidłowa_odpowiedź"], ".")

with open("quiz.json") as json_file:
   questions =  json.load(json_file)
   
   
   for i in range(0, len(questions)):
       show_question(questions[i])
   
