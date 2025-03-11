import random

greetings = ["Hello", "Hi", "Hey", "Greetings", "Salutations"]
name = input("Enter your name: ").strip() or "World"
print(f"{random.choice(greetings)}, {name}!")

