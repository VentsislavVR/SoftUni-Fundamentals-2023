def take_odd_func(text):
    return text[1::2]

def cutting_func(text, idx, length):
    text = text[:idx] + text[idx + length:]
    return text

def substitute_func(text, old, new):
    if old in text:
        text = text.replace(old, new)
        return text
    else:
        return "Nothing to replace!"


initial_text = input()

while True:
    line = input()
    if line == "Done":
        print(f"Your password is: {initial_text}")
        break

    command = line.split()
    if command[0] == "TakeOdd":
        initial_text = take_odd_func(initial_text)
        print(initial_text)

    elif command[0] == "Cut":
        idx = int(command[1])
        length = int(command[2])
        initial_text = cutting_func(initial_text, idx, length)
        print(initial_text)

    elif command[0] == "Substitute":
        substring = command[1]
        new_string = command[2]
        result = substitute_func(initial_text, substring, new_string)
        if result == "Nothing to replace!":
            print("Nothing to replace!")
        else:
            initial_text = result
            print(initial_text)
