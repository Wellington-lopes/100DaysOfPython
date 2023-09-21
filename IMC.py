# Calculando IMC
peso = float(input("Qual seu peso? "))
altura = float(input("Qual sua altura? "))

imc = (peso / (altura ** 2))

print(f"O IMC é {imc}.")