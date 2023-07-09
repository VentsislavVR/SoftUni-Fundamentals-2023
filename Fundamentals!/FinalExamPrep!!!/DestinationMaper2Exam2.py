import re

destinations = input()
location_group = re.findall(r"([=/])([A-Z][A-Za-z]{2,})\1", destinations)

print(f"Destinations: {', '.join([match[1] for match in location_group])}")

travel_points = 0
for match in location_group:
    travel_points += len(match[1])

print(f"Travel Points: {travel_points}")