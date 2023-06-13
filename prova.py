nome="1"
lettere=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
numeri=["1","2","3","4","5","6","7","8","9","0"]
import tkinter as tk
from tkinter import *
from functools import partial
window = tk.Tk()
window.geometry("600x600")
window.resizable(False, False)
window.title("AgaGym Software")

Titolo = "AgaGym"
titolo_output = tk.Label(window, text=Titolo, fg="red", font=("Courier", 30,"bold"))
titolo_output.grid(row=0, column=1, padx=100)
testo="Avvia il programma per cominciare"
testo_output=tk.Label(window, text=testo, fg="black", font=("Courier", 20,"bold"))
testo_output.grid(row=1, column=1, padx=100)
menu_button = tk.Button(text="Avvia Programma",command=lambda:[ inizio(),menu_button.grid_remove(),titolo_output.grid_remove(), testo_output.grid_remove()])
menu_button.grid(row=2, column=1)

exit_button = tk.Button(text="Termina Sessione",command=quit)
exit_button.grid(row=6, column=1)                                                                                                                                                                                                                                                                                                                                                                                                                                      



def inizio():
    testo="Seleziona Una opzione:"
    sottotitolo= tk.Label(window, text=testo, fg="blue", font=("Courier", 30,"bold"))
    sottotitolo.grid(row=0, column=1, padx=100)
    iscrizioni_button = tk.Button(window, text="Nuova iscrizione",command=lambda:[iscrizione(),visualizza_button.grid_remove(),iscrizioni_button.grid_remove(),sottotitolo.grid_remove(),rinnovo_button.grid_remove(), exit_button.grid_remove(), cancella_button.grid_remove()])
    iscrizioni_button.grid(row=2, column=1)
    rinnovo_button=tk.Button(window, text="Rinnova Iscrizione", command=lambda:[rinnova(),visualizza_button.grid_remove(),cancella_button.grid_remove(),iscrizioni_button.grid_remove(),sottotitolo.grid_remove(),rinnovo_button.grid_remove(), exit_button.grid_remove()])
    rinnovo_button.grid (row=3, column=1)
    cancella_button=tk.Button(window, text="Cancella Iscrizione",command=lambda:[cancella(),visualizza_button.grid_remove(), cancella_button.grid_remove() ,iscrizioni_button.grid_remove(),sottotitolo.grid_remove(),rinnovo_button.grid_remove(), exit_button.grid_remove()])
    cancella_button.grid(row=4, column=1)
    visualizza_button=tk.Button(window, text="Visualizza Iscrizioni", command=lambda:[visualizza(), visualizza_button.grid_remove(),cancella_button.grid_remove(), iscrizioni_button.grid_remove(),sottotitolo.grid_remove(),rinnovo_button.grid_remove(), exit_button.grid_remove() ])
    visualizza_button.grid(row=5, column=1)
def iscrizione():
    text = "Menu Iscrizione:"
    text1_output = tk.Label(window, text=text, fg="red", font=("Courier", 30,"bold"))
    text1_output.grid(row=0, column=1, padx=150)
    indietro_button = tk.Button(window,text="Indietro",command=lambda:[indietro_button.grid_remove(),text1_output.grid_remove(),inizio(), exit_button.grid(row=6, column=1)])
    indietro_button.grid(row=10, column=1)

    def name():
        global nome
        nome=scrivi.get()
        nome=nome.upper()
        errore=Label(window, text="Errore, Nome non valido!")
        print (nome)
        ctrl=0
        if len(nome)>2 and len(nome)<31:
            for i in range(len(nome)):
                if nome[i] not in lettere: 
                    errore.grid (row=4, column=1)
                    ctrl=1
                else:
                    ctrl=0
                    errore.grid_remove() #??????
        else:
            errore.grid (row=4, column=1)
            ctrl=1
        if ctrl==0:
            errore.destroy() #??????
            #......
            
    testo=Label(window, text="Inserisci il tuo nome:")
    bottone=Button(window, text="Invia", command=name)
    scrivi=Entry(window)
    testo.grid(row=1, column=1)
    scrivi.grid(row=2, column=1)
    bottone.grid(row=5, column=1)
def rinnova():
    text = "Menu Rinnova:"
    text2_output = tk.Label(window, text=text, fg="red", font=("Courier", 30,"bold"))
    text2_output.grid(row=0, column=1, padx=160)
    indietro_button = tk.Button(window,text="Indietro",command=lambda:[indietro_button.grid_remove(),text2_output.grid_remove(),inizio(), exit_button.grid(row=6, column=1)])
    indietro_button.grid(row=3, column=1)

def cancella():
    text = "Menu Cancella:"
    text3_output = tk.Label(window, text=text, fg="red", font=("Courier", 30,"bold"))
    text3_output.grid(row=0, column=1, padx=150)
    indietro_button = tk.Button(window,text="Indietro",command=lambda:[indietro_button.grid_remove(),text3_output.grid_remove(),inizio(), exit_button.grid(row=6, column=1)])
    indietro_button.grid(row=3, column=1)

def visualizza():
    testo = "Menu Visualizza:"
    text4_output = tk.Label(window, text=testo, fg="red", font=("Courier", 30,"bold"))
    text4_output.grid(row=0, column=1, padx=150)
    indietro_button = tk.Button(window,text="Indietro",command=lambda:[indietro_button.grid_remove(),text4_output.grid_remove(),inizio(), exit_button.grid(row=6, column=1)])
    indietro_button.grid(row=3, column=1)

    




    
window.mainloop() 















