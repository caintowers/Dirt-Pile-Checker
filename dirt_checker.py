# Query the amount of dirt in the pile
import random

praise = [
    "Nice dirt pile youve got there.",
    "Thats a fine heap of soil!",
    "Impressive mound, friend.",
    "The envy of all gardeners.",
    "Truly majestic dirt.",
]

critique = [
    "This dirt pile is lacking in volume.",
    "I expected more from such a prominent gardener.",
    "This mound could use some serious work.",
    "Not the best dirt I've seen.",
    "I've seen better piles at the compost heap.",
]

amount = int(input("How much dirt is in the pile? "))

if amount > 22:
    print("You have passed the check. Proceeding to the next section...")
    print("This program is excellent for determining whether the amount of dirt you have is above 22")
    while True:
        answer = input("Has the amount of dirt in the pile changed since I last asked how much dirt was in the pile? (yes/no/quit)")
        if answer.lower() == "yes":
            try:
                amount = int(input("How much dirt is in the pile now? "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            while amount < 22:
                print(random.choice(critique))
                print("Perhaps you should add more dirt to the pile.\n")
                try:
                    amount = int(input("How much dirt is in the pile now? "))
                except ValueError:
                    print("Please enter a valid number.\n")
                    continue
            print(random.choice(praise))
            print("You now have enough dirt...\n")
        elif answer.lower() == "no":
            print(random.choice(praise))
            print("Awesome. You still have enough dirt!\n")
        elif answer.lower() == "quit":
            print("Exiting the program.")
            exit()
        else:
            print("Invalid response.")
else:
    print("You don't have enough dirt to start. Perhaps grow a bigger dirt pile. You are poor. Program will terminate.")
    exit()