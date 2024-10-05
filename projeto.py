import random

times = ['pikachu', 'squirtle', 'mewtwo', 'charmander', 'bandeira', 'gengar']
saldo = 0

while True:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n' \
          'Bem-vindo blablabla\n' \
          'Insira um comando númerico de 1 a 5\n' \
          '=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n'
          )
    comando = int(input('Comando: '))

    if comando not in range(1,6):
        print("Comando inválido!\nDigite um novo comando.\n")
    else:
        if comando == 1:    #comando para verificar saldo
            pass
        elif comando == 2:  #comando para comer batatinha
            pass
        elif comando == 3:
            pass
        elif comando == 4:
            pass
        elif comando == 5:
            print('volte sempre!')
            break