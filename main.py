import random


pont = {'pc': 0, 'player': 0}
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
    """print("Vitórias")
    print(f"PC: {pont['pc']} - Player: {pont['player']}")"""
    print("="*24)
    hc = int(input("(1)Pedra, (2)Papel ou (3)Tesoura? - "));
    print("="*24)
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
        pont['player'] += 1
        print("Você ganhou!!!")

    elif status == "perdeu":
        pont['pc'] += 1
        print("Você perdeu!!")

    elif status == "empate":
        print("Meh... empate")

    print(f"{'='*30}\n Vitórias\nPC: {pont['pc']} - Player: {pont['player']}\n{'='*30}")
    
    print("="*24)
    