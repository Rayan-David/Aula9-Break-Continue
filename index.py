#Atividade 1
#contador = 1

#while contador <= 10:
#   print(contador)
    
#  if contador == 6:
#     break
#contador += 1
 
#Atividade 2    
#num = 1

#while num <= 10:

#    if num == 5:
#        num += 1
#        continue
#    
#    print(num)
#    num += 1 

#Atividade 3
#num = 1

#while num <= 20:
    
#    if num % 2 == 0:
#        print(num)
    
    #    if num == 15+1:
#        break
#    num += 1

#Atividade 4
#while True:
#    nome_produto = input("Digite o nome do produto: ")
    
#    if nome_produto == "sair":
#        print("Programa encerrado.")
#        break

#    print("Produto adicionado ao carrinho.", nome_produto)

#Atividade 5
#soma = 0
#while True:
#    numero = int(input("Digite um número: "))
#    soma += numero
    
#    if soma >= 20:
#        print("A soma ultrapassou 20. Programa encerrado.")
#        break
#print("A soma total é:", soma)


#Atividade 6
#soma = 0
#while True:
#    numero = int(input("Digite um número: "))
#    soma += numero
    
#    if soma >= 50:
#        print("A soma ultrapassou 50. Programa encerrado.")
#        break
#print("A soma total é:", soma)

#Atividade 7
senha = ""

while True:
    senha = input("Digite a senha: ")
    
    if senha == "Teste":
        print("Senha correta. Acesso liberado.")
        break
    else:
        print("Senha incorreta. Tente novamente.")