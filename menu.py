#menu pozwlające na wybór aktywności
from hero import heromenu
from inventory import inventorymenu
import json
from arena import arenamenu



def mainmenu():

    anstrue=True

    while anstrue:
        print("""
        1.Otwórz swój ekwipunek
        2.Udaj się na arenę
        3.Przejdź do statystyk swojej postaci
        4.Wyjdź z gry
            """)
        ans=input("Co zamierzasz zrobić?")
        if ans =="1":
            print("Witaj w swoim ekwipunku!")
            inventorymenu()

        elif ans =="2":
            print("Zmierzasz w kierunku areny...")
            arenamenu()
            exit()
        elif ans=="3":
            heromenu()
            exit()
        elif ans=="4":
            print("Do zobaczenia!")
            exit()
        else:
            print('Wybierz wartosc 1-4')

