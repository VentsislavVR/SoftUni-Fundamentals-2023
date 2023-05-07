#5th
# input
# 3
# XXXXXXX 5
# XXXX 5
# XXXXXX 8
#output
# 1 more chairs needed in room 2
# 2 more chairs needed in room 3
def check_the_rooms(numbers_of_room):
    total_free_chairs = 0
    total_needed_chairs = 0
    for room in range(1,numbers_of_room+1):
        free_chairs, visitors = input().split()
        difference = len(free_chairs) - int(visitors)
        if difference >= 0:
            total_free_chairs += difference
        else:
            total_needed_chairs += abs(difference)
            print(f"{abs(difference)} more chairs needed in room {room}")

    return total_free_chairs, total_needed_chairs


number_of_rooms = int(input())
free_chairs, needed_chairs = check_the_rooms(number_of_rooms)
if free_chairs >= needed_chairs:
    print(f"Game On, {free_chairs} free chairs left")

