c = float(input("Quantos dias o carro alugado?: "))
k = float(input("quantos kilomentros o carro andou?: "))
n1 = (c * 60) + (k * 0.15)
print(f"O custo do uso sera: R${n1:.2f}")
