import json
import random
from pathlib import Path

DATA_FOLDER = Path(r"C:\\Users\\theyt\\.vscode\\Wrld_Sim\\world_data")
DATA_FOLDER.mkdir(exist_ok=True)

DEATH_LOG = DATA_FOLDER / "death_log.txt"
WORLD_HISTORY = DATA_FOLDER / "world_history.txt"
CREATURE_FILES = DATA_FOLDER / "creatures.json"

DEATH_LOG.touch(exist_ok=True)
WORLD_HISTORY.touch(exist_ok=True)
CREATURE_FILES.touch(exist_ok=True)


def log_event(message):
    with WORLD_HISTORY.open("a", encoding="utf-8") as file:
        file.write(message + "\n")

def log_death(creature, turn, cause):
    message = (f"{creature.name} died at age {creature.age} on turn {turn} due to {cause} with {creature.energy} energy left.")
    with DEATH_LOG.open("a", encoding="utf-8") as file:
        file.write(message + "\n")
    

class Creature:
    def __init__(self, name, energy=None, age=0):
        self.name = name
        self.energy = energy if energy is not None else random.randint(5, 15)
        self.age = age
        self.max_age = random.randint(20, 35)
        self.alive = True

    def live(self):
        print(f"\n{self.name}'s turn!")

        # Age one year/turn
        self.age += 1

        # Lose energy
        self.energy -= 1
        print(f"{self.name} loses 1 energy. Energy: {self.energy}")

        # 30% chance to find food
        if random.random() < 0.30: # 30% chance to find food
            self.energy += 3
            print(f"{self.name} found food! Energy: {self.energy}")

        # Check for death
        if self.energy <= 0:
            self.alive = False
            print(f"{self.name} died of starvation!")
            log_death(self, turn, "starvation")

        if self.age >= self.max_age:
            self.alive = False
            print(f"{self.name} died of old age ;( she was {self.age})")
            log_death(self, turn, "old age")


    def mate(self, creature2):
        if (self.alive and creature2.alive
         and self.energy > 5 and creature2.energy > 5):

         self.energy -= 2
         creature2.energy -= 2

        baby_name = input("What should we name the baby?")
        baby = Creature(baby_name)

        creatures.append(baby)

        print(f"The baby is name {baby_name}")
        log_event(f"{self.name} and {creature2.name} mated and had a baby named {baby_name}.")
        


# Create the starting population
creatures = [
    Creature("Dave"),
    Creature("Martha"),
    Creature("Dawn"),
    Creature("Bob")
]

for turn in range(1, 51):
    print(f"\n--- Turn {turn} ---")
    for creature in creatures:
        if creature.alive:
            creature.live()
            if random.random() < 0.02:  # 2% chance to mate
                creature.mate(random.choice(creatures))

    # Remove dead creatures from the population
    creatures = [creature for creature in creatures if creature.alive]

    # Check if all creatures are dead
    if not creatures:
        print("\nAll creatures have died. Game over.")
        break
