def soma(a, b):
    return a + b 

def subtracao(a, b): 
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero" 
    return a / b 

while True: 
    print ("\n=== CALCULADORA ===")
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
    except:
        print("Entrada inválida!")
        continue

    if op == "1": 
        print("Resultado", soma(num1, num2))
    elif op =="2":
        print("Resulatado", subtracao(num1, num2))
    elif op == "3":
        print("Resultado", multiplicacao(num1, num2))
    elif op=="4":
        print("Resultado", divisao(num1, num2))

    sair = input("Deseja sair? (s/n): ")
    if sair.lower() == "s":
        break


  
    

