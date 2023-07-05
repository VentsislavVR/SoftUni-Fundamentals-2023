# kiwi orange banana apple
woooord = input().split()
words = [w for w in woooord if len(w) % 2 == 0]
# for i in words:
#     print(i)
print("\n".join(words))