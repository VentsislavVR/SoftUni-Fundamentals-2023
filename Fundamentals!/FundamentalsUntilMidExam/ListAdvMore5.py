rooms = int(input())
free_chairs = 0
visit_num = 0
for chair in range(1,rooms+1):

    data = input().split()
    chairs = data[0]
    visitors = int(data[1])
    if len(chairs) < visitors:
        print(f"{visitors-len(chairs)} more chairs needed in room {chair}")
        visit_num += visitors - len(chairs)
    elif len(chairs) > visitors:
        free_chairs += len(chairs) - visitors

if free_chairs > visit_num:
    print(f"Game On, {free_chairs} free chairs left")