# Примеры построения графиков
# автор: Bignick, bignick58@gmail.com

import tkinter as tk

#
def do_close():
    window.destroy()

# создание главного окна программы
window = tk.Tk()
window.geometry("450x450")
window['bg'] = '#8fffff'
window.title('Примеры построения графиков')

# добавление кнрпки закрытия
btn_close = tk.Button(window, text="Закрыть", font=('Bahnschrift', 12, 'bold'))
btn_close.place(x=330, y=400, width = 90, height = 30)


# запуск цикла
window.mainloop()