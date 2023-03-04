import smtplib
from email.message import EmailMessage
import pandas as pd
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
    
def buscarMateria( self:str):
    busqueda = self.materia.get()
    hoja = 'materia'
    id = 'codigo'
    result = recuperarInfoExcel(hoja, busqueda, id)
    self.tree = ttk.Label('', text=result ).grid(column=1, row=4)
    
def buscarProfesores(self:str):
    busqueda = self.profe.get()
    hoja = 'profes'
    id = 'legajo'
    result = recuperarInfoExcel(hoja, id, busqueda)
    self.tree = ttk.Label('', text=result ).grid(column=1, row=4)

def buscarCurso(self:str):
    busqueda = self.curso.get()
    hoja = 'curso'
    id = 'numero'
    result = recuperarInfoExcel(hoja,id,busqueda)
    self.tree = ttk.Label('', text=result ).grid(column=1, row=4)
    
        
        

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

