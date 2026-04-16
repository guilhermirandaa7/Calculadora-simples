def soma(a, b):
    return a + b 

def subtracao(a, b): 
    return a - b

def multiplicacao(a,b):
    return a * b

def divisão(a, b):
    if b==0:
        return 'erro: divisão por zero' 
    return a / b 

while true: 
    print ("\n===CALCULADORA===")
    print ("1 - Soma")
    print ("2 - Subtração")
    print ("3 - Multiplicação")
    print ("4 - Divisão")

    
    
           
           
           )
op = (input("Escolha uma operação"))

if op == "1":
    resultado = num_1 + num_2
elif op == "2":d
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
    

