import menu
import hero
import pickle
import json
import gamesave


def gamemenu():
    print("Witaj w AzeRPG!")

    while anstrue:
        print("""
        1.Przejdź do głównego menu
        2.Stwórz postać
        3.Wczytaj grę
        4.Wyjdź z gry
            """)
        ans=input("Co zamierzasz zrobić?")
        if ans == "1":
            print("Witaj w głownym menu!")
            menu.mainmenu()
            exit()
        elif ans == "2":
            hero.chooseclass()
        elif ans == "3":
            gamesave.loaddata()
        elif ans == "4":
            print("See you soon!")
            exit()
anstrue=True
gamemenu()
