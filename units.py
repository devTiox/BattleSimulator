
class Unit:
    def __init__(self, name, power, experience, miss_ratio: float = 1):
        self.name = name
        self.power = power
        self.miss_ratio = clamp(miss_ratio, 0, 1)
        self.experience = experience
        self.experience = clamp(experience, 1, 5)

    def show_unit(self):
        print("-Name:",self.name,"\n-Power:",self.power, "\n-Miss ratio:", self.miss_ratio)

def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))


#LINEAR UNITS
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
class KapitanBomba(Unit):
    def __init__(self, name, experience):
        super().__init__(name, 5, experience)

# --------------------------------------


#QUADRATIC UNITS
# --------------------------------------
class Slingers(Unit):
    def __init__(self, name, experience):
        super().__init__(name, 1, experience, 0.1)

# --------------------------------------
class Archers(Unit):
    def __init__(self, name, experience):
        super().__init__(name, 2, experience, 0.12)

# --------------------------------------
class Crossbowmen(Unit):
    def __init__(self, name, experience):
        super().__init__(name, 3, experience, 0.18)

# --------------------------------------
class Musketeers(Unit):
    def __init__(self, name, experience):
        super().__init__(name, 4, experience, 0.03)

# --------------------------------------
class Artillery(Unit):
    def __init__(self, name, experience):
        super().__init__(name, 5, experience, 0.12)
