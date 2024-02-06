numero = 0.0
n = float(input(f"Dígite um número: "))
while n >= numero:
    numero = n 
    n = float(input("Dígite outro número "))
    if n < numero:
        print("obrigado")