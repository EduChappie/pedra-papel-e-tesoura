'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import random

answer = str(input("Let's play a game? (y/n)"));
if answer == "y":
    game = bool(True)
elif answer == "n":
    game = bool(False)
    exit()
    
def escoia(num):
    """ Função para resultado final, saber qual foi jogado """
    if num == 1:
        return "Pedra"
    elif num == 2:
        return "Papel"
    elif num == 3:
        return "Tesoura"
    else:
        return "tem algo errado Berg"


while game:
    print("=========")
    hc = int(input("(1)Pedra, (2)Papel ou (3)Tesoura? - "));
    print("=========")
    hp = int(random.uniform(1,4));
    
    # Decisão do game
    if hc == 1 and hp == 3 or hc == 2 and hp == 1 or hc == 3 and hp == 2:
        status = "ganhou"
        
    elif hc == 1 and hp == 2 or hc == 2 and hp == 3 or hc == 3 and hp == 1:
        status = "perdeu"
        
    else:
        status = "empate"
    
    print("Você: {}".format(escoia(hc)));
    print("PC: {}".format(escoia(hp)));
    
    if status == "ganhou":
        print("Você ganhou!!!")
    elif status == "perdeu":
        print("Você perdeu!!")
    elif status == "empate":
        print("Meh... empate")
    
    print("======================")
    