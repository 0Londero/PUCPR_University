A = []

for i in range(6):
    # A
    numeros = [1, 0, 5, -2 ,-5, 7]
    A.append(numeros[i])

# B
A.append((A[0])+(A[1])+(A[5]))
print(A)

#C
A[4] = 100

#D
for i in range(A[0], (len(A)-1)):
    print(A[i])
