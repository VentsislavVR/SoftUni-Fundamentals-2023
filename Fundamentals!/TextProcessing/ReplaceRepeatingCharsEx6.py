# some_text = input()
#
# final_text = ""
#
# for current_letter in some_text:
#     if current_letter not in final_text:
#         final_text += current_letter
# print(final_text)

some_text = input()

final_text = ""
last_letter = ""

for current_letter in some_text:
    if current_letter != last_letter:
        final_text += current_letter
        last_letter = current_letter
print(final_text)

