def f(x):
    return x**3-3*x+7

a = int(input("Masukkan batas atas = "))
b = int(input("Masukkan batas bawah = "))
n = int(input("Masukkan jumlah iterasi = "))

def tabel(a, b, n):
    h = (a-b)/n

    for i in range(n):
        x = (b+(i*h))
        x_next = x + h    

        if f(x) == 0:
            print(x)
            return x
        
        if f(x)*f(x_next) < 0:
            if abs(f(x)) < abs(f(x_next)):
                print(x)
                return x
            else:
                print(x_next)
                return x_next
    print("\nTidak ditemukan perubahan tanda dalam interval tersebut.")
    return None
            
tabel(a, b, n)
        
