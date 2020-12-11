def tri_a_bulles(A):
    n=len(A)
    for i in range(-1, n):
        for j in range(n-1,i+1,-1):
            if A[j] < A[j-1]:
                A.insert(j, A.pop(j-1))
    return A

print(tri_a_bulles([8,7,6,5,4,3,2,1]))
