text = input()

while True:
    actions = input().split(":|:")

    if actions[0] =="Reveal":
        print(f"You have a new text message: {text}")
        break
    elif actions[0] =="InsertSpace":
        index = int(actions[1])
        text = text[:index] + " " + text[index:]
        print(text)

    elif actions[0] == "Reverse":
        substring = actions[1]
        if substring in text:
            text = text.replace(substring,substring[::-1],1)
            print(text)
        elif substring not in text:
            print("error")

    elif actions[0] == "ChangeAll":
        old = actions[1]
        new = actions[2]
        if old in text:
            text = text.replace(old,new)
            print(text)

