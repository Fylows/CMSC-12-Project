import os
import gen
import random
import time

def generate_question(directory: str) -> dict:
    file =  open(directory,"r")
    lines = file.readlines()[1:]
    file.close()

    questions = {}
    random.shuffle(lines)

    for i in range(6):
        temp = lines[i][:-1].split(",")
        questions[temp[0].replace("ඞ",",")] = [temp[1].replace("ඞ",","), temp[2].replace("ඞ",","), temp[3].replace("ඞ",","), temp[4].replace("ඞ",","), temp[5].replace("ඞ",",")]
    return questions
    
def question_user( k:str, v:list) -> None:
    question = f"""

    
~~~ Question: {str(k).rjust(3,'0')} ~~~

A: {v[0].ljust(65, ' ')}B: {v[1]}

C: {v[2].ljust(65, ' ')}D: {v[3]}
    """

    gen.line_print(question)

def category() -> str:
    d = {
    "1" : "lang_prof",
    "2" : "read_comp",
    "3" : "math",
    "4" : "sci",
    "5" : "gen_info",
}
    def choose() -> str:
        size = os.get_terminal_size().columns
        os.system('cls||clear')
        choose_categ = f"""


        Which Category?
        ====================================

        {'[1] Language Proficiency'.ljust(25, ' ')}
        {'[2] Reading Comprehension'.ljust(25, ' ')}
        {'[3] Mathematics'.ljust(25, ' ')}
        {'[4] Science'.ljust(25, ' ')}
        {'[5] General Knowledge'.ljust(25, ' ')}
        """
        gen.line_print(choose_categ)
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

