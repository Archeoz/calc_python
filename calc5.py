# import module tkinter
from tkinter import *

# function buat handle tombol klik simbol operator
def button_click_operator(value):
    # ambil semua angka dan simbol di layar
    current = str(layar.get())
    # handle jika objek terakhir pda layar adalah simbol operasi hitung / operator maka akan dihapus
    if current and current[-1] in {'+','-','*','/'}:
        current = current[:-1]
    # menghapus semua yang ada dilayar
    layar.delete(0,END)
    # memasukkan atau menambah hasil inputan atau hasil dari proses handle diatas
    layar.insert(END,current + str(value))
        
# function buat handle tombol angka
def button_click(value):
    current = str(layar.get())
    layar.delete(0,END)
    layar.insert(END,current + str(value))

# function buat handle proses hitung atau tombol =
def hitung():
    # mencoba untuk menghitung semua yang ada dilayar menggunakan eval
    try :
        hasil= eval(layar.get())
        layar.delete(0,END)
        layar.insert(END,str(hasil))
    # kalau operasinya salah atau tidak sesuai atau ada kendala lain maka akan memunculkan pesan error
    except :
        layar.delete(0,END)
        layar.insert(END,str('error'))
        
# function buat handle tombol hapus 1 karakter atau DEL
def hapus_satu():
    current = str(layar.get())
    # jika current ( semua yang ada dilayar ) ada isinya maka akan menghapus 1 objek yang paling belakang atau terakhir
    if current :
        current = current[:-1]
        layar.delete(0,END)
        layar.insert(END,current)

# function buat handle tombol hapus semua atau C
def hapus_all():
    layar.delete(0,END)

# function buat handle semua tombol yang di klik
def button_handler(value):
    # jika tombol yang di klik adalah tombol operator/operasi hitung maka akan mengarahkan ke function button_click_operator
    if value in {'+','-','*','/'}:
        button_click_operator(value)
    # jika tombol yang di klik adalah tombol = maka akan mengarahkan ke function hitung
    elif value == '=':
        hitung()
    # jika tombol yang di klik adalah tombol DEL maka akan mengarahkan ke function hapus_satu
    elif value == 'DEL':
        hapus_satu()
    # jika tombol yang di klik adalah tombol C maka akan mengarahkan ke function hapus_all
    elif value == 'C':
        hapus_all()
    # jika tombol yang di klik adalah simbol selain yang di 'if' kan diatas maka akan mengarahkan ke function button_click
    else:
        button_click(value)

# untuk membuat app kalkulator menggunakan tkinter
app = Tk()
# tambah tittle app
app.title('testCalc2')

# menginisalisasi / memulai untuk membangun / membuat tampilan layar
layar = Entry(app, width=10, borderwidth=5, font=('Arial',30))
# buat tampilan layarnya menggunakan grid
layar.grid(row=0,column=0,padx=8,pady=8,columnspan=5)

# membuat tombolnya
tombol = [
    'C','DEL','/','*',
    '7','8','9','-',
    '4','5','6','+',
    '1','2','3','=',
    '.','0','00','000'
]

jumlah_row = 1
jumlah_column = 0

# men-looping atau mengulang terus menerus button menggunakan 'for'
for button in tombol:
    # menginisialisasi / memulai membuat button / tombol dan memfungsikan menggunakan command lambda dan mengarahkan ke function button_handler
    Button(app,text=button,width=4,height=2,command= lambda b = button: button_handler(b),font=('Arial',12),bd=5).grid(padx=5,pady=5,row=jumlah_row,column=jumlah_column)
    jumlah_column += 1
    # jika jumlah kolom / tombol dalam 1 baris sudah berjumlah 4 
    if jumlah_column > 3:
    # maka akan menambah atau berpindah ke row atau baris baru kemudian -
        jumlah_row += 1
    # mengembalikan jumlah column ke 0
        jumlah_column = 0

# menjalankan aplikasi dengan fungsi mainloop ( menjalankan dan mengulangi semua code dari atas ampai bawah )
app.mainloop()