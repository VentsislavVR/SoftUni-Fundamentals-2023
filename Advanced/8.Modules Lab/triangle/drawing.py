def draw_numbers_triangle(n):
    for row in range(1,n+2):
        print(*[col for col in range(1,row)])
    for row in range(n,0,-1):
        print(*[col for col in range(1,row)])



# def draw_upper_part(n):
#     for row in range(1, n + 1):
#         for num in range(1, row + 1):
#             print(num, end=" ")
#         print()
#
#
# def draw_bottom_part(n):
#     for row in range(n, 0, -1):
#         for num in range(1, row):
#             print(num, end=" ")
#         print()
#         pass
#
#
# def draw_numbers_triangle(n):
#     draw_upper_part(n)
#     draw_bottom_part(n)

