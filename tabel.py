import re

def parse(fungsi):
    fungsi = fungsi.replace('^', '**')
    fungsi = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', fungsi)
    return fungsi

fungsi_input = input("Masukkan fungsi (cth. 2x^2 - 3x + 7), f(x) =  ")  
fungsi_parsed = parse(fungsi_input)

def f(x):
    return eval(fungsi_parsed)

a = int(input("Masukkan batas atas = "))
b = int(input("Masukkan batas bawah = "))
n = int(input("Masukkan jumlah iterasi = "))

def tabel(a, b, n):
    h = (a-b) / n
    print(f"{'i':<5}{'x':>12}{'f(x)':>15}{'f(x+1)':>15}{'f(x)*f(x+1)':>18}")
    print("-"*65)

    for i in range(n):
        x = b + (i * h)
        x_next = x + h   

        print(f"{i:<5}{x:12.4f}{f(x):15.4f}{f(x_next):15.4f}{f(x)*f(x_next):18.4f}")

        if f(x) == 0:
            print(f"\nAkar tepat di x = {x:.4f}")
            return x
        
        if f(x)*f(x_next) < 0:
            if abs(f(x)) < abs(f(x_next)):
                print(f"\nPendekatan akar berada di x = {x:.4f}")
                return x
            else:
                print(f"\nPendekatan akar berada di x = {x_next:.4f}")
                return x_next
            
    print("\nTidak ditemukan perubahan tanda dalam interval tersebut.")
    return None
            
tabel(a, b, n)
        
