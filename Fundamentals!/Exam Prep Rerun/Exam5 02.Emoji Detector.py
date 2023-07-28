import re
pattern = r"(:{2}|\*{2})([A-Z][a-z]{2,})\1"
text = input()

matches = re.findall(pattern,text)

cool_treshold = [int(x) for x in text if x.isdigit()]
cool_avrage = 1
for el in cool_treshold:
    cool_avrage *= int(el)
the_coolest_emojis = []

for emoji in matches:
    current_coolnes = 0
    for e in emoji[1]:
        current_coolnes += ord(e)
        if current_coolnes >= cool_avrage:
            the_coolest_emojis.append(''.join(f"{emoji[0]}{emoji[1]}{emoji[0]}"))
            break


print(f"Cool threshold: {cool_avrage}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for em in the_coolest_emojis:
    print(em)