
class Unit:
    def __init__(self, name, power, experience):
        self.name = name
        self.power = power
        self.experience = experience
        self.experience = clamp(experience, 1, 5)

    def show_unit(self):
        print("-Name:",self.name,"\n-Power:",self.power)

def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))

#--------------------------------------
class Infantry(Unit):
    def __init__(self, name, experience):
        super().__init__(name, 1, experience)

#--------------------------------------
class Knights(Unit):
    def __init__(self, name, experience):
        super().__init__(name, 2, experience)

#--------------------------------------
class Cavalry(Unit):
    def __init__(self, name, experience):
        super().__init__(name, 3, experience)

# --------------------------------------
class Hussars(Unit):
    def __init__(self, name, experience):
        super().__init__(name, 4, experience)

# --------------------------------------
class Kapitan_Bomba(Unit):
    def __init__(self, name, experience):
        super().__init__(name, 5, experience)

# --------------------------------------
