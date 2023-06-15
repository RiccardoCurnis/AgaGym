from tkinter import *
from PIL import ImageTk,Image
import tkinter
from tkinter import *
from tkinter import ttk
import datetime
from tkinter import messagebox
from datetime import datetime

w=Tk()
w.geometry('900x500')
w.configure(bg='#262626')#12c4c0')
w.resizable(0,0)
w.title('Toggle Menu')


def default_home():
    f2=Frame(w,width=900,height=455,bg='#262626')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Home',fg='white',bg='#262626')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=290,y=150-45)

   
def home():
    f1.destroy()
    f2=Frame(w,width=900,height=455,bg='#262626')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Home',fg='white',bg='#262626')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=290,y=150-45)
    toggle_win()
 

def acer():
    f1.destroy()
    f2=Frame(w,width=900,height=455,bg='white')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Acer',fg='black',bg='white')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=290,y=150-45)
    toggle_win()
   
    

def dell():
    f1.destroy()
    f2=Frame(w,width=900,height=455,bg='white')
    f2.place(x=0,y=45)
    l2=Label(f2,text='Dell',fg='black',bg='white')
    l2.config(font=('Comic Sans MS',90))
    l2.place(x=320,y=150-45)
    toggle_win()


def toggle_win():
    global f1
    f1=Frame(w,width=300,height=500,bg='#12c4c0')
    f1.place(x=0,y=0)
    
    #buttons
    def bttn(x,y,text,bcolor,fcolor,cmd):
     
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= '#262626'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#262626'

        myButton1 = Button(f1,text=text,
                       width=42,
                       height=2,
                       fg='#262626',
                       border=0,
                       bg=fcolor,
                       activeforeground='#262626',
                       activebackground=bcolor,            
                        command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

    bttn(0,80,'H O M E','#0f9d9a','#12c4c0',home)
    bttn(0,117,'A C E R','#0f9d9a','#12c4c0',acer)
    bttn(0,154,'D E L L','#0f9d9a','#12c4c0',dell)
    bttn(0,191,'A S U S','#0f9d9a','#12c4c0',None)
    bttn(0,228,'A P P L E','#0f9d9a','#12c4c0',None)
    bttn(0,265,'A C E R','#0f9d9a','#12c4c0',None)

    #
    def dele():
        f1.destroy()
        b2=Button(w,image=img1,
               command=toggle_win,
               border=0,
               bg='#262626',
               activebackground='#262626')
        b2.place(x=5,y=8)

    global img2
    img2 = ImageTk.PhotoImage(Image.open("close.png"))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#12c4c0',
           activebackground='#12c4c0').place(x=5,y=10)
    

default_home()

img1 = ImageTk.PhotoImage(Image.open("open.png"))

global b2
b2=Button(w,image=img1,
       command=toggle_win,
       border=0,
       bg='#262626',
       activebackground='#262626')
b2.place(x=5,y=8)

def main_iscrizione():
    window = tkinter.Tk()
    window.title("Dati")
    lettere=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
    numeri=["1","2","3","4","5","6","7","8","9","0","/"]
    dati=[]

    #----------------------------------------------------------------------------------------------------
    def error_data():
        tkinter.messagebox.showwarning(title="Error", message="Errore con la data")

    #----------------------------------------------------------------------------------------------------
    def error_nomecorto():
        tkinter.messagebox.showwarning(title="Error", message="Nome troppo corto")

    #----------------------------------------------------------------------------------------------------
    def error_nomeval():
        tkinter.messagebox.showwarning(title="Error", message="Il nome deve includere solo lettere")

    #----------------------------------------------------------------------------------------------------
    def error_cogncorto():
        tkinter.messagebox.showwarning(title="Error", message="Cognome troppo corto")

    #----------------------------------------------------------------------------------------------------
    def error_cognval():
        tkinter.messagebox.showwarning(title="Error", message="Il cognome deve includere solo lettere")

    #----------------------------------------------------------------------------------------------------
    def error_codicefisc():
        tkinter.messagebox.showwarning(title="Error", message="Codice fiscale non valido")

    #----------------------------------------------------------------------------------------------------
    def error_eta():
        tkinter.messagebox.showwarning(title="Error", message="Errore con l'età")

    #----------------------------------------------------------------------------------------------------
    def error_durataabb():
        tkinter.messagebox.showwarning(title="Error", message="Errore con il tipo di abbonamento")

    #----------------------------------------------------------------------------------------------------
    def error_non_iscritt():
        tkinter.messagebox.showwarning(title="Error", message="utente non iscitto in pelastra")

    #----------------------------------------------------------------------------------------------------
    def rinnov():
        nome = nome_entry.get()
        nome=nome.upper()
        cognome = cognome_entry.get()
        cognome=cognome.upper()
        codicefisc = codicefisc_entry.get()
        codicefisc=codicefisc.upper()
        dataiscriz = dataiscriz_entry.get()
        durataabb = durataabb_combobox.get()
        durataabb=durataabb.upper()

        if nome not in dati and cognome not in dati or datah not in dati:
            error_non_iscritt
        else:
            print("ciao")
            ctrl=0
            if len(nome)>2 and len(nome)<31:

                        for i in range(len(nome)):
                            if nome[i] not in lettere:
                                ctrl=1 

                            else:
                                ctrl=0


            else:

                    ctrl=2
            if ctrl==0:
                 pass

            elif ctrl==2:
                error_nomecorto()

            elif ctrl==1:
                error_nomeval()





            if len(cognome)>2 and len(cognome)<31:

                        for i in range(len(cognome)):
                            if cognome[i] not in lettere:
                                ctrl=1 

                            else:
                                ctrl=0


            else:

                    ctrl=2
            if ctrl==0:
                    pass
            elif ctrl==2:
                  error_cogncorto()
            elif ctrl==1:
                 error_cognval()



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
                    pass
            elif ctrl==1:
                  error_eta()





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
                    pass





            buffer=dataiscriz.split("/")
            d=int(buffer[0])
            m=int(buffer[1])
            y=int(buffer[2])
            ctrl=0
            if y<1900 or y>datetime.now().year:
                ctrl=1
            else:
                if m<1 or m>12:
                    ctrl=1
                elif y==datetime.now().year and m>datetime.now().month:
                     ctrl=1
                else:
                    if d<1 or d>31:
                        ctrl=1
                    elif y==datetime.now().year and m==datetime.now().month and d>datetime.now().day:
                        ctrl=1
                    else:
                        ctrl=0
            if ctrl==1:
                 error_data()
            else:
                datah=str(datetime(y,m,d))
                if datah<datetime.now:
                    file1=open("datafile.txt","r")
                    a=file1.read()
                    a=a.split("\n")

                    bb=[]








            if durataabb=="TRIMESTRE" or durataabb=="SEMESTRE" or durataabb=="ANNUALE":
                  pass
            else:
                  error_durataabb()


    #----------------------------------------------------------------------------------------------------

    def prendidati():
        file1=open("datifile.txt","a")
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

                ctrl=2
        if ctrl==0:
                dati.append(nome)

        elif ctrl==2:
            error_nomecorto()

        elif ctrl==1:
            error_nomeval()




        cognome = cognome_entry.get()
        cognome=cognome.upper()
        if len(cognome)>2 and len(cognome)<31:

                    for i in range(len(cognome)):
                        if cognome[i] not in lettere:
                            ctrl=1 

                        else:
                            ctrl=0


        else:

                ctrl=2
        if ctrl==0:
                dati.append(cognome)

        elif ctrl==2:
              error_cogncorto()
        elif ctrl==1:
             error_cognval()



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

        elif ctrl==1:
              error_eta()




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




        dataiscriz = dataiscriz_entry.get()
        buffer=dataiscriz.split("/")
        d=int(buffer[0])
        m=int(buffer[1])
        y=int(buffer[2])
        ctrl=0
        if y<1900 or y>datetime.now().year:
            ctrl=1
        else:
            if m<1 or m>12:
                ctrl=1
            elif y==datetime.now().year and m>datetime.now().month:
                 ctrl=1
            else:
                if d<1 or d>31:
                    ctrl=1
                elif y==datetime.now().year and m==datetime.now().month and d>datetime.now().day:
                    ctrl=1
                else:
                    ctrl=0
        if ctrl==1:
             error_data()
        else:
            datah=str(datetime(y,m,d))
            dati.append(datah)





        durataabb = durataabb_combobox.get()
        durataabb=durataabb.upper()
        if durataabb=="TRIMESTRE" or durataabb=="SEMESTRE" or durataabb=="ANNUALE":
              dati.append(durataabb)
        else:
              error_durataabb()
        file1.write(dati)








    frame = tkinter.Frame(window)
    frame.pack()

    utente_info_frame = tkinter.LabelFrame(frame, text="Informazioni dell'Utente")
    utente_info_frame.grid(row = 0, column = 0, padx = 20, pady = 20)

    nome_label= tkinter.Label(utente_info_frame, text="Nome")
    nome_label.grid(row = 0, column = 0)
    nome_entry = tkinter.Entry(utente_info_frame)
    nome_entry.grid(row = 1, column = 0)
    cognome_label= tkinter.Label(utente_info_frame, text="Cognome")
    cognome_label.grid(row = 0, column = 1)
    cognome_entry = tkinter.Entry(utente_info_frame)
    cognome_entry.grid(row = 1, column = 1)




    eta_label = tkinter.Label(utente_info_frame, text="Eta'")
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

    courses_frame = tkinter.LabelFrame(frame)
    courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

    enter_button = tkinter.Button(courses_frame,text="Iscrizione", command=prendidati,width=25)
    enter_button.grid(row=5, column=0, sticky="news", padx=20, pady=10)

    rinnovo_button = tkinter.Button(courses_frame ,text="Rinnovo", command=rinnov,width=25)
    rinnovo_button.grid(row=5, column=1, sticky="news", padx=20, pady=10)

    #----------------------------------------------------------------------------------------------------
    def on_click(event):
        dataiscriz_entry.configure(state=NORMAL)
        dataiscriz_entry.delete(0, END)

        # make the callback only work once
        dataiscriz_entry.unbind('<Button-1>', on_click_id)





    on_click_id = dataiscriz_entry.bind('<Button-1>', on_click)

    adesso = datetime.now()
w.mainloop()
