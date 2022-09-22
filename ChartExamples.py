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

# добавление метки заголовка
lbl_title = tk.Label(text='Примеры построения графиков', font=('Bahnschrift', 16, 'bold'  ), fg = '#0000cc', bg= '#8fffff')
lbl_title.place(x=55, y=30)


# добавление кнопки закрытия
btn_close = tk.Button(window, text="Закрыть", font=('Bahnschrift', 12, 'bold'), command = do_close)
btn_close.place(x=330, y=400, width = 90, height = 30)


# запуск цикла
window.mainloop()