# import re
#
# destinations = input()
# location_group = re.findall(r"([=/])([A-Z][A-Za-z]{2,})\1", destinations)
#
# print(f"Destinations: {', '.join([match[1] for match in location_group])}")
#
# travel_points = 0
# for match in location_group:
#     travel_points += len(match[1])
#
# print(f"Travel Points: {travel_points}")

import re
data = input()
pattern = r"([=/])[A-Z][A-Za-z]{2,}\1"
result = re.finditer(pattern,data)
points = 0

all_destinations = []

for destination in result:
    current_destination = re.split("\/|=",destination.group())[1]
    points += len(current_destination)
    all_destinations.append(current_destination)
print(f"Destinations: {', '.join(all_destinations)}")
print(f"Travel Points: {points}")
