#1.2
n, m = [int(num) for num in input().split()]

first_set = {int(input())for _ in range(n)}
second_set= {int(input())for _ in range(m)}
print(*first_set.intersection(second_set), sep='\n')
print(first_set & second_set, sep='\n')
print(first_set | second_set, sep='\n')
print(first_set - second_set, sep='\n')
print(first_set ^ second_set, sep='\n')




#1.1
# n, m = [int(num) for num in input().split()]
#
# first_set = {int(input())for _ in range(n)}
# second_set= {int(input())for _ in range(m)}
#
# print(*first_set.intersection(second_set), sep='\n')



#1.0
# length = input().split()
#
# n,m = int(length[0]),int(length[1])
#
# first_set = set()
# second_set = set()
#
# for i in range(1,n+m+1):
#    if i <= n:
#         first_set.add(int(input()))
#    else:
#         second_set.add(int(input()))
# for res in first_set.intersection(second_set):
#     print(res)



