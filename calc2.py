from tkinter import *

# function
def button_click(value):
    current = str(layar.get())

    # Menambahkan operator hanya jika operator baru ditekan
    if value in {'+', '-', '*', '/','%'}:
        if current and current[-1] in {'+', '-', '*', '/','%'}:
            # Menggantikan operator terakhir dengan operator baru
            current = current[:-1]

    layar.delete(0, END)
    layar.insert(END, current + str(value))
    
def toggle_sign():
    current = str(layar.get())
    if current and current[0] == '-':
        current = current[1:]  # Remove the negative sign
    else:
        current = '-' + current  # Add the negative sign

    layar.delete(0, END)
    layar.insert(END, current)
    
def calculate():
    try:
        # Mengganti '%' dengan '/100' untuk menangani persentase
        expression = layar.get().replace('%', '/100')
        hasil = eval(expression)
        layar.delete(0, END)
        layar.insert(END, str(hasil))
    except:
        layar.delete(0, END)
        layar.insert(END, 'Error')

    
def clear_layar():
    layar.delete(0, END)
    
def delete_satu():
    current = str(layar.get())
    if current:
        current = current[:-1]
        layar.delete(0, END)
        layar.insert(END, current)
    
def button_click_handler(value):
    if value in {'+', '-', '*', '/', '%'}:
        button_click(value)
    elif value == '=':
        calculate()
    elif value == 'C':
        clear_layar()
    elif value == 'DEL':
        delete_satu()
    elif value == "+/-":
        toggle_sign()
    else:
        button_click(value)

# Tampilan Aplikasi
app = Tk()
app.title('Simple Calc')

# Memberikan warna latar belakang pada aplikasi
app.configure(bg='lightblue')

layar = Entry(app, width=10, borderwidth=5, font=('Arial', 30))
layar.grid(row=0, column=0, padx=8, pady=8, columnspan=5)

tombol = [
    'C', 'DEL', '(', ')', '%',
    '7', '8', '9', '/', '*',
    '4', '5', '6', '-', '+',
    '1', '2', '3', '', '',
    '+/-', '0', '.', '', '=',
]

row_value = 1
col_value = 0

for button in tombol:
    Button(app, text=button, width=4, height=2, command=lambda b=button: button_click_handler(b)).grid(padx=5, pady=5, row=row_value, column=col_value)
    col_value += 1    
    if col_value > 4:
        col_value = 0
        row_value += 1

app.mainloop()
