import os
import time
import gen

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
        elif curr_page == max_page and count % display != 0:
            curr_max_display -= count % display

        else:
            curr_max_display -= display


        curr_page -= 1
        curr_display -= display
        return curr_page, curr_display, curr_max_display

# Simple function (int to letter) that assigns 1,2,3,4 to A,B,C,D respectively
def itol(n:int) -> str:
    d = {
        1 : "A",
        2 : "B",
        3 : "C",
        4 : "D",
    }
    return d[n]

# Function that returns the category defined by admin
def category(size) -> str:
    d = {
        "1" : "lang_prof",
        "2" : "read_comp",
        "3" : "math",
        "4" : "sci",
        "5" : "gen_info",
        "6" : "final",
        "B" : "B",
    }

    while 1:
        os.system('cls||clear')
        choose_categ = f"""

        
        Which Category?
        ====================================

        {'[1] Language Proficiency'.ljust(25, ' ')}
        {'[2] Reading Comprehension'.ljust(25, ' ')}
        {'[3] Mathematics'.ljust(25, ' ')}
        {'[4] Science'.ljust(25, ' ')}
        {'[5] General Knowledge'.ljust(25, ' ')}
        {'[6] Final Round Questions'.ljust(25, ' ')}
        {'[B] Back to Main Menu'.ljust(25, ' ')}

        """
        gen.line_print(choose_categ)
        ans = input("Enter your choice: ".center(size).rstrip() + " ")
        if (ans not in d.keys()):
            gen.invalid()
            continue
        break
    return d[ans]

# Function that returns the difficulty defined by admin
def diff(size:int) -> str:

    d = {
        "1" : "easy",
        "2" : "med",
        "3" : "hard",
        "B" : "B",
    }
    def choose():

        difficulty = f"""

        What Difficulty?
        ====================================

        {'[1] Easy'.ljust(25, ' ')}
        {'[2] Medium'.ljust(25, ' ')}
        {'[3] Hard'.ljust(25, ' ')}
        {'[B] Back to Category'.ljust(25, ' ')}

        """
        gen.line_print(difficulty)
        ans = input("Enter your choice: ".center(size).rstrip() + " ")
        return ans

    while 1:
        os.system('cls||clear')
        ans = choose()
        if (ans not in d.keys()):
            gen.invalid()
            continue
        break
    return d[ans]

def display_question(questions: dict, k:any) -> None:
    if k == "C":
        return
    question = f"""
~~~ Question {str(k).rjust(3,'0')} ~~~

{questions[k][0].replace('ඞ',',')}

A: {questions[k][1].replace("ඞ",",").ljust(65, ' ')}B: {questions[k][2].replace("ඞ",",")}

C: {questions[k][3].replace("ඞ",",").ljust(65, ' ')}D: {questions[k][4].replace("ඞ",",")}

Correct answer: {(questions[k][5])}
"""
    gen.line_print(question)
    return

def populate_questions(myDict:dict, directory: str) -> None:
    file = open(directory,"r")
    i = 1
    for line in file:
        if line[0:2] == "C ":
            myDict["C"] = int(line[2:-1])
            continue
        myDict[str(i)] = line[:-1].split(",")
        i += 1

def edit_question(questions: dict, curr_page:int, curr_display:int, curr_max_display:int, max_page:int, display:int, count:int) -> None:
    def edit(questions:dict, key:int, size:int):
        while 1:
            os.system("cls||clear")
            print("\n\n")
            print(f"============ EDIT QUESTION ============".center(size))
            print("")
            display_question(questions, key)
            print("")
            print("[1] Question".center(size))
            print("[2] Choices".center(size))
            print("[3] Answer".center(size))
            print("[0] Save question".center(size))
            print("[X] Discard Changes".center(size))

            copy = [questions,key]
            option = input("What do you want to edit? ".center(size).rstrip() + " ")
            if option == "1":
                print("")
                new_question = input("Enter new Question: ".center(size).rstrip() + " ").replace(",","ඞ")
                questions[key][0] = new_question
            elif option == "2":
                for i in range(1,5):
                    print("")
                    questions[key][i] = input(f"Enter new choice {itol(i)}: ".center(size).rstrip() + " ")
            elif option == "3":
                print("")
                new_ans = input("Enter new answer: ".center(size).rstrip() + " ").upper()
                if new_ans not in ["A", "B", "C", "D"]:
                    gen.invalid()
                    continue
                questions[key][5] = new_ans
            elif option == "0":
                return "0"
            elif option.upper() == "X":
                return "X"
            else:
                gen.invalid()

    while 1:
        os.system('cls||clear')
        size = os.get_terminal_size().columns
        print("\n\n")
        print(f"============ EDIT QUESTION ============".center(size))
        print("")
        for i in range(curr_display,curr_max_display + 1): 
            display_question(questions, str(i))
        print("")
        print(f"Page {curr_page} of {max_page}".center(size))
        print("[<] Previous Page            Next Page [>]".center(size))
        print("[B] Back".center(size))
        print("")
        choice = input("Which question do you want to edit? ".center(size).rstrip() + " ").lstrip('0')

        if choice in questions.keys():
            while 1:
                os.system('cls||clear')
                print("\n\n")
                print(f"============ EDIT QUESTION ============".center(size))
                print("")
                display_question(questions, choice)
                confirm = input("Are you sure you want to edit this question? [y/n] ".center(size).rstrip() + " ").lower()
                if confirm == "y":
                    edit(questions, choice, size)
                    return
                elif confirm == "n":
                    break
                else: 
                    gen.invalid()    
        elif choice == "<":
            curr_page, curr_display, curr_max_display = prev_page(curr_page, curr_display, curr_max_display, max_page, display, count)
        elif choice == ">":
            curr_page, curr_display, curr_max_display = next_page(curr_page, curr_display, curr_max_display, max_page, display, count)   
        elif choice == "B":
            break
        else: 
            gen.invalid()

    return

def delete_question(questions: dict, curr_page:int, curr_display:int, curr_max_display:int, max_page:int, display:int, count:int) -> None:
    while 1:
        size = os.get_terminal_size().columns
        os.system('cls||clear')
        print("\n\n")
        print(f"============ DELETE QUESTION ============".center(size))
        print("")
        for i in range(curr_display,curr_max_display + 1): 
            display_question(questions, str(i))
        print("")
        print(f"Page {curr_page} of {max_page}".center(size))
        print("[<] Previous Page            Next Page [>]".center(size))
        print("[B] Back ".center(size))
        print("")
        choice = input("Which question do you want to delete? ".center(size).rstrip() + " ").lstrip('0')

        if choice in questions.keys():
            while 1:
                os.system('cls||clear')
                print("\n\n")
                print(f"============ EDIT QUESTION ============".center(size))
                print("")
                display_question(questions, choice)
                print("")
                confirm = input("Are you SURE you want to delete this question? [y/n] ".center(size).rstrip() + " ").lower()
                if confirm == "y":
                    del questions[choice]
                    return
                elif confirm == "n":
                    break
                else: 
                    gen.invalid()   
        elif choice == "<":
                    curr_page, curr_display, curr_max_display = prev_page(curr_page, curr_display, curr_max_display, max_page, display, count)
        elif choice == ">":
            curr_page, curr_display, curr_max_display = next_page(curr_page, curr_display, curr_max_display, max_page, display, count)   
        elif choice == "B":
            break
        else: 
            gen.invalid()
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
        file.write(f"{myDict[k][0].replace(',','ඞ')},{myDict[k][1].replace(',','ඞ')},{myDict[k][2].replace(',','ඞ')},{myDict[k][3].replace(',','ඞ')},{myDict[k][4].replace(',','ඞ')},{myDict[k][5]}\n")
    file.close()