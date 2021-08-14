import random

class Faction:
    def __init__(self, name):
        self.name = name
        self.units = 10
        self.resources = {"water": 0, "food": 0, "energy": 0}
        self.allocated_units = {"gather_water": 0, "gather_food": 0, "gather_energy": 0, "defend": 0, "attack": 0}

    def allocate_units(self):
        print(f"\n{self.name}'s turn to allocate units:")
        self.allocated_units["gather_water"] = int(input("Units to gather water: "))
        self.allocated_units["gather_food"] = int(input("Units to gather food: "))
        self.allocated_units["gather_energy"] = int(input("Units to gather energy: "))
        self.allocated_units["defend"] = int(input("Units to defend: "))
        self.allocated_units["attack"] = int(input("Units to attack: "))
        total_allocated = sum(self.allocated_units.values())
        if total_allocated > self.units:
            print("You allocated more units than available! Please allocate again.")
            self.allocate_units()
        else:
            self.units -= total_allocated

    def reset_units(self):
        self.units += sum(self.allocated_units.values())
        for key in self.allocated_units:
            self.allocated_units[key] = 0

    def gather_resources(self, resource_type, hazard_level):
        gather_key = f"gather_{resource_type}"
        collected = max(0, self.allocated_units[gather_key] - hazard_level)
        self.resources[resource_type] += collected
        print(f"{self.name} collected {collected} units of {resource_type}.")

class EnvironmentController:
    def __init__(self):
        self.hazards = {"water": 0, "food": 0, "energy": 0}

    def introduce_hazard(self):
        hazard_type = random.choice(["water", "food", "energy"])
        self.hazards[hazard_type] = random.randint(1, 3)
        print(f"\nHazard introduced: {hazard_type} level {self.hazards[hazard_type]}")

    def reset_hazards(self):
        for key in self.hazards:
            self.hazards[key] = 0

class Game:
    def __init__(self):
        self.faction1 = Faction("Faction 1")
        self.faction2 = Faction("Faction 2")
        self.env_controller = EnvironmentController()
        self.round = 1
        self.total_rounds = 8

    def play_round(self):
        print(f"\n--- Round {self.round} ---")
        self.env_controller.introduce_hazard()

        self.faction1.allocate_units()
        self.faction2.allocate_units()

        self.resolve_actions(self.faction1)
        self.resolve_actions(self.faction2)

        self.faction1.reset_units()
        self.faction2.reset_units()
        self.env_controller.reset_hazards()

        self.round += 1

    def resolve_actions(self, faction):
        faction.gather_resources("water", self.env_controller.hazards["water"])
        faction.gather_resources("food", self.env_controller.hazards["food"])
        faction.gather_resources("energy", self.env_controller.hazards["energy"])

        # Simple attack/defend mechanics (can be expanded)
        if faction.allocated_units["attack"] > 0:
            print(f"{faction.name} is attacking!")
        if faction.allocated_units["defend"] > 0:
            print(f"{faction.name} is defending!")

    def check_winner(self):
        resources1 = sum(self.faction1.resources.values())
        resources2 = sum(self.faction2.resources.values())

        print(f"\nFinal Resources:")
        print(f"{self.faction1.name}: Water={self.faction1.resources['water']}, Food={self.faction1.resources['food']}, Energy={self.faction1.resources['energy']}")
        print(f"{self.faction2.name}: Water={self.faction2.resources['water']}, Food={self.faction2.resources['food']}, Energy={self.faction2.resources['energy']}")

        if resources1 > resources2:
            print(f"\n{self.faction1.name} wins with {resources1} total resources!")
        elif resources2 > resources1:
            print(f"\n{self.faction2.name} wins with {resources2} total resources!")
        else:
            print("\nIt's a tie!")

    def play(self):
        for _ in range(self.total_rounds):
            self.play_round()
        self.check_winner()

# Run the game
if __name__ == "__main__":
    game = Game()
    game.play()
