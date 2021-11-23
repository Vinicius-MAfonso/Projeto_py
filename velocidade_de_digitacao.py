from time import sleep
from tkinter import *
import random
from main import window


def sorteador():
    palavras = ['manga', 'laranja', 'olá', 'banana', 'indore', 'hospital', 'python', 'java', 'jamghat', 'ratlam',
                'vaca', 'amarelo', 'preto', 'computador', 'azul']
    random.shuffle(palavras)
    print(random.choice(palavras))
    palavra = random.randint(0, (len(palavras) - 1))
    return palavra


def countdown(num_of_secs):
    contador = num_of_secs
    while num_of_secs >= 0:
        contador = contador + 1
        sleep(1)

# cronometro = Label(main_menu, text=countdown(180))
