import time
import random


def count_down(sec=5):                 #to display time
    for i in range(sec):
        print(sec-i, end='\r')
        time.sleep(1)
    print("time over")
    exit()




questions = ["Who was the first Prime Minister of India?",
             "Who invented the Computer?",
             "Brain of a computer is?",
             "Smallest state of India is?",
             "National animal of India?"]            #list of quetions         

answers = ["Jawaharlal Nehru",
           "Charles Babbage",
           "CPU",
           "Goa",
           "Tiger"]           #list of answerkey

qus = random.choice(questions)
print(qus)                           # Start the countdown

print(count_down())
ans = input("Enter your answer: ")  

if qus == questions[0] and ans == answers[0]:
    print("Correct answer")
elif qus == questions[1] and ans == answers[1]:
    print("Correct answer")
elif qus == questions[2] and ans == answers[2]:
    print("Correct answer")
elif qus == questions[3] and ans == answers[3]:
    print("Correct answer")
elif qus == questions[4] and ans == answers[4]:
    print("Correct answer")
else:
    print("Wrong answer")



