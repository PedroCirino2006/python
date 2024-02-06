salario = float(input("Digite o salário para cálculo do imposto: "))
if salario >= 2112 and salario <=2826:
   imposto = salario * 0.075
   print(f"voce pagará {imposto} de imposto")
elif salario >= 2826 and salario <=3700:
   imposto = salario * 0.15
   print(f"voce pagará {imposto} de imposto")
if salario >= 3751 and salario <=4664:
   imposto = salario * 0.225
   print(f"voce pagará {imposto} de imposto")
elif salario > 4664:
   imposto = salario * 0.275
   print(f"{imposto}")
