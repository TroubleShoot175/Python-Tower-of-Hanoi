# Tower of Hanoi
# Libraries
from TowerOfHanoi import TowerOfHanoi

# Program
TOH = TowerOfHanoi()

# Print Towers
print(f"Tower of Hanoi")
while len(TOH.towers[3].stack) != TOH.diskCount:
    print(f"Minimum Moves: {TOH.minimumMoves}")
    print(f"Move Count: {TOH.moveCount}")
    TOH.print_game()
    fromTowerNum = int(input("Please enter a tower to move a disk from: "))
    toTowerNum = int(input("Please enter a tower to move a disk to: "))
    if fromTowerNum == toTowerNum:
        continue
    else:
        if TOH.move_disk(TOH.towers[fromTowerNum], TOH.towers[toTowerNum]):
            continue
        else:
            print("Bad move...")

TOH.print_game()
print("You win!")
