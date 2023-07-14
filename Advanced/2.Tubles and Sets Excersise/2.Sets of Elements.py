lenght = input().split()

n,m = int(lenght[0]),int(lenght[1])

first_set = set()
second_set = set()

for i in range(1,n+m+1):
   if i <= n:
        first_set.add(int(input()))
   else:
        second_set.add(int(input()))
for res in first_set.intersection(second_set):
    print(res)



