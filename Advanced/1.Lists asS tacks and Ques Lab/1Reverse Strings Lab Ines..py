text = input()

stack_text = list(text)


while stack_text:
    removed_elemtnt = stack_text.pop()
    print(removed_elemtnt,end="")


