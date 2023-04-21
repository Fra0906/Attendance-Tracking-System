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
