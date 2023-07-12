# from collections import deque
#
# names = deque(input().split())
#
# rotation_num = int(input())-1
#
# while len(names) > 1:
#     names.rotate(-rotation_num)
#     exited_name = names.popleft()
#     print(f"Removed {exited_name}")
# print(f"Last is {names.popleft()}")


from collections import deque

class NameGame:
    def __init__(self):
        self.names = deque()

    def get_input(self):
        name_list = input("Enter names (space-separated): ").split()
        self.names.extend(name_list)

    def play_game(self):
        rotation_num = int(input("Enter rotation number: ")) - 1

        while len(self.names) > 1:
            self.names.rotate(-rotation_num)
            exited_name = self.names.popleft()
            print(f"Removed {exited_name}")

        print(f"Last is {self.names.popleft()}")

game = NameGame()
game.get_input()
game.play_game()



