data = [int(x) for x in input().split()]
removed_elements = 0
while data:
    indexes = int(input())
    catch = data.pop(indexes)
    if indexes < 0:
        first_el = data.pop(0)
        last_el = data[-1]
        data.insert(0, last_el)
    if len(data) > 1 or data[indexes] > data[-1]:
        first_el = data[0]
        last_el = data.pop(-1)
        data.insert(first_el, -1)
    for index,c in enumerate(data):
        if c <= catch:
            data[index] += catch
        else:
            data[index] -= catch
    # if indexes < 0:
    #     first_el=data.pop(0)
    #     last_el = data[-1]
    #     data.insert(0,last_el)
    # if data[indexes] > data[-1]:
    #     first_el = data[0]
    #     last_el = data.pop(-1)
    #     data.insert(first_el,-1):






