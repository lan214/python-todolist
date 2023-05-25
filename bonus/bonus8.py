date = input("Enter the date: ")
mood = input("On a scale of 1 to 10, how was your mood? ")
thoughts = input("Share your thoughts for the day:\n")

with open(f"../journal/{date}.txt", "w") as file:
    file.write(mood + "\n" * 2)
    file.write(thoughts)