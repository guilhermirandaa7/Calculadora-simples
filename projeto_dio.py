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

    op = input("Escolha:")

    if op not in ["1", "2", "3", "4"]:
           print("Opção inválida:") 
           continue  

try: 
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
except ValueError:
    print("Entrada inválida!")
    

  
    

