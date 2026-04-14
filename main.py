# This is a sample Python script.
from army import Army
import TUI
from units import *
import copy as cp


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def start():
    # Use a breakpoint i the code line below to debug your script.
    #TUI input
    #frontline_size = int(input("Długość lini starcia: "))

    #army1 = TUI.input_army()
    #army2 = TUI.input_army()

    #TEST input
    army1 = Army(10000, Infantry("BPP", 1))
    army2 = Army(12000,Infantry("BPP", 2))
    frontline_size = 1000

    ##########################################
    army1.set_parameters(army2)
    army2.set_parameters(army1)
    ##########################################
    TUI.show_army(army1)
    TUI.show_army(army2)
    fight_duration = 0
    #turn_duration = 1 => 1 turn = 1 hour
    turn_duration = float(input("Wybierz długość tury(0;1] 1 = godzina:"))
    turn_duration = max(turn_duration, 0.1)
    time = 0

    TUI.Storage.A1array.append(cp.deepcopy(army1))
    TUI.Storage.A2array.append(cp.deepcopy(army2))

    while army2.current_size > 1 and army1.current_size > 1:
        display_time(fight_duration, time)
        army1.size_change(army2, frontline_size, turn_duration)
        army2.size_change(army1, frontline_size, turn_duration)

        army1.morale_change(army2, fight_duration, turn_duration)
        army2.morale_change(army1, fight_duration, turn_duration)

        TUI.show_army(army1)
        TUI.show_army(army2)

        TUI.Storage.A1array.append(cp.deepcopy(army1))
        TUI.Storage.A2array.append(cp.deepcopy(army2))

        fight_duration+=1
        time += turn_duration

    print("\n\n###########################################")
    print("Arrays:")
    TUI.Storage.print_arrays()


def display_time(fight_duration, time):
    minutes = time*60
    hours = int(minutes/60)
    minutes = int(minutes%60)
    print("\nFight duration:\n-Turns:", fight_duration, "\n-Time:", hours, "h:", minutes,"m")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
