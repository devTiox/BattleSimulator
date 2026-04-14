from army import Army
from units import *
import questionary

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


class Storage:
    A1array = []
    A2array = []

    @staticmethod
    def print_arrays():
        print("Array1:")
        for x in Storage.A1array:
            show_army_basic(x)

        print("Array2")
        for x in Storage.A2array:
            show_army_basic(x)