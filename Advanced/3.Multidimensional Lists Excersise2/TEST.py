a = [-2, -1, 1, 2 ]
positions = [(x,y) for x in a for y in a if abs(x) != abs(y)]

print(positions)
print(len(positions))