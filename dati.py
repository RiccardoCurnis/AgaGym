import tkinter
from tkinter import *
from tkinter import ttk
import datetime
from tkinter import messagebox


window = tkinter.Tk()
window.title("Dati")
lettere=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
numeri=["1","2","3","4","5","6","7","8","9","0"]

def error_message():
    tkinter.messagebox.showwarning(title="Error", message="Dati errati")


def prendidati():
    dati=[]
    nome = nome_entry.get()
    nome=nome.upper()
    ctrl=0
    if len(nome)>2 and len(nome)<31:
            
                for i in range(len(nome)):
                    if nome[i] not in lettere:
                        ctrl=1 
    
                    else:
                        ctrl=0

                
    else:

            ctrl=1
    if ctrl==0:
            dati.append(nome)
            
    elif ctrl==1:
          error_message()
            



    cognome = cognome_entry.get()
    cognome=cognome.upper()
    if len(cognome)>2 and len(cognome)<31:
            
                for i in range(len(cognome)):
                    if cognome[i] not in lettere:
                        ctrl=1 
    
                    else:
                        ctrl=0

                
    else:
           
            ctrl=1
    if ctrl==0:
            dati.append(cognome)
            print(dati)
    elif ctrl==1:
          error_message()



    eta = eta_spinbox.get()
    if len(eta)>0 and len(eta)<3:
            
                for i in range(len(eta)):
                    if eta[i] not in numeri:
                        ctrl=1 
    
                    else:
                        ctrl=0

                
    else:
            ctrl=1
    if ctrl==0:
            dati.append(eta)
            print(dati)
    elif ctrl==1:
          error_message()




    codicefisc = codicefisc_entry.get()
    codicefisc=codicefisc.upper()
    ctrl=0
    



    dataiscriz = dataiscriz_entry.get()
    dataiscriz=dataiscriz.upper()
    while True:
                anno=dataiscriz
                if anno>datetime.datetime.now().year or anno<1900:
                    error_message()
                    continue
                elif anno==datetime.datetime.now().year:
                    mese=dataiscriz
                    if mese==datetime.datetime.now().month:
                        giorno=dataiscriz
                        if giorno>datetime.datetime.now().day:
                            error_message()
                            continue
                    elif mese<datetime.datetime.now().month:
                        giorno=dataiscriz
                        if giorno>31 or giorno<1:
                            error_message()
                            continue
                    elif mese>12 or mese<1:
                        error_message()
                        continue
                else:
                    mese=dataiscriz
                    if mese>12 or mese<1:
                        error_message()
                        continue
                    giorno=dataiscriz
                    if giorno>31 or giorno<1:
                        error_message()
                        continue
                try:
                    datap=datetime.datetime(anno, mese, giorno)
                    print(datap)
                    break
                except ValueError:
                    error_message()
                    continue


    durataabb = durataabb_combobox.get()



frame = tkinter.Frame(window)
frame.pack()

utente_info_frame = tkinter.LabelFrame(frame, text="Informazioni dell'Utente")
utente_info_frame.grid(row = 0, column = 0, padx = 20, pady = 20)

nome_label= tkinter.Label(utente_info_frame, text="Nome")
nome_label.grid(row = 0, column = 0)
cognome_label= tkinter.Label(utente_info_frame, text="Cognome")
cognome_label.grid(row = 0, column = 1)

nome_entry = tkinter.Entry(utente_info_frame)
cognome_entry = tkinter.Entry(utente_info_frame)
nome_entry.grid(row = 1, column = 0)
cognome_entry.grid(row = 1, column = 1)

eta_label = tkinter.Label(utente_info_frame, text="Età")
eta_spinbox = tkinter.Spinbox(utente_info_frame, from_=16, to=90)
eta_label.grid(row = 0, column = 2)
eta_spinbox.grid(row = 1, column= 2)

codicefisc_label = tkinter.Label(utente_info_frame, text="Codice Fiscale")
codicefisc_label.grid(row = 2, column=0)
codicefisc_entry = tkinter.Entry(utente_info_frame)
codicefisc_entry.grid(row = 3, column = 0)
dataiscriz_label = tkinter.Label(utente_info_frame, text="Data di iscrizione")
dataiscriz_label.grid(row = 2, column=1)
dataiscriz_entry = tkinter.Entry(utente_info_frame,bg="white",disabledbackground="white")
dataiscriz_entry.grid(row = 3, column = 1)
dataiscriz_entry.insert(0, "dd/mm/yyyy")
dataiscriz_entry.configure(state=DISABLED)

durataabb_label= tkinter.Label(utente_info_frame, text="Abbonamento")
durataabb_combobox= ttk.Combobox(utente_info_frame, values=["Trimestre","Semestre","Annuale"])
durataabb_label.grid(row = 2, column = 2)
durataabb_combobox.grid(row = 3, column=2)

enter_button = tkinter.Button(frame,text="Invio", command=prendidati)
enter_button.grid(row=4, column=0, sticky="news", padx=20, pady=10)


def on_click(event):
    dataiscriz_entry.configure(state=NORMAL)
    dataiscriz_entry.delete(0, END)

    # make the callback only work once
    dataiscriz_entry.unbind('<Button-1>', on_click_id)





on_click_id = dataiscriz_entry.bind('<Button-1>', on_click)

adesso = datetime.datetime.now()







window.mainloop()