



data = input()

while True:
    commands = input().split()

    if commands[0] == "Finish":
        break
    elif commands[0] == "Replace":
        current_char = commands[1]
        new_char = commands[2]
        data = data.replace(current_char,new_char)
        print(data)

    elif commands[0] == "Cut":
        start_idx=int(commands[1])
        end_idx = int(commands[2])
        if 0 <= start_idx <= end_idx <= len(data):
            data = data[:start_idx] + data[end_idx+1:]
            print(data)
        else:
            print("Invalid indices!")

    elif commands[0] == "Make":
        make = commands[1]
        if make == "Upper":
            data = data.upper()
        elif make == "Lower":
            data = data.lower()
        print(data)

    elif commands[0] == "Check":
        cur_str = commands[1]
        if cur_str in data:
            print(f"Message contains {cur_str}")
        else:
            print(f"Message doesn't contain {cur_str}")

    elif commands[0] == "Sum":
        start = int(commands[1])
        end= int(commands[2])
        if 0 <= start <= end <= len(data):
            score = 0
            for i in data[start:end+1]:
                score+=ord(i)
            print(score)

        else:
            print("Invalid indices!")



# o "Finish"
#
# o "Replace {currentChar} {newChar}"
#
# o "Cut {startIndex} {endIndex}"
#
# o "Make {Upper/Lower}"
#
# o "Check {string}"
#
# o "Sum {startIndex} {endIndex}




# HappyNameDay
# Replace p r
# Make Lower
# Cut 2 23
# Sum -2 2
# Finish



# ILikeSoftUni
# Replace I We
# Make Upper
# Check SoftUni
# Sum 1 4
# Cut 1 4
# Finish