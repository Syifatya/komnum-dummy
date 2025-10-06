def f(x):
    return x*3-3*x-7

# def batas_atas()

def tabel():
    a = int(input("Masukkan batas atas = "))
    b = int(input("Masukkan batas bawah = "))
    n = int(input("Masukkan jumlah iterasi = "))
    h = (a-b)/n

    for i in range(0, n+1):
        xi = (b+(i*h))
        y = f(xi)

        print (f"{i}\t {xi:.6f}\t {y:.6f}")
tabel()


    
    
