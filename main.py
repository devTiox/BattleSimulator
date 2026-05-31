# This is a sample Python script.
import TUI
import copy as cp

from TUI import choose_model


def start():
    #TUI input
    model = choose_model()
    print("Model chosen: ", model)
    if model == "Linear":
        frontline_size = int(input("Frontline size: "))

    army1 = TUI.input_army(model)
    army2 = TUI.input_army(model)

    #TEST input
    #army1 = Army(10000, Infantry("BPP", 1))
    #army2 = Army(12000,Infantry("BPP", 2))
    #frontline_size = 1000

    ##########################################
    army1.set_parameters(army2)
    army2.set_parameters(army1)
    ##########################################
    TUI.show_army(army1)
    TUI.show_army(army2)
    fight_duration = 0
    #turn_duration = 1 => 1 turn = 1 hour
    turn_duration = float(input("Turn length(0;1] 1 = 1 hour:"))
    turn_duration = max(turn_duration, 0.1)
    time = 0

    TUI.Storage.A1name = army1.units.name
    TUI.Storage.A2name = army2.units.name
    TUI.Storage.A1array.append(cp.deepcopy(army1))
    TUI.Storage.A2array.append(cp.deepcopy(army2))
    TUI.Storage.Time.append(cp.copy(time))

    while army2.current_size > 1 and army1.current_size > 1:
        display_time(fight_duration, time)
        if model == "Linear":
            army1.size_change(army2, frontline_size, turn_duration)
            army2.size_change(army1, frontline_size, turn_duration)
        else:
            a1_size = army1.current_size
            army1.size_change(army2, army2.current_size, turn_duration)
            army2.size_change(army1, a1_size, turn_duration)

        army1.morale_change(army2, fight_duration, turn_duration)
        army2.morale_change(army1, fight_duration, turn_duration)

        TUI.show_army(army1)
        TUI.show_army(army2)
        fight_duration+=1
        time += turn_duration
        TUI.Storage.Time.append(cp.copy(time))
        TUI.Storage.A1array.append(cp.deepcopy(army1))
        TUI.Storage.A2array.append(cp.deepcopy(army2))

    print("\n\n###########################################")
    TUI.plot_armies_stats()


def display_time(fight_duration, time):
    minutes = time*60
    hours = int(minutes/60)
    minutes = int(minutes%60)
    print("\nFight duration:\n-Turns:", fight_duration, "\n-Time:", hours, "h:", minutes,"m")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
