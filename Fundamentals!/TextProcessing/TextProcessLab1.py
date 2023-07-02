def reversing():
    while True:
        text = input()
        if text == "end":
            break

        print(f"{text} = {text[::-1]}")
        continue
    return


reversing()
