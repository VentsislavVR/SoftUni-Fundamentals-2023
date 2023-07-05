def chat_func(chat, some_messege):
    if some_messege not in chat:
        chat.append(some_messege)
    return chat


def delete_func(chat, some_messege):
    if some_messege in chat:
        chat.remove(some_messege)
    return chat


def edit_func(chat, old, new):
    if old in chat:
        index = chat.index(old)
        chat[index] = new
    return chat


def pin_func(chat, some_messege):
    if some_messege in chat:
        chat.remove(some_messege)
        chat.append(messege)
    return chat


def spam_func(chat, some_messege):
    spaming = some_messege[1:]
    for i in range(len(spaming)):
        chat.append(spaming[i])
    return chat


command = input()
chat = []
while command != "end":
    action = command.split()
    if action[0] == "Chat":
        messege = action[1]
        result = chat_func(chat, messege)
    elif action[0] == "Delete":
        messege = action[1]
        result = delete_func(chat, messege)
    elif action[0] == "Edit":
        messege = action[1]
        new_messege = action[2]
        result = edit_func(chat, messege, new_messege)
    elif action[0] == "Pin":
        messege = action[1]
        result = pin_func(chat, messege)
    elif action[0] == "Spam":
        messege = action
        result = spam_func(chat, messege)
    command = input()

for item in chat:
    print(item)

# Chat John
# Spam Let's go to the zoo
# Edit zoo cinema
# Chat tonight
# Pin John
# end

