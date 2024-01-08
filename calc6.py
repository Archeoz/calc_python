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
    current = str(layar.get())
    try:
        hasil = eval(current)
        layar.delete(0,END)
        layar.insert(END,str(hasil))
    
    except:
        layar.delete(0,END)
        layar.insert(END,str('error'))
        
def hapus_satu():
    current = str(layar.get())
    if current:
        current = current[:-1]
        layar.delete(0,END)
        layar.insert(END,str(current))
        
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
app.title('calc simple')

layar = Entry(app,width=10,borderwidth=5,font=('Arial', 30))
layar.grid(column=0,row=0,columnspan=5,padx=8,pady=8)

tombol = [
    'C','DEL','/','*',
    '7','8','9','-',
    '4','5','6','+',
    '1','2','3','=',
    '','0','00','000',
]

row_val = 1
col_val = 0

for button in tombol:
    Button(app,text = button,width=4,height=2,command= lambda b= button: button_handler(b),font=('Arial',12),bd=5 ).grid(padx=5,pady=5,column=col_val,row=row_val)
    col_val += 1
    if col_val == 4:
        row_val += 1
        col_val = 0

app.mainloop()