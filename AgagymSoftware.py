import time
import qrcode
nome="1"
lettere=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
numeri=["1","2","3","4","5","6","7","8","9","0"]
import datetime
import tkinter as tk
from tkinter import *
from functools import partial
window = tk.Tk()
window.geometry("600x600")
window.resizable(True, True)
window.title("AGym Software")

Titolo = "AgaGym"
titolo_output = tk.Label(window, text=Titolo, fg="red", font=("Courier", 30,"bold"))
titolo_output.grid(row=0, column=1, padx=100)
testo="Avvia il programma per cominciare"
testo_output=tk.Label(window, text=testo, fg="black", font=("Courier", 20,"bold"))
testo_output.grid(row=1, column=1, padx=100)
menu_button = tk.Button(text="Avvia Programma",command=lambda:[ inizio(),menu_button.grid_remove(),titolo_output.grid_remove(), testo_output.grid_remove()])
menu_button.grid(row=2, column=1)

exit_button = tk.Button(text="Termina Sessione",command=quit)
exit_button.grid(row=7, column=1)                                                                                                                                                                                                                                                                                                                                                                                                                                      
def indietroB():
    for widgets in window.winfo_children():
      widgets.destroy()
      
    inizio()
def cancellatutto():
    for widgets in window.winfo_children():
      widgets.destroy()
def inizio():
    testo="Seleziona Una opzione:"
    exit_button = tk.Button(text="Termina Sessione",command=quit)
    exit_button.grid(row=7, column=1)
    sottotitolo= tk.Label(window, text=testo, fg="blue", font=("Courier", 30,"bold"))
    sottotitolo.grid(row=0, column=1, padx=100)
    iscrizioni_button = tk.Button(window, text="Nuova iscrizione",command=lambda:[cancellatutto(),iscrizione()])
    iscrizioni_button.grid(row=2, column=1)
    rinnovo_button=tk.Button(window, text="Rinnova Iscrizione", command=lambda:[cancellatutto(),rinnova()])
    rinnovo_button.grid (row=3, column=1)
    cancella_button=tk.Button(window, text="Cancella Iscrizione",command=lambda:[cancellatutto(),cancella()])
    cancella_button.grid(row=4, column=1)
    visualizza_button=tk.Button(window, text="Visualizza Iscrizioni", command=lambda:[cancellatutto(),visualizza()])
    visualizza_button.grid(row=5, column=1)
    verifica_button=tk.Button(window, text="Verifica Iscrizioni", command=lambda:[cancellatutto(),verifica()])
    verifica_button.grid(row=6, column=1)

def iscrizione():
    text = "Menu Iscrizione:"
    text1_output = tk.Label(window, text=text, fg="red", font=("Courier", 30,"bold"))
    text1_output.grid(row=0, column=1, padx=150)
    indietro_button = tk.Button(window,text="Indietro",command=indietroB)
    
    def name():
        ctrl=0
        global nome
        nome=scrivi.get()
        nome=nome.upper()
        if (len(nome))>2 and (len(nome))<31:
            print ("è tutto ok")
            for i in range (len(nome)):
                if nome[i] not in lettere:
                    print("Errore")
                    ctrl=1 
                    sbagliato.grid(row=3, column=1)
        else:
            print("Errore")
            ctrl=1
            sbagliato.grid(row=3, column=1)
        if ctrl==0:
            print ("Chiedo il cognome")
            sbagliato.grid_remove()
            testo.grid_remove()
            scrivi.grid_remove()
            bottone.grid_remove()
            def cognome ():
                ctrl=0
                global cognome
                cognome=scrivi1.get()
                cognome=cognome.upper()
                if len(cognome)>2 and len(cognome)<31:
                    for i in range(len(cognome)):
                        if cognome[i] not in lettere:
                            ctrl=1
                            print("Errore! Cognome non valido!\n")
                            sbagliato1.grid(row=3, column=1)   
                else:
                    ctrl=1
                    print("Cognome non valido!\n")
                    sbagliato1.grid(row=3, column=1)
                if ctrl==0:
                    sbagliato1.grid_remove()
                    testo1.grid_remove()
                    scrivi1.grid_remove()
                    bottone1.grid_remove()
                    print(nome,cognome)
                    def codicefiscale():
                        ctrl=0
                        global cod_fis
                        cod_fis=scrivi2.get()
                        cod_fis=cod_fis.upper()
                        if (len(cod_fis))!=16:
                            ctrl=1
                            print("Errore! Codice Fiscale non valido! 1 \n")
                            sbagliato2.grid(row=3, column=1)
                        if ctrl==0:
                            
                            for i in range(6):
                                
                                if cod_fis[i]not in lettere and ctrl!=1:
                                    ctrl=1
                                    print("Errore! Codice Fiscale non valido!2 \n")
                                    sbagliato2.grid(row=3, column=1)
                            for i in range (6,8):
                                if cod_fis[i]not in numeri and ctrl!=1:
                                    ctrl=1
                                    print("Errore! Codice Fiscale non valido!3 \n")
                                    sbagliato2.grid(row=3, column=1)
                            if cod_fis[8] not in lettere and ctrl!=1:
                                ctrl=1
                                print("Errore! Codice Fiscale non valido!4 \n")
                                sbagliato2.grid(row=3, column=1)
                            for i in range (9,11):
                                if cod_fis[i] not in numeri and ctrl!=1:
                                    ctrl=1
                                    print("Errore! Codice Fiscale non valido!5 \n")
                                    sbagliato2.grid(row=3, column=1)
                            if cod_fis[11] not in lettere and ctrl!=1:
                                ctrl=1
                                print("Errore! Codice Fiscale non valido!6 \n")
                                sbagliato2.grid(row=3, column=1)
                            for i in range (12,15):
                                if cod_fis[i] not in numeri and ctrl!=1:
                                    ctrl=1
                                    print("Errore! Codice Fiscale non valido!7 \n")
                                    sbagliato2.grid(row=3, column=1)
                            if cod_fis[15] not in lettere and ctrl!=1:
                                ctrl=1
                                print("Errore! Codice Fiscale non valido8 ! \n")
                                sbagliato2.grid(row=3, column=1)
                            if ctrl==0:
                                miofile=open("AgaGym.txt","r")
                                buffer=miofile.read()
                                buffer=buffer.split("\n")
                                
                                miofile.close()
                                listaUtenti=buffer
                                ctrll=0
                                for i in range(len(listaUtenti)-1):
                                    uten=listaUtenti[i].split("|")
                                    codf=uten[2]
                                    print(codf)
                                    if codf==cod_fis:
                                        ctrll=1
                                        break
                                    else:
                                        ctrll=0
                                if ctrll==0:

                                    print("Inserire la data")
                                    sbagliato2.grid_remove()
                                    testo2.grid_remove()
                                    scrivi2.grid_remove()
                                    bottone2.grid_remove()

                                    def abbonamento(datap):
                                        print ("Ciao Sono qui")
                                        abbonamento=""
                                        print (datap)
                                        testo7=Label(window, text="Seleziona Tipologia di Abbonamento:")
                                        def annuale():
                                            abbonamento="Annuale"
                                            resoconto(abbonamento)
                                        def semestrale():
                                            abbonamento="Semestrale"
                                            resoconto(abbonamento)
                                        def trimestrale():
                                            abbonamento="Trimestrale"
                                            resoconto(abbonamento)
                                        
                                        def resoconto(abbonamento):
                                            record=("{:}|{:}|{:}|{:}|{:}".format(nome, cognome, cod_fis, datap, abbonamento))
                                            print(record)
                                            def salva():
                                                code=qrcode.make(cod_fis)
                                                name="{:}.{:}.png".format(nome,cognome)
                                                code.save (name)
                                                record1=str(record+"\n")
                                                nomefile="AgaGym.txt"
                                                miofile=open(nomefile,"a")
                                                miofile.write(record1)
                                                miofile.flush()
                                                miofile.close()
                                                text1_output.grid_remove()
                                                inizio()


                                            testo7.grid_remove()
                                            BottoneAbb1.grid_remove()
                                            BottoneAbb2.grid_remove()
                                            BottoneAbb3.grid_remove()
                                            testofinale="Utente Registrato con successo!\n--> {:} \n È corretto?".format(record)
                                            testo8=Label(window, text=testofinale)
                                            testo8.grid(row=1, column=1)
                                            bottonerifiuta=Button(window, text="Annulla", command=lambda:[testo8.grid_remove(), bottoneFinale.grid_remove(),bottonerifiuta.grid_remove(),text1_output.grid_remove(),inizio()])
                                            bottoneFinale=Button(window, text="Si", command=lambda:[salva(), testo8.grid_remove(), bottoneFinale.grid_remove()])
                                            bottoneFinale.grid(row=2, column=1)
                                            bottonerifiuta.grid(row=3, column=1)
                                            
                                        BottoneAbb1=Button(window, text="Annuale", command=annuale)
                                        BottoneAbb2=Button(window, text="Semestrale",command=semestrale)
                                        BottoneAbb3=Button(window, text="Trimestrale",command=trimestrale)


                                        testo7.grid (row=1, column=1)
                                        BottoneAbb1.grid(row=2, column=1)
                                        BottoneAbb2.grid(row=3, column=1)
                                        BottoneAbb3.grid(row=4, column=1)
                                        
                                    def inserisciData():
                                        print("Sono in inserisci data manuale")
                                        testo4=Label(window, text="Inserisci Anno:")
                                        testo5=Label(window, text="Inserisci Mese:")
                                        testo6=Label(window, text="Inserisci Giorno:")
                                        IAnno=Entry(window)
                                        IMese=Entry(window)
                                        Igiorno=Entry(window)
                                        errore6=Label(window, text="Errore!", fg="red")
                                        def controlloData():
                                            ctrl=0
                                            Anno=IAnno.get()
                                            Mese=IMese.get()
                                            Giorno=Igiorno.get()
                                            if Anno=="" or Mese=="" or Giorno=="":
                                                errore6.grid(row=8, column=1)
                                                ctrl=1
                                            try:
                                                Anno=int(Anno)
                                                Mese=int(Mese)
                                                Giorno=int(Giorno)
                                            except ValueError:
                                                errore6.grid(row=8, column=1)
                                                
                                                
                                                ctrl=1
                                            if ctrl==0 and Anno>datetime.datetime.now().year or Anno<1900:
                                                print("Errore anno non valido!")
                                                errore6.grid(row=12, column=1)
                                                
                                                
                                                ctrl=1
                                            elif ctrl==0 and Mese>datetime.datetime.now().month and Anno==datetime.datetime.now().year and ctrl==0:
                                                print("Errore Mese non valido!")
                                                errore6.grid(row=12, column=1)
                                                
                                                
                                                ctrl=1
                                            elif ctrl==0 and Giorno>datetime.datetime.now().day and Mese>=datetime.datetime.now().month and Anno==datetime.datetime.now().year and ctrl==0:
                                                print("Errore Giorno non valido!")
                                                errore6.grid(row=12, column=1)
                                                
                                                
                                                ctrl=1
                                            elif ctrl==0 and Mese>12 or Mese<1 and ctrl==0:
                                                print("Errore Mese non valido!")
                                                errore6.grid(row=12, column=1)
                                                
                                                
                                                ctrl=1
                                            elif ctrl==0 and Giorno>31 or Giorno<1 and ctrl==0:
                                                print("Giorno non valido!")
                                                errore6.grid(row=12, column=1)
                                                
                                                
                                                ctrl=1
                                            if ctrl==0:
                                                datap=datetime.datetime(Anno, Mese, Giorno)
                                                print (datap)
                                                errore6.grid_remove()
                                                testo4.grid_remove()
                                                testo5.grid_remove()
                                                testo6.grid_remove()
                                                IAnno.grid_remove()
                                                IMese.grid_remove()
                                                Igiorno.grid_remove()
                                                bottone6.grid_remove()
                                                abbonamento(datap)


                                    



                                        bottone6=Button(window, text="Inserisci", command=controlloData)
                                        testo4.grid(row=1, column=1)
                                        testo5.grid(row=3, column=1)
                                        testo6.grid(row=5, column=1)
                                        IAnno.grid(row=2, column=1)
                                        IMese.grid(row=4, column=1)
                                        Igiorno.grid(row=6, column=1)
                                        bottone6.grid(row=7, column=1)

                                    def dataOdierna():
                                        datap=datetime.datetime.now()
                                        abbonamento(datap)

                                
                                    testo3=Label(window, text="Scegli La data da inserire:")
                                    data=datetime.datetime.now()
                                    DataAttuale="Data Odierna ({:})".format(data)
                                    bottoneData1=Button(window, text=DataAttuale, command=lambda:[dataOdierna(), bottoneData1.grid_remove(),bottoneData2.grid_remove(),testo3.grid_remove()])
                                    bottoneData2=Button(window, text="Altra Data", command=lambda:[inserisciData(), bottoneData1.grid_remove(),bottoneData2.grid_remove(),testo3.grid_remove()])
                                    testo3.grid(row=1, column=1)
                                    bottoneData1.grid(row=2, column=1)
                                    bottoneData2.grid(row=3, column=1)
                                else:
                                    errorefatal=Label(window, text="Codice Fiscale Gia' Registrato!", fg="red")
                                    bottonerecupera=Button(window, text="Rinnova", command=lambda:[cancellatutto(), rinnova()])
                                    errorefatal.grid(row=10, column=1)
                                    bottonerecupera.grid(row=11, column=1)


                    testo2=Label(window, text="Inserisci il Codice Fiscale:")
                    sbagliato2=Label(window, text="Errore, Codice Fiscale non valido!")
                    bottone2=Button(window, text="Invia", command=codicefiscale)
                    scrivi2=Entry(window)
                    testo2.grid(row=1, column=1)
                    scrivi2.grid(row=2, column=1)
                    bottone2.grid(row=5, column=1)
            testo1=Label(window, text="Inserisci il cognome:")
            sbagliato1=Label(window, text="Errore, Cognome non valido!")
            bottone1=Button(window, text="Invia", command=cognome)
            scrivi1=Entry(window)
            testo1.grid(row=1, column=1)
            scrivi1.grid(row=2, column=1)
            bottone1.grid(row=5, column=1)
            

        
            
    testo=Label(window, text="Inserisci il nome:")
    sbagliato=Label(window, text="Errore, Nome non valido!")
    bottone=Button(window, text="Invia", command=name)
    scrivi=Entry(window)
    testo.grid(row=1, column=1)
    scrivi.grid(row=2, column=1)
    bottone.grid(row=5, column=1)
def rinnova():
    text = "Menu Rinnova:"
    text2_output = tk.Label(window, text=text, fg="red", font=("Courier", 30,"bold"))
    text2_output.grid(row=0, column=1, padx=160)
    indietro_button = tk.Button(window,text="Indietro",command=indietroB)
    miofile=open("AgaGym.txt","r")
    buffer=miofile.read()
    buffer=buffer.split("\n")
    miofile.close()
    listaUtenti=buffer
    text3=tk.Label(window, text="Abbonamenti", font=("Courier",20,"bold"))
    text3.grid(row=1, column=1)
    posizione=2
    posizione2=1
    for i in range (len(listaUtenti)-1):
        cliente=listaUtenti[i]
        cliente=cliente.split("|")
        testo="{:}.{:}|Abbonamento: {:}".format(cliente[0], cliente [1], cliente[4])
        output=tk.Label(window, text=testo)
        if i>30:
            posizione2=posizione2+1
            output.grid(row=posizione2, column=2)
        else:
            output.grid(row=posizione, column=1)
            posizione=posizione+1
    def invia():
        Nome_cognome=inserisci.get()
        Nome_cognome=Nome_cognome.upper()
        ctrl=0
        def rinnova1(index):
            for widgets in window.winfo_children():
                widgets.destroy()
            text = "Menu Rinnova:"
            text2_output = tk.Label(window, text=text, fg="red", font=("Courier", 30,"bold"))
            text2_output.grid(row=0, column=1, padx=160)
            global cliente
            cliente=listaUtenti[index]
            cliente=cliente.split("|")
            data=cliente[3]
            data=data.split("-")
            giorno=data[2]
            n_1=giorno[0]
            n_2=giorno[1]
            giorno=n_1+n_2
            giorno=int(giorno)
            data.pop()
            anno=data[0]
            anno=int(anno)
            mese=data[1]
            mese=int(mese)
            if cliente[4]=="Annuale":
                anno=anno+1
            if cliente[4]=="Semestrale":
                mese=mese+6
                if mese>12:
                    anno=anno+1
                    c=mese-12
                    mese=c
            if cliente[4]=="Trimestrale":
                mese=mese+3
                if mese>12:
                    anno=anno+1
                    c=mese-12
                    mese=c

            testo1="Cliente: {:} {:} \n Abbonamento: {:}\n Data di scadenza: {:}/{:}/{:}".format(cliente[0], cliente[1], cliente[4], anno, mese, giorno)
            text5=Label(window, text=testo1)
            text5.grid(row=1, column=1)
            text6=Label(window, text="Scegli il tipo di abbonamento:")
            text6.grid(row=2, column=1)
            def riscrivi(listaUtenti):
                miofile=open("AgaGym.txt","w")
                miofile.close()
                miofile=open("AgaGym.txt","a")
                for i in range(len(listaUtenti)-1):
                    inser=str("{:}\n".format(listaUtenti[i]))
                    miofile.write(inser)
                miofile.close()
                indietroB()
            def annuale():
                controllomese=datetime.datetime.now().month
                controllomese=int(controllomese)
                controlloanno=datetime.datetime.now().year
                controlloanno=int(controlloanno)
                controllogiorno=datetime.datetime.now().day
                controllogiorno=int(controllogiorno)
                data=str(datetime.datetime.now())
                cliente=listaUtenti[index]
                cliente=cliente.split("|")
                print(cliente)
                errore1=Label(window, text="Errore, Impossibile Rinnovare!", fg="red")
                tornaindietro=Button(window, text="Indietro", command=indietroB)
                if controlloanno>anno:
                    cliente[4]="Annuale"
                    cliente[3]=data
                    print("Ciao!!")
                    cliente=str("{:}|{:}|{:}|{:}|{:}".format(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4]))
                    listaUtenti[index]=cliente
                    riscrivi(listaUtenti)
                    
                elif controlloanno==anno:
                    if controllomese>mese:
                        cliente[4]="Annuale"
                        cliente[3]=data
                        cliente=str("{:}|{:}|{:}|{:}|{:}".format(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4]))
                        listaUtenti[index]=cliente
                        print("Ciao!!!")
                        riscrivi(listaUtenti)
                        
                    elif controllomese==mese:
                        if controllogiorno>=giorno:
                            print("CIao!!!!")
                            cliente[4]="Annuale"
                            cliente[3]=data
                            cliente=str("{:}|{:}|{:}|{:}|{:}".format(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4]))
                            listaUtenti[index]=cliente
                            riscrivi(listaUtenti)
                        else:
                            errore1.grid(row=10, column=1)
                            tornaindietro.grid(row=11, column=1)
                    else:
                        errore1.grid(row=10, column=1)
                        tornaindietro.grid(row=11, column=1)
                else:
                    errore1.grid(row=10, column=1)
                    tornaindietro.grid(row=11, column=1)
            def semestrale():
                controllomese=datetime.datetime.now().month
                controllomese=int(controllomese)
                controlloanno=datetime.datetime.now().year
                controlloanno=int(controlloanno)
                controllogiorno=datetime.datetime.now().day
                controllogiorno=int(controllogiorno)
                data=str(datetime.datetime.now())
                cliente=listaUtenti[index]
                cliente=cliente.split("|")
                print(cliente)
                errore1=Label(window, text="Errore, Impossibile Rinnovare!", fg="red")
                tornaindietro=Button(window, text="Indietro", command=indietroB)
                if controlloanno>anno:
                    cliente[4]="Semestrale"
                    cliente[3]=data
                    print("Ciao!!")
                    cliente=str("{:}|{:}|{:}|{:}|{:}".format(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4]))
                    listaUtenti[index]=cliente
                    riscrivi(listaUtenti)
                    
                elif controlloanno==anno:
                    if controllomese>mese:
                        cliente[4]="Semestrale"
                        cliente[3]=data
                        cliente=str("{:}|{:}|{:}|{:}|{:}".format(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4]))
                        listaUtenti[index]=cliente
                        print("Ciao!!!")
                        riscrivi(listaUtenti)
                        
                    elif controllomese==mese:
                        if controllogiorno>=giorno:
                            print("CIao!!!!")
                            cliente[4]="Semestrale"
                            cliente[3]=data
                            cliente=str("{:}|{:}|{:}|{:}|{:}".format(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4]))
                            listaUtenti[index]=cliente
                            riscrivi(listaUtenti)
                        else:
                            errore1.grid(row=10, column=1)
                            tornaindietro.grid(row=11, column=1)
                    else:
                        errore1.grid(row=10, column=1)
                        tornaindietro.grid(row=11, column=1)
                else:
                    errore1.grid(row=10, column=1)
                    tornaindietro.grid(row=11, column=1) 

            def trimestrale():
                controllomese=datetime.datetime.now().month
                controllomese=int(controllomese)
                controlloanno=datetime.datetime.now().year
                controlloanno=int(controlloanno)
                controllogiorno=datetime.datetime.now().day
                controllogiorno=int(controllogiorno)
                data=str(datetime.datetime.now())
                cliente=listaUtenti[index]
                cliente=cliente.split("|")
                print(cliente)
                errore1=Label(window, text="Errore, Impossibile Rinnovare!", fg="red")
                tornaindietro=Button(window, text="Indietro", command=indietroB)
                if controlloanno>anno:
                    cliente[4]="Trimestrale"
                    cliente[3]=data
                    print("Ciao!!")
                    cliente=str("{:}|{:}|{:}|{:}|{:}".format(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4]))
                    listaUtenti[index]=cliente
                    riscrivi(listaUtenti)
                    
                elif controlloanno==anno:
                    if controllomese>mese:
                        cliente[4]="Trimestrale"
                        cliente[3]=data
                        cliente=str("{:}|{:}|{:}|{:}|{:}".format(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4]))
                        listaUtenti[index]=cliente
                        print("Ciao!!!")
                        riscrivi(listaUtenti)
                        
                    elif controllomese==mese:
                        if controllogiorno>=giorno:
                            print("CIao!!!!")
                            cliente[4]="Trimestrale"
                            cliente[3]=data
                            cliente=str("{:}|{:}|{:}|{:}|{:}".format(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4]))
                            listaUtenti[index]=cliente
                            riscrivi(listaUtenti)
                        else:
                            errore1.grid(row=10, column=1)
                            tornaindietro.grid(row=11, column=1)
                    else:
                        errore1.grid(row=10, column=1)
                        tornaindietro.grid(row=11, column=1)
                else:
                    errore1.grid(row=10, column=1)
                    tornaindietro.grid(row=11, column=1)             
            BottoneAbb1=Button(window, text="Annuale", command=annuale)
            BottoneAbb2=Button(window, text="Semestrale",command=semestrale)
            BottoneAbb3=Button(window, text="Trimestrale", command=trimestrale)
            BottoneAbb1.grid(row=3, column=1)
            BottoneAbb2.grid(row=4, column=1)
            BottoneAbb3.grid(row=5, column=1)


        for i in range (len(listaUtenti)-1):
            cliente=listaUtenti[i]
            cliente=cliente.split("|")
            index=0
            nomeControllo="{:}.{:}".format(cliente[0],cliente[1])
            if nomeControllo==Nome_cognome:
                ctrl=1
                index=i
                print("Ciao")
                
                break
            else:
                continue
        if ctrl==0:
            errore=Label(window, text="Errore!", fg="red")
            errore.grid(row=posizione+4,column=1)
        else:
            rinnova1(index)

    text4=Label(window, text="-------------------------- \n Inserisci il nome.cognome di chi vuoi rinnovare:")
    text4.grid(row=posizione, column=1)
    inserisci=Entry(window)
    inserisci.grid(row=posizione+1, column=1)
    posizione=posizione+2
    bottone=Button(window, text="Invia", command=invia)
    bottone.grid(row=posizione, column=1)
    indietro_button.grid(row=posizione+1, column=1)
    

def cancella():
    text = "Menu Cancella:"
    text3_output = tk.Label(window, text=text, fg="red", font=("Courier", 30,"bold"))
    text3_output.grid(row=0, column=1, padx=150)
    indietro_button = tk.Button(window,text="Indietro",command=indietroB)
    miofile=open("AgaGym.txt","r")
    buffer=miofile.read()
    buffer=buffer.split("\n")
    miofile.close()
    listaUtenti=buffer
    text3=tk.Label(window, text="Abbonamenti", font=("Courier",20,"bold"))
    text3.grid(row=1, column=1)
    errore=Label(window, text="Errore!", fg="red")
    def cancella1():
        Nome_cognome=entra.get()
        Nome_cognome=Nome_cognome.upper()
        ctrl=0
        for i in range (len(listaUtenti)-1):
            cliente=listaUtenti[i]
            cliente=cliente.split("|")
            index=0
            nomeControllo="{:}.{:}".format(cliente[0],cliente[1])
            if nomeControllo==Nome_cognome:
                ctrl=1
                index=i
                print("Ciao")
                
                break
            else:
                continue
        if ctrl==0:
            errore.grid(row=posizione+4,column=1)
        else:
            print("wfwefop")
            listaUtenti.pop(index)
            miofile=open("AgaGym.txt", "w")
            miofile.close()
            miofile=open("AgaGym.txt", "a")
            for i in range(len(listaUtenti)-1):
                inser=str("{:}\n".format(listaUtenti[i]))
                miofile.write(inser)
            miofile.close()
            errore.grid_remove()
            yee=Label(window, text="Cancellato Con Successo (Ricarico in corso...)", fg="green")
            def ricarica():
                time.sleep(3)
                cancellatutto()
                cancella()
            yee.grid(row=posizione+4, column=1)
            ricarica()
            
    posizione=2
    posizione2=1
    for i in range (len(listaUtenti)-1):
        cliente=listaUtenti[i]
        cliente=cliente.split("|")
        testo="{:}.{:}|Abbonamento: {:}".format(cliente[0], cliente [1], cliente[4])
        output=tk.Label(window, text=testo)
        if i>30:
            posizione2=posizione2+1
            output.grid(row=posizione2, column=2)
        else:
            output.grid(row=posizione, column=1)
            posizione=posizione+1

    text5=Label(window, text="--------------------------\nInserisci Nome.Cognome dell'abbonamento da cancellare:")
    entra=Entry(window)
    invio=Button(window, text="Invia", command=lambda:[cancella1()])
    posizione=posizione+1
    text5.grid(row=posizione,column=1)
    entra.grid(row=posizione+1, column=1)
    invio.grid(row=posizione+2, column=1)
    indietro_button.grid(row=posizione+3, column=1)

def visualizza():
    testo = "Menu Visualizza:"
    text4_output = tk.Label(window, text=testo, fg="red", font=("Courier", 30,"bold"))
    text4_output.grid(row=0, column=1, padx=150)
    indietro_button = tk.Button(window,text="Indietro",command=indietroB)
    indietro_button.grid(row=5, column=1)
    text1=Label(window, text="Inserisci il codice fiscale formato A A A A A A N N A N N A N N N A: ")
    sbagliato2=Label(window,text="Errore, Codice fiscale non valido!", fg="red")
    def codicefiscale():
        ctrl=0
        print("Ciao Siamo qyi")
        global cod_fis
        cod_fis=scrivi2.get()
        cod_fis=cod_fis.upper()
        if (len(cod_fis))!=16:
            ctrl=1
            print("Errore! Codice Fiscale non valido! 1 \n")
            sbagliato2.grid(row=4, column=1)
        if ctrl==0:
            
            for i in range(6):
                
                if cod_fis[i]not in lettere and ctrl!=1:
                    ctrl=1
                    print("Errore! Codice Fiscale non valido!2 \n")
                    sbagliato2.grid(row=4, column=1)
            for i in range (6,8):
                if cod_fis[i]not in numeri and ctrl!=1:
                    ctrl=1
                    print("Errore! Codice Fiscale non valido!3 \n")
                    sbagliato2.grid(row=4, column=1)
            if cod_fis[8] not in lettere and ctrl!=1:
                ctrl=1
                print("Errore! Codice Fiscale non valido!4 \n")
                sbagliato2.grid(row=4, column=1)
            for i in range (9,11):
                if cod_fis[i] not in numeri and ctrl!=1:
                    ctrl=1
                    print("Errore! Codice Fiscale non valido!5 \n")
                    sbagliato2.grid(row=4, column=1)
            if cod_fis[11] not in lettere and ctrl!=1:
                ctrl=1
                print("Errore! Codice Fiscale non valido!6 \n")
                sbagliato2.grid(row=4, column=1)
            for i in range (12,15):
                if cod_fis[i] not in numeri and ctrl!=1:
                    ctrl=1
                    print("Errore! Codice Fiscale non valido!7 \n")
                    sbagliato2.grid(row=4, column=1)
            if cod_fis[15] not in lettere and ctrl!=1:
                ctrl=1
                print("Errore! Codice Fiscale non valido8 ! \n")
                sbagliato2.grid(row=4, column=1)
            if ctrl==0:
                print("Siamo qui")
                sbagliato2.grid_remove()
                miofile=open("AgaGym.txt","r")
                buffer=miofile.read()
                buffer=buffer.split("\n")
                
                miofile.close()
                listaUtenti=buffer
                ctrll=0
                for i in range(len(listaUtenti)-1):
                    uten=listaUtenti[i].split("|")
                    codf=uten[2]
                    print(codf)
                    if codf==cod_fis:
                        ctrll=1
                        break
                    else:
                        ctrll=0
                if ctrll==1:
                    for widgets in window.winfo_children():
                        widgets.destroy()
                    testo = "Visualizza:"
                    text4_output = tk.Label(window, text=testo, fg="red", font=("Courier", 30,"bold"))
                    text4_output.grid(row=0, column=1, padx=150)
                    testoNome=f"Nome: {uten[0]}"
                    testoCogone=f"Cognome: {uten[1]}"
                    testoCod_Fiscale=f"Codice Fiscale: {uten[2]}"
                    testoData=f"Data:{uten[3]}"
                    testoAbb=f"Abbonamento:{uten[4]}"
                    labelNome=Label(window, text=testoNome)
                    labelCogone=Label(window, text=testoCogone)
                    labelCodiceFis=Label(window, text=testoCod_Fiscale)
                    labelData=Label(window, text=testoData)
                    labelAbb=Label(window, text=testoAbb)
                    labelNome.grid(row=1, column=1)
                    labelCogone.grid(row=2,column=1)
                    labelCodiceFis.grid(row=3, column=1)
                    labelData.grid(row=4, column=1)
                    labelAbb.grid(row=5, column=1)
                    tornapatras=Button(window, text="Torna Indietro", command=lambda:[cancellatutto(), visualizza()]) 
                    tornapatras.grid(row=6, column=1)                                                                                                           
                else:
                    sbagliato2.grid(row=4, column=1)
                        


    text1.grid(row=1, column=1)
    scrivi2=Entry(window)
    invio=Button(window, text="Invia", command=codicefiscale)
    scrivi2.grid(row=2, column=1)
    invio.grid(row=3, column=1)

    

def verifica():
    testo = "Menu Verifica:"
    text4_output = tk.Label(window, text=testo, fg="red", font=("Courier", 30,"bold"))
    text4_output.grid(row=0, column=1, padx=150)
    indietro_button = tk.Button(window,text="Indietro",command=indietroB)
    indietro_button.grid(row=190, column=1)
    text5=Label(window, text="Inserisci il codice Fiscale: formato: A A A A A A N N A N N A N N N A" )
    text5.grid(row=1, column=1)
    sbagliato2=Label(window,text="Errore, Codice fiscale non valido!", fg="red")
    
    def codicefiscale():
        ctrl=0
        print("Ciao Siamo qyi")
        global cod_fis
        cod_fis=scrivi3.get()
        cod_fis=cod_fis.upper()
        if (len(cod_fis))!=16:
            ctrl=1
            print("Errore! Codice Fiscale non valido! 1 \n")
            sbagliato2.grid(row=4, column=1)
        if ctrl==0:
            
            for i in range(6):
                
                if cod_fis[i]not in lettere and ctrl!=1:
                    ctrl=1
                    print("Errore! Codice Fiscale non valido!2 \n")
                    sbagliato2.grid(row=4, column=1)
            for i in range (6,8):
                if cod_fis[i]not in numeri and ctrl!=1:
                    ctrl=1
                    print("Errore! Codice Fiscale non valido!3 \n")
                    sbagliato2.grid(row=4, column=1)
            if cod_fis[8] not in lettere and ctrl!=1:
                ctrl=1
                print("Errore! Codice Fiscale non valido!4 \n")
                sbagliato2.grid(row=4, column=1)
            for i in range (9,11):
                if cod_fis[i] not in numeri and ctrl!=1:
                    ctrl=1
                    print("Errore! Codice Fiscale non valido!5 \n")
                    sbagliato2.grid(row=4, column=1)
            if cod_fis[11] not in lettere and ctrl!=1:
                ctrl=1
                print("Errore! Codice Fiscale non valido!6 \n")
                sbagliato2.grid(row=4, column=1)
            for i in range (12,15):
                if cod_fis[i] not in numeri and ctrl!=1:
                    ctrl=1
                    print("Errore! Codice Fiscale non valido!7 \n")
                    sbagliato2.grid(row=4, column=1)
            if cod_fis[15] not in lettere and ctrl!=1:
                ctrl=1
                print("Errore! Codice Fiscale non valido8 ! \n")
                sbagliato2.grid(row=4, column=1)
            if ctrl==0:
                print("Siamo qui")
                sbagliato2.grid_remove()
                miofile=open("AgaGym.txt","r")
                buffer=miofile.read()
                buffer=buffer.split("\n")
                
                miofile.close()
                listaUtenti=buffer
                ctrll=0
                for i in range(len(listaUtenti)-1):
                    uten=listaUtenti[i].split("|")
                    codf=uten[2]
                    print(codf)
                    if codf==cod_fis:
                        ctrll=1
                        break
                    else:
                        ctrll=0
                if ctrll==0:
                    sbagliato2.grid(row=4, column=1)
                else:
                    print("OLE")
                    cliente=listaUtenti[i]
                    cliente=cliente.split("|")
                    data=cliente[3]
                    data=data.split("-")
                    giorno=data[2]
                    n_1=giorno[0]
                    n_2=giorno[1]
                    giorno=n_1+n_2
                    giorno=int(giorno)
                    data.pop()
                    anno=data[0]
                    anno=int(anno)
                    mese=data[1]
                    mese=int(mese)
                    if cliente[4]=="Annuale":
                        anno=anno+1
                    if cliente[4]=="Semestrale":
                        mese=mese+6
                        if mese>12:
                            anno=anno+1
                            c=mese-12
                            mese=c
                    if cliente[4]=="Trimestrale":
                        mese=mese+3
                        if mese>12:
                            anno=anno+1
                            c=mese-12
                            mese=c
                    controllomese=int(datetime.datetime.now().month)
                    controlloanno=int(datetime.datetime.now().year)
                    controllogiorno=int(datetime.datetime.now().day)
                    Testo="Data di scadenza: {:}/{:}/{:} ".format(anno, mese, giorno)
                    Testog=Testo+"(Scaduto)"
                    Scaduto=Label(window, text=Testog, fg="red")
                    NonScaduto=Label(window, text=Testo, fg="green")
                    testoNome=f"Nome: {cliente[0]}"
                    testoCogone=f"Cognome: {cliente[1]}"
                    testoCod_Fiscale=f"Codice Fiscale: {cliente[2]}"
                    testoAbb=f"Abbonamento:{cliente[4]}"
                    labelNome=Label(window, text=testoNome)
                    labelCogone=Label(window, text=testoCogone)
                    labelCodiceFis=Label(window, text=testoCod_Fiscale)
                    labelAbb=Label(window, text=testoAbb)
                    labelNome.grid(row=1, column=1)
                    labelCogone.grid(row=2,column=1)
                    labelCodiceFis.grid(row=3, column=1)
                    labelAbb.grid(row=4, column=1)
                    tornapatras=Button(window, text="Torna Indietro", command=lambda:[cancellatutto(), verifica()]) 
                    tornapatras.grid(row=6, column=1)
                    if controlloanno>anno:
                        print("Scaduti")
                        Scaduto.grid(row=5, column=1)
                    elif controlloanno==anno:
                        print("Scaduti")
                        Scaduto.grid(row=5, column=1)
                        if controllomese>mese:
                            print("Scaduti")
                            Scaduto.grid(row=5, column=1)
                        elif controllomese==mese:
                            print("Scaduti")
                            Scaduto.grid(row=5, column=1)
                            if controllogiorno>=giorno:
                                print("Scaduti")
                                Scaduto.grid(row=5 , column=1)
                            else:
                                print("No")
                                NonScaduto.grid(row=5 , column=1)
                        else:
                            print("No")
                            NonScaduto.grid(row=5 , column=1)
                    else:
                        print("No")
                        NonScaduto.grid(row=5 , column=1)
            
    scrivi3=Entry(window)
    scrivi3.grid(row=2, column=1)
    invio1=Button(window, text="Invia", command=lambda:[codicefiscale(), scrivi3.grid_remove(), invio1.grid_remove(), indietro_button.grid_remove(),text5.grid_remove()])
    invio1.grid(row=3, column=1)

    
window.mainloop() 














