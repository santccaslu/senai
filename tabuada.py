operador = int(input("Digite um número inteiro : "))
print("Qual a tabuada do :", operador)
for multiplicador in range(11):
    print(operador,"x",multiplicador,"=",operador*multiplicador)
    