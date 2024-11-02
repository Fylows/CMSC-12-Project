import random
import time
import os

intro = """
╦ ╦╦ ╦╔═╗  ╦ ╦╔═╗╔╗╔╔╦╗╔═╗  ╔╦╗╔═╗  ╔═╗╔═╗╔═╗╔═╗  ╔╦╗╦ ╦╔═╗  ╦ ╦╔═╗╔═╗╔═╗╔╦╗
║║║╠═╣║ ║  ║║║╠═╣║║║ ║ ╚═╗   ║ ║ ║  ╠═╝╠═╣╚═╗╚═╗   ║ ╠═╣║╣   ║ ║╠═╝║  ╠═╣ ║ 
╚╩╝╩ ╩╚═╝  ╚╩╝╩ ╩╝╚╝ ╩ ╚═╝   ╩ ╚═╝  ╩  ╩ ╩╚═╝╚═╝   ╩ ╩ ╩╚═╝  ╚═╝╩  ╚═╝╩ ╩ ╩ 
"""

# TODO LIMIT QUESTIONS TO MAX OF 99 (5 categories * 3 difficulties * 99 questions each + 99 questions for final = 1584 possible questions)

""" ======= GENERAL FUNCTIONS ======= """
# Simple function (int to letter) that assigns 1,2,3,4 to A,B,C,D respectively
def itol(n:int) -> str:
    d = {
        1 : "A",
        2 : "B",
        3 : "C",
        4 : "D",
    }
    return d[n]

def invalid() -> None:
    os.system("cls||clear")
    print("Invalid Try again.")
    time.sleep(1)

# Moving page menu logic
def next_page(curr_page:int, curr_display:int, curr_max_display:int, max_page:int, display:int, count:int) -> int:
    if curr_page == max_page:
            os.system("cls||clear")
            print("No page follows.")
            time.sleep(1)
            return curr_page, curr_display, curr_max_display
    curr_page += 1

    if curr_page == max_page:
        curr_max_display = count

    else:
        curr_max_display += display

    curr_display += display
    return curr_page, curr_display, curr_max_display

def prev_page(curr_page:int, curr_display:int, curr_max_display:int, max_page:int, display:int, count:int) -> int:
        if curr_page == 1:
            os.system("cls||clear")
            print("No page preceeds.")
            time.sleep(1)
            return curr_page, curr_display, curr_max_display

        # if page # is last page, decrement count not w/ ones digit of count to even out max page number
        elif curr_page == max_page:
            curr_max_display -= count % display

        else:
            curr_max_display -= display


        curr_page -= 1
        curr_display -= display
        return curr_page, curr_display, curr_max_display

    # Function that populates the questions dictionary with the contents of the file in directory

# Function for modifying leaderboard/s
def update_leaderboard(uname:str, score:float) -> None:
    myDict = {}
    Readfile = open("./leaderboard.dat", "r")
    for line in Readfile:
        temp = line[:-1].split(",")
        myDict[temp[0]] = float(temp[1])

    # TODO add them to Hall of Passers
    # If perfect score, then remove their names from leaderboard
    if score == 100.00:
        del myDict[uname]

    # Adds a name when there are less than 5 ppl
    else:
        print("pass")
        if len(myDict) < 5:
            myDict[uname] = score
        else:
            for k in myDict:
                if score >= myDict[k]:
                    myDict.popitem()
                    myDict[uname] = score
                    break
    print(myDict)
    time.sleep(2)

    # Sorts dictionary based on keys, key = calling lambda to retrieve its item
    myDict = dict(sorted(myDict.items(), reverse=True, key=lambda item: item[1]))
    Writefile = open("./leaderboard.dat", "w")
    for k,v in myDict.items():
        Writefile.write(f"{k},{v}\n")
    
    Readfile.close()
    Writefile.close()

def user_login(myList:list) -> str:
    while 1:
        os.system("cls||clear")
        usr = input("Enter your desired username: ").replace(" ", "ඞ").lower()

        if 3 > len(usr) or len(usr) > 10:
            print("Username must be between 3 and 10 letters")
            time.sleep(1)
            continue
        elif usr in myList:
            print("That user already exists! Please choose another.")
            time.sleep(1)
            os.system('cls||clear')
            continue
        elif "ඞ" in usr:
            invalid()
            continue
        break
    pw = input("Enter your password: ")
    
    return usr,pw         

def populate_players(myDict:dict, directory:str = "./players.dat", mode:str = "any") -> None:

    Readfile = open(directory, "r")

    if mode == "pb":
        for line in Readfile:
            temp = line[:-1].split(",")
            myDict[temp[0]] = float(temp[1])

    else:
        for line in Readfile:
            temp = line[:-1].split(",")
            myDict[temp[0]] = temp[1]
    Readfile.close()

def populate_questions(myDict:dict, directory: str) -> None:
    file = open(directory,"r")
    i = 1
    for line in file:
        if line[0] == "C":
            myDict["C"] = int(line[2:-1])
            continue
        myDict[str(i)] = line[:-1].split(",")
        i += 1

def rewrite_players(myDict:dict, directory:str = "./players.dat") -> None:
    Writefile = open(directory, "w")
    for k, v in myDict.items():
        Writefile.write(f"{k},{v}\n")
    Writefile.close()
# function that adds ALL questions in a dictionary, then returns that dictionary
def endless() -> dict:

    # questions = {}



    cat = random.randrange(0,6)
    if cat == 5:
        diff = "final"
    else:
        diff = random.randrange(0,3)
        category = {
            0 : "lang_prof",
            1 : "read_comp",
            2 : "math",
            3 : "sci",
            4 : "gen_info",
            5 : "final"
    
        }
        
        difficulty = {
            0 : "easy",
            1 : "med",
            2 : "hard"
        }
    # return f"./{category[cat]}/{difficulty[diff]}"


""" ======= MENUS ======= """
def login_menu() -> None:
    size = os.get_terminal_size()
    def display() -> None:
        os.system('cls||clear')
        # splits intro into multiple lines and prints that
        centered_intro = "\n".join(line.center(size.columns) for line in intro.strip().splitlines())
        print(centered_intro)
        print("")
        print("Welcome!\n".center(size.columns))
        print("[1] Login".center(size.columns))
        print("[2] Register".center(size.columns))

    def login() -> tuple:
        players = {}
        populate_players(players)

        while 1:
            os.system('cls||clear')
            usr = input("Enter your Username: ").lower()
            pw = input("Enter your password: ")
           

            if (usr,pw) in players.items():
                if usr == "admin" and pw == players[usr]:
                    return (2,usr)
                return (1,usr)
            
            stop = input("Invalid login.\nEnter any key to try again or go back with [0] ")
            if stop == "0":
                return stop
            else: continue

    def register() -> None:
        file_append = open("./players.dat", "a")
        file_read = open("./players.dat", "r")
        
        # puts usernames in a list 
        users = [line.split(',')[0].lower() for line in file_read.readlines()]

        while 1:
            os.system('cls||clear')
            uname,pw = user_login(users)

            # Append new user to the file
            file_append.write(f"{uname},{pw}\n")
            
            print("Registration successful!")
            file_read.close()
            file_append.close()
            time.sleep(1)
            return  # Exit the function after successful registration
    
    # Main loop
    while 1:
        display()
        print("What would you like to do?".center(size.columns))
        choice = input("".center(size.columns//2))
        if choice == "1":
            player = login()
            if player != "0":
                return player
        elif choice == "2":
            register()
        else:
            invalid()

def player_menu(name: str) -> None:
    print("Logging in", end='')
    for i in range(4):
        dots = "." * i
        print(f"\rLogging in{dots}", end='')  # \r brings the cursor back to the start of the line
        time.sleep(0.5)
    os.system('cls||clear')
    print(f"Hello {name.capitalize()}!")
    time.sleep(1)

        

# Easy retry until you get it, time limit of 10
# Medium No Retries, Time limit of 10
# Hard No Retries, Timel limit of 5
    def play_game(uname:str, best_progress:dict) -> None:
        def generate_question(directory: str) -> dict:
            file =  open(directory,"r")
            lines = file.readlines()
            file.close()

            questions = {}

            total = int(lines[0][2])

            indecies = list(range(1, total+1))
            random.shuffle(indecies)


            for i in indecies[:5]:
                temp = lines[i][:-1].split(",")
                questions[temp[0]] = [temp[1], temp[2], temp[3], temp[4], temp[5]]
            return questions
        
        def display_question( k:str, v:list) -> None:
            print(f"~~~ Question: {str(k).rjust(3,'0')} ~~~\n")
            print(f"A: {v[0]}\t\t",end='')
            print(f"C: {v[2]}")
            print(f"B: {v[1]}\t\t",end='')
            print(f"D: {v[3]}\n")

        def category() -> str:
            d = {
            "1" : "lang_prof",
            "2" : "read_comp",
            "3" : "math",
            "4" : "sci",
            "5" : "gen_info",
        }
            def choose() -> str:
                os.system('cls||clear')
                print("Which Category?")
                print("=====================")
                print("[1] Language Proficiency")
                print("[2] Reading Comprehension")
                print("[3] Mathematics")
                print("[4] Science")
                print("[5] General Knowledge")
                ans = input("Enter your choice: ")
                return ans
        
            while 1:
                os.system('cls||clear')
                ans = choose()
                if (ans not in d.keys()):
                    invalid()
                    continue
                break
            return d[ans]
        
        def ask_question(k:str, v:list, life:int) -> bool:
            while 1:
                os.system("cls||clear")
                display_question(k,v)
                print(f"You have {life} mistake/s remaining")
                answer = input("What is the answer? ")
                answer = answer.upper()

                if answer in ["A", "B", "C", "D"]:
                    if answer == v[4]:
                        print("Correct!")
                        time.sleep(1.25)
                        return True
                    
                    elif answer != v[4]:
                        print("Inorrect.")  
                        time.sleep(1.25)
                        return False
                else:
                    invalid()
                time.sleep(.25)
        
        difficulties = ["easy","med","hard", "final"]
        highscore = best_progress[name]
        i = 0
        points = 0
        lives = 5
        time_limit = ((i == 0) * 15) + ((i == 1) * 10) + ((i == 2) * 10) + ((i==3)*5)
        
        while lives > 0 and i < 4:
            if i == 3:
                cat = "final"
            else:
                cat = category()

            # ques is a dictionary containing 5 random questions
            ques = generate_question(f"./questions/{cat}/{difficulties[i]}.dat")

            os.system("cls||clear")
            print(f"You are playing {cat} on {difficulties[i]}, goodluck!")
            time.sleep(1)

            for k,v in ques.items():
                os.system("cls||clear")
                start,elapsed = time.time(),0

                # Ask same question until they get it right'
                while lives > 0:
                    elapsed = time.time() - start
                    if elapsed > time_limit:
                        print("You took too long.")
                        lives -= 1
                        time.sleep(1.25)
                        break
                    elif ask_question(k,v,lives):
                        points += 1
                        break
                    else:
                        lives -= 1

            os.system("cls||clear")
            print("Congratulations You just moved up a level!")
            # Moves difficulty
            i+=1
            os.system("cls||clear")
        
        points = (points/20) * 100
        if lives == 0:
            print(f"Sorry you lost with {points}% progress")
            time.sleep(2)

        # If you complete the game or you have a new highscore
        elif lives != 0 or points > highscore:
            if points > highscore:
                print(f"You have set a new personal best of {points}% completed!")
            elif points == 100.00:
                print("Congratulations you have earned a crown and a spot in UPLB!")
            best_progress[name] = points
            update_leaderboard(uname,points)
            rewrite_players(bests, "./pbs.dat")
            time.sleep(2)
            return
        
    def print_rules():
        ...

    def print_leaderboard():
        os.system("cls||clear")
        file = open("./leaderboard.dat", "r")
        lines = file.readlines()

        print("TOP 5 PLAYERS' PROGRESS\n")


        for i in range(5):
            if i < len(lines):
                temp = lines[i][:-1].split(",")
                print(f"{i+1}. {temp[0].capitalize().ljust(15)}{temp[1].rjust(5)}%\n")
                continue
            
            print(f"{i+1}. {'N/A'.ljust(15)}{'00.00'.rjust(5)}%\n")
            

        input("Enter any key to go back\n")

 
    def account_settings():
        # Winner?
        # Personal Best
        # Change uname
        # change pw
        ...
    def print_winners():
        print("== UPCAT Passers ==")
        with open("./pbs.dat", "r") as file:
            count = 1
            for line in file:
                i = line[:-1].split(",")
                if float(i[1]) == 100.00:
                    print(f"{count}. {i[0]}")
                    count + 1
            input("Enter any key to go back. ")

    while 1:
        os.system("cls||clear")

        bests = {}
        populate_players(bests, "pbs.dat", "pb")

        if name in bests:
            if int(bests[name]) == 100:
                print("^^^ crowned passer")
            else:
                print(f"Your personal best progress is: {bests[name]}%")
        else:
            print("You have no previous progress.")

        options = {
            "1" : lambda : play_game(name, bests),
            "2" : lambda : print_rules(),
            "3" : lambda : print_leaderboard(),
            "4" : lambda : account_settings(),
            "5" : lambda : print_winners()
        }
      
        print("\n== PLAYER OPTIONS ==")
        print("[1] Play Game!")
        print("[2] How to play")
        print("[3] Leaderboard")
        print("[4] Account Settings")
        print("[5] Hall of Passers" )
        print("[B] Quit")
        choice = input("What would you like to do? ")
        if choice in options.keys():
            options[choice]()
        elif choice == "B":
            return
        else:
            invalid()

def admin_menu() -> None:
    
    print("Logging in", end='')
    for i in range(3):
        a = "."*i
        print(a,end='')
        time.sleep(0.5)
    os.system('cls||clear')
    print("Log in complete! ")
    print("Hello admin!")
    time.sleep(1)

    """ == GENERAL FUNCTIONS == """

    # Function that returns the category defined by admin
    def category() -> str:
        d = {
            "1" : "lang_prof",
            "2" : "read_comp",
            "3" : "math",
            "4" : "sci",
            "5" : "gen_info",
            "6" : "final",
            "B" : "B",
        }
        def choose() -> str:
            os.system('cls||clear')
            print("Which Category?")
            print("=====================")
            print("[1] Language Proficiency")
            print("[2] Reading Comprehension")
            print("[3] Mathematics")
            print("[4] Science")
            print("[5] General Knowledge")
            print("[6] Final Round Questions")
            print("[B] Back to Main Menu")
            ans = input("Enter your choice: ")
            return ans
        
        while 1:
            os.system('cls||clear')
            ans = choose()
            if (ans not in d.keys()):
                invalid()
                continue
            break
        return d[ans]
    
    # Function that returns the difficulty defined by admin
    def diff() -> str:

        d = {
            "1" : "easy",
            "2" : "med",
            "3" : "hard",
            "B" : "B",
        }
        def choose():
            print("What Difficulty?")
            print("=====================")
            print("[1] Easy")
            print("[2] Medium")
            print("[3] Hard")
            print("[B] Back to Category")
            ans = input("Enter your choice: ")
            return ans

        while 1:
            os.system('cls||clear')
            ans = choose()
            if (ans not in d.keys()):
                invalid()
                continue
            break
        return d[ans]

    def display_question(questions: dict, k:any) -> None:
        if k == "C":
            return
        print(f"~~~ Question {str(k).rjust(3,'0')} ~~~\n")
        print(f"{questions[k][0]}")
        print(f"A: {questions[k][1]}\t\t",end='')
        print(f"C: {questions[k][3]}")
        print(f"B: {questions[k][2]}\t\t",end='')
        print(f"D: {questions[k][4]}\n")
        print(f"Correct answer {(questions[k][5])}\n")
        return
    
    def populate_questions(myDict:dict, directory: str) -> None:
        file = open(directory,"r")
        i = 1
        for line in file:
            if line[0] == "C":
                myDict["C"] = int(line[2:-1])
                continue
            myDict[str(i)] = line[:-1].split(",")
            i += 1
    
    def edit_question(questions: dict, curr_page:int, curr_display:int, curr_max_display:int, max_page:int, display:int, count:int) -> None:
        def edit(questions:dict, key:int):
            while 1:
                os.system("cls||clear")
                
                display_question(questions, key)

                print("[1] Question")
                print("[2] Choices")
                print("[3] Answer")
                print("[0] Save question")
                option = input("What do you want to edit? ")
                if option == "1":
                    new_question = input("Enter new Question: ")
                    questions[key][0] = new_question
                elif option == "2":
                    for i in range(1,5):
                        questions[key][i] = input(f"Enter new choice {itol(i)}: ")
                elif option == "3":
                    new_ans = input("Enter new answer: ").upper()
                    if new_ans not in ["A", "B", "C", "D"]:
                        invalid()
                        continue
                    questions[key][5] = new_ans
                elif option == "0":
                    return
                else:
                    invalid()

        while 1:
            os.system('cls||clear')
            for i in range(curr_display,curr_max_display + 1): 
                display_question(questions, str(i))
            print(f"Page {curr_page} of {max_page}")
            print("[<] Previous Page  Next Page [>]")
            print("[B] Back")
            choice = input("Which question do you want to edit? ").lstrip('0')

            if choice in questions.keys():
                while 1:
                    os.system('cls||clear')
                    display_question(questions, choice)
                    confirm = input("Are you sure you want to edit this question? [y/n] ").lower()
                    if confirm == "y":
                        edit(questions, choice)
                        return
                    elif confirm == "n":
                        break
                    else: 
                        invalid()    
            elif choice == "<":
                curr_page, curr_display, curr_max_display = prev_page(curr_page, curr_display, curr_max_display, max_page, display, count)
            elif choice == ">":
                curr_page, curr_display, curr_max_display = next_page(curr_page, curr_display, curr_max_display, max_page, display, count)   
            elif choice == "B":
                break
            else: 
                invalid()

        return

    def delete_question(questions: dict, curr_page:int, curr_display:int, curr_max_display:int, max_page:int, display:int, count:int) -> None:
        while 1:
            os.system('cls||clear')
            for i in range(curr_display,curr_max_display + 1): 
                display_question(questions, str(i))
            print(f"Page {curr_page} of {max_page}")
            print("[<] Previous Page   Next Page [>]")
            print("[B] Back ")
            choice = input("Which question do you want to delete? ").lstrip('0')

            if choice in questions.keys():
                while 1:
                    os.system('cls||clear')
                    display_question(questions, choice)
                    confirm = input("Are you SURE you want to delete this question? [y/n] ").lower()
                    if confirm == "y":
                        del questions[choice]
                        return
                    elif confirm == "n":
                        break
                    else: 
                        invalid()   
            elif choice == "<":
                        curr_page, curr_display, curr_max_display = prev_page(curr_page, curr_display, curr_max_display, max_page, display, count)
            elif choice == ">":
                curr_page, curr_display, curr_max_display = next_page(curr_page, curr_display, curr_max_display, max_page, display, count)   
            elif choice == "B":
                break
            else: 
                invalid()
        return
    # function that adds questions to questions dictionary
    
    # Function that rewrites the contents of .dat file by taking in a dictionary of questions and putting those in the file
    # Mode for incrementing or decrementing count
    def rewrite(myDict:dict, directory:str, mode:str = "any") -> None:
        file = open(directory, "w")
        for k in myDict:
            if k == "C":
                if mode == "+":
                    file.write(f"C {int(myDict[k]) + 1}\n")
                elif mode == "2":
                    file.write(f"C {int(myDict[k]) - 1}\n")
                else:
                    file.write(f"C {int(myDict[k])}\n")

                continue
            file.write(f"{myDict[k][0]},{myDict[k][1]},{myDict[k][2]},{myDict[k][3]},{myDict[k][4]},{myDict[k][5]}\n")


    """ == MENU OPTIONS == """
    # View questions prints all questions from a category and difficulty
    # Page by page view 
    def view_questions() -> None:
        d = {
            "1" : lambda q, cp, cd, cmd, mp, d, c : edit_question(q, cp, cd, cmd, mp, d, c),
            "2" : lambda q, cp, cd, cmd, mp, d, c : delete_question(q, cp, cd, cmd, mp, d, c)
        }
        while 1:
            topic = category()
            if topic == "B":
                return
            elif topic == "final":
                difficulty = "final"
            else:
                difficulty = diff()
                if difficulty == "B":
                    continue

            
            while 1:
                directory = f"./questions/{topic}/{difficulty}.dat"
                # Populate questions array with questions and count of questions
                questions = {}
                populate_questions(questions, directory)

                os.system('cls||clear')

                # count for maximum number of questions
                count = questions["C"]

                # How many questions to display
                display = 5

                # Initializing counts for page viewing
                curr_display = 1
                curr_max_display = ((count <= display) * count) + ((count > display) * display)
                curr_page = 1

                # max page is count's tens digit + 1
                max_page = (count//display) + (count%display != 0 * 1)

                while 1:
                    os.system("cls||clear")
                    print(f"\n ==== {difficulty.upper()} {topic.upper()} QUESTIONS MASTER LIST ====\n")
                    for i in range(curr_display,curr_max_display + 1): 
                        display_question(questions, str(i))
                    print(f"Page {curr_page} of {max_page}")

                    print("[1] Edit a question")
                    print("[2] Delete a question")
                    print("[3] View other questions")
                    print("[<] prev page              next page [>]")
                    print("[B] Go back to Menu")
                    choice = input("What would you like to do? ")
                    if choice == "B": 
                        return
                    # Delete or edit then rewrite file, then repopulate questions dictionary, then update count
                    elif choice == "1" or choice == "2":
                        if choice == "2" and count == 5:
                            print("Can not remove any more questions.")
                            time.sleep(1)
                            continue
                        d[choice](questions, curr_page, curr_display, curr_max_display, max_page, display, count)
                        
                        rewrite(questions,directory, choice)
                        populate_questions(questions, directory)


                        # If deleting a question, update display variables
                        # if collision with question display, move to previous image, and update max page
                        if choice == "2":
                            count = questions["C"]
                            if curr_page == max_page:
                                curr_max_display = count
                                if count % display == 0:
                                    curr_page, curr_display, curr_max_display = prev_page(curr_page, curr_display, curr_max_display, max_page, display, count)
                                    max_page = (count//display + (count%display != 0 * 1))

                        continue
                    elif choice == "3":
                        break
                    elif choice == "<":
                        curr_page, curr_display, curr_max_display = prev_page(curr_page, curr_display, curr_max_display, max_page, display, count)

                    elif choice == ">":
                        curr_page, curr_display, curr_max_display = next_page(curr_page, curr_display, curr_max_display, max_page, display, count)
                    else:
                        invalid()
                break

    # adds a question to your master list 
    def add_question() -> None:

        def ques(directory):
            while 1:
                os.system('cls||clear')
                choices = [0,0,0,0]
                question = input("Enter a question: ")

                for i in range(4):
                    choices[i] = input(f"Enter choice {itol(i+1)}: ")
                
                
                while 1:
                    os.system('cls||clear')
                    print(question)
                    print("Your choices are:")
                    print(f"A: {choices[0]}\t\t",end='')
                    print(f"C: {choices[2]}")
                    print(f"B: {choices[1]}\t\t",end='')
                    print(f"D: {choices[3]}\n")
                    right = input("Which choice is the correct answer? ").upper()
                    if right not in ["A", "B", "C", "D"]: 
                        invalid()
                        continue
                    break
                

                while 1:
                    os.system('cls||clear')
                    print(f"{question}")
                    print(f"A: {choices[0]}\t\t",end='')
                    print(f"C: {choices[2]}")
                    print(f"B: {choices[1]}\t\t",end='')
                    print(f"D: {choices[3]}\n")
                    print(f"Correct answer: {right}")
                    proceed = input("Is this correcct?[y/n] ").lower()
                    if proceed == "y":
                        break
                    elif proceed == "n":
                        return
                    else:
                        invalid()
                break

            questions = {}
            populate_questions(questions, directory)
            count = questions["C"] + 1
            questions[str(count)] = [question,choices[0],choices[1],choices[2],choices[3],right]
            print(questions)
            rewrite(questions, directory, "+")

            os.system("cls||clear")
            print("Successfully added to Question List!")
            time.sleep(0.5)
            return

        while 1:
            topic = category()
            if topic == "B":
                return
            elif topic == "final":
                difficulty = "final"
                break
            else:
                difficulty = diff()
                if difficulty == "B":
                    continue
                break

        while 1:
            directory = f"./questions/{topic}/{difficulty}.dat"
            file =  open(directory, "r")
            if file.readline()[2:-1] == "99":
                print(f"Too many questions in {difficulty} {topic} already!")
                time.sleep(1)
                break
            ques(directory)

            while 1:
                os.system("cls||clear")
                again = input("Would you like to add another question? [y/n] ").lower()
                if again == "y":
                    break
                elif again == "n":
                    file.close()
                    return
                else:
                    invalid()

    def change_pass(players: dict) -> None:
        os.system("cls||clear")
        new_pass = input("Enter new password: ")

        while 1:
            confirm = input(f"Change password?\nfrom: {players['admin']}\nTo: {new_pass}\n[y/n] ")
            if confirm == "y":
                players["admin"] = new_pass
                break
            elif confirm == "n":
                return
            else:
                invalid()
        rewrite_players(players)

    def remove_player(players:dict) -> None:
        while 1:
            os.system("cls||clear")
            for k,v in players.items():
                print(f"Username: {k}\nPassword: {v}\n")

            uname = input("[B] Go back\nWho do you want to remove? ")
            if uname in players.keys():
                confirm = input(f"Are you sure you want to remove player {uname}? [y/n] ")
                if confirm == "y":
                    players.pop(uname)
                    rewrite_players(players)
                    print(f"Successfully removed Player {uname}")
                    time.sleep(1)
                    break
                elif confirm == "n":
                    break
                else:
                    invalid()
            elif uname == "admin":
                print("Can't remove that.")
            elif uname == "B":
                break
            else:
                print("That person does not have an account.")
            time.sleep(1)

    def reset_leaderboard() -> None:
        while 1:
            os.system("cls||clear")
            confirm = input("Are you sure you want to reset the progress boards? [y/n] ")
            if confirm == "y":
                f1 = open("./leaderboard.dat", "w")
                f2 = open("./pbs.dat", "w")
                f1.close()
                f2.close()
                os.system("cls||clear")
                print("Leaderboard Cleared.")
                time.sleep(1)
                break
            elif confirm == "n":
                break
            else:
                invalid()
    
    def clear_player_list(players:dict) -> None:
        while 1:
            os.system("cls||clear")
            confirm = input("Are you sure you want to clear all players? [y/n] ")
            if confirm == "y":
                with open("./players.dat", "w") as file:
                    file.write(f"admin, {players['admin']}")

                os.system("cls||clear")
                print("Players Cleared.")
                time.sleep(1)
                break
            elif confirm == "n":
                break
            else:
                invalid()

    while 1:
        os.system("cls||clear")
        # populate players list wth players
        players = {}
        populate_players(players)
        print(players)

        controls = {
            "1" : lambda : add_question(),
            "2" : lambda : view_questions(),
            "3" : lambda : reset_leaderboard(),
            "4" : lambda : change_pass(players),
            "5" : lambda : remove_player(players),
            "6" : lambda : clear_player_list(players),
        }
        print("\n== ADMIN CONTROLS ==")
        print("[1] Add a question")
        print("[2] View questions")
        print("[3] Reset Leaderboard")
        print("[4] Change Password")
        print("[5] Remove a Player")
        print("[6] Clear Players")
        print("[B] Quit")

        choice = input("What would you like to do? ")
        if choice in controls.keys():
            controls[choice]()
        elif choice == "B":
            return
        else:
            invalid()

# Main
def main():
    while 1:
        mode = login_menu()
        time.sleep(1)
        if mode[0] == 1: 
            player_menu(mode[1])
        elif mode[0] == 2: 
            admin_menu()
    
if __name__ == "__main__":
    
    main()
    


# Maybe add user password simple cypher (Subsitute)
# Final question is mix of all questions 

# If person has won unlock a new mode, endless mode with its own leaderboard, endless leaderboard lang
# endless mode is just reapeated questions over and over until you lose or until you score 1584 T__T


