# Faca um programa que leia um valor um numero inteiro qualquer e mostre na tela a sua tabuada.
p1 = int(input("Escreva um numero e faarei sua tabuada: "))
print("======Tabuada======")
for a in range(1, 11):
  n2 = p1 * a
  print(f"{p1:6} x {a} = {n2}")
print("=====Finalizado=====")
