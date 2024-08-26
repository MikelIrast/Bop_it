import random
from IPython.display import Audio, display
from threading import Timer # Cuenta regresiva
import time

def seleccionar_estado():
    '''Seleccionar aleatoriamente uno de los tres posibles estados'''
    estado = random.choice(("gira", "estira", "bop-it"))
    return estado

def comando_voz(estado):
    '''Reproduce el comando de voz asociado al estado seleccionado'''
    # Leer el archivo de audio
    sonido = Audio(filename='./' + estado + '.wav', autoplay=True)
    # Reproducir el sonido
    display(sonido, clear=True)

def interaccion_usuario(estado):    
    # Solicitar entrada al usuario
    tecla = input('PULSE TECLA: ')
    # Convertir la tecla oprimida a minúsculas en caso de que el teclado esté en mayúscula
    tecla = tecla.lower()
    # Imprimir valores para depuración
    print(f'Estado: {estado}, Tecla presionada: {tecla}')
    
    # Verificación
    exito = False
    if (estado == 'bop-it') and (tecla == 's'):
        exito = True
    elif (estado == 'estira') and (tecla == 'a'):
        exito = True
    elif (estado == 'gira') and (tecla == 'd'):
        exito = True
    
    return exito

# Variables iniciales
puntaje = 0
timeout = 3  # El tiempo asignado inicialmente al usuario
delta = 0.1  # El tiempo (en segundos) que se irá reduciendo de la cuenta regresiva
success = True

while success:
    # Seleccionar el estado
    estado = seleccionar_estado()
    
    # Crear timer
    t = Timer(timeout, print, ["¡SE ACABÓ EL TIEMPO!"])
    t.start()  # Iniciar cuenta regresiva
    
    # Ejecutar el comando de voz correspondiente
    comando_voz(estado)
    print(estado)
    
    # Interacción con el usuario y verificar el resultado
    success = interaccion_usuario(estado)
    t.cancel() # Cancelar el temporizador si el usuario interactúa
    
    if not success or not t.is_alive():  # Si no hubo éxito o el tiempo se agotó, salir del bucle
        break
    
    # Incrementar el puntaje y reducir el tiempo si el usuario tuvo éxito
    if success:
        puntaje += 1
        if timeout - delta > 0:  # Evitar valores negativos
            timeout -= delta

print(f"Puntaje final: {puntaje} puntos")
