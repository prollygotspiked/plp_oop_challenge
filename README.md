# plp_oop_challenge
# 🐶 Digital Pet – Python OOP Challenge

Welcome to the Python OOP Challenge! This project is a fun and interactive way to practice Object-Oriented Programming concepts by building your very own virtual pet.

## 🧠 Objective

Create a `Pet` class that simulates a digital pet with basic needs and behaviors like eating, sleeping, and playing. You'll also implement functionality to train and show tricks.

---

## 📦 Features

### Pet Class Attributes:
- `name`: Name of the pet (string)
- `hunger`: Hunger level (int, 0 = full, 10 = very hungry)
- `energy`: Energy level (int, 0 = exhausted, 10 = fully rested)
- `happiness`: Happiness level (int, 0–10)

### Pet Class Methods:
- `eat()`: Decreases hunger by 3 (min 0), increases happiness by 1.
- `sleep()`: Increases energy by 5 (max 10).
- `play()`: Decreases energy by 2, increases happiness by 2, increases hunger by 1.
- `get_status()`: Displays current stats of the pet.

### 🎯 Bonus Features:
- `train(trick)`: Teaches a new trick and adds it to a tricks list.
- `show_tricks()`: Displays all tricks the pet has learned.

---

## 🏁 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Evans-mutuku/OOP-Challenge
   cd OOP-Challenge
