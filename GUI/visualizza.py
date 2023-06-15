import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
import datetime
from tkinter import messagebox


lettere=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
numeri=["1","2","3","4","5","6","7","8","9","0","/"]
dati=[]

window = tkinter.Tk()
window.title("Visualizza")
frame = tkinter.Frame(window)
frame.pack()

def error_codicefisc():
    tkinter.messagebox.showwarning(title="Error", message="Codice fiscale non valido")

def codicefisc():
    codicefisc = codicefisc_entry.get()
    codicefisc=codicefisc.upper()
    ctrl=0
    if (len(codicefisc))!=16:
        ctrl=1
        print("Errore! Codice Fiscale non valido! 1 \n")
        error_codicefisc()
    if ctrl==0:
        
        for i in range(6):
            
            if codicefisc[i]not in lettere and ctrl!=1:
                ctrl=1
                error_codicefisc()
        for i in range (6,8):
            if codicefisc[i]not in numeri and ctrl!=1:
                ctrl=1
                
                error_codicefisc()
        if codicefisc[8] not in lettere and ctrl!=1:
            ctrl=1
            
            error_codicefisc()
        for i in range (9,11):
            if codicefisc[i] not in numeri and ctrl!=1:
                ctrl=1
                
                error_codicefisc()
        if codicefisc[11] not in lettere and ctrl!=1:
            ctrl=1
            
            error_codicefisc()
        for i in range (12,15):
            if codicefisc[i] not in numeri and ctrl!=1:
                ctrl=1
                
                error_codicefisc()
        if codicefisc[15] not in lettere and ctrl!=1:
            ctrl=1
            
            error_codicefisc()
        if ctrl==0:
            dati.append(codicefisc)
    lista2=[]
    miofile=open("datifile.txt","r")
    buffer=miofile.read()
    buffer=buffer.split("\n")
    miofile.close()
    for i in range(len(buffer)-1):#non l'ultimo perche' e' vuoto
        yeah=buffer[i].split("|")
        lista2.append(yeah)
        cod=yeah[2]
        if cod==codicefisc:
            cod_label=tkinter.Label(text=codicefisc)
            cod_label.grid(row=5,column=1)
             
              
utente_info_frame = tkinter.LabelFrame(frame, text="Informazioni dell'Utente")
utente_info_frame.grid(row = 0, column = 0, padx = 20, pady = 20)

codicefisc_label= tkinter.Label(utente_info_frame, text="Codice fiscale")
codicefisc_label.grid(row = 0, column = 0)
codicefisc_entry = tkinter.Entry(utente_info_frame,width=28)
codicefisc_entry.grid(row = 1, column = 0)
testocod_label= tkinter.Label(utente_info_frame, text="Formato: ")
testocod_label.grid(row = 2, column = 0)
testocod_label= tkinter.Label(utente_info_frame, text="A A A A A A N N A N N A N N N A")
testocod_label.grid(row = 3, column = 0)


enter_button = tkinter.Button(frame,text="Verifica",command= codicefisc, width=10)
enter_button.grid(row=2, column=0, sticky="news", padx=10, pady=10)





window.mainloop()