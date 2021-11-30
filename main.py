from tkinter import *
from timeit import default_timer as timer
import random

frases = ['A dúvida já é a resposta',
          'Deixe pra trás o que não te leva pra frente',
          'Se for pra desistir, desista de ser fraco',
          'Aqui se faz, aqui se paga',
          'Sem sacrifício, não há vitória',
          'Você é o que escolhe ser',
          'Gel de cabelo é muito gorduroso',
          'O Feitiço das Gêmeas',
          'Popularidade é desejada por todos',
          'Eu sou alérgico a abelhas e amendoins',
          'Meu presente preferido é chocolate',
          'Apenas para sua informação',
          'O meu navegador favorito',
          'Esta é uma ideia muito boa',
          ]


def game():
    start = timer()
    def func(event):
        if entry.get() == frases[word]:
            end = timer()
            resultados(end - start)
        else:
            print("Wrong Input")

    root = Tk()
    root.title("Velocidade de digitação")
    root.geometry("500x300+200+200")
    root.resizable(False, False)
    root.iconbitmap("images/icon.ico")
    root['bg'] = "#023e8a"

    word = random.randint(0, (len(frases) - 1))

    start = timer()

    sorteado = Label(root, text=frases[word], font="arial 13", bg="white", justify=LEFT)
    sorteado.place(width=300, height=25, x=95, y=80)

    lb_titulo = Label(root, text="Comece a digitar!", font="times 20", bg="#0077b6", fg="white", )
    lb_titulo.place(x=145, y=25)

    entry = Entry(root, font="arial 15")
    entry.place(width=280, height=25, x=100, y=200)
    func(entry)
    # Botão enter
    root.bind('<Return>', func)
    # Dica
    lb_dica = Label(root, text="Pressione 'enter' \npara confirmar a palavra!", font="times 10", bg="#023e8a",
                    fg="white")
    lb_dica.place(x=170, y=250)

    root.mainloop()


def resultados(tempo):
    start.quit()
    niveis = ['Bom', 'Mediano', 'Ruim']
    if tempo < 6:
        resultado = niveis[0]
    elif tempo >= 6 or tempo < 10:
        resultado = niveis[1]
    else:
        resultado = niveis[2]
    resultados = Tk()
    resultados.title("Velocidade de digitação")
    resultados.geometry("300x200+200+200")
    resultados.resizable(False, False)
    resultados.iconbitmap("images/icon.ico")
    resultados['bg'] = "#023e8a"

    lb_score_title = Label(resultados, text="Resultados", font="times 15", fg="white", bg="#0096c7")
    lb_score_title.place(x=5, y=10)

    lb_result = Label(resultados, text="Resultado geral:", font="times 12", fg="white", bg="#023e8a")
    lb_result.place(x=5, y=50)

    lb_result_result = Label(resultados, text=resultado, font="times 12", fg="white", bg="#023e8a")
    lb_result_result.place(x=110, y=50)

    lb_time = Label(resultados, text="Tempo levado:", font="times 12", fg="white", bg="#023e8a")
    lb_time.place(x=5, y=80)

    lb_time_result = Label(resultados, text=tempo, font="times 12", fg="white", bg="#023e8a")
    lb_time_result.place(x=110, y=80)
    btn_resetar_tempo = Button(resultados, text="Resetar o jogo", font="arial 10", padx=15, pady=5,
                               bg='#caf0f8', command=game)
    btn_resetar_tempo.place(x=80, y=150)

    resultados.mainloop()


start = Tk()
start.title("Velocidade de digitação")
start.geometry("500x200+200+200")
start.resizable(False, False)
start.iconbitmap("images/icon.ico")
start['bg'] = "#023e8a"

lb_titulo = Label(start, text="Teste sua velocidade para digitar!", font="times 20", bg="#0077b6", fg="white", )
lb_titulo.place(x=65, y=25)

btn_resetar_tempo = Button(start, text="Comece o jogo", font="arial 10", padx=15, pady=5,
                           bg='#caf0f8', command=game)
btn_resetar_tempo.place(x=180, y=90)

start.mainloop()
