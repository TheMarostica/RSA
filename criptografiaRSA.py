import random as rd
import os

# Calcula o máximo divisor comum
def mdc(n1, n2):

    # Algoritmo de Euclides
    #   Enquanto o menor número divide o maior
    #       subtraia o menor do maior
    #   Se o menor divide o maior
    #       então o menor é o máximo divisor comum
    while(n2 != 0):
        r = n1 % n2
        n1 = n2
        n2 = r

    return n1

# Gera Número Primo Aleatório
def gerarPrimoAleatorio():

    primo = False

    while primo == False:
        n = rd.randrange(2, 1000)
        primo = verificaPrimo(n)

    return n

def verificaPrimo(n):

    cont = 0
    aux = 0

    for c in range(1, n+1):
        if(n % c == 0):
            aux += 1

    if aux == 2:
        return True

    return False

# Verifica p e q
def verificaPQ(p, q):

    # se pe já for diferente de q, é retornado o próprio valor de q
    if(p != q):
        return q
    
    # verifica se p e q são iguais
    while p == q:
        aux = gerarPrimoAleatorio()

        # se p for diferente de q
        if(p != aux):
            return aux

# Chave Pública
def gerarChavePublica(n):

    # Chave pública é aleatória
    while True:
        numeroAleatorio = rd.randrange(2, n)
        
        # MDC entre um número aleatório e um enviado
        if(mdc(n, numeroAleatorio) == 1):
            return numeroAleatorio

# Chave Privada
def gerarChavePrivada(totiente, chavePublica):

    # totiente = número gerado em outra função

    d = 0

    # Incrementado até o resto da divisão ser 1
    while((d * chavePublica) % totiente != 1):
        d += 1

    return d

# Cifrar mensagem
def cifrar(mensagem, chavePublica, n):
    # para cifrar se usa a chave pública

    msgCifrada = ""
    
    # laço para criptografar cada letra
    for letra in mensagem:
        k = (ord(letra) ** chavePublica) % n

        # a string vazia recebe cada letra que foi criptografada
        msgCifrada += chr(k)

    return msgCifrada

# Descriptografar a mensagem
def decifrar(mensagem, n, chavePrivada):
    # para decifrar se usa a chave privada

    # praticamente o mesmo algoritimo que a função de cifrar a mensagem

    msgDecifrada = ""

    for letra in mensagem:
        k = (ord(letra) ** chavePrivada % n)
        msgDecifrada += chr(k)

    return msgDecifrada

def opcao(escolha, chavePublica, chavePrivada, n, totiente, p, q):
    if(escolha == 1):
        print("\n")
        msg = input("Digite a mensagem: ")
        msgCifrada = cifrar(msg, chavePublica, n)

        print("\nMensagem cifrada: {}".format(msgCifrada))

        print("\n")

        os.system("pause")

    if(escolha == 2):
        print("\n")
        msg = input("Digite a mensagem: ")
        msgDecifrada = decifrar(msg, n, chavePrivada)

        print("\nMensagem Decifrada: {}".format(msgDecifrada))

        print("\n")

        os.system("pause")
    
    if(escolha == 3):
        print("\nValor de p: {}".format(p))        
        print("Valor de q: {}".format(q))      
        print("Valor de n: {}".format(n))
        
        print("\nValor do totiente: {}".format(totiente))

        print("\nChave Privada: {}".format(chavePrivada))
        print("Chave Pública: {}".format(chavePublica))

        print("\n")

        os.system("pause")
    
    if(escolha == 9):
        print("\nFinalizando...")

def menu(escolha, n, totiente, chavePrivada, chavePublica, p, q):
    
    while(escolha != 9):
        os.system('cls') or None
        
        print("--------------------")
        print("1 - Cifrar")
        print("2 - Decifrar")
        print("3 - Mostrar informações")
        print("9 - SAIR")
        print("--------------------")
        escolha = int(input("Digite a opção desejada: "))

        opcao(escolha, chavePublica, chavePrivada, n, totiente, p, q)

def rsa():

    # você precisa de dois números primos
    p = gerarPrimoAleatorio()
    q = gerarPrimoAleatorio()
    
    # verifica se p é igual ao q
    q = verificaPQ(p, q)
    
    n = p * q
    y = p - 1
    x = q - 1

    # para calcular os totientes
    totiente = x * y
    
    # gerar chave pública
    chavePublica = gerarChavePublica(totiente)
    
    # gerar chave privada
    chavePrivada = gerarChavePrivada(totiente, chavePublica)
    
    escolha = 0
    
    menu(escolha, n, totiente, chavePrivada, chavePublica, p, q)


# chamando a função e rodando o programa
rsa()
print("\n\nFinalizado!")
