from ast import While
import random

contador = 0;
acerto = False;
numero_usuario = 0;
numero_aleatorio = 0;

#gerar um número aleatorio
def gerar_numero_aleatorio_0_e_100():
    return random.randint(0,100)
    

#solicita número ao usuário
def solicita_numero_ao_usuario():
    while True:
        try:
            number = int(input('digita um número de 0 à 100 '))
            if  0 <= number <= 100:
                return number
            else:
                print('digite apenas números entre 0 e 100')
                solicita_numero_ao_usuario()
        except ValueError:
            print('Erro, Favor digitar um número inteiro válido')

def verificar_acerto(numero_usuario, numero_aleatorio):
    if numero_usuario == numero_aleatorio:
            return True
    elif numero_usuario > numero_aleatorio:
            print('O número é menor que o informado!')
            return False
    else:
            print('O número é maior que o digitado')
            return False


numero_aleatorio = gerar_numero_aleatorio_0_e_100()    

while acerto == False:
    contador += 1
    numero_usuario = solicita_numero_ao_usuario()
    acerto = verificar_acerto(numero_usuario, numero_aleatorio)

print('Parabéns você acertou!!!! Foram necessárias ',contador, ' tentativas!') 