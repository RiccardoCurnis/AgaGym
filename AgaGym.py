#Curnis Riccardo - Daniele Morgan - Medolago Simone - Panseri Gabriele - Ratti Gabriele - Tosques Simone
#Progetto Summer Camp - 12-16 Giugno 2023

#--------------Codice---------------

#Dichiaro i dizionari

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

<<<<<<< HEAD
p_input("int","Scelta: ","Errore!!1!")
=======
p_input("int","Scelta: ","Errore!!1")
>>>>>>> 0b6fda8a1209dd56af51d01f78fe4c739985f812
