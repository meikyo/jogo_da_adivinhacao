import random


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


numero_aleatorio = gerar_numero_aleatorio_0_e_100()    
numero_usuario = solicita_numero_ao_usuario()



print('esse é o número gerado', numero_aleatorio, 'numero do usuario', numero_usuario)