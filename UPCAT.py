import time
import os

import gen
import admin
import user

# Menus      
def login_menu() -> None:
    def main_menu(size:int) -> None:
        size = os.get_terminal_size().columns
        os.system('cls||clear')
        intro = """
        ╦ ╦╦ ╦╔═╗  ╦ ╦╔═╗╔╗╔╔╦╗╔═╗  ╔╦╗╔═╗  ╔═╗╔═╗╔═╗╔═╗  ╔╦╗╦ ╦╔═╗  ╦ ╦╔═╗╔═╗╔═╗╔╦╗
        ║║║╠═╣║ ║  ║║║╠═╣║║║ ║ ╚═╗   ║ ║ ║  ╠═╝╠═╣╚═╗╚═╗   ║ ╠═╣║╣   ║ ║╠═╝║  ╠═╣ ║ 
        ╚╩╝╩ ╩╚═╝  ╚╩╝╩ ╩╝╚╝ ╩ ╚═╝   ╩ ╚═╝  ╩  ╩ ╩╚═╝╚═╝   ╩ ╩ ╩╚═╝  ╚═╝╩  ╚═╝╩ ╩ ╩ 
        """
        print("\n\n")

        # splits intro into multiple lines and prints that
        gen.line_print(intro)
        print("\n")
        print("Welcome!".center(size))
        print("")
        print("[1] Login".center(size))
        print("[2] Register".center(size))
        print("")

    def login(size:int) -> str:
        players = {}
        menu_login = """
        LOGIN
        ====================================
        """

        gen.populate_players(players)

        while 1:
            os.system('cls||clear')
            print("\n\n")
            gen.line_print(menu_login)
            print("")
            usr = input("Enter your Username: ".center(size).rstrip() + " ").lower() 
            if usr in players.keys():
                pw = input("Enter your Password: ".center(size).rstrip() + " ").replace(",", "ඞ")
                if (usr,pw) in players.items():
                    return (usr)
            print("")
            print("Invalid login.".center(size))
            stop = input("Enter any key to try again or go back with [B] ".center(size).rstrip() + " ").upper()
            if stop == "B":
                return stop

    def register(size:int) -> None:
        directory = "./player_data/players.dat"
        file_append = open(directory, "a")
        file_read = open(directory, "r")
        
        # puts usernames in a list 
        users = [line.split(',')[0].lower() for line in file_read.readlines()]

        menu_register = """
        REGISTER
        ====================================
        """

        while 1:
            os.system('cls||clear')
            print("\n\n")
            gen.line_print(menu_register)
            print("")
            uname = input("Username: ".center(size).rstrip() + " ").lower()

            if uname in users:
                print("That user already exists! Please choose another.".center(size))
                time.sleep(1)
                os.system('cls||clear')
                continue
            elif len(uname) < 3:
                print("Username must be atleast 3 characters!".center(size))
                time.sleep(1)
                continue
            elif len(uname) > 11:
                print("Username must no more than 10 characters!".center(size))
                time.sleep(1)
                continue
            elif uname.isalnum() == False:
                print("Invalid characters.".center(size))
                time.sleep(1)
                continue
  
            pw = input("Password: ".center(size).rstrip() + " ").strip().replace(",", "ඞ")
            print("")
            confirm = input("Are these details correct? [y/n] ".center(size).rstrip() + " ").lower()
            if confirm == "y":
                # Append new user to the file
                break
            elif confirm == "n":
                return
            else:
                gen.invalid()
            
        # Exit the function after successful registration
        file_append.write(f"{uname},{pw}\n")
        print("Registration successful!".center(size))
        time.sleep(1)
        file_read.close()
        file_append.close()
        return
    
    # Main loop
    while 1:
        size = os.get_terminal_size().columns
        main_menu(size)
        choice = input("What would you like to do?".center(size).rstrip() + " ")
        if choice == "1":
            player = login(size)
            if player != "B":
                return player
        elif choice == "2":
            register(size)
        else:
            gen.invalid()

def player_menu(name: str) -> None:
    size = os.get_terminal_size().columns
    os.system("cls||clear")
    print("\n\n")
    print("Logging in".center(size).rstrip(),end='',flush=True)
    for i in range(3):
        time.sleep(0.5)
        print(".",end='',flush=True)
    time.sleep(0.5)
    os.system("cls||clear")
    print("\n\n")
    print(f"Hello {name.capitalize()}!".center(size))
    time.sleep(1)


    def play_game(uname:str, best_progress:dict, size:int) -> None:
 
        highscore = 00.00
        difficulties = ["easy","med","hard", "final"]

        # Loads your highscore if it exists
        if name in best_progress.keys():
            highscore = best_progress[name]
        i = 0
        points = 0
        time_limit = ((i == 0) * 15) + ((i == 1) * 10) + ((i == 2) * 10) + ((i == 3)*5)

        incorrect = {}
        wrong = 0

        # Variable initialization for lifelines
        skip = 1
        change = 1
        extra_time = 1

        while i < 4:
            if i == 3:
                cat = "final"
            else:
                cat = user.category()

            # ques is a dictionary containing 5 random questions
            ques = user.generate_question(f"./questions/{cat}/{difficulties[i]}.dat")
            os.system("cls||clear")
                

            top = (cat == "gen_info") * "General Information " + (cat == "final") * "Final " + (cat == "lang_prof") * "Language Proficiency " + (cat == "math") * "Mathematics " + (cat == "read_comp") * "Reading Comprehension " + (cat == "sci") * "Science "
            diff = (i == 0) * "Easy " + (i == 1) * "Medium " + (i == 2) * "Hard "
            print("\n\n")
            if i != 3:
                print(f"You are answering {diff}{top}Questions, Goodluck!".center(size))
            elif i == 3:
                print("Final Level, Good luck!".center(size))
            q = 5
            time.sleep(1)

            # 5 questions
            for k,v in ques.items():
                os.system("cls||clear")
                start = time.time()

                # ends current questions if q is 0
                if q == 0:
                    break

                # Answer validation
                while 1:
                    os.system("cls||clear")

                    user.question_user(k,v)
                    life_lines = (change == 1)*"[H] Change question" + (skip == 1)*" [S] Skip question" + (extra_time == 1)*" [T] Extra time" 
                    print(f"Life lines: {life_lines}".center(size))
                    print("")
                    answer = input("What is the answer? ".center(size).rstrip() + " ").upper()
                    elapsed = time.time() - start

                    # Extra life lifeline
                    if answer == "T" and extra_time == 1:
                        elapsed -= 20
                        extra_time = 0
                        print("+20 seconds!".center(size))
                        time.sleep(.5)

                    elif answer == "H" and change == 1:
                        q += 1
                        change = 0
                        break

                    elif answer == "S" and skip == 1:
                        points += 1
                        break

                    elif elapsed > time_limit: 
                        print("You took too long.".center(size))
                        points -= 0.25
                        time.sleep(1.25)
                        break

                    elif answer in ["A", "B", "C", "D"]:
                        if answer == v[4]:
                            time.sleep(.25)
                            points += 1                        
                        elif answer != v[4]:
                            v.insert(0,k)
                            wrong += 1
                            incorrect[str(wrong)] = (v)
                            time.sleep(.25)
                            points -= 0.25
                        break

                    else:
                        gen.invalid()
                q -= 1
                time.sleep(.25)

            # Next Level moves difficulty           
            if i != 3:
                os.system("cls||clear")
                print("\n\n")
                print("Congratulations You just moved up a level!".center(size))
                time.sleep(1)
                os.system("cls||clear")
            i+=1
        
        points = round((points/20) * 100, 2)

        # cap score range [0,100]
        points = max(0, min(100, points))
        os.system("cls||clear")
        print("\n\n")
        # If you complete the game or you have a new highscore or if you have a name not in your current pb
        if name not in best_progress.keys() or points > highscore:
            best_progress[name] = points
            # Updates scoreboard
            gen.update_scores(uname,points)
            
        if points > highscore and highscore != 100:
            if points == 100.00:
                print("Congratulations you have earned a crown and a spot in UPLB!".center(size))
            elif points > highscore:
                print(f"You have set a new personal best of {points}% completed!".center(size))
            time.sleep(2)
        
        # For those who have already Won
        if points < highscore:
            print(f"You achieved {points}% progress in this run! well done!".center(size))
        time.sleep(2)

        if len(incorrect) > 0:
            # How many questions to display
            display = 5

            # Initializing counts for page viewing
            curr_display = 1
            curr_max_display = ((wrong <= display) * wrong) + ((wrong > display) * display)
            curr_page = 1

            # max page is count's tens digit + 1
            max_page = (wrong//display) + (wrong%display != 0 * 1)
            
            while 1:
                os.system("cls||clear")
                print("============ INCORRECT ANSWERS ============\n".center(size))
                print("You got these questions wrong, make sure to review them.\n".center(size))
                for i in range(curr_display,curr_max_display + 1): 
                    admin.display_question(incorrect, str(i))
                print("")
                print(f"Page {curr_page} of {max_page}".center(size))
                print("[<] Previous Page            Next Page [>]".center(size))
                choice = input(": ".center(size).rstrip() + " ")
                if choice == "<":
                    curr_page, curr_display, curr_max_display = admin.prev_page(curr_page, curr_display, curr_max_display, max_page, display, wrong)
                elif choice == ">":
                    curr_page, curr_display, curr_max_display = admin.next_page(curr_page, curr_display, curr_max_display, max_page, display, wrong)
                else:
                    return

    def print_rules(size: int) -> None:
        rules_page1 = f"""

        ============ GAME RULES ============

        This is a quiz like game where you have to answer 20 questions in a row


        You are free to choose among the categories:
        {'- Language Proficiency'.ljust(25,' ')}
        {'- Reading Comprehension'.ljust(25,' ')}
        {'- Mathematics'.ljust(25,' ')}
        {'- Science'.ljust(25,' ')}
        {'- General Knowledge'.ljust(25,' ')}

            
        There will be a total of 4 rounds with increasing difficulty,
        {'- Easy 15 seconds to give an answer.'.ljust(50,' ')}
        {'- Medium and Hard 10 seconds to give an answer.'.ljust(50,' ')}
        {'- Final Round 5 seconds to give an answer.'.ljust(50,' ')}

            
        There will be 5 questions per round.
        You may answer with A, B, C, or D.


        You get a point for every questions you get right, 
        and every incorrect answer will equate to a 0.25 deduction


        Goodluck and have fun!

        """
        
        rules_page2 = """

        ============ LIFELINES ============

        [CHANGE QUESTION]
        -- 1 USAGE -- 

        You can change the current question with a for a new question from the same category.

        [EXTRA TIME]
        -- 1 USAGE -- 

        You are given an extra 15 seconds to give an answer.

        [SKIP]
        -- UNLIMITED USAGE --

        You can skip a question, but you get no points for that question.

        """


        shift = 1
        while 1:
            os.system("cls||clear")
            
            if shift == 1:
                gen.line_print(rules_page1)
            elif shift == 2:
                gen.line_print(rules_page2)
            print("")
            print(f"Page {shift} of 2".center(size))
            print("Press any key To Go back".center(size))
            print("[<] Previous Page            Next Page [>]".center(size))
            change = input(": ".center(size).rstrip() + " ")

            if change == "<" and shift > 1:
                shift -= 1
            elif change == ">" and shift < 2:
                shift += 1
            elif (change == ">" or change == "<") and (shift == 1 or shift == 2):
                os.system("clear||cls")
                print("No Page follows.".center(size))
                time.sleep(1)
            else:
                return
        print()

    def print_leaderboard(size:int) -> None:
        os.system("cls||clear")
        file = open("./player_data/scores.dat", "r")
        pairs = [pair[:-1].split(",") for pair in file.readlines()]
        high = [values for values in pairs if float(values[1]) != 100.00]

        print("\n\n")
        print("============ TOP 5 PLAYERS' PROGRESS ============\n".center(size))

        for i in range(5):
            if i < len(high):
                print(f"{i+1}. {high[i][0].capitalize().ljust(15)}{high[i][1].rjust(5)}%\n".center(size))
                continue
            
            print(f"{i+1}. {'N/A'.ljust(15)}{'00.00'.rjust(5)}%\n".center(size))
            

        input("Enter any key to go back".center(size).rstrip() + " ")

    def account_settings(old_name:str, best_scores:dict, size:int) -> tuple:
        players = {}
        gen.populate_players(players)

        while 1:
            os.system('cls||clear')
            print("\n\n")
            print("============ ACCOUNT SETTINGS ============".center(size))
            print("")
            print(f"{'[1] Change Username'.ljust(25)}".center(size))
            print(f"{'[2] Change Password'.ljust(25)}".center(size))
            print(f"{'[B] To Go Back'.ljust(25)}".center(size))
            print("")
            choice = input("What would you like to do?".center(size).rstrip() + " ")


            os.system('cls||clear')
            if choice == "1":
                print("\n\n")
                print("============ ACCOUNT SETTINGS ============".center(size))
                print("")
                uname = input("Enter your new username: ".center(size).rstrip() + " ").lower()
                if uname in players:
                    print("That name already exists!".center(size))
                    time.sleep(1)
                    continue
                elif len(uname) < 3:
                    print("Username must be atleast 3 characters!".center(size))
                    time.sleep(1)
                    continue
                elif len(uname) > 11:
                    print("Username must no more than 10 characters!".center(size))
                    time.sleep(1)
                    continue
                elif uname.isalnum() == False:
                    gen.invalid()
                    continue
                print("")
                print("Are you sure you want to change your name?".center(size))
                print(f"{f'From: {old_name}'.ljust(5)}".center(size))
                print(f"{f'To: {uname}'.ljust(5)}".center(size))

            elif choice == "2":
                print("\n\n")
                print("============ ACCOUNT SETTINGS ============".center(size))
                print("")
                pw = input("Enter your new password: ".center(size).rstrip() + " ").strip()
                
                print("")
                print(f"Are you sure you want to change your Password?".center(size))
                print(f"{f'From: {players[old_name].replace('ඞ',',')}'.ljust(5)}".center(size))
                print(f"{f'To: {pw}'.ljust(5)}".center(size))
                print("")
                if len(pw) == 0:
                    print("NOTE: Since nothing was entered, you will have no password!".center(size))
            elif choice.upper() == "B":
                return (0,0)
            else:
                gen.invalid()
                continue
            
            print("")
            confirm = input("[y/n] ".center(size).rstrip() + " ").lower()
            if confirm == "y":
                if choice == "1":
                    players[uname] = players[old_name]
                    del players[old_name]

                    if old_name in best_scores:
                        best_scores[uname] = best_scores[old_name]
                        del best_scores[old_name]
                        gen.rewrite_players(best_scores, "./player_data/scores.dat")
                        gen.update_scores(uname, best_scores[uname])

                    gen.rewrite_players(best_scores, "./player_data/players.dat")

                elif choice == "2":
                    uname = old_name
                    players[old_name] = pw.replace(",", "ඞ")
                
                gen.rewrite_players(players)

                print("Success!".center(size))
                time.sleep(1)
                return (choice, uname)
            
            elif confirm == "n":
                return "0"
            else:
                gen.invalid()
    
    def print_winners(size: int):
        os.system("cls||clear")
        print("\n\n")
        print("============ UPCAT Passers ============\n".center(size))
        with open("./player_data/scores.dat", "r") as file:
            count = 1
            for line in file:
                i = line[:-1].split(",")
                if float(i[1]) == 100.00:
                    print(f"{count}. {i[0]}".center(size))
                    count += 1
            print("")
            input("Enter any key to go back.\n".center(size).rstrip() + " ")

    while 1:
        os.system("cls||clear")
        
        main_menu = f"""
        ============ MAIN MENU ============

        {'[1] Play Game!'.ljust(25,' ')}
        {'[2] Game Rules?'.ljust(25,' ')}
        {'[3] Leaderboard'.ljust(25,' ')}
        {'[4] Hall of Passers'.ljust(25,' ')}
        {'[5] Account Settings'.ljust(25,' ')}
        {'[B] Exit'.ljust(25,' ')}
        """

        # Populate a dictionary w/ the scores of players
        bests = {}
        gen.populate_players(bests, "./player_data/scores.dat", "scores")

        print("\n\n")
        if name in bests:
            if bests[name] == 100.00:
                print("^-^ crowned passer".center(size))
            else:
                print(f"Your personal best progress is: {bests[name]}%".center(size))
        else:
            print("You have no previous progress.".center(size))

        options = {
            "1" : lambda : play_game(name, bests, size),
            "2" : lambda : print_rules(size),
            "3" : lambda : print_leaderboard(size),
            "4" : lambda : print_winners(size)
        }
        
        gen.line_print(main_menu)
        print("\n")
        choice = input("What would you like to do? ".center(size).rstrip() + " ")
        if choice in options.keys():
            options[choice]()
        elif choice == "5":
            temp = account_settings(name, bests, size)
            if temp[0] == "1":
                name = temp[1]
        elif choice.upper() == "B":
            return
        else:
            gen.invalid()

def admin_menu() -> None:
    size = os.get_terminal_size().columns
    os.system("cls||clear")
    print("\n\n")
    print("Logging in".center(size).rstrip(),end='',flush=True)
    for i in range(3):
        time.sleep(0.5)
        print(".",end='',flush=True)
    time.sleep(0.5)

    os.system("cls||clear")
    print("\n\n")
    print("Hello admin!".center(size))
    time.sleep(1)

    # View questions prints all questions from a category and difficulty
    # Page by page view 
    def view_questions(size:int) -> None:
        d = {
            "1" : lambda q, cp, cd, cmd, mp, d, c : admin.edit_question(q, cp, cd, cmd, mp, d, c),
            "2" : lambda q, cp, cd, cmd, mp, d, c : admin.delete_question(q, cp, cd, cmd, mp, d, c)
        }
        while 1:
            topic = admin.category(size)
            if topic == "B":
                return
            elif topic == "final":
                difficulty = "final"
            else:
                difficulty = admin.diff(size)
                if difficulty == "B":
                    continue

            
            while 1:
                directory = f"./questions/{topic}/{difficulty}.dat"
                # Populate questions array with questions and count of questions
                questions = {}
                admin.populate_questions(questions, directory)

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
                    diff = (difficulty == "easy") * "easy " + (difficulty == "med") * "medium " + (difficulty == "hard") * "hard " + (difficulty == "final") * ""

                    top = (topic == "gen_info") * "General Information " + (topic == "final") * "Final " + (topic == "lang_prof") * "Language Proficiency " + (topic == "math") * "Mathematics " + (topic == "read_comp") * "Reading Comprehension " + (topic == "sci") * "Science "
                    
                    print("\n\n")
                    print(f"============ {diff.upper()}{top.upper()}QUESTIONS MASTER LIST ============".center(size))
                    print("")
                    for i in range(curr_display,curr_max_display + 1): 
                        admin.display_question(questions, str(i))

                    print("")
                    print(f"Page {curr_page} of {max_page}".center(size))
                    print("")
                    print("[1] Edit a question".center(size))
                    print("[2] Delete a question".center(size))
                    print("[3] View other questions".center(size))
                    print("[<] Previous Page            Next Page [>]".center(size))
                    print("[B] Go back to Menu".center(size))

                    choice = input(": ".center(size).rstrip() + " ")
                    if choice == "B": 
                        return
                    # Delete or edit then rewrite file, then repopulate questions dictionary, then update count
                    elif choice == "1" or choice == "2":
                        if choice == "2" and count == 5:
                            print("Can not remove any more questions.".center(size))
                            time.sleep(1)
                            continue
                        
                        d[choice](questions, curr_page, curr_display, curr_max_display, max_page, display, count)
                        
                        admin.rewrite(questions,directory, choice)
                        admin.populate_questions(questions, directory)


                        # If deleting a question, update display variables
                        # if collision with question display, move to previous image, and update max page
                        if choice == "2":
                            count = questions["C"]
                            if curr_page == max_page:
                                curr_max_display = count
                                if count % display == 0:
                                    curr_page, curr_display, curr_max_display = admin.prev_page(curr_page, curr_display, curr_max_display, max_page, display, count)
                                    max_page = (count//display + (count%display != 0 * 1))

                        continue
                    elif choice == "3":
                        break
                    elif choice == "<":
                        curr_page, curr_display, curr_max_display = admin.prev_page(curr_page, curr_display, curr_max_display, max_page, display, count)
                    elif choice == ">":
                        curr_page, curr_display, curr_max_display = admin.next_page(curr_page, curr_display, curr_max_display, max_page, display, count)
                    else:
                        gen.invalid()
                break

    # adds a question to your master list 
    def add_question(size:int) -> None:

        def ques(directory):
            while 1:
                os.system('cls||clear')
                print("\n\n")
                choices = [0,0,0,0]
                print("============ ADD QUESTION ============".center(size))
                print("")
                question = input("Enter a question: ".center(size).rstrip() + " ").strip()

                for i in range(4):
                    choices[i] = input(f"Enter choice {admin.itol(i+1)}: ".center(size).rstrip() + " ").strip()
                
                
                while 1:
                    os.system('cls||clear')
                    print("\n\n")
                    print("============ ADD QUESTION ============".center(size))
                    print("")
                    question_inc = f"""
~~~ Question: {question} ~~~

A: {choices[0].ljust(65, ' ')}B: {choices[1]}

C: {choices[2].ljust(65, ' ')}D: {choices[3]}
                    """
                    gen.line_print(question_inc)
                    right = input("Which choice is the correct answer? ".center(size).rstrip() + " ").upper()
                    if right not in ["A", "B", "C", "D"]: 
                        gen.invalid()
                        continue
                    break
                

                while 1:
                    os.system('cls||clear')
                    print("\n\n")
                    print("============ ADD QUESTION ============".center(size))
                    print("")
                    question_complete = f"""
~~~ Question: {question} ~~~

A: {choices[0].ljust(65, ' ')}B: {choices[1]}

C: {choices[2].ljust(65, ' ')}D: {choices[3]}

Correct answer: {right}
                    """

                    gen.line_print(question_complete)
                    print("")
                    proceed = input("Is this correcct? [y/n] ".center(size).rstrip() + " ").lower()
                    if proceed == "y":
                        break
                    elif proceed == "n":
                        return
                    else:
                        gen.invalid()
                break
            

            questions = {}
            admin.populate_questions(questions, directory)
            count = questions["C"] + 1
            # Question isnt the key to match with how the edit function rewrites
            questions[str(count)] = [question,choices[0],choices[1],choices[2],choices[3],right]
            time.sleep(3)
            admin.rewrite(questions, directory, "+")

            os.system("cls||clear")
            print("\n\n")
            print("============ ADD QUESTION ============".center(size))
            print("")
            print("Successfully added to Question List!".center(size))
            time.sleep(0.5)
            return

        while 1:
            topic = admin.category(size)
            if topic == "B":
                return
            elif topic == "final":
                difficulty = "final"
                break
            else:
                difficulty = admin.diff(size)
                if difficulty == "B":
                    continue
                break

        while 1:
            directory = f"./questions/{topic}/{difficulty}.dat"
            file =  open(directory, "r")
            if file.readline()[2:-1] == "99":
                print(f"Too many questions in there already!".center(size))
                time.sleep(1)
                break
            ques(directory)

            while 1:
                os.system("cls||clear")
                print("\n\n")
                print("============ ADD QUESTION ============".center(size))
                print("")
                again = input("Would you like to add another question? [y/n] ".center(size).rstrip() + " ").lower()
                if again == "y":
                    break
                elif again == "n":
                    file.close()
                    return
                else:
                    gen.invalid()

    def change_pass(players: dict, size:int) -> None:
        os.system("cls||clear")
        print("\n\n")
        print("============ PASSWORD CHANGE ============".center(size))
        print("")
        new_pass = input("Enter new password: ".center(size).rstrip() + " ")

        while 1:
            print("")
            print(f"Are you sure you want to change your Password?".center(size))
            print(f"{f'From: {players['admin'].replace('ඞ',',')}'.ljust(5)}".center(size))
            print(f"{f'To: {new_pass}'.ljust(5)}".center(size))
            print("")
            confirm = input("[y/n] ".center(size).rstrip() + " ")
            if confirm == "y":
                players["admin"] = new_pass.replace(",","ඞ")
                break
            elif confirm == "n":
                return
            else:
                gen.invalid()
        gen.rewrite_players(players)

    def remove_player(players:dict, size:int) -> None:
        highscore = {}
        gen.populate_players(highscore, "./player_data/scores.dat")
        while 1:
            os.system("cls||clear")
            print("\n\n")
            print("============ REMOVE PLAYER ============".center(size))
            print("")
            for k,v in players.items():
                print(f"Username: {k.capitalize()}".center(size))
                print(f"Password: {v.replace('ඞ',',')}".center(size))
                print("")
            print("[B] Go back".center(size))
            uname = input("Who do you want to remove? ".center(size).rstrip() + " ").lower()
            if uname == "admin":
                print("Can't remove that.".center(size))
            elif uname == "b":
                break
            elif uname in players.keys():
                confirm = input(f"Are you sure you want to remove player {uname}? [y/n] ".center(size).rstrip() + " ").lower()
                if confirm == "y":
                    del players[uname]
                    if uname in highscore.keys():
                        del highscore[uname]
                        gen.rewrite_players(highscore, "./player_data/scores.dat")
                    gen.rewrite_players(players)
                    print(f"Successfully removed Player {uname}".center(size))
                    time.sleep(1)
                    break
                elif confirm == "n":
                    break
                else:
                    gen.invalid()
            else:
                print("That person does not have an account.".center(size))
            time.sleep(1)

    def reset_leaderboard(size:int) -> None:
        while 1:
            os.system("cls||clear")
            print("\n\n")
            confirm = input("Are you sure you want to reset the progress boards? [y/n] ".center(size).rstrip() + " ")
            if confirm == "y":
                f1 = open("./player_data/scores.dat", "w")
                f1.close()
                os.system("cls||clear")
                print("Leaderboard Cleared.".center(size))
                time.sleep(1)
                break
            elif confirm == "n":
                break
            else:
                gen.invalid()
    
    def clear_player_list(players:dict, size:int) -> None:
        while 1:
            os.system("cls||clear")
            print("\n\n")
            confirm = input("Are you sure you want to remove all players? [y/n] ".center(size).rstrip() + " ")
            if confirm == "y":
                with open("./player_data/players.dat", "w") as file:
                    file.write(f"admin,{players['admin']}\n")
                f1 = open("./player_data/scores.dat", "w")
                f1.close()
                os.system("cls||clear")
                print("Players and leaderboards Cleared.".center(size))
                time.sleep(1)
                break
            elif confirm == "n":
                break
            else:
                gen.invalid()

    while 1:
        os.system("cls||clear")
        # populate players list wth players
        players = {}
        gen.populate_players(players)

        controls = {
            "1" : lambda : add_question(size),
            "2" : lambda : view_questions(size),
            "3" : lambda : reset_leaderboard(size),
            "4" : lambda : change_pass(players,size),
            "5" : lambda : remove_player(players,size),
            "6" : lambda : clear_player_list(players,size),
        }
        print("\n\n")
        menu_admin = f"""
        ============ ADMIN CONTROLS ============

        {'[1] Add a Question'.ljust(25,' ')}
        {'[2] View Questions'.ljust(25,' ')}
        {'[3] Reset Leaderboards'.ljust(25,' ')}
        {'[4] Change Password'.ljust(25,' ')}
        {'[5] Remove a Player'.ljust(25,' ')}
        {'[6] Remove all Players'.ljust(25,' ')}
        {'[B] Exit'.ljust(25,' ')}

        """
        gen.line_print(menu_admin)
        choice = input("What would you like to do? ".center(size).rstrip() + " ")
        if choice in controls.keys():
            controls[choice]()
        elif choice == "B":
            return
        else:
            gen.invalid()

# Main
def main():
    while 1:
        user = login_menu()
        time.sleep(1)
        if user == "admin": 
            admin_menu()
        elif user != "B":
            player_menu(user)

if __name__ == "__main__":
	main()
