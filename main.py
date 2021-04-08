import numpy as np

# a = np.arange(2)
# print(a)
#
# a = np.array([0, 1])
# print(a)
#
# print(type(a))
#
# print(a.dtype)
#
# a = np.arange(2, dtype='int64')
# print(a)
# print(a.dtype)
#
# b = a.astype('float')
# print(b)
#
# print(a.ndim)
# print(a.shape)
#
# a = np.array([np.arange(2), np.arange(2)])
# print(a)
# print(a.shape)
# print(a.ndim)

zera = np.zeros((5, 5))
jedynki = np.ones((4, 4))
print(zera)
print(jedynki)

print(zera.dtype)
print(jedynki.dtype)

pusta = np.empty((2,2))
print(pusta)

poz_1 = pusta[1, 1]
poz_2 = pusta[0, 1]
print(poz_1)
print(poz_2)

macierz = np.array([[1, 2],[3, 4]])
print(macierz)

liczby = np.arange(1, 2, 0.1)
print(liczby)

liczby_lin = np.linspace(1, 2, 5, endpoint=False)
print(liczby_lin)

macierz = np.indices((5, 3))
print(macierz)

x, y = np.mgrid[0:5, 0:5]
print(x)
print(y)

mat_diag = np.diag([a for a in range(5)])
print(mat_diag)

# m = np.fromiter(range(5), dtype='int32')
# print(m)
#
# mar = b'Kacper'
#
# m = np.frombuffer(mar,dtype='S1')
# print(m)
# m = np.frombuffer(mar, dtype='S2')
# print(m)


