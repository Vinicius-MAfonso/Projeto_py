from tkinter import *
import velocidade_de_digitacao

window = Tk()
window.title("Velocidade de digitação")

window.geometry("500x300+200+200")
window.resizable(False, False)
window.iconbitmap("images/icon.ico")
window['bg'] = "#90e0ef"

entry = Entry(window)
entry.place(width=200,height = 25, x=155, y=150)

label = Label(text="Bem vindo ao jogo")
btn_resetar_tempo = Button(window, text="Resetar o jogo", padx=50, pady=5)
btn_resetar_tempo.pack(side=BOTTOM, padx=50, pady=50)

window.mainloop()
window.colorchooser.chooser()
