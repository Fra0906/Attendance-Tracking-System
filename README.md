# Attendance-Tracking-System
System that keeps track of the presence of students in a class. <br>

## Prerequisiti 
Prima di far partire il sistema, è necessario aver installato alcune librerie e moduli: <br>
• **Python** scaricabile al seguente link: https://www.python.org/downloads/ <br>
• **Anacona** (opzionale) scaricabile al seguente link: https://www.anaconda.com/products/distribution <br>
• Installazione di **OpenCV**: *pip install opencv-python* <br>
• Scaricare il **classificatore pre-addestrato** dal repository OpenCV: https://github.com/opencv/opencv e inserirlo all’interno della directory del progetto. Per implementare l’algoritmo del Sistema di Rilevamento delle Presenze è stata sfruttata la potenzialità della libreria OpenCV che implementa già uno degli algoritmi di classificazione più usati in questo contesto. Questo algoritmo permette sfruttare un classificatore pre ddestrato: **haarcascade_frontalface_default**.<br>
• Installazione dei seguenti **moduli**: 
- *pip install tk-tools*
- *pip install datetime*
- *pip install pytest-shutil*
- *pip install python-csv*
- *pip install numpy*
- *pip install pillow*
- *pip install pandas*
- *pip install times*

 <p> Al fine di un corretto uso dell’applicazione è necessario essere in possesso di una semplice webcam, esterna o interna al pc.
  
  ## Istruzioni per l'avvio
  
- Apri il prompt dei comandi o Anaconda prompt
- *Cd C:\Users\Utente\Desktop\... \SistemaDiRilevamentoDellePresenze*
- *Pip install requirements.txt* (sono gli stessi menzionati nei prerequisiti)
- *Main.py*
 
## Come funziona il sistema
 
Appena avviato il sistema, si apre la pagina principale, un menù dove è possibile scegliere l’operazione da compiere, consultabile in ogni momento. <br>
<img src="images/1.PNG"> <br>

Nel menù ci sono tre pulsanti: <br>

### 1) “COME FUNZIONA?”

Cliccando questo pulsante si apre una finestra che spiega all’utente le funzionalità del sistema e in che modo procedere in base alle proprie esigenze. <br>

<img src="images/2.PNG"> <br>

### 2) “REGISTRATI”
Cliccando questo pulsante si accede alla pagina di registrazione nuovo utente.
<img src="images/3.PNG"> <br>

La registrazione dell’utente deve essere fatta solo una volta, la prima volta che si accede al sistema. Per effettuare la registrazione è necessario essere a conoscenza della password per salvare un nuovo profilo utente. Se la password inserita non è corretta, viene mostrato un messaggio di errore. <br>
L’idea di inserire una password per questa funzionalità nasce pensando al contesto di applicazione nel sistema, quindi una scuola o una università prevalentemente. Da qui nasce la necessità di ridurre il rischio di compromissione del sistema attraverso l’inserimento di una password.<br>
L’utente che si sta registrando, deve inserire il proprio numero di Matricola ed il proprio Nome e Cognome. Questi dati nel momento del salvataggio, verranno salvati un file csv chiamato **StudentDetails.csv** all’interno della cartella StudentDetails. Se l’utente per errore non inserisce i propri dati, comparirà il seguente messaggio <br>
<img src="images/6.PNG"> <br>
A questo punto si deve passare all’acquisizione delle immagini del proprio volto, quindi l’utente deve premere il pulsante **“1) Acquisisci immagini”** e deve attendere l’apertura della schermata di acquisizione. Una volta aperta attendere qualche secondo davanti alla webcam mostrando il volto. Il sistema acquisirà 100 immagini del viso in qualche secondo. <br>
<p>In base alle prestazioni del computer dal quale si avvia il programma potrebbe mettercivqualche secondo in più. Attendere sempre davanti la webcam. Al termine la schermata divchiuderà automaticamente.vDa notare che se il sistema non riesce a rilevare bene il volto per vari motivi, potrebbe rallentare fino a chiudersi. Le immagini appena acquisite verranno salvate nella cartella *TrainingImage*. <br>
<p>Ora l’utente deve completare la registrazione cliccando sul pulsante **“2) Salva Profilo”**. A questo punto della registrazione è necessario inserire la password per terminare l’operazione di registrazione. Sulla password inserita vengono effettuati tutti i controlli necessari. Se la password non è corretta viene mostrato un messaggio di errore. <br>
<p>I dettagli dello studente che si è appena registrato, verranno automaticamente inseriti anche all’interno di un file csv chiamato **StudentDetails.csv** presente nella cartella *StudentDetail* del repository. <br>
Una volta salvato il profilo avviene il training delle immagini salvate nel dataset. Il modello risultante chiamato *Trainner.yml* verrà salvato nella cartella *TrainingImageLabel*. <br>

### LOGIN
