# Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta nessesaria para pinta-la , sabendo que cada litro de tinta, pinta uma area de 2m.
p1 = float(input("Escreva a lagura da parede: "))
p2 = float(input("esceva a altura da parede: "))
n1 = (p1 * p2)
n2 =  n1 / 2
print(f"Sua parede tem a dimesao de {p1}x{p2} e sua area e de {n1}m2. \nPara pintar essa parede, voce precisara de {n2} de tinta.")
