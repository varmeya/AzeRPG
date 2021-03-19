import hero
import json

def loaddata():
    with open("save.json", "r") as save:
        data = json.loads(save.read())
        hero.yourhero = str(data['Name'])
        print(f"Wczytano bohatera: {data['Name']}")
        if int(data['Class']) == 1:
            chooseclassB = hero.warriorbasestats()
        else:
            chooseclassB = hero.magebasestats()
        hero.heromenu(data['Class'],chooseclassB)