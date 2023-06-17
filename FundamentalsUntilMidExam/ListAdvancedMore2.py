initial_string = input()

numbers = [x for x in initial_string if x.isdigit()]
strings = [x for x in initial_string if not x.isdigit()]

take_numbers = [int(x) for idx,x in enumerate(numbers) if idx % 2 == 0]
skip_numbers = [int(x) for idx,x in enumerate(numbers) if idx % 2 != 0]
letters = ""
final_string =""
for take, skip in zip(take_numbers, skip_numbers):
    if take == 0:
        letters = letters[skip:]
    elif take != 0:
        final_string = final_string + letters[:take]
        letters = letters[skip + take:]

print(final_string)

