print("===calculador===")

num_1 = float(input("Qual o primeiro número?"))
num_2 = float(input("Qual o segundo número?"))

print("/n Escolha a operação:")
print("1 - soma(+)")
print("2 - subtração (-)")
print("3 - multiplicação(*)")
print("4 - divisão(/)")

op = (input("Escolha uma operação"))

if op == "1":
    resultado = num_1 + num_2
elif op == "2":
    resultado = num_1 - num_2
elif op == "3":
    resultado = num_1 * num_2
elif op == "4":
    if num_2 !=0:
        resultado = num_1 / num_2
    else:
        resultado = "erro: divisão por zero"
else: 
    resultado = "operação invalida"
    
print(f"\nResultado: {resultado}")
    

