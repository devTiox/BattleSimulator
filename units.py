
class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def show_unit(self):
        print("-Name:",self.name,"\n-Power:",self.power)


#--------------------------------------
class Infantry(Unit):
    def __init__(self, name):
        super().__init__(name, 1)

#--------------------------------------
class Cavalry(Unit):
    def __init__(self, name):
        super().__init__(name, 2)

# --------------------------------------