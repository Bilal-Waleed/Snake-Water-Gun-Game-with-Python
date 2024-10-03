import random
from colorama import Fore

'''
1 for Snake w
-1 for Water
0 for Gun
'''

while True:
    computer = random.choice([-1, 0, 1])
    you_str = input(Fore.YELLOW + "Enter your choice (s for Snake, w for Water, g for Gun) or 'exit' to stop: ").lower()

    if you_str == 'exit':
        print(Fore.CYAN + "Thank you for playing!")
        break

    you_Dict = {"s": 1, "w": -1, "g": 0}
    reverse_Dict = {1: "Snake", -1: "Water", 0: "Gun"}

    if you_str not in you_Dict:
        print(Fore.RED + "Invalid choice! Please choose either 's', 'w', or 'g'.")
    else:
        you = you_Dict[you_str]
        print(Fore.CYAN + f"You choose {reverse_Dict[you]}\nComputer choose {reverse_Dict[computer]} ")

        if computer == you:
            print(Fore.MAGENTA + "Tie!")
        else:
            if (computer == -1 and you == 1): 
                print(Fore.GREEN + "You Win!")
            elif (computer == -1 and you == 0):
                print(Fore.RED + "You Lose!")
            elif (computer == 1 and you == -1): 
                print(Fore.RED + "You Lose!")
            elif (computer == 1 and you == 0): 
                print(Fore.GREEN + "You Win!")
            elif (computer == 0 and you == -1): 
                print(Fore.GREEN + "You Win!")
            elif (computer == 0 and you == 1): 
                print(Fore.RED + "You Lose!")
            else:
                print(Fore.RED + "Something went wrong!")
