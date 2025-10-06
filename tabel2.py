import re

def parse(fungsi):
    fungsi = fungsi.replace('^', '**') 
    fungsi = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', fungsi) 
    return fungsi

fungsi_input = input("Masukkan fungsi (cth. 2x^2 - 3x + 7), f(x) = ")
fungsi_parsed = parse(fungsi_input)

def f(x):
    return eval(fungsi_parsed)

a = float(input("Masukkan batas atas = "))
b = float(input("Masukkan batas bawah = "))
n = int(input("Masukkan jumlah iterasi = "))

def tabel(a, b, n):
    h = (a - b) / n
    akar = None 

    print(f"{'i':<5}{'x':>12}{'f(x)':>15}{'f(x+1)':>15}{'f(x)*f(x+1)':>18}")
    print("-"*65)

    for i in range(n):
        x = b + (i * h)
        x_next = x + h

        fx = f(x)
        fx_next = f(x_next)
        hasil = fx * fx_next

        print(f"{i:<5}{x:12.4f}{fx:15.4f}{fx_next:15.4f}{hasil:18.4f}")

        if fx == 0:
            akar = x
        elif fx * fx_next < 0:
            if abs(fx) < abs(fx_next):
                akar = x
            else:
                akar = x_next

    if akar is not None:
        print(f"\nPendekatan akar berada di x = {akar:.4f}")
    else:
        print("\nTidak ditemukan perubahan tanda dalam interval tersebut.")

tabel(a, b, n)
