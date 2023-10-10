#rules
print("only 5 questions \nAnswer all questions in 10 seconds \n5 mark for each question\n")

import time


def count_down(sec=10):                 #to display time
    for i in range(sec):
        print(sec-i, end='\r')
        time.sleep(1)
    print("time over")
    exit()



score=0
questions = ["1. Which type of Programming does Python support?\n\n  a.object-oriented programming         b.structured programming\n\n  c. functional programming         d.all of the mentioned",
             "\n2. Which keyword is used for function in Python language?\n\n  a.def        b.Function\n\n  c.Fun      d.Define",
             "\n3.Brain of a computer is?\n\n  a.monitor        b.keyboard\n\n  c.cpu       d.mouse",
             "\n4. Which of the following character is used to give single-line comments in Python?\n\n  a.//         b.# \n\n  c.!       d./*",
             "\n5.Which of the following functions is a built-in function in python?\n\n  a.factorial()      b.print()\n\n  c.seed()       d.sqrt()"]            #list of quetions         

answers_key = ["d","a","c","b","b"]    


for i in range(len(questions)):
    print(questions[i])
    user_answer=input("\nEnter The Answer:").lower()
    if user_answer==answers_key[i]:
        print("\ncorrect answer")
        score=score+5
    else:
        print("\nincorrect answer")

print("Total Mark : ",score)