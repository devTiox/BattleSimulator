from army import Army
from units import *
import os

import questionary

os.environ.setdefault("MPLCONFIGDIR", os.path.join(os.path.dirname(__file__), ".matplotlib"))
import matplotlib

matplotlib.use("qtagg")
import matplotlib.pyplot as plt

def show_army(army):
    print("Unit:")
    army.units.show_unit()
    print("Size:", army.current_size,
          "\nTotal Loss:", army.total_loss, "\tTurn Loss:", army.turn_loss,
          "\nTotal desertion:", army.total_desertion, "\tTurn Desertion", army.turn_desertion,
          "\nMorale:", army.morale, "\tEfficiency:", army.efficiency, "\tCombat tiredness", army.tiredness)
    print("###########################################")
    if (army.routed == True):
        print("Army ", army.units.name, " collapsed at:", army.collapse_desertion, "units")


def show_army_basic(army):
    print("Size:", army.current_size,
          "\nTotal Loss:", army.total_loss, "\tTurn Loss:", army.turn_loss,
          "\tMorale:", army.morale, "\tEfficiency:", army.efficiency)
    print("###########################################")

def input_army():
    print("Konfiguracja armii:")

    unit_classes = {
        "Infantry": Infantry,
        "Knights": Knights,
        "Cavalry": Cavalry,
        "Hussars":  Hussars,
        "Kapitan Bomba": Kapitan_Bomba
    }

    choice = questionary.select(
        "Wybierz jednostkę:",
        choices=list(unit_classes.keys())
    ).ask()

    unit_class = unit_classes[choice]  # teraz to jest klasa

    name = input("Nazwa armii: ")
    size = int(input("Rozmiar armii: "))
    experience = int(input("Doświadczenie jednostek[1,5]: "))

    army = Army(size, unit_class(name, experience))  # wywołanie konstruktora klasy

    return army

import matplotlib.pyplot as plt
import math


def plot_armies_stats():
    time = Storage.Time

    stats = [
        ("current_size", "Size"),
        ("total_desertion", "Total desertion"),
        ("turn_loss", "Turn Loss"),
        ("morale", "Morale"),
        ("efficiency", "Efficiency")
    ]

    # max 2 wykresy na figurę
    plots_per_figure = 2

    for i in range(0, len(stats), plots_per_figure):

        current_stats = stats[i:i + plots_per_figure]

        fig, axes = plt.subplots(
            len(current_stats),
            1,
            figsize=(12, 8)
        )

        # gdy jest tylko 1 subplot
        if len(current_stats) == 1:
            axes = [axes]

        for ax, (field, title) in zip(axes, current_stats):

            army1_values = [
                getattr(a, field)
                for a in Storage.A1array
            ]

            army2_values = [
                getattr(a, field)
                for a in Storage.A2array
            ]

            ax.plot(time, army1_values, label="Army 1")
            ax.plot(time, army2_values, label="Army 2")

            ax.set_title(title)

            ax.set_xlabel("Time")
            ax.set_ylabel(title)

            ax.grid(True)
            ax.legend()

        plt.tight_layout()

    plt.show()

class Storage:
    A1array = []
    A2array = []
    Time = []

    @staticmethod
    def print_arrays():
        print("Array1:")
        for x in Storage.A1array:
            show_army_basic(x)

        print("Array2")
        for x in Storage.A2array:
            show_army_basic(x)
