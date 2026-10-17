import random
import pathlib

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

        if self.age >= self.max_age:
            self.alive = False
            print(f"{self.name} died of old age ;( she was {self.age})")


    def mate(self, creature2):
        if (self.alive and creature2.alive
         and self.energy > 5 and creature2.energy > 5):

         self.energy -= 2
         creature2.energy -= 2

        baby_name = input("What should we name the baby?")
        baby = Creature(baby_name)

        creatures.append(baby)

        print(f"The baby is name {baby_name}")


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
