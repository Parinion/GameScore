import random
import datetime
import time
import pandas as pd


def only_digits(numbers):
    for c in numbers:
        if c not in '0987654321':
            return False
    return True


def gameheader():
    fname = input("Enter your name: ")
    print_hi(fname)
    return fname


def multi_and_div():
    choice = ('m', 'd')
    begin = 1
    end = 12
    fname = gameheader()
    n = None
    while n is None:
        # print ("Hello! Welcome to Math Quiz,")
        s = input("How many questions would you like?\n")
        if s not in ('0', '', ' '):
            if only_digits(s):
                n = int(s)
                # G
                # print ("\n")
            else:
                print("Not an accepted answer, try again\n")
        else:
            print("Not an accepted answer, try again\n")
    # execute n time
    wrong_answer = 0
    startt = time.monotonic()
    for z in range(n):
        rdc = random.choice(choice)
        x = random.randrange(begin, end)
        y = random.randrange(begin, end)
        correct_answer = x * y
        if rdc == 'm':
            print("What is the result of " + str(x) + "*" + str(y) + "? ")
        else:
            print("What is the result of " + str(correct_answer) + "/" + str(y) + "? ")
        # print correct_answer
        result = 0
        wrong = 0
        while result == 0:
            quiz_answer = input()
            if only_digits(quiz_answer):
                quiz_integer = int(quiz_answer)
                if rdc == 'm':
                    sol = correct_answer
                else:
                    sol = x
                if quiz_integer == sol:
                    # total_correct += 1
                    print("Correct!\n")
                    result = 1
                else:
                    print("Wrong, try again")
                    wrong = 1
                    # total_correct -= 1
                    result = 0
            else:
                print("Not a integer, try again\n")
            wrong_answer += wrong
    stopt = time.monotonic()
    #print ("Time" + str(round(stopt-startt,2)))
    avg_t_per_sec = round((stopt-startt)/n,1)
    correct_percent = round(((n - wrong_answer) * 100) / n,0)
    nbr = n - wrong_answer
    dte = datetime.datetime.now()
    lbstr = fname + ",M&B," + str(avg_t_per_sec) +","+ str(nbr) + "," + str(correct_percent) + "%" + "," + dte.strftime("%x %X")
    if n>=10:
        writeleader(lbstr)
    reportout(lbstr)
    return


def multiplication_game():
    begin = 1
    end = 12
    fname = gameheader()
    n = None
    while n is None:
        # print ("Hello! Welcome to Math Quiz,")
        s = input("How many questions would you like?\n")
        if s not in ('0', '', ' '):
            if only_digits(s):
                n = int(s)
            else:
                print("Not an accepted answer, try again\n")
        else:
            print("Not an accepted answer, try again\n")
    # execute n time
    wrong_answer = 0
    startt = time.monotonic()
    for z in range(n):
        x = random.randrange(begin, end)
        y = random.randrange(begin, end)
        print("What is the result of "+str(x) + "*" + str(y)+"? ")
        correct_answer = x * y
        # print correct_answer
        result = 0
        wrong = 0
        while result == 0:
            quiz_answer = input()
            if only_digits(quiz_answer):
                quiz_integer = int(quiz_answer)
                if quiz_integer == correct_answer:
                    # total_correct += 1
                    print("Correct!\n")
                    result = 1
                else:
                    print("Wrong, try again")
                    wrong = 1
                    # total_correct -= 1
                    result = 0
            else:
                print("Not a integer, try again\n")
            wrong_answer += wrong
    # print(wrong_answer)
    stopt = time.monotonic()
    avg_t_per_sec = round((stopt - startt) / n, 1)
    correct_percent = round(((n - wrong_answer) * 100) / n, 0)
    nbr = n - wrong_answer
    dte = datetime.datetime.now()
    lbstr = fname + ",MULT," + str(avg_t_per_sec) + "," + str(nbr) + "," + str(correct_percent) + "%" + "," + dte.strftime("%x %X")
    if n >= 10:
        writeleader(lbstr)
    reportout(lbstr)
    return lbstr


def division_game():
    begin = 1
    end = 12
    # ask number of tine
    # ok = False
    # while not ok :
    #     print ("Hello! Welcome to Math Quiz,")
    #     question_nbr = raw_input("How many questions would you like?\n")
    fname = gameheader()
    n = None
    while n is None:
        # print ("Hello! Welcome to Math Quiz,")
        s = input("How many questions would you like?\n")
        if s not in ('0', '', ' '):
            if only_digits(s):
                n = int(s)
                # G
                # print ("\n")
            else:
                print("Not an accepted answer, try again\n")
        else:
            print("Not an accepted answer, try again\n")

    # execute n time
    wrong_answer = 0
    # total_correct = 0
    startt = time.monotonic()
    for z in range(n):
        x = random.randrange(begin, end)
        y = random.randrange(begin, end)
        correct_answer = x * y
        print("What is the result of " + str(correct_answer) + "/" + str(y) + "? ")
        # print correct_answer
        result = 0
        wrong = 0
        while result == 0:
            quiz_answer = input()
            if only_digits(quiz_answer):
                quiz_integer = int(quiz_answer)
                if quiz_integer == x:
                    # total_correct += 1
                    print("Correct!\n")
                    result = 1
                else:
                    print("Wrong, try again")
                    wrong = 1
                    # total_correct -= 1
                    result = 0
            else:
                print("Not a integer, try again\n")
            wrong_answer += wrong
    # print(wrong_answer)
    stopt = time.monotonic()
    # print ("Time" + str(round(stopt-startt,2)))
    avg_t_per_sec = round((stopt - startt) / n, 1)
    correct_percent = round(((n - wrong_answer) * 100) / n, 0)
    nbr = n - wrong_answer
    dte = datetime.datetime.now()
    lbstr = fname + ",DIV," + str(avg_t_per_sec) + "," + str(nbr) + "," + str(
        correct_percent) + "%" + "," + dte.strftime("%x %X")
    if n>=10:
        writeleader(lbstr)
    reportout(lbstr)
    return lbstr


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi,' + name)


def writeleader(lbstr):
    # Write to Leaderboard
    f = open("leaderboard.txt", "a")
    f.write(lbstr + "\n")
    f.close()


def deleteleader():
    # Delete leaderboard
    f = open("leaderboard.txt", "w")
    f.truncate()
    f.close()


def readsortleader():
    # Read leaderboard file. Sort file by score, select top 10
    x = 10  # number of players on leaderboard
    f = open("leaderboard.txt", "r")
    # print("Number of rows ", len(f.index))
    df = pd.read_csv(f, sep=',', header=None)
    sdf = df.sort_values(by=2, ascending=True)
    sdf = sdf.head(n=x)
    sdf = sdf.rename(columns={0: 'Name', 1: 'Game', 2: 'Avg.Time(s)', 3:'# Correct', 4: '% Correct', 5: 'Date'})
    sdf = sdf.reset_index(drop=True)
    print("\n\n************************************************************************************")
    print("*********************************** LEADER BOARD ***********************************")
    print("************************************************************************************")
    # print(sdf)
    print(sdf.to_string(index=False))
    print("\n\n")
    # delleader = input("Type Y if you want to delete the leaderboard?\n")
    # if delleader.upper() == "Y":
    #     deleteleader()


def reportout(res):
    my_list = res.split(",")
    #print (my_list[1])
    if my_list[1] == "M&B":
        game = "Multiplication and Division"
    elif my_list[1] == "MULT":
        game = "Multiplication"
    elif my_list[1] == "DIV":
        game = "Division"
    else:
        game = "UNK"
    print("You played the "+game+" game. Your average answer speed was " + my_list[2]+" seconds. You got " + my_list[4]+" correct.\n\n")
    return


######### MAIN CODE ####################
qst_string_title = "What do you want to do?\n"
qst_string_options1 = "   To play the multiplication game, type M\n   To play the division game, type D\n"
qst_string_options2 = "   To play the M&D game, type B\n   To see the leaderboard, type L\n   To quit, type Q\n"
qst_string_options3 = "** You can only get on the leaderboard if you select at least 10 questions.\n\n"
qst_string = qst_string_title + qst_string_options1 + qst_string_options2 + qst_string_options3

print('\nHello, Welcome to MathQuiz!\n')
play = input(qst_string)
while play.upper() != "Q":
    if play.upper() == "M":
        multiplication_game()
        play = input(qst_string)
    elif play.upper() == "D":
        division_game()
        play = input(qst_string)
    elif play.upper() == "B":
        multi_and_div()
        play = input(qst_string)
    elif play.upper() == "L":
        readsortleader()
        play = input(qst_string)
    else:
        print("'" + play + "' is not a valid response. Try again\n\n")
        play = input(qst_string)
if play.upper() == "Q":
    print("Goodbye :)")
    exit()
