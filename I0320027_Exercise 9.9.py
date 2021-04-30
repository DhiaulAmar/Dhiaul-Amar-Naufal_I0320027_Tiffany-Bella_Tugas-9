import array

A = array.array('i', [100, 200, 300, 400, 500])
print(A)

A[1] = -700     # menggunakan elemen kedua
A[4] = 800      # menggunakan elemen kelima
print(A)