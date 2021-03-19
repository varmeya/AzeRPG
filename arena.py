import menu
import hero
import inventory
import gamesave
import json
import random
import hero

def arenamenu():
    with open("save.json", "r") as save:
        json.load(save)
    print(f"Witaj na arenie,  {hero.yourhero}")
    print("Wybierz przeciwnika z którym będziesz walczyć:")
    anstrue = True
    while anstrue:
        print("""
            1. Poziom 1 : Kretoszczur
            2. Poziom 5 : Wilk
            3. Poziom 10 : Bandyta
            4. Wróć do menu
            """)
        enemy = input()
        if enemy == "1":
            print("Stajesz naprzeciw Kretoszczura. Potwór zgrzyta zębami i szykuje się do ataku. Co robisz?")
            combat()
        elif enemy == "2":
            print("Wilk wyje na twój widok i zanim się obejrzałeś, atakuje. Co robisz?")
            combat()
        elif enemy == "3":
            print("Bandyta opiera swój miecz na ramieniu i uśmiecha się w Twoją stronę kpiąco. Jaki jest Twój ruch?")
            combat()
        elif enemy == "4":
            print("Wracasz do menu")
            menu.mainmenu()
            exit()
        else:
            print('Wybierz wartosc 1-4')

def combat():

    print("""
            1. Atakuj
            2. Zrób unik
            3. Uciekaj
    """)
    move = input()
    if move == "1":
        random
        if enemyhealth >= 0:
            print("Udało Ci się pokonać przeciwnika!")
    elif move == "2":
        random
    elif move == "3":
        random.randint(0, 5)
        if random.randint(0,5) >= 3:
            print("Udało Ci się uciec!Wracasz przed wrota areny.")
            arenamenu()
