# Exercicio do video 6 = antes das lioces do 003
n1 = int(float(input("Escreva um numero: ")))
n2 = int(float(input("Escreva outro numero: ")))
s = n1 + n2
print(f"A soma dessa conta sera {s}")
print(f"A soma de {n1} + {n2} vale {s}")
# Teste de boleano
t = bool(input("Digite algo: ")) # --> O boleano e um tipo de dado que so tem dois valores possiveis, que sao o True e o False, e ele e muito usado em comparacoes, como por exemplo, se um numero e maior que outro, ou se uma string e igual a outra. 
print(t) # --> se escrever um numero ou algo va aparecer True, se escrever nada ou 0 vai aparecer False.
print(t.isalnum()) # --> o isalnum() e um metodo que verifica se uma string e composta apenas por letras e numeros, e retorna True ou False.
print(t.isalpha()) # --> o isalpha() e um metodo que verifica se uma string e composta apenas por letras, e retorna True ou False.