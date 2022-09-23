# Примеры построения графиков
# автор: Bignick, bignick58@gmail.com

import tkinter as tk

import chart1, chart2, chart3

#
def do_close():
    window.destroy()


# создание главного окна программы
window = tk.Tk()
window.geometry("450x550")
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
lbl_chart2.place(x= 170, y=162)

# добавление кнопки и метки для графика 3
btn_chart3 = tk.Button(window, text='График 3',  font=('Helvetica', 12, 'bold'), command=chart2.plot_chart2)
btn_chart3.place(x=40 , y=205, width=90, height=30)

lbl_chart3 = tk.Label(window, text='Нормальное распределение - 3 ГРАФИКА', bg='#8fffff', font=('Helvetica', 10))
lbl_chart3.place(x= 170, y=202)

# добавление кнопки и метки для графика 4
btn_chart4 = tk.Button(window, text='График 4',  font=('Helvetica', 12, 'bold'), command=chart3.plot_chart)
btn_chart4.place(x=40 , y=245, width=90, height=30)

lbl_chart4 = tk.Label(window, text='Гистограмма Seaborn', bg='#8fffff', font=('Helvetica', 10))
lbl_chart4.place(x= 170, y=242)

# добавление кнопки и метки для графика 5
btn_chart5 = tk.Button(window, text='График 5',  font=('Helvetica', 12, 'bold'), command=chart3.plot_chart2)
btn_chart5.place(x=40 , y=285, width=90, height=30)

lbl_chart5 = tk.Label(window, text='Сдвоенная истограмма Seaborn', bg='#8fffff', font=('Helvetica', 10))
lbl_chart5.place(x= 170, y=282)

# добавление кнопки и метки для графика 6
btn_chart6 = tk.Button(window, text='График 6',  font=('Helvetica', 12, 'bold'), command=chart2.plot_chart)
btn_chart6.place(x=40 , y=325, width=90, height=30)

lbl_chart6 = tk.Label(window, text='Описание графика', bg='#8fffff', font=('Helvetica', 10))
lbl_chart6.place(x= 170, y=322)

# добавление кнопки и метки для графика 7
btn_chart7 = tk.Button(window, text='График 7',  font=('Helvetica', 12, 'bold'), command=chart2.plot_chart)
btn_chart7.place(x=40 , y=365, width=90, height=30)

lbl_chart7 = tk.Label(window, text='Описание графика', bg='#8fffff', font=('Helvetica', 10))
lbl_chart7.place(x= 170, y=362)

# добавление кнопки закрытия
btn_close = tk.Button(window, text="Закрыть", font=('Bahnschrift', 12, 'bold'), command=do_close)
btn_close.place(x=330, y=500, width=90, height=30)

# запуск цикла
window.mainloop()
