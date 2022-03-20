import random
numero_aleatorio = random.randrange(0,100)
gane = False
print("Tenes 5 intentos para adivinar un numero entre 0 y 100")
intento_num = 1
while ((intento_num < 6) and (not gane)):
    numero_ingresado = int(input('Ingresa tu numero: '))
    if numero_ingresado == numero_aleatorio:
        print('Ganaste! y necesitaste {} intentos!!!'.format(intento_num))
        gane = True
    else:
        print('Ese no es el numero, segui intentando.')
        intento_num += 1
if not gane:
    print('\n Perdiste :(\n El numero era: {}'.format(numero_aleatorio))