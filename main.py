from tkinter import *
from time import sleep


def countdown(num_of_secs):
    contador = num_of_secs
    while num_of_secs >= 0:
        contador=contador+1
        sleep(1)


main_menu = Tk()
main_menu.title("Demencia verifier")

main_menu.geometry("500x300+200+200")
main_menu.resizable(False, False)
main_menu.iconbitmap("images/icon.ico")
main_menu['bg'] = "#90e0ef"

# Botão para resetar o tempo

btn_resetar_tempo = Button(main_menu, text="Resetar tempo", command=lambda: countdown(180), anchor="center")
# cronometro = Label(main_menu, text=countdown(180))


# Tamanho quando maximizar -->
# main_menu.minsize()
# main_menu.maxsize()

btn_resetar_tempo.pack()
main_menu.mainloop()

main_menu.colorchooser.chooser()
