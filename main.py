from tkinter import *
from timeit import default_timer as timer
import random

window = Tk()
window.title("Velocidade de digitação")
window.geometry("500x300+200+200")
window.resizable(False, False)
window.iconbitmap("images/icon.ico")
window['bg'] = "#023e8a"


# class Pontuacao:
#
#     def __init__(self, pontos, ganhar, perder):
#         self.pontos = 0
#         self.perder = ganhar
#         self.ganhar = perder
#         self.verpontos = pontos
#
#     def perder(self):
#         self.pontos -= 25
#
#     def ganhar(self):
#         self.pontos += 50
#
#     def verpontos(self):
#         self.verpontos()
#         print(self.verpontos())


def check_result():
    if entry.get() == words[word]:
        end = timer()
        print(end - start)
        Pontuacao.ganhar()
    else:
        print("Wrong Input")
        Pontuacao.perder()


words = ['manga', 'laranja', 'olá', 'banana', 'indore', 'hospital', 'python', 'java', 'ratlam',
         'vaca', 'amarelo', 'preto', 'computador', 'azul']

word = random.randint(0, (len(words) - 1))

start = timer()

sorteado = Label(window, text=words[word], font="arial 20", bg="#90e0ef")
sorteado.place(x=160, y=85)

lb_titulo = Label(window, text="Teste sua velocidade para digitar!", font="times 20", bg="#0077b6", fg="white")
lb_titulo.place(x=65, y=25)

entry = Entry(window)
entry.place(width=200, height=25, x=160, y=147)

lb_box = Label(window, bg="#0096c7", width=14, height=5)
lb_box.place(x=15, y=95)

lb_score_title = Label(window, text="Pontuação", font="times 15", fg="white", bg="#0096c7")
lb_score_title.place(x=25, y=100)

lb_score = Label(window, text="200", font="times 15", fg="yellow", bg="#0096c7")
lb_score.place(x=49, y=145)

btn_resetar_tempo = Button(window, text="Palavra feita!", font="arial 10", command=check_result, padx=5, pady=2,
                           bg='#caf0f8')
btn_resetar_tempo.place(x=370, y=146)

btn_resetar_tempo = Button(window, text="Resetar o jogo", font="arial 10", command=check_result, padx=15, pady=5,
                           bg='#caf0f8')
btn_resetar_tempo.place(x=160, y=200)

window.mainloop()
