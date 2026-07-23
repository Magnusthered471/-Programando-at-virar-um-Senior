# Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta nessesaria para pinta-la , sabendo que cada litro de tinta, pinta uma area de 2m.
p1 = int(float(input("Escreva a lagura da parede: ")))
p2 = int(float(input("esceva a altura da parede: ")))
n1 = (p1 * p2) / 2
print(f"A quantidade de tinta que voce deve usar sera: {n1}")