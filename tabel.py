def f(x):
    return x**3-2*x-7

a = int(input("Masukkan batas atas = "))
b = int(input("Masukkan batas bawah = "))
n = int(input("Masukkan jumlah iterasi = "))

def tabel(a, b, n):
    h = (a-b)/n

    for i in range(n):
        x = (b+(i*h))
        y = f(x)
        if f(y) == 0:
            print(x[i])
            return x[i]
        
        elif f(x[i])*f(x[i+1]) < 0:
            if abs(f(x[i])) < abs(f(x[i+1])):
                print(x[i])
                return x[i]
            else:
                print(x[i+1])
                return x[i+1]
    print("\nTidak ditemukan perubahan tanda dalam interval tersebut.")
    return None
            
tabel(a, b, n)
        
