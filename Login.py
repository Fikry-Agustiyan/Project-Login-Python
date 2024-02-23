from tkinter import *
from tkinter import messagebox
import tempfile
import os

login = Tk()
login.title('PROGRAM LOGIN_FIKRY AGUSTIYAN')
login.geometry("1280x720+0+0")
login.config(bg='light grey')
login.resizable(False, False)

label1 = Label(login, text='LOGIN', font="Normal 30 bold", bg='light grey', foreground='black')
footer = Label(login, text='@Fikry Agustiyan_SMK Telkom Jakarta_2023', font="normal 12", bg='light grey', foreground='black')
username = Label(login, text='Username :', font="arial 20 bold ", bg='light grey', foreground='black')
password = Label(login, text='Password :', font="arial 20 bold ", bg='light grey', foreground='black')
entry1 = Entry(login, bd=5,relief=RIDGE, font="arial 15 bold ")
entry2 = Entry(login,bd=5, relief=RIDGE, font="arial 15 bold ", show="*")

label1.place(x=550, y=160)
footer.place(x=800, y=600)
username.place(x=420, y=300)
password.place(x=420, y=360)
entry1.place(x=600, y=300, height=50)
entry2.place(x=600, y=360, height=50)

def show_password():
    if entry2.cget('show') == '*':
        entry2.config(show="")
    else:
        entry2.config(show="*")

def windowlogin():
    username = entry1.get()
    password = entry2.get()
    if (username == 'FIKRY' and password == '12345'):
        messagebox.showinfo('Sukses', 'Login Berhasil')
        login.destroy()
        login.destroy()
    else:
        messagebox.showerror('Invalid', 'Username atau Password Salah')

eye_pass = Checkbutton(login,command=show_password, text="show password", bg='light grey', activebackground="grey",font="normal 20" )
eye_pass.place(x=540, y=420)

tombol_button = Button(login, text='LOGIN',font="20", command=windowlogin)
tombol_button.place(x=600, y=500, height=50, width=90)
def on_closing():
    if messagebox.askokcancel("Keluar", "Apakah Anda yakin ingin keluar?"):
        login.destroy()
login.protocol("WM_DELETE_WINDOW", on_closing)
login.mainloop()