#Curnis Riccardo - Daniele Morgan - Medolago Simone - Panseri Gabriele - Ratti Gabriele - Tosques Simone
#Progetto Summer Camp - 12-16 Giugno 2023

#--------------Codice---------------

#Dichiaro i dizionari

import qrcode
import datetime

lettere=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
numeri=["1","2","3","4","5","6","7","8","9","0"]
def p_input(tipo,msg,err):
    if tipo=="int":
        while True:
            try:
                x=int(input(msg))
                break
            except ValueError:
                print(err)
                continue
    elif tipo=="float":
        while True:
            try:
                x=float(input(msg))
                break
            except ValueError:
                print(err)
                continue
    else:
        print("Errore nel programma")
    return x

#--------------------------------------------------------------------------------
def info():
    while True:
        nome=str(input("Inserisci il nome: "))
        nome=nome.upper()
        cntrl=0
        if len(nome)>2 and len(nome)<31:
            for i in range(len(nome)):
                if nome[i] not in lettere:
                    cntrl=1
                    print("Errore! Nome non valido!\n")
                    break
            
        else:
            cntrl=1
            print("Nome non valido!\n")
            continue
        if cntrl==0:
            break

#--------------------------------------------------------------------------------
    while True:
        cognome=str(input("Inserisci il cognome: "))
        cognome=cognome.upper()
        cntrl=0
        if len(cognome)>2 and len(cognome)<31:
            for i in range(len(cognome)):
                if cognome[i] not in lettere:
                    cntrl=1
                    print("Errore! Cognome non valido!\n")
                    break
                    
        else:
            cntrl=1
            print("Cognome non valido!\n")
            continue
        if cntrl==0:
            break

#--------------------------------------------------------------------------------
    while True:
        print("FORMATO CODICE FISCALE: A A A A A A N N A N N A N N N A")
        cod_fis=str(input("Inserisci il codice fiscale : "))
        cod_fis=cod_fis.upper()
        cntrl=0
        if (len(cod_fis))!=16:
            cntrl=1
            print("Errore! Codice Fiscale non valido! \n")
        if cntrl==0:
            for i in range(6):
                if cod_fis[i]not in lettere and cntrl!=1:
                    cntrl=1
                    print("Errore! Codice Fiscale non valido! \n")
                    break
            for i in range (6,8):
                if cod_fis[i]not in numeri and cntrl!=1:
                    cntrl=1
                    print("Errore! Codice Fiscale non valido! \n")
                    break
            if cod_fis[8] not in lettere and cntrl!=1:
                cntrl=1
                print("Errore! Codice Fiscale non valido! \n")
            for i in range (9,11):
                if cod_fis[i] not in numeri and cntrl!=1:
                    cntrl=1
                    print("Errore! Codice Fiscale non valido! \n")
                    break
            if cod_fis[11] not in lettere and cntrl!=1:
                cntrl=1
                print("Errore! Codice Fiscale non valido! \n")

            for i in range (12,15):
                if cod_fis[i] not in numeri and cntrl!=1:
                    cntrl=1

                    print("Errore! Codice Fiscale non valido! \n")
                    break
            if cod_fis[15] not in lettere and cntrl!=1:
                cntrl=1
                print("Errore! Codice Fiscale non valido! \n")

        if cntrl==0:
            break

#--------------------------------------------------------------------------------
    while True:
        yn=str(input("Registrare una data nel passato? "))
        yn=yn.upper()
        if yn=="SI":
            while True:
                anno=p_input("int","Anno: ","Inserisci un anno valido")
                if anno>datetime.datetime.now().year or anno<1900:
                    print("Errore anno non valido!")
                    continue
                elif anno==datetime.datetime.now().year:
                    mese=p_input("int","Mese: ","Inserisci un mese valido")
                    if mese==datetime.datetime.now().month:
                        giorno=p_input("int","Giorno: ","Inserisci un giorno valido")
                        if giorno>datetime.datetime.now().day:
                            print("Errore giorno non valido!")
                            continue
                    elif mese<datetime.datetime.now().month:
                        giorno=p_input("int","Giorno: ","Inserisci un giorno valido")
                        if giorno>31 or giorno<1:
                            print("Giorno non valido!")
                            continue
                    elif mese>12 or mese<1:
                        print("Mese non valido!")
                        continue
                else:
                    mese=p_input("int","Mese: ","Inserisci un mese valido")
                    if mese>12 or mese<1:
                        print("Mese non valido!")
                        continue
                    giorno=p_input("int","Giorno: ","Inserisci un giorno valido")
                    if giorno>31 or giorno<1:
                        print("Giorno non valido!")
                        continue
                datap=datetime.datetime(anno, mese, giorno)
                print(datap)
                break
            break
        elif yn=="NO":
            datap=datetime.datetime.now()
            print(datap)
            break
        else:
            print("Errore! Riprova!")
            continue

#--------------------------------------------------------------------------------
    while True:
        abb=["Annuale","Semestrale","Trimestrale"]
        for i in range(len(abb)):
            print("{:d}. {:s}".format(i+1,abb[i]))
        a=p_input("int","Scelta Abbonamento: ","Scelta non valida!")
        if a>0 and a<4:
            abbonamento=abb[a-1]
            break
        else:
            print("Errore!")
            continue
    global record
    record=("{:}|{:}|{:}|{:}|{:}".format(nome, cognome,cod_fis,datap,abbonamento))
    print(record)
    #crea QrCode
    code=qrcode.make(cod_fis)
    name="{:}.{:}.png".format(nome,cognome)
    code.save (name)

def aggiungi(nomefile): #codice fiscale, nome e cognome, data di iscrizione, tipo di abbonamento
    print("Iscriviti!")
    info()
    record1=str(record+"\n")
    miofile=open(nomefile,"a")
    miofile.write(record1)
    miofile.flush()
    miofile.close()
    
def rinnova(nomefile):
    print("Rinnova l'abbonamento!")
    miofile=open(nomefile,"r")
    buffer=miofile.read()
    buffer=buffer.split("\n")
    for i in range(len(buffer)-1):
        print("{:})".format(i+1),buffer[i])
    

def cancella(nomefile):
    print("Elimina un'iscrizione!")
    print("Seleziona l'iscrizione da rimuovere: ")
    miofile=open(nomefile,"r")
    buffer=miofile.read()
    buffer=buffer.split("\n")
    for i in range(len(buffer)-1):
        print("{:})".format(i+1),buffer[i])
    scel=p_input("int","Indica il numero dell'iscrizione che vuoi rimuovere: ","Numero non valido")
    scel-=1
    buffer.pop(scel)
    miofile.flush()
    miofile.close()
    miofile=open(nomefile,"w")
    miofile.close()
    miofile=open(nomefile,"a")
    for f in range(len(buffer)-1):
        miofile.write(buffer[f]+"\n")
    miofile.flush()
    miofile.close()

def visualizza(nomefile):
    print("Visualizza le iscirzioni")
    miofile=open(nomefile,"r")
    buffer=miofile.read()
    buffer=buffer.split("\n")
    for i in range(len(buffer)-1):
        print(buffer[i])
        
def verifica():
    print




#--------------------------------------------------------------------------------
def main():
    while True:
        print("---MENU---")
        print("1. Aggiungi Iscrizione")
        print("2. Rinnova Iscrizione")
        print("3. Cancella Iscrizione")
        print("4. Visualizza Iscrizioni")
        print("5. Verifica Validità")
        print("6. Esci")
        s=p_input("int","Scelta: ","Scelta non valida!")
        if s>0 and s<7:
            if s==1:
                aggiungi("AgaGym.txt")
            elif s==2:
                rinnova("AgaGym.txt")
            elif s==3:
                cancella("AgaGym.txt")
            elif s==4:
                visualizza("AgaGym.txt")
            elif s==5:
                verifica()
            elif s==6:
                print("Uscita in corso...")
                quit()

main()