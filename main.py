############################################# IMPORTING ################################################
import tkinter as tk
from tkinter import Entry, ttk
from tkinter import messagebox as mess
from tkinter import Frame
from tkinter import *
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time



############################################# FUNZIONI ################################################

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


def tick():
    time_string = time.strftime('%H:%M:%S')  #setto l'ora del formato time 00:00:00
    clock.config(text=time_string)
    clock.after(200,tick)  #Richiama la funzione dopo 200 MS = 0,2 s


def contact():
    mess._show(title='Contatti', message="Email: fra9cesca9@gmail.com / Telegram: @F23A99 ")


### Verifico la presenza del classificatore pre addestrato ###
def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='File Mancanti', message='File mancanti nel sistema. Contattami per aiuto.')
        window.destroy()


### Memorizzare la password nel file per la prima volta o modificare la password esistente ###
def save_pass():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Password non trovata.', 'Inserisci una nuova password      ', show='*')
        if new_pas == None:
            mess._show(title='Nessuna Password Inserita', message='Non è stata inserita nessuna password. Riprova!')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registrata', message='Nuova password registrata correttamente.')
            return
    op = (old.get())
    newp= (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if(newp == nnewp):
            txf = open("TrainingImageLabel\psd.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Errore', message='Prima di salvare devi riconfermare correttamente la nuova password!')
            return
    else:
        mess._show(title='Password Errata', message='La password inserita non è valida.Inserisci la vecchia password correttamente.')
        return
    mess._show(title='Password cambiata', message='La Password è stata cambiata correttamente!')
    master.destroy()


def change_pass():
    global master
    master = tk.Tk()
    master.geometry("445x160")
    master.resizable(False,False)
    master.title("Modifica Password")
    master.configure(background="white")
    lbl4 = tk.Label(master,text='Inserisci vecchia Password',bg='white',font=('times', 12, ' bold '))
    lbl4.place(x=10,y=10)
    global old
    old=tk.Entry(master,width=25 ,fg="black",relief='solid',font=('times', 12, ' bold '),show='*')
    old.place(x=210,y=10)
    lbl5 = tk.Label(master, text='Inserisci Nuova Password', bg='white', font=('times', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black",relief='solid', font=('times', 12, ' bold '),show='*')
    new.place(x=210, y=45)
    lbl6 = tk.Label(master, text='Conferma Nuova Password', bg='white', font=('times', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid',font=('times', 12, ' bold '),show='*')
    nnew.place(x=210, y=80)
    cancel=tk.Button(master,text="Cancella", command=master.destroy ,fg="black"  ,bg="red" ,height=1,width=25 , activebackground = "white" ,font=('times', 10, ' bold '))
    cancel.place(x=220, y=120)
    save1 = tk.Button(master, text="Salva", command=save_pass, fg="black", bg="#3ece48", height = 1,width=25, activebackground="white", font=('times', 10, ' bold '))
    save1.place(x=30, y=120)
    master.mainloop()


### Verifica e confornta la password con il file psd.txt prima di iniziare la fase di training ###
def psw():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        new_pas = tsd.askstring('Password non trovata', 'Inserisci una nuova password:   \t\t\t   ', show='*')
        if new_pas == None:
            mess._show(title='Nessuna Password Inserita', message='Non è stata inserita nessuna password. Riprova!')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password inserita', message='La Password è stata inserita correttamente!')
            return
    password = tsd.askstring('Password', 'Inserisci Password', show='*')
    if (password == key):
        TrainImages()
    elif (password == None):
        pass
    else:
        mess._show(title='Password Errata', message='Hai inserito la password errata. Riprova!')



def clear():
    txt.delete(0, 'end')
    res = "Procedi con l'acquisizione delle immagini. Attendi davanti la webcam qualche secondo."
    message1.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = "Procedi con l'acquisizione delle immagini. Attendi davanti la webcam qualche secondo."
    message1.configure(text=res)


### Acquisizione di volti nell'immagine ###
def TakeImages():
    check_haarcascadefile()
    columns = ['SERIAL NO.', '', 'MATRICOLA', '', 'NOME']
    assure_path_exists("StudentDetails/")
    assure_path_exists("TrainingImage/")
    serial = 0
    exists = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists:
        with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for l in reader1:
                serial = serial + 1
        serial = (serial // 2)
        csvFile1.close()
    else:
        with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(columns) #Inserimento delle colonne nel file csv
            serial = 1
        csvFile1.close()
    Id = (txt.get())  #Sia la matricola che il nome-cognome sono usati per riconoscere l'immagine
    name = (txt2.get())
    if ((name.isalpha()) or (' ' in name)):  #Controlli sui parametri 
    #Istanziare l'oggetto VideoCapture per accedere alla webcam. Se voglio usare una webcam esterna il parametro è 1
        cam = cv2.VideoCapture(0)   
        harcascadePath = "haarcascade_frontalface_default.xml" #Specifico il percorso del file haarcascade
        detector = cv2.CascadeClassifier(harcascadePath) #creazione del modello pre addestrato
        sampleNum = 0 #Inizializzazione del numero di campione (n. di immagini) come 0
        while (True):
            ret, img = cam.read() #Lettura delle riprese video fotogramma per fotogramma
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #Conversione dell'immagine in scala di grigi
            #Rilevamento volti nell'immagine --> parametri gray=immagine in scala di grigi; 
            # 1.3=fattore di scala richiesto dal classificatore Haar-Cascade per realizzare una serie di versioni 
            # ridotte dell'immagine originaria, a formare una sorta di piramide; 
            # 5=numero di regioni vicine che deve essere considerato dall'algoritmo per ognuna delle aree candidate 
            # ad essere riconosciute come volti.
            faces = detector.detectMultiScale(gray, 1.3, 5)  
            for (x, y, w, h) in faces: #per creare un rettangolo attorno all'immagine
                #La lista faces, contiene le coordinate di ognuno dei volti identificati dall'algoritmo, e sfrutta queste 
                # informazioni per disegnare un rettangolo attorno ad ognuno dei volti identificati. 
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  
                # incremento del numero di campioni
                sampleNum = sampleNum + 1
                # Salvataggio del volto catturato della cartella del dataset TrainingImage
                cv2.imwrite("TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                # visualizzare il fotogramma che è stato catturato e il rettangolo disegnato intorno ad esso.
                cv2.imshow('Acquisizione delle immagini in corso. Attendere.', img) #con questi valori disgeno un rettangolo
            # Tempo: attendi 100 ms
            if cv2.waitKey(100) & 0xFF == ord('q'):         
                break
            # interrompi se il numero del campione è superiore a 100
            elif sampleNum > 100:
                break
        cam.release()
        cv2.destroyAllWindows()  #chiudo tutte le finestre
        #Visualizzazione del messaggio per l'utente
        res = "Immagini acquisite per la matricola: " + Id +". Ora devi salvare il profilo." 
        row = [serial, '', Id,  '', name] #Creare le voci per l'utente in un file csv
        with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row) #Inserimento della riga nel file csv
        csvFile.close()
        message1.configure(text=res)
    else:
        if (name.isalpha() == False):
            res = "Attenzione: Inserire Matricola, Nome e Cognme."
            message.configure(text=res)


### Training delle immagini salvate nella cartella di Training delle  immagini ###
def TrainImages():
    check_haarcascadefile()
    assure_path_exists("TrainingImageLabel/")
    #algoritmo all'interno del modulo OpenCV utilizzato per la formazione del set di dati dell'immagine
    recognizer = cv2.face_LBPHFaceRecognizer.create() 
    harcascadePath = "haarcascade_frontalface_default.xml" #Specificare il percorso per il file HaarCascade
    detector = cv2.CascadeClassifier(harcascadePath) #creazione del rivelatore per il viso
    #Salvare i volti addestrati e i rispettivi ID in un modello denominato "trainner.yml
    faces, ID = getImagesAndLabels("TrainingImage") 
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='Nessuna Registrazione', 
            message='Si prega di registrare gli utenti prima di effettuare il riconoscimento.')
        return
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Profilo salvato con successo."  #Visualizzazione messaggi
    message1.configure(text=res)
     #Messaggio visualizzato con contatore registrazioni
    message.configure(text='Profili attualmente registrati  : ' + str(ID[0])) 


### Estrarre i volti dal campione di training ###
def getImagesAndLabels(path):
    # ottenere il percorso di tutti i file nella cartella
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # creazione di una lista di volti vuota
    faces = []
    # creazione di una lista di matricole vuota
    Ids = []
    
    for imagePath in imagePaths:
        # caricare l'immagine e convertirla in scala di grigi
        pilImage = Image.open(imagePath).convert('L')
        # Ora stiamo convertendo l'immagine PIL nell' array numpy
        imageNp = np.array(pilImage, 'uint8')
        # ottenere l'Id dall'immagine
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # estrarre il viso dal campione dell'immagine di training
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids

### Fase di test ###
def TrackImages():
    check_haarcascadefile()
    assure_path_exists("Attendance/")
    assure_path_exists("StudentDetails/")
    for k in tv.get_children():
        tv.delete(k)
    msg = ''
    i = 0
    j = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
    if exists3:
        recognizer.read("TrainingImageLabel\Trainner.yml") #Lettura del modello addestrato
    else:
        mess._show(title='Dati Mancanti', message='Registrare prima  un nuovo utente. Dopo procedere con il login.')
        return
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);

    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX  #Tipo di carattere
    col_names = ['Matricola', '', 'Nome', '', 'Data', '', 'Ora'] #creo un dataframe per contenere i dati
    exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
    if exists1:
        df = pd.read_csv("StudentDetails\StudentDetails.csv") #ottenere il nome da "userdetails.csv"
    else:
        mess._show(title='Dettagli Mancanti', message='Attenzione! I dati di alcuni studenti sono mancanti. Si prega di ricontrollare.')
        cam.release()
        cv2.destroyAllWindows()
        window.destroy()
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
            serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50): #una confidence inferiore a 50 indica un buon riconoscimento facciale
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['SERIAL NO.'] == serial]['NOME'].values
                ID = df.loc[df['SERIAL NO.'] == serial]['MATRICOLA'].values
                ID = str(ID)
                ID = ID[1:-1]
                bb = str(aa)
                bb = bb[2:-2]
                attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]

            else:
                Id = 'Unknown'
                bb = str(Id)
            cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
        cv2.imshow("Riconoscimento utente in corso. Premere 'Q' per registrare la presenza.", im)
        if (cv2.waitKey(1) == ord('q')):  #Interrompi quando premi "Q" da tastiera
             break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    exists = os.path.isfile("Attendance\Attendance_" + date + ".csv")
    if exists:
        with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1: #Apro il foglio delle presenze per aggiornarlo
            writer = csv.writer(csvFile1)
            writer.writerow(attendance)
        csvFile1.close()
    else:
        with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
            writer = csv.writer(csvFile1)
            writer.writerow(col_names)
            writer.writerow(attendance)
        csvFile1.close()
    with open("Attendance\Attendance_" + date + ".csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for lines in reader1:
            i = i + 1
            if (i > 1):
                if (i % 2 != 0):
                    iidd = str(lines[0]) + '   '
                    tv.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
    csvFile1.close()
    cam.release()
    cv2.destroyAllWindows()

####################################################################################
    
global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day,month,year=date.split("-")

mont={'01':'Gennaio',
      '02':'Febbraio',
      '03':'Marzo',
      '04':'Aprile',
      '05':'Maggio',
      '06':'Giugno',
      '07':'Luglio',
      '08':'Agosto',
      '09':'Settembre',
      '10':'Ottobre',
      '11':'Novembre',
      '12':'Dicembre'
      }


################################################ WINDOW ############################################################################
window = tk.Tk()
window.geometry("1000x700")
window.resizable(False,False)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)


#window.state('zoomed')

window.iconphoto(False, tk.PhotoImage(file='C:/Users/Utente/Desktop/BIOMETRIA/ESAME_BIO/SistemaDiRilevamentoDellePresenze/logo2.png'))
window.title("Sistema di rilevamento delle presenze")

#### FRAME ####
page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)
page4 = Frame(window)

for frame in (page1,page2,page3,page4):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(page1)

######################################## START WINDOW (page1) ##################################################################
page1.configure(bg='#C6E4D9')

message11 = tk.Label(page1, text="RICONOSCIMENTO DEGLI ALUNNI" ,background='#C6E4D9',fg="white",bg="#116062",width=55 ,height=1,font=('times', 26, ' bold '))
message11.place(x=-90, y=0)
message12 = tk.Label(page1, text="PRESENTI NELL'AULA" ,background='#C6E4D9',fg="white",bg="#116062",width=55 ,height=1,font=('times', 26, ' bold '))
message12.place(x=-90, y=40)

frame3 = tk.Frame(page3, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.12, relheight=0.07)

frame4 = tk.Frame(page3, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.18, relheight=0.07)

page1_label2 = Label(page1, text="Scegli una delle seguenti voci:", background='#C6E4D9', font=('Calibri Light', 13, 'bold'))
page1_label2.place(x=380, y=150)

page1_button = Button(page1, text='COME FUNZIONA?', font=('Arial', 13, 'bold'), width=20, height=2, background='#116062',fg='white', command=lambda: show_frame(page2))
page1_button.place(x=400, y=250)

page1_button2 = Button(page1, text='REGISTRATI', font=('Arial', 13, 'bold'), width=20, height=2, background='#116062', fg='white', command=lambda: show_frame(page3))
page1_button2.place(x=400, y=350)

page1_button3 = Button(page1, text='LOGIN', font=('Arial', 13, 'bold'), width=20, height=2, background='#116062',fg='white', command=lambda: show_frame(page4))
page1_button3.place(x=400, y=450)


###################################################### COME FUNZIONA(page2) ##################################################################
page2.config(bg='#C6E4D9')

message10 = tk.Label(page2, text='Come funziona?' ,background='#C6E4D9',fg="white",bg="#116062",width=55 ,height=1,font=('times', 30, ' bold '))
message10.place(x=-145, y=0)

frame3 = tk.Frame(page3, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.12, relheight=0.07)

frame4 = tk.Frame(page3, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.18, relheight=0.07)

page2_label3 = Label(page2, text='- Benvenuto nel sistema di riconsocimento delle presenze!',background='#C6E4D9', font=('Calibri', 16,'bold'))
page2_label3.place(x=50, y=100)

page2_label4 = Label(page2, text="  Questo è un sistema di riconoscimento facciale che ha come unico scopo quello di registrare la presenza ", background='#C6E4D9',font=('Calibri', 16,))
page2_label4.place(x=50, y=130)

page2_label5 = Label(page2, text="  di uno studente all'interno dell'aula, utilizzando una semplice webcam.", background='#C6E4D9',font=('Calibri', 16,))
page2_label5.place(x=50, y=160)

page2_label6 = Label(page2, text='- Sei un nuovo utente? È la prima volta che accedi al sistema?',background='#C6E4D9', font=('Calibri', 16, 'bold'))                                           
page2_label6.place(x=50, y=240)

page2_label7 = Label(page2, text='  Clicca sul pulsante "REGISTRATI" e procedi inserendo il Numero di Matricola, Nome e Cognome.',background='#C6E4D9', font=('Calibri', 16,))
page2_label7.place(x=50, y=270)

page2_label8 = Label(page2, text='  Dopo, procedi cliccando sul pulsante "Acquisisci immagini" e posiziona il volto davanti alla webcam ', background='#C6E4D9',font=('Calibri', 16,))
page2_label8.place(x=50, y=300)

page2_label9 = Label(page2, text='  attendendo qualche secondo. Attendi fino a quando il sistema di acquisizione immagini si chiude.', background='#C6E4D9',font=('Calibri', 16,))
page2_label9.place(x=50, y=330)

page2_label10 = Label(page2, text='  A questo punto clicca sul pulsante "Salva profilo" per completare la registrazione.', background='#C6E4D9',font=('Calibri', 16,))
page2_label10.place(x=50, y=360)

page2_label11 = Label(page2, text='- Sei già registrato nel sistema? Hai già un profilo utente?', background='#C6E4D9',font=('Calibri', 16, 'bold'))                                           
page2_label11.place(x=50, y=440)

page2_label12 = Label(page2, text='  Clicca sul pulsante "LOGIN".', background='#C6E4D9',font=('Calibri', 16,))                                           
page2_label12.place(x=50, y=470)

page2_label13 = Label(page2, text='  A questo punto puoi registrare la tua presenza in aula attraverso il pulsante "REGISTRA PRESENZA".', background='#C6E4D9',font=('Calibri', 16,))                                           
page2_label13.place(x=50, y=500)

page2_label14 = Label(page2, text='  Premi il pulsante "Q" quando il sistema ti riconosce, così da registrare la tua presenza e poterla',background='#C6E4D9', font=('Calibri', 16,))                                           
page2_label14.place(x=50, y=530)

page2_label15 = Label(page2, text="  visualizzare nella Tabella delle Presenze." ,background='#C6E4D9', font=('Calibri', 16,))                                           
page2_label15.place(x=50, y=560)

page2_button = Button(page2, text='BACK', bg='#D2D2D2', font=('Arial', 13, 'bold'), command=lambda: show_frame(page1))
page2_button.place(x=450, y=600)


####################################################### REGISTRATI(page3) ############################################################
page3.config(bg='#C6E4D9')

message3 = tk.Label(page3, text='Registrazione nuovo utente' ,fg="white",bg="#116062",width=55 ,height=1,font=('times', 30, ' bold '))
message3.place(x=-130, y=0)

datef = tk.Label(frame4, text = day+"-"+mont[month]+"-"+year+"  |  ", fg="#C6E4D9",bg="#C6E4D9", width=55 ,height=1,font=('times', 20, ' bold '))
datef.pack(fill='both',expand=1)

clock = tk.Label(frame3,fg="#C6E4D9",bg="#C6E4D9" ,width=55 ,height=1,font=('times', 22, ' bold '))
clock.pack(fill='both',expand=1)
tick()

lbl = tk.Label(page3, text="Matricola:",width=20  ,height=1 ,fg="black"  ,background='#C6E4D9',font=('Calibri', 22, ' bold ') )
lbl.place(x=40, y=120)

txt = tk.Entry(page3,width=40, fg="black",font=('Calibri', 15, ' bold '))
txt.place(x=350, y=130)

lbl2 = tk.Label(page3, text="Nome e Cognome:",background='#C6E4D9',width=20  ,height=1, fg="black", font=('Calibri', 22, ' bold '))
lbl2.place(x=40, y=220)

txt2 = tk.Entry(page3,width=40 ,fg="black",font=('Calibri', 15, ' bold ') )
txt2.place(x=350, y=230)

message1 = tk.Label(page3, text="Procedi con l'acquisizione delle immagini. Attendi davanti la webcam qualche secondo. " ,bg="#C6E4D9" ,fg="black"  ,width=100 ,height=1, font=('Courier', 12, 'roman'))
message1.place(x=20, y=350)

clearButton = tk.Button(page3, text="Cancella", command=clear  ,fg="black"  ,bg="#ea2a2a"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
clearButton.place(x=820, y=130)
clearButton2 = tk.Button(page3, text="Cancella", command=clear2  ,fg="black"  ,bg="#ea2a2a"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
clearButton2.place(x=820, y=230)   

takeImg = tk.Button(page3, text="1)  Acquisisci Immagini", command=TakeImages  ,fg="white"  ,bg="#116062"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
takeImg.place(x=300, y=400)
trainImg = tk.Button(page3, text="2)  Salva Profilo", command=psw ,fg="white"  ,bg="#116062"  ,width=34  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trainImg.place(x=300, y=450)

message = tk.Label(page3,fg="black", background='#C6E4D9',width=39,height=1, font=('times', 12, ' bold '))
message.place(x=310, y=550)

res=0
exists = os.path.isfile("StudentDetails\StudentDetails.csv")
if exists:
    with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2) - 1
    csvFile1.close()
else:
    res = 0
message.configure(text='Profili attualmente registrati  : '+str(res))

page3_button = Button(page3, text='BACK', bg='#D2D2D2', font=('Arial', 13, 'bold'), command=lambda: show_frame(page1))
page3_button.place(x=450, y=600)

####################################################### LOGIN(page4) #########################################################################
page4.config(bg='#C6E4D9')

message4 = tk.Label(page4, text='Login utente' ,fg="white",bg="#116062",width=60 ,height=1,font=('times', 30, ' bold '))
message4.place(x=-230, y=0)

frame5 = tk.Frame(page4)
frame5.place(relx=0.52, rely=0.075, relwidth=0.12, relheight=0.07)

frame6 = tk.Frame(page4)
frame6.place(relx=0.36, rely=0.075, relwidth=0.18, relheight=0.07)

datef = tk.Label(frame6, text =  day+"-"+mont[month]+"-"+year+"  |  ", fg="white",bg="#116062", width=55 ,height=1,font=('times', 14, ' bold '))
datef.pack(fill='both',expand=1)

clock = tk.Label(frame5,fg="white",bg="#116062" ,width=55 ,height=1,font=('times', 14, ' bold '))
clock.pack(fill='both',expand=1)
tick()

trackImg = tk.Button(page4, text="Registra Presenza", command=TrackImages  ,fg="black"  ,bg="yellow"  ,width=35  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
trackImg.place(x=550,y=250)

lbl3 = tk.Label(page4, text="Presenze registrate:",width=20  ,fg="black"  ,bg='#C6E4D9'  ,height=1 ,font=('times', 15, ' bold '))
lbl3.place(x=150, y=150)

quitWindow = tk.Button(page4, text="Esci", command=window.destroy  ,fg="black"  ,bg="red"  ,width=35 ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
quitWindow.place(x=550, y=350)

page4_button = Button(page4, text='BACK', bg='#D2D2D2', font=('Arial', 13, 'bold'), command=lambda: show_frame(page1))
page4_button.place(x=450, y=600)



########################## MENUBAR(help) ################################

menubar = tk.Menu(window,relief='ridge',)
filemenu = tk.Menu(menubar,tearoff=0, background='#EFEFEF')
filemenu.add_command(label='Modifica Password', command = change_pass)
filemenu.add_command(label='Contatti', command = contact)
filemenu.add_command(label='Esci',command = window.destroy)
menubar.add_cascade(label='Help', font=('times', 29, ' bold '),menu=filemenu)

####################### TABELLA DELLE PRESENZE ##########################

tv= ttk.Treeview(page4,height =13, columns = ('nome','data','ora'))
tv.column('#0',width=82)
tv.column('nome',width=130)
tv.column('data',width=133)
tv.column('ora',width=133)
tv.grid(row=2,column=0,padx=(0,0),pady=(150,0),columnspan=4)
tv.heading('#0',text ='MATRICOLA')
tv.heading('nome',text ='NOME')
tv.heading('data',text ='DATA')
tv.heading('ora',text ='ORA')
tv.place(x=50, y=200)


###################### SCROLLBAR ################################

scroll=ttk.Scrollbar(page4,orient='vertical',command=tv.yview)
scroll.grid(row=2,column=4,padx=(0,100),pady=(300,0),sticky='ns')
tv.configure(yscrollcommand=scroll.set)
scroll.place(x=511, y=201, height=282)





window.configure(menu=menubar)
window.mainloop()