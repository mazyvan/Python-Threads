import threading
import sys
import time
from random import randint

print('SUPER THREADING GAME v0.1   By Iván Sánchez')
print()
# Declaramos nuestras variables globales para guardar los numeros aleatorios
number1 = 0
number2 = 0
ejecutarHilo_1 = True
ejecutarHilo_2 = True


# Declaramos la función que genera un nuevo número aleatorio
def generate_random_number():
    return randint(1, 99)


def hilo1():
    global number1, ejecutarHilo_1
    time.sleep(100 / generate_random_number())
    while ejecutarHilo_1:
        number1 = generate_random_number()
        print('Hilo 1: ' + str(number1))
        print('')
        time.sleep(3)


def hilo2():
    global number2, ejecutarHilo_2
    time.sleep(100 / generate_random_number())
    while ejecutarHilo_2:
        number2 = generate_random_number()
        print('Hilo 2: ' + str(number2))
        print('')
        time.sleep(3)


print('Muy bien, las instrucciones son simples. En la pantalla apareceran numeros aleatorios entre el 0 y el 100')
print('Tu mision (si decides aceptarla 8) sera intruducir esos valores antes de que el tiempo termine')
print('Si no logras ingresar los valores, el juego continuara generando números aleatorios')
start = input('>> ¿Deseas comenzar el desafio? (yes) (y/n): ')
if start == 'n' or start == 'no':
    print('Ahh...  que nena :(')
    sys.exit()

print()
print('Ready?    Goo!')
print()
time.sleep(1)
start_time = time.time()

hilo_1 = threading.Thread(target=hilo1)
hilo_1.start()
hilo_2 = threading.Thread(target=hilo2)
hilo_2.start()

while hilo_1.isAlive() or hilo_2.isAlive():
    isThisNumber = int(input(''))
    if isThisNumber == number1:
        ejecutarHilo_1 = False
        print('Bien mataste al hilo 1')
        print('')
    elif isThisNumber == number2:
        ejecutarHilo_2 = False
        print('Bien mataste al hilo 2')
        print('')
    else:
        print('Uy, que lento!')

final_time = time.time() - start_time

print('Has terminaado con todos los hilos ¡Felicidades!')
print('/---------------------------------------------------\ ')
print('|                SCORE / PUNTUACION                 |')
print('|---------------------------------------------------| ')
print('|----------|----------------------------------------| ')
print('|   Time   |              ' + str(final_time) + ' Seg    |')
print('\----------|----------------------------------------/ ')
