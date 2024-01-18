import time
from termcolor import colored
import sys
import os

def clear():
    for x in range(2):
        print()
    os.system('clear')

score = 0
bonus = 0

def level_1():
    global score
    global bonus
    beginner = input("hit l for start the Game: ")
    print()
    print()
    if beginner == 'l':
        print(colored("LEVEL 1", "green"))
        print()
        sentence = "best of luck for your typing test! this is the simple text for your typing skill test. but next time typing test level is difficult."
        print(sentence)
        start_time = time.time()
        level_input = input("Type the sentence above : ")
        end_time = time.time() - start_time
        print()
        if level_input == sentence:
            score += 1
            bonus += 0.5
            print("Score :", score)
            print("Time taken :", end_time)
            print()
            print(colored('------------------------------------', 'blue'))
            print()
        else:
            score -= 1
            bonus = 0
            print("Score :", score)
            print("Time taken :", end_time)
            print()
            print()

        level_2()

def level_2():
    global score
    global bonus
    beginner = input("hit l to begin : ")
    print()
    print()
    if beginner == 'l':
        print(colored("LEVEL 2", "green"))
        print()
        sentence2 = "DSA is foundational in computer science, enabling efficient algorithms, data structures, and problem-solving, crucial for software development"
        print(sentence2)
        start_time = time.time()
        level_input = input("Type the sentence above : ")
        end_time = time.time() - start_time
        print()
        if level_input == sentence2:
            score += 1
            bonus += 0.5
            print("Score :", score)
            print("Time taken :", end_time)
            print()
            print(colored('------------------------------------', 'blue'))
            print()

        else:
            score -= 1
            bonus = 0
            print("Score :", score)
            print("Time taken :", end_time)
            print()
            print(colored('------------------------------------', 'blue'))
            print()

        level_3()

def level_3():
    global score
    global bonus
    beginner = input("hit l to begin : ")
    print()
    print()
    if beginner == "l":
        print(colored("LEVEL 3", "green"))
        print()
        sentence3 = "Python, a versatile and high-level programming language, has become a cornerstone in the world of software development. Known for its simplicity and readability, Python facilitates rapid development and encourages clean, maintainable code. Its extensive standard library and a vast ecosystem of third-party packages make it suitable for diverse applications, from web development and data analysis to artificial intelligence and scientific computing."
        print(sentence3)
        start_time = time.time()
        level_input = input("Type the sentence above : ")
        end_time = time.time() - start_time
        print()
        if level_input == sentence3:
            score += 1
            bonus += 1
            print("Score :", score)
            print("Time taken :", end_time)
            print()
            print()
        else:
            score -= 1
            bonus = 0
            print("Score :", score)
            print("Time taken :", end_time)
            print()
            print(colored('------------------------------------', 'blue'))

time.sleep(2)

for x in ("WELCOME TO TYPOMANIA!!!", "red"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.05)

print('\n---------------------------------------')
time.sleep(1)
print()
print(colored("DIRECTIONS: there are 3 levels in this typing game, complete all of them, and check your score, and the time it took you to type the sentence. The sentences get harder as you go on.", 'blue'))
print()
print()

level_1()

clear()

if score == 3:
    print("You got 3 sentences correct!"); print()
    print(colored("YOU WIN!", "green")); print(); print("Score :", score); print("Bonus :", bonus); print("Total Score =", score + bonus)
elif score == 2 or score == 1:
    print("You got 2 sentences correct!")
    print()
    print(colored("Fantastic job, keep trying!", "green"))
    print()
    print("Score :", score)
    print("Bonus :", bonus)
    print("Total Score =", score + bonus)
elif score == 0 or score == -1:
    print("You got 1 sentence correct!")
    print()
    print(colored("Ok... practice more.", "yellow"))
    print()
    print("Score :", score)
    print("Bonus :", bonus)
    print("Total Score =", score + bonus)
elif score < 1:
    print("You got no sentences correct!")
    print()
    print(colored("YOU LOST", "red"))
    time.sleep(1)
    print()
    print("Score :", score)
    time.sleep(1)
    print("Bonus :", bonus)
    time.sleep(1)
    print("Total Score =", score + bonus)

print()

for x in colored("Thank you for playing this game😊, please come back again!👍", "green"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.05)

print()
print()

d = input("do you want to play again : ")

score = 0
bonus = 0

if d == "yes":
    os.system('clear')
    level_1()
    time.sleep(2)

    clear()

    if score == 3:
        print("You got 3 sentences correct!"); print()
        print(colored("YOU WIN!", "green")); print(); print("Score :", score); print("Bonus :", bonus); print("Total Score =", score + bonus)
    elif score == 2 or score == 1:
        print("You got 2 sentences correct!")
        print()
        print(colored("Fantastic job, keep trying!", "green"))
        print()
        print("Score :", score)
        print("Bonus :", bonus)
        print("Total Score =", score + bonus)
    elif score == 0 or score == -1:
        print("You got 1 sentence correct!")
        print()
        print(colored("Ok... practice more.", "yellow"))
        print()
        print("Score :", score)
        print("Bonus :", bonus)
        print("Total Score =", score + bonus)
    elif score < 1:
        print("You got no sentences correct!")
        print()
        print(colored("YOU LOST", "red"))
        time.sleep(1)
        print()
        print("Score :", score)
        time.sleep(1)
        print("Bonus :", bonus)
        time.sleep(1)
        print("Total Score =", score + bonus)

    print()

    for x in colored("Thank you for playing this game, please come back again!", "green"):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.05)

else:
    os.system('clear')
    print("cool.. have a nice day!!")
    time.sleep(1.5)
    os.system('clear')
  
print()
print()
