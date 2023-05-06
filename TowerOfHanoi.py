# TowerOfHanoiClass


# Game Class
class TowerOfHanoi:
    def __init__(self, diskCount: int = 3):
        self.towers = {1: self.start_stack(diskCount, Tower()), 2: Tower(), 3: Tower()}
        self.minimumMoves = (2**diskCount) - 1
        self.towerCount = 3
        self.diskCount = diskCount
        self.moveCount = 0

    def start_stack(self, diskCount, tower):
        for i in range(diskCount, 0, -1):
            tower.stack.append(i)
        return tower

    def move_disk(self, fromTower, toTower):
        if len(toTower.stack) == 0:
            disk = fromTower.stack.pop(-1)
            toTower.stack.append(disk)
            self.updated_move_count()
            return True
        elif toTower.stack[-1] > fromTower.stack[-1]:
            disk = fromTower.stack.pop(-1)
            toTower.stack.append(disk)
            self.updated_move_count()
            return True
        else:
            self.updated_move_count()
            return False

    def updated_move_count(self):
        self.moveCount += 1

    def print_game(self):
        print(f"Tower 1: {self.towers[1].stack}")
        print(f"Tower 2: {self.towers[2].stack}")
        print(f"Tower 3: {self.towers[3].stack}")


# Tower Class
class Tower:
    def __init__(self):
        self.stack = []
