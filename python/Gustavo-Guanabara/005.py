# Dia 5
# crie um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.
p1 = int(float(input("Digite um numero inteiro: "))) # --> aqui temos um pergunta, ele tem duas coisas estremamentes importantes para esse cordigo funsionar sem poblema e isso seria o (float e int), pois eles fas que nao tenhamos poblema do float exemplo numeros como o 7.5 vao virar 7 por causa do int, mas primeiramente os numeros float so funsionam direito por causa do float()
n1 = p1 + 1
n2 = p1 - 1
print(f"O numeo que voce digitou {p1} e o seu sucessor sera {n1} e o seu antecessor {n2}")