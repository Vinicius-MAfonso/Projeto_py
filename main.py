from tkinter import *
import random
import time


def verificador():
    if entry.get() == palavra_sorteada:
        print("Acertou!")
    else:
        print("Errou")


def countdown(num_of_secs):
    contador = num_of_secs
    while num_of_secs >= 0:
        contador = contador - 1
        time.sleep(1)
        return str(contador)


def sorteador():
    palavras = ['manga', 'laranja', 'olá', 'banana', 'indore', 'hospital', 'python', 'java', 'ratlam',
                'vaca', 'amarelo', 'preto', 'computador', 'azul']
    random.shuffle(palavras)
    return random.choice(palavras)


window = Tk()
window.title("Velocidade de digitação")

window.geometry("500x300+200+200")
window.resizable(False, False)
window.iconbitmap("images/icon.ico")
window['bg'] = "#90e0ef"

lb_titulo = Label(window, text="Teste sua velocidade para digitar!", font="times 20", bg="#0077b6")
lb_titulo.place(x=80, y=25)

lb_cont = Label(window, text=countdown(180), fg="white", bg="#0077b6")
lb_cont.place(x=380, y=150)

palavra_sorteada = sorteador()
lb_palavra_sorteada = Label(window, text=palavra_sorteada, fg="white", font="times 18", bg="#0077b6")
lb_palavra_sorteada.place(x=250, y=100)

lb_score_title = Label(window, text="Pontuação", font="times 15", fg="black")
lb_score_title.place(x=73, y=100)

lb_score = Label(window, text="200", font="times 10", fg="black")
lb_score.place(x=100, y=150)

entry = Entry(window)
entry.place(width=200, height=25, x=160, y=150)
verificador()

btn_resetar_tempo = Button(window, text="Resetar o jogo", padx=25, pady=5, bg="#caf0f8", command=countdown(180))
btn_resetar_tempo.pack(side=BOTTOM, pady=50)

window.mainloop()
window.colorchooser.chooser()
