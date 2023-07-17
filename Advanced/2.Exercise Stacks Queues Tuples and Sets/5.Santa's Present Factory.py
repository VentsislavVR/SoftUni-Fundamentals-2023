from collections import deque

materials = deque(int(x) for x in input().split())
magick_levels = deque(int(x) for x in input().split())
crafted = []
presents = {
    150: "Doll",
    250:"Wooden train",
    300:"Teddy bear",
    400:"Bicycle",
}

while materials and magick_levels:
    material = materials.pop() if magick_levels[0] or not materials[0] else 0
    magick_level = magick_levels.popleft() if material or not magick_levels[0] else 0

    if not magick_level:
        continue
    product = material * magick_level

    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        materials.append(material + magick_level)
    elif product > 0:
        materials.append(material+15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")

if magick_levels:
    print(f"Magic left: {', '.join([str(x) for x in magick_levels])}")

[print(f"{toy}: {crafted.count(toy)}")for toy in sorted(set(crafted))]

