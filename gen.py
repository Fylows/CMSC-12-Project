import os
import time

# Simple invalid display
def invalid() -> None:
    os.system("cls||clear")
    print("\n\n\n\n")
    print("Invalid Try again.".center(os.get_terminal_size().columns))
    time.sleep(1)

# Function for modifying leaderboard
# Stores name,score in a dictionary then sorts it then saves it
def update_scores(uname:str, score:float) -> None:
	myDict = {}
	gen.populate_players(myDict, "./player_data/scores.dat", "scores")
    
	if uname not in myDict.keys() or (uname in myDict.keys() and score >= myDict[uname]):
		myDict[uname] = score

	myDict = dict(sorted(myDict.items(), reverse = True, key = lambda x : x[1]))
	Writefile = open("./player_data/scores.dat", "w")
	for k,v in myDict.items():
		Writefile.write(f"{k},{v}\n")
	Writefile.close()

def user_reg(myList:list, size:int, reg_menu:str) -> str:
    while 1:
        os.system("cls||clear")
        print(reg_menu)
        print("")
        print("Username: ".center(size).rstrip(), end= '')
        usr = input(" ").lower()

        if usr in myList:
            print("That user already exists! Please choose another.".center(size))
            time.sleep(1)
            os.system('cls||clear')
            continue
        elif len(usr) < 3:
            print("Username must be atleast 3 characters!".center(size))
            time.sleep(1)
            continue
        elif len(usr) > 11:
            print("Username must no more than 10 characters!".center(size))
            time.sleep(1)
            continue
        elif usr.isalnum() == False:
            invalid()
            continue
        break    
    return usr         

def populate_players(myDict:dict, directory:str = "./player_data/players.dat", mode:str = "any") -> None:
    Readfile = open(directory, "r")

    if mode == "scores":
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

def rewrite_players(myDict:dict, directory:str = "./player_data/players.dat") -> None:
    Writefile = open(directory, "w")
    for k, v in myDict.items():
        Writefile.write(f"{k},{v}\n")
    Writefile.close()

def line_print(string:str):
    size = os.get_terminal_size().columns
    print("\n".join(line.center(size) for line in string.splitlines()))
