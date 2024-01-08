from tkinter import *
 
def button_click_operator(value):
    current = str(layar.get())
    if current and current[-1] in {'+','-','*','/'}:
        current = current[:-1]
    layar.delete(0,END)
    layar.insert(END,surrent + str(value))

def button_click(value):
    current = str(layar.get())
    layar.delete(0, END)
    layar.insert(END, current + str(value))

def hitung():
    try:
        hasil = eval(layar.get())
        layar.delete(0, END)
        layar.insert(END, str(hasil))
    except:
        layar.delete(0, END)
        layar.insert(END, str('error'))

def hapus_all():
    layar.delete(0, END)

def hapus_satu():
    current = str(layar.get())
    if current:
        current = current[:-1]
        layar.delete(0, END)
        layar.insert(END, current)

def button_handler(value):
    if value in {'+', '-', '*', '/'}:
        button_click_operator(value)
    elif value == '=':
        hitung()
    elif value == 'C':
        hapus_all()
    elif value == 'DEL':
        hapus_satu()
    else:
        button_click(value)

calc = Tk()
calc.title("testCalc")

layar = Entry(calc, width=10, borderwidth=5, font=("Arial", 30))
layar.grid(row=0, column=0, padx=8, pady=8, columnspan=5)

tombol = [
    {'text': 'C', 'bg': 'orange'},
    {'text': 'DEL', 'bg': 'yellow'},
    {'text': '*', 'bg': 'lightblue'},
    {'text': '/', 'bg': 'lightblue'},
    '7', '8', '9', {'text': '-', 'bg': 'lightblue'},
    '4', '5', '6', {'text': '+','bg': 'lightblue'},
    '1', '2', '3', {'text': '=','bg': 'cyan'},
    '.', '0', '00','000',
]

row_val = 1
col_val = 0

for button in tombol:
    if isinstance(button, dict):
        Button(calc, text=button['text'], width=4, height=2, command=lambda b=button['text']: button_handler(b),
               font=('Arial', 12), bd=5, bg=button['bg']).grid(padx=5, pady=5, row=row_val, column=col_val)
    else:
        Button(calc, text=button, width=4, height=2, command=lambda b=button: button_handler(b),
               font=('Arial', 12), bd=5).grid(padx=5, pady=5, row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        row_val += 1
        col_val = 0

calc.mainloop()
