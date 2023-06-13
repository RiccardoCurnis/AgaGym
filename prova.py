import tkinter as tk

window = tk.Tk()
window.geometry("600x600")
window.resizable(False, False)
window.title("AgaGym")

text = "AgaGym"
text_output = tk.Label(window, text=text, fg="red", font=("Courier", 20,"bold"))
text_output.grid(row=0, column=1, padx=200)

menu_button = tk.Button(text="Avvia Programma",command=lambda:[ inizio(),menu_button.grid_remove()])
menu_button.grid(row=2, column=1)

exit_button = tk.Button(text="Termina",command=quit)
exit_button.grid(row=0, column=0)                                                                                                                                                                                                                                                                                                                                                                                                                                      



def inizio():
    
    iscrizioni_button = tk.Button(text="Iscrizioni",command=lambda:[iscrizione(),iscrizioni_button.grid_remove(),text_output.grid_remove(),rinnovo_button.grid_remove()])
    iscrizioni_button.grid(row=3, column=1)
    rinnovo_button = tk.Button(text="Area Personale")
    rinnovo_button.grid(row=4, column=1)

def iscrizione():
    text = "Abbonamenti"
    text1_output = tk.Label(window, text=text, fg="red", font=("Courier", 20,"bold"))
    text1_output.grid(row=0, column=1, padx=190)
    indietro()
    
    

def indietro():
    indietro_button = tk.Button(window,text="Indietro",command=lambda:[indietro_button.grid_remove(),inizio()])
    indietro_button.grid(row=1, column=1)




    
window.mainloop() 















