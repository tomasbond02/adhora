import smtplib
from email.message import EmailMessage
import pandas as pd
from pandastable import Table
from tkinter import * 
from tkinter import ttk

def recuperarInfoExcel(hoja:str, busqueda:str, id:str):
    path = 'baseDatos.xlsx'
    exc = pd.read_excel(path,sheet_name=hoja,dtype= str)
    cont= exc[exc[id] == busqueda]
    if not cont.empty:
        return cont
    else:
        return '¡El contenedor no se ha encontrado!\n'
    
def buscarMateria(self:str):
    busqueda = self.materia.get()
    hoja = 'materia'
    id = 'codigo'
    result = recuperarInfoExcel(hoja, busqueda, id)
    
    #################### tabla ############################
    if busqueda == '':
        materias(self)
    else: 
        self.frame = LabelFrame(self.wind, text = 'materias')
        self.tree = ttk.Treeview(height=10, columns=("codigo", "nombre","horas","semestre","sede","carrera","docente"))
        self.tree.grid(row=2, column= 0, columnspan=2)
        self.tree['column'] = list(result.columns)
        self.tree['show'] = "headings"
        for columna in self.tree['column']:
            self.tree.heading(columna, text = columna)
        db_fila = result.to_numpy().tolist()
        for fila in db_fila:
            self.tree.insert('', 'end', values= fila)
            
def agregarMateria():
    pass


 
def enviarMail(remitente, destinatario, asunto, mensaje, mail_envio, mail_contraseña):
    
    mensaje = EmailMessage()
    
    mensaje['Subject'] = asunto
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
        
    mensaje.set_content(mensaje)

    mail_smtp = "mail.uade.com"
    server = smtplib.SMTP(mail_smtp, '25')#no se si pasarlo por parametro ya que no se si va a cambiar esto
    
    server.ehlo()
    server.starttls()
    
    server.login(mail_envio, mail_contraseña)
    
    server.send_message(mensaje)
    
    server.quit()

#################### armado de la app #####################

   
def materias(self):
    #creando contenedor
    frame = LabelFrame(self.wind, text = 'selecciona una materia')
    frame.grid(row= 0, column= 2 , columnspan= 3, pady= 20)
    
    #entrada 
    Label(frame, text= 'Pon el codigo de la materia: ').grid(row=1, column=0)
    self.materia = Entry(frame)
    self.materia.focus()
    self.materia.grid(row=1, column=1)
    
    #boton
    self.boton = Button(frame,text="Enter", command=lambda: buscarMateria(self))
    self.boton.grid(row=1, column=3)
    
  