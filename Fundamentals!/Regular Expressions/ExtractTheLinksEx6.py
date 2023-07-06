import re

links = []
while True:
    line = input()

    if not line:
        break
    matches = re.findall(r'(www\.[A-Za-z\d\-]+(\.[a-z]+)+)',line)
    links.extend([m[0] for m in matches])

for link in links:
    print(link)
