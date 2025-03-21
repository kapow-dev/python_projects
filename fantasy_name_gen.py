print("Welcome to Simple Fantasy Name Generator")
street = input("What street did you grow up on? ").capitalize()
color = input("Pick a color: Black, Gray, Green, Blue ").capitalize()
animal = input("Choose an animal: Lion, Horse, Unicorn, Walrus ").lower()

if animal == "lion":
    surname = "beard"
elif animal == "horse":
    surname = "mane"
elif animal == "unicorn":
    surname = "horn"
elif animal == "walrus":
    surname = "tusk"

print(f"Your fantasy name is {street} {color}{surname}.")
