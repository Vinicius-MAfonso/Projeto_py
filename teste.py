from tkinter import *
from timeit import default_timer as Timer
import random
from palavras import frases


def sair():
    start.destroy()


def game():

    def resultados(tempo):

        niveis = ['Bom', 'Mediano', 'Ruim']
        if tempo < 6:
            resultado = niveis[0]
        elif tempo >= 6 or tempo < 10:
            resultado = niveis[1]
        else:
            resultado = niveis[2]

        lb_result = Label(root, text="Resultado geral:", font="times 12", fg="white", bg="#023e8a")
        lb_result.place(x=120, y=120)

        lb_result_result = Label(root, text=resultado, font="times 12", fg="white", bg="#023e8a")
        lb_result_result.place(x=240, y=120)

        lb_time = Label(root, text="Tempo levado:", font="times 12", fg="white", bg="#023e8a")
        lb_time.place(x=120, y=150)

        lb_time_result = Label(root, text=tempo, font="times 12", fg="white", bg="#023e8a")
        lb_time_result.place(x=240, y=150)
        btn_resetar_jogo = Button(root, text="Sair do jogo", font="arial 10", padx=15, pady=5,
                                  bg='#caf0f8', command= root.destroy)
        btn_resetar_jogo.place(x=350, y=250)

    timer = Timer()

    root = Tk()
    root.title("Velocidade de digitação")
    root.geometry("500x300+200+200")
    root.resizable(False, False)
    root.iconbitmap("images/icon.ico")
    root['bg'] = "#023e8a"

    word = random.randint(0, (len(frases) - 1))

    timer = Timer()

    sorteado = Label(root, text=frases[word], font="arial 13", bg="white", justify=LEFT)
    sorteado.place(width=300, height=25, x=95, y=80)

    lb_titulo = Label(root, text="Comece a digitar!", font="times 20", bg="#0077b6", fg="white", )
    lb_titulo.place(x=145, y=25)

    def func(event):
        if entry.get() == frases[word]:
            end = Timer()
            resultados(end - timer)
        elif entry.get() != frases[word]:
            print("Palavra errada!")

    entry = Entry(root, font="arial 15")
    entry.place(width=280, height=25, x=100, y=200)
    func(entry)
    root.bind('<Return>', func)
    lb_dica = Label(root, text="Pressione 'enter' \npara confirmar a palavra!", font="times 10", bg="#023e8a",
                    fg="white")
    lb_dica.place(x=170, y=250)
    root.mainloop()


start = Tk()
start.title("Velocidade de digitação")
start.geometry("500x200+200+200")
start.resizable(False, False)
start.iconbitmap("images/icon.ico")
start['bg'] = "#023e8a"

lb_titulo = Label(start, text="Teste sua velocidade para digitar!", font="times 20", bg="#0077b6", fg="white", )
lb_titulo.place(x=65, y=25)

btn_start = Button(start, text="Comece o jogo", font="arial 10", padx=15, pady=5,
                   bg='#caf0f8', command=lambda: [start.destroy(), game()])
btn_start.place(x=100, y=90)

btn_sair = Button(start, text="Sair do jogo", font="arial 10", padx=15, pady=5,
                  bg='#caf0f8', command=sair)
btn_sair.place(x=280, y=90)

start.mainloop()
