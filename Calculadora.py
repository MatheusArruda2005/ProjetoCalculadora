#Projeto Calculadora
print(f"Escolha Uma Operação:\n ADIÇÃO 1 \n SUBTRAÇÃO 2 \n MULTIPLICAÇÃO 3 \n DIVISÃO 4 \n SAIR 5\n")
cont = 0 
cont =(int(input("Operação:")))
if cont <= 0 or cont >=6:
 (input(f"Insira Um Numero Valido: "))
while cont <= 0 or cont >=6:
  print(f"A Operação escolhido foi: {cont}") 
while cont == 5: 
   print("Saiu Do Site")
print(f"A Operação escolhido foi: {cont}")  
Num1 = (float(input("Numero 1: ")))
Num2 = (float(input("Numero 2: ")))
if cont == 1:
 Resultado = Num1 + Num2
 print(f"O Resultado é: {Resultado}")
if cont == 2:
   Resultado = Num1 - Num2
   print(f"O Resultado é: {Resultado}")
if cont == 3:
   Resultado = Num1 * Num2
   print(f"O Resultado é: {Resultado}")
if cont == 4:
   Resultado = Num1 / Num2
   print(f"O Resultado é: {Resultado}")
  
