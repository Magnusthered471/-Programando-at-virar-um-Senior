# Introducao de desafios do site Edabit modo muito facil para iniciantes em Python.
def hello():
  return "hello edabit.com" #<-- Returno cria um retorno da função, ou seja, quando a função for chamada, ela vai retornar o valor que está depois do return.
print(hello())                  # "hello edabit.com"

# Errei feio pois me esqueci como escrever return direito.
def cubes(a):
	return a ** 3
print(cubes(3))                 # 27

# Como tonar qualquer resultado numeral escrito em string, em numeros inteiros.
def string_int(txt):
	return int(txt)
print(string_int("42"))         # 42

# Encontrando  o perimentro de um retangulo, que é a soma de todos os lados.
def find_perimeter(length, width):
  return (length + width) * 2
print(find_perimeter(6, 7))     # 26

# Retorne a soma de dois números.
def addition(a, b):
  return (a + b)
print(addition(5, 10))          # 15

# Retorna o próximo número dentre os inteiros passados.
def addition(num):
  return(num + 1)
print(addition(5))              # 6

# Converter horas em segundos
def how_many_seconds(hours):
  return( hours * 60 ) * 60
print(how_many_seconds(2))       # 7200