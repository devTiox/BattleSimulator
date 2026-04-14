class Army:

    def __init__(self, size, unit_type):

        self.units = unit_type
        self.morale = 0

        self.efficiency = 0

        self.initial_size = size

        self.current_size = size

        self.total_loss = 0

        self.turn_loss = 0

        self.total_desertion = 0

        self.turn_desertion = 0

        self.collapse_desertion = 0

        self.tiredness = 0

        self.fight_progress = 0


        self.routed = False

    def set_parameters(self, enemy):
        self.morale = (self.current_size * self.units.power) / (enemy.current_size * enemy.units.power)

        self.morale = clamp(self.morale,0, 1.2)

        self.efficiency = self.units.power * self.morale

    def size_change(self, enemy, frontline_size, turn_duration):
        self.turn_loss = 0
        self.turn_desertion = 0
        if(self.current_size < self.initial_size * 0.15) and (self.morale < 0.6):
            self.route()
            #return

        self.turn_loss = int(enemy.efficiency * frontline_size * turn_duration * 2)
        self.turn_loss = clamp(self.turn_loss, 0, self.current_size)


        self.current_size -= self.turn_loss
        self.desertion(turn_duration)

        self.total_loss += self.turn_loss
        self.total_loss = min(self.total_loss, self.initial_size)

        self.current_size = max(0, self.current_size)

    def desertion(self, turn_duration):  #min 0 max 1
        desertion_rate = 0.1 * self.total_loss/self.initial_size * (1.2 - self.morale) * turn_duration * (1-self.fight_progress)
        desertion = int(self.initial_size * desertion_rate)
        desertion = min(desertion, self.current_size)
        self.turn_desertion = desertion
        self.current_size -= desertion
        self.total_desertion += desertion

    def morale_change(self, enemy, combat_duration, turn_duration):
        fragility = self.total_loss / max(self.initial_size, 1e-9)

        loss_ratio = self.turn_loss / max(self.current_size+self.turn_loss, 1e-9)
        self.fight_progress = enemy.turn_loss / max(enemy.initial_size, 1e-9) - self.turn_loss / max(self.initial_size, 1e-9)
        self.fight_progress = clamp(self.fight_progress, -0.2, 0.2)

        combat_tiredness = turn_duration * combat_duration/(800*self.units.experience)
        self.tiredness = combat_tiredness

        self.morale *= (1 - 0.1 * loss_ratio * fragility - combat_tiredness)
        self.morale *= (1 + self.fight_progress)
        self.morale = clamp(self.morale, 0.2, 1.1)

        self.efficiency = (self.units.power + 0.1 * self.units.experience) * (1/2 + self.morale) * self.current_size/self.initial_size
        self.efficiency = max(0.1, self.efficiency)

    def route(self):
        self.routed = True
        self.collapse_desertion = self.current_size
        self.current_size = 0

def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))