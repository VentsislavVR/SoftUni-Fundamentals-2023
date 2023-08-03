

def check(A, B, N):
    if A.issubset(B) and B.issubset(A):
        return True
    return False

N = 3
A= {1,2,5}
B= {2,1,5}
print(B.issubset(A))

print(check(A,B,N))

