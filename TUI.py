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
    if army.routed:
        print("Army ", army.units.name, " collapsed at:", army.collapse_desertion, "units")

def show_army_basic(army):
    print("Size:", army.current_size,
          "\nTotal Loss:", army.total_loss, "\tTurn Loss:", army.turn_loss,
          "\tMorale:", army.morale, "\tEfficiency:", army.efficiency)
    print("###########################################")

def choose_model():
    models_list = ["Linear", "Quadratic"]
    choice = questionary.select(
        "Choose model:",
        choices=list(models_list)
    ).ask()

    return choice


def input_army(model):
    print("Army configuration:")
    if model == "Linear":
       unit_classes = {
            "Infantry": Infantry,
            "Knights": Knights,
            "Cavalry": Cavalry,
            "Hussars":  Hussars,
            "Kapitan Bomba": KapitanBomba
        }
    else:
        unit_classes = {
            "Slingers": Slingers,
            "Archers": Archers,
            "Crossbowmen": Crossbowmen,
            "Musketeers": Musketeers,
            "Artillery": Artillery
        }

    choice = questionary.select(
        "Chose unit:",
        choices=list(unit_classes.keys())
    ).ask()

    unit_class = unit_classes[choice]

    name = input("Name of army: ")
    size = int(input("Size of army: "))
    experience = int(input("Units experience[1,5]: "))

    army = Army(size, unit_class(name, experience))

    return army

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

            ax.plot(time, army1_values, label=Storage.A1name)
            ax.plot(time, army2_values, label=Storage.A2name)

            ax.set_title(title)

            ax.set_xlabel("Time")
            ax.set_ylabel(title)

            ax.grid(True)
            ax.legend()

        plt.tight_layout()

    plt.show()

class Storage:
    A1array = []
    A1name = ""
    A2array = []
    A2name = ""
    Time = []

    @staticmethod
    def print_arrays():
        print("Array1:")
        for x in Storage.A1array:
            show_army_basic(x)

        print("Array2")
        for x in Storage.A2array:
            show_army_basic(x)
