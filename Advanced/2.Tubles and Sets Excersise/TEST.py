n= int(input())


for i in range(n):
    current_max = set()
    intersection = input().split("-")
    first = intersection[0]
    second = intersection[1]
    fstart =first.split(",")
    sstart = first.split(',')
    first_start = int(fstart[0])
    second_start= int(sstart[1])
