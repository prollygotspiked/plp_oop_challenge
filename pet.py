import random

class Pet:
    def __init__(self, name, pet_type="🐶 Dog"):
        self.name = name
        self.type = pet_type
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
        self.age = 0  # in "days"
        print(f"🎉 Welcome your new {self.type} named {self.name}!")

    def greet(self):
        moods = self._get_mood()
        print(f"👋 {self.name} says: '{random.choice(moods)}'")

    def eat(self):
        old_hunger = self.hunger
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"🍽️ {self.name} eats happily! Hunger: {old_hunger} → {self.hunger}, Happiness +1")

    def sleep(self):
        old_energy = self.energy
        self.energy = min(10, self.energy + 5)
        self.age += 1
        print(f"😴 {self.name} takes a nap. Energy: {old_energy} → {self.energy}, Age +1 day")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"🎾 {self.name} plays joyfully! Energy -2, Happiness +2, Hunger +1")
        else:
            print(f"⚠️ {self.name} is too tired to play. They need rest! 💤")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            self.energy = max(0, self.energy - 1)
            print(f"🎓 {self.name} learns a new trick: {trick}! (+Happiness, -Energy)")
        else:
            print(f"🤔 {self.name} already knows how to {trick}.")

    def show_tricks(self):
        if self.tricks:
            print(f"🧠 {self.name} knows: {', '.join(self.tricks)}")
        else:
            print(f"🤷 {self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"\n📊 {self.name}'s Status Report {self.type}")
        print(f"📅 Age      : {self.age} day(s)")
        print(f"🍗 Hunger   : {self.hunger}/10")
        print(f"⚡ Energy   : {self.energy}/10")
        print(f"😊 Happiness: {self.happiness}/10")
        print(f"🎩 Tricks   : {', '.join(self.tricks) if self.tricks else 'None'}")
        print(f"🧭 Mood     : {self._current_mood()}")
        
    def _current_mood(self):
        if self.happiness >= 8:
            return "😁 Very Happy"
        elif self.happiness >= 5:
            return "🙂 Content"
        elif self.happiness >= 3:
            return "😕 Bored"
        else:
            return "😢 Sad"

    def _get_mood(self):
        if self.hunger >= 8:
            return [f"I'm starving! 🍖", f"Feed me please... 🥺", "So hungry... 😩"]
        if self.energy <= 2:
            return ["I'm exhausted... 💤", "I need a nap... 😴"]
        if self.happiness >= 8:
            return [f"I'm so happy! 😄", "Wanna play again? 🎉"]
        return ["Hey there! 🐾", "Let's hang out!"]

