def f(x):
    return x**3-2*x-7

a = float(input("Masukkan batas atas = "))
b = float(input("Masukkan batas bawah = "))
n = float(input("Masukkan jumlah iterasi = "))

def tabel():
    h = (a-b)/n

    for i in range(n):
        x = (b+(i*h))
        y = f(x[i])
        if f(x[i]) == 0:
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
            
tabel()
