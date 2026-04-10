# This is a sample Python script.
from asyncio import wait


from army import Army

from units import Cavalry, Infantry

import questionary


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def input_army():
    unit_classes = {
        "Cavalry": Cavalry,
        "Infantry": Infantry
    }

    choice = questionary.select(
        "Wybierz jednostkę:",
        choices=list(unit_classes.keys())
    ).ask()

    unit_class = unit_classes[choice]  # teraz to jest klasa

    name = input("Nazwa armii: ")
    size = int(input("Rozmiar armii: "))
    experience = int(input("Doświadczenie jednostek[1,5]: "))

    army = Army(size, unit_class(name), experience)  # wywołanie konstruktora klasy

    return army

def start(frontline_size):
    # Use a breakpoint i the code line below to debug your script.
    #print("Konfiguracja pierwszej armii:")
    #army1 = input_army()
    army1 = Army(10000, Infantry("BPP"), 3)
    #print("Konfiguracja drugiej armii:")
    #army2 = input_army()
    army2 = Army(12000,Infantry("BPP"), 2)
    ##########################################
    army1.set_parameters(army2)
    army2.set_parameters(army1)
    ##########################################
    army1.show_army()
    army2.show_army()
    fight_duration = 0
    #turn_duration = 1 => 1 turn = 1 hour
    turn_duration = float(input("Wybierz długość tury(0;1] 1 = godzina:"))
    turn_duration = max(turn_duration, 0.1)
    time = 0

    while army2.current_size > 1 and army1.current_size > 1:
        display_time(fight_duration, time)
        army1.size_change(army2, frontline_size, turn_duration)
        army2.size_change(army1, frontline_size, turn_duration)

        army1.morale_change(army2, fight_duration, turn_duration)
        army2.morale_change(army1, fight_duration, turn_duration)

        army1.show_army()
        army2.show_army()

        fight_duration+=1
        time += turn_duration


def display_time(fight_duration, time):
    minutes = time*60
    hours = int(minutes/60)
    minutes = int(minutes%60)
    print("\nFight duration:\n-Turns:", fight_duration, "\n-Time:", hours, "h:", minutes,"m")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start(500)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
