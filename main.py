from tkinter import *
from timeit import default_timer as timer
import random
from threading import Timer


def resultados(tempo):
    niveis = ['Bom', 'Mediano', 'Ruim']
    if tempo < 10:
        resultado = niveis[0]
    elif tempo >= 10 or tempo < 20:
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
                               bg='#caf0f8')
    btn_resetar_tempo.place(x=80, y=150)

    resultados.mainloop()


def func(event):
    if entry.get() == words[word]:
        end = timer()
        print(end - start)
        resultados(end - start)
    else:
        print("Wrong Input")
    # Pontuacao.perder()


def game(event):
    root = Tk
    root.mainloop()


root = Tk()
root.title("Velocidade de digitação")
root.geometry("500x300+200+200")
root.resizable(False, False)
root.iconbitmap("images/icon.ico")
root['bg'] = "#023e8a"

words = ['Imagine uma nova história para \nsua vida e acredite nela',
         'A alegria de fazer o bem é a única \nfelicidade verdadeira', 'A persistência é o caminho do êxito',
         'Quem semeia a injustiça colherá \na desgraça', 'Deixa para trás o que não te leva \npara frente',
         'A dúvida já é a resposta',
         'Você viverá uma vida monótona e \nentediante se não correr riscos!',
         'Eu não tenho sonhos, eu tenho \nobjetivos',
         'Quanto mais alto, maior é a queda',
         'A imaginação é mais \nimportante que o conhecimento']

word = random.randint(0, (len(words) - 1))

start = timer()

sorteado = Label(root, text=words[word], font="arial 15", bg="#90e0ef", justify=CENTER)
sorteado.place(x=100, y=80)

lb_titulo = Label(root, text="Teste sua velocidade para digitar!", font="times 20", bg="#0077b6", fg="white", )
lb_titulo.place(x=65, y=25)

entry = Entry(root, font="arial 15")
entry.place(width=280, height=25, x=100, y=200)

# # Cronometro
# lb_box_cronometro = Label(root, bg="#0096c7", width=14, height=5)
# lb_box_cronometro.place(x=384, y=95)
# lb_cronometro_title = Label(root, text="Tempo restante", font="times 12", fg="white", bg="#0096c7")
# lb_cronometro_title.place(x=385, y=100)
# lb_cronometro = Label(root, text="200", font="times 15", fg="yellow", bg="#0096c7")
# lb_cronometro.place(x=415, y=145)

# Botão enter

root.bind('<Return>', func)
# Dica
lb_dica = Label(root, text="Pressione 'enter' \npara confirmar a palavra!", font="times 10", bg="#023e8a",
                fg="white")
lb_dica.place(x=170, y=250)

root.mainloop()
