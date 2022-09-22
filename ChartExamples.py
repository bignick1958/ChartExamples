# Примеры построения графиков
# автор: Bignick, bignick58@gmail.com

import tkinter as tk

import chart1, chart2


#
def do_close():
    window.destroy()


# создание главного окна программы
window = tk.Tk()
window.geometry("450x450")
window['bg'] = '#8fffff'
window.title('Примеры построения графиков')

# добавление метки заголовка
lbl_title = tk.Label(text='Примеры построения графиков', font=('Bahnschrift', 16, 'bold'), fg='#0000cc', bg='#8fffff')
lbl_title.place(x=55, y=30)

# добавление кнопки и метки для графика 1
btn_chart1 = tk.Button(window, text='График 1',  font=('Helvetica', 12, 'bold'), command=chart1.plot_chart)
btn_chart1.place(x=40 , y=115, width=90, height=30)

lbl_chart1 = tk.Label(window, text='График синуса MatPlotLib', bg='#8fffff', font=('Helvetica', 10))
lbl_chart1.place(x= 170, y=122)

# добавление кнопки и метки для графика 2
btn_chart2 = tk.Button(window, text='График 2',  font=('Helvetica', 12, 'bold'), command=chart2.plot_chart)
btn_chart2.place(x=40 , y=165, width=90, height=30)

lbl_chart2 = tk.Label(window, text='Нормальное распределение', bg='#8fffff', font=('Helvetica', 10))
lbl_chart2.place(x= 170, y=172)


# добавление кнопки закрытия
btn_close = tk.Button(window, text="Закрыть", font=('Bahnschrift', 12, 'bold'), command=do_close)
btn_close.place(x=330, y=400, width=90, height=30)

# запуск цикла
window.mainloop()
