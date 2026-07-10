# Lado máximo de um triângulo
def next_edge(side1, side2):
   return(side1 + side2) - 1
print(next_edge(8, 10))          # 17

# Calculadora de potência
def circuit_power(voltage, current):
  return voltage * current
print(circuit_power(230, 10))    # 2300

# Soma dos ângulos do polígono
def sum_polygon(n):
  return(n - 2) * 180
print(sum_polygon(3))             # 180

# Converter minutos em segundos
def convert(minutes):
  return minutes * 60
print(convert(5))               # 300

# O Problema da Fazenda
def animals(chickens, cows, pigs):
  return (cows * 4) + (pigs * 4) + chickens * 2
print(animals(2, 3, 5))          # 32

# Área de um triângulo
def tri_area(base, height):
  return(base * height) / 2
print(tri_area(10, 5))           # 25

# Retorne o resto da divisão de dois números. 
def remainder(x, y):
	return x % y
print(remainder(10, 3))          # 1


