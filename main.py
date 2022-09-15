import random
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
iniciar_trivia = True
intentos = 0
while iniciar_trivia == True:
    intentos += 1
    puntaje3 = random.randint(0, 10)
    numero_carga = 0
    print("\nIntento número:", intentos)
    print(MAGENTA + "El juego empezara en" + RESET)
    for numero_carga in range(5, 0, -1):
        print(numero_carga)
        time.sleep(1)
    print(GREEN + 'Bienvenido a la trivia sobre The lord of the Rings')
    time.sleep(1)
    print('\nPondremos a Prueba tus conocimientos')
    time.sleep(1)
    nombre = input('\nIngresa tu nombre o nickname: ' + RESET)
    print(
        BLUE + '\nMuy buen dia', nombre,
        ',Responde las siguientes preguntas escribiendo la letra de la alternativa correcta y presionando ENTER para enviar tu respuesta :\n '
    )
    time.sleep(4)
    print(
        'El juego consta de 4 preguntas ,en la primera pregunta todas las alternativas tienen puntaje;Mientras más te acerques a la alternativa correcta mas puntos ganaras'
        + RESET)
    time.sleep(4)
    print(YELLOW + '\nEmpezemos')
    time.sleep(2)
    puntaje1 = 0
    print('\n1) Aragon es heredero de?')
    print('\na) heredero de Isildur-heredero del trono de Gondor')
    print('b) heredero de Moria - heredero de Minas Tirith')
    print(
        'c) heredero de la tierra media- heredero de todo aquello que toca el sol'
    )
    print('d) heredero de la comarca -heredero de una casa bolson')
    respuesta_1 = input(RED + '\nTu respuesta:' + RESET)
    while respuesta_1 not in ('a', 'b', 'c', 'd'):
        print(CYAN + 'Debes responder a ,b,c o d .')
        time.sleep(1)
        respuesta_1 = input('\nIngresa tu respuesta: ' + RESET)

    if respuesta_1 == 'b':
        puntaje1 += 3
        print('Incorrecto', nombre, ',Ganas 3 puntos')
        time.sleep(1)
    elif respuesta_1 == 'c':
        puntaje1 += 7
        print('Incorrecto', nombre, ',Ganas 7 puntos')
        time.sleep(1)
    elif respuesta_1 == 'd':
        puntaje1 += 5
        print('Incorrecto', nombre, ',Ganas 5 puntos')
        time.sleep(1)
    else:
        puntaje1 += 10
        print('Correcto', nombre, ',Ganas 10 puntos ')
        time.sleep(1)
    print('\nTu puntaje es', puntaje1)
    time.sleep(1)
    print(
        BLUE +
        '\nLa segunda pregunta solo te dara puntos si  aciertas a la alternativa correcta'
        + RESET)
    time.sleep(2)
    print(YELLOW + '\n2)Quien es el tio de Frodo Bolson?')
    print('\na)Gandalf')
    print('b)Bilbo')
    print('c)Thorin')
    print('d)Sauron' + RESET)
    puntaje2 = 0
    respuesta_2 = input(RED + '\nTu respuesta:' + RESET)
    while respuesta_2 not in ('a', 'b', 'c', 'd'):
        print(CYAN + 'Debes responder a ,b,c o d .')
        time.sleep(1)
        respuesta_2 = input(print('\nIngresa tu respuesta: ' + RESET))
    if respuesta_2 == 'b':
        puntaje2 += 10
        print('\nCorrecto', nombre, 'Ganas 10 puntos')
        time.sleep(1)
    else:
        puntaje2 = 0
        print('\nIncorrecto', nombre, 'No ganas puntos')
    puntajeacu = puntaje1 + puntaje2
    time.sleep(1)
    print('\nTu puntaje acumulado es', puntajeacu, '' + RESET)
    time.sleep(1)
    print(
        BLUE +
        '\nAhora la tercera pregunta.Esta pregunta consta en asumir un riesgo ,en el cual tu escogeras un numero del 1 al 10 y si respondas correctamente , el numero que elegiste multiplicara a tu puntaje acumulado , pero si fallas ese mismo numero que elegiste se restara de tu puntaje acumulado.'
        + RESET)
    time.sleep(5)
    apuesta = int(input(YELLOW + '\nIngresar numero:'))
    print('Empezemos')
    time.sleep(1)
    print(
        '\n2)Quien es la criatura demoniaca que ataca a gandalf y se lo llevo al inframundo?'
    )
    print('\na)Baltraj')
    print('b)Belrog')
    print('c)Bolrog')
    print('d)Balrog' + RESET)
    respuesta_4 = input(RED + '\nTu respuesta:' + RESET)
    while respuesta_4 not in ('a', 'b', 'c', 'd'):
        print(CYAN + 'Debes responder a ,b,c o d .')
        time.sleep(1)
        respuesta_4 = input('\nIngresa tu respuesta: ' + RESET)
    puntaje4 = 0
    if respuesta_4 == 'a':
        puntaje4 = puntajeacu - apuesta
        print('Incorrecto', nombre, ',Pierdes', apuesta, 'puntos')
        time.sleep(1)
        print('tu puntaje acumulado es', puntaje4)
        time.sleep(1)
    elif respuesta_4 == 'b':
        puntaje4 = puntajeacu - apuesta
        print('Incorrecto', nombre, ',Pierdes', apuesta, 'puntos')
        time.sleep(1)
        print('tu puntaje acumulado es', puntaje4)
        time.sleep(1)
    elif respuesta_4 == 'c':
        puntaje4 = puntajeacu - apuesta
        print('Incorrecto', nombre, ',Pierdes', apuesta, 'puntos')
        time.sleep(1)
        print('tu puntaje acumulado es', puntaje4)
        time.sleep(1)
    else:
        puntaje4 = puntajeacu * apuesta
        print('Correcto', nombre)
        time.sleep(1)
        print('tu puntaje acumulado es', puntaje4)
        time.sleep(1)
    print(
        BLUE +
        '\nAhora la cuarta y ulitma pregunta, recordar que esta es opcional ,ya que,si decides responderla te puede sumar una puntuacion al azar entre 1 a 10 puntos pero si fallas te restara de igual forma.'
        + RESET)
    time.sleep(3)
    puntajeacu2 = 0
    print(YELLOW + '\nTu respusta solo puede ser si o no')
    sigues1 = input('\nDeseas realizar esta pregunta:' + RESET)
    while sigues1 not in ('si', 'no'):
        sigues1 = input(
            print(CYAN + 'Solo puedes poner si o no ,Ingrese su respuesta:' +
                  RESET))
    if sigues1 == 'no':
        time.sleep(1)
        print('\nMuy bien , Aqui culmina la trivia ,muchas gracias por jugar',
              nombre, 'tu puntajes es', puntaje4)
    else:
        print(YELLOW + '\nEntonces muchas suerte, la pregunta es:')
        time.sleep(1)
        print('\n3)Quien es el autor del señor de los anillos?')
        print('\na)Suzanne Collins')
        print('b)Richard Dawkins')
        print('c)J. K. Rowling')
        print('d)J. R. R. Tolkien' + RESET)
        respuesta_3 = input(RED + '\nIngrese su respuesta:' + RESET)
        while respuesta_3 not in ('a', 'b', 'c', 'd'):
            print(CYAN + 'Debes responder a ,b,c o d .')
            time.sleep(1)
            respuesta_3 = input('\nIngresa tu respuesta: ' + RESET)
        if respuesta_3 == "d":
            print('\nCorrecto ganas', puntaje3, 'puntos')
            puntajeacu2 = puntaje3 + puntaje4
            time.sleep(1)
            print('Muy bien', nombre, 'Aqui culmina la trivia ,tu puntajes es',
                  puntajeacu2)
        else:
            print('\nIncorrecto pierdes', puntaje3, 'puntos')
            puntajeacu2 = puntaje4 - puntaje3
            time.sleep(1)
            print('Muy bien', nombre, 'Aqui culmina la trivia ,tu puntajes es',
                  puntajeacu2)
    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower(
        )
    if repetir_trivia != "si":
        print("\nEspero que lo hayas pasado bien, hasta pronto!")
        iniciar_trivia = False
