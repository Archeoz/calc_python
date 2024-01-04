from tkinter import *

def button_click_operator(value):
    current = str(layar.get())
    if current and current[-1] in {'+','-','*','/'}:
        current = current[:-1]
    layar.delete(0,END)
    layar.insert(END,current + str(value))
        
def button_click(value):
    current = str(layar.get())
    layar.delete(0,END)
    layar.insert(END,current + str(value))

def hitung():
    try :
        hasil= eval(layar.get())
        layar.delete(0,END)
        layar.insert(END,str(hasil))
    except :
        layar.delete(0,END)
        layar.insert(END,str('error'))
        
def hapus_satu():
    current = str(layar.get())
    if current :
        current = current[:-1]
        layar.delete(0,END)
        layar.insert(END,current)

def hapus_all():
    layar.delete(0,END)


def button_handler(value):
    if value in {'+','-','*','/'}:
        button_click_operator(value)
    elif value == '=':
        hitung()
    elif value == 'DEL':
        hapus_satu()
    elif value == 'C':
        hapus_all()
    else:
        button_click(value)

app = Tk()
app.title('testCalc2')

layar = Entry(app, width=10, borderwidth=5, font=('Arial',30))
layar.grid(row=0,column=0,padx=8,pady=8,columnspan=5)

tombol = [
    'C','DEL','/','*',
    '7','8','9','-',
    '4','5','6','+',
    '1','2','3','=',
    '.','0','00','000'
]

row_val = 1
column_val = 0

for button in tombol:
    Button(app,text=button,width=4,height=2,command= lambda b = button: button_handler(b),font=('Arial',12),bd=5).grid(padx=5,pady=5,row=row_val,column=column_val)
    column_val += 1
    if column_val > 3:
        row_val += 1
        column_val = 0

app.mainloop()