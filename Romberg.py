import numpy as np

# fungsi
def f(x):
    return np.sin(x)


# metode romberg
def romberg(a, b, n):
    n = n+1
    # declare array
    arr = [ [0]*n for i in range(n)]

    # hitung R(n, 1)
    for i in range(1, n):
        x = trapezoid(a, b,  2 ** i)
        arr[i][1] = x


    # hitung R(n, m)
    for k in range (2, n): 
        for j in range(k, n):
            arr[j][k] = arr[j][k-1] + (1/(4**k - 1))*(arr[j][k-1]-arr[j-1][k-1])

    # print array
    for i in range(1, n):
        print(i, "\t", end=" ")
        for j in range(1, i+1):
            print(arr[i][j], "\t", end=" ")
        print()

    print()
    return arr[n-1][n-1]


# metode trapezoid
def trapezoid(a, b, n):
    # cari nilai h
    h = (b - a)/n

    # metode trapezoid
    result = 0
    result += (f(a) + f(b))

    # s untuk menyimpan 2*sigma(f(xi)) dari i = 1 ke i =n-1
    s = 0
    for i in range (1, n):
        xi = i*h + batasBawah
        s += f(xi) 

    s *= 2
    result += s

    result *= h/2

    return result

# mengukur error 
def Er(x):
    er = (2-x)/2  * 100
    return er


# Driver code
batasBawah = 0
batasAtas = np.pi 
iterasi = 5

print("Implementasi metode numerik Romberg untuk mencari integrasi f(x) = sin(x) dengan batas bawah =", batasBawah, " dan batas atas =", batasAtas, "sebanyak", iterasi, "iterasi")

T = trapezoid(batasBawah, batasAtas, iterasi)
R = romberg(batasBawah, batasAtas, iterasi)

print("Metode Trapezoid: I =", T)
print("Er =", Er(T), "%", "\n")

print("Metode Romberg: I =", R)
print("Er =", Er(R), "%", "\n")
