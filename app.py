import smtplib
from email.message import EmailMessage
import pandas as pd

def recuperarInfoExcel(hoja:str, busqueda:str, id:str):
    path = 'baseDatos.xlsx'
    exc = pd.read_excel(path,sheet_name=hoja,dtype= str)
    cont= exc[exc[id] == busqueda]
    if not cont.empty:
        return cont
    else:
        return '¡El contenedor no se ha encontrado!\n'
    
def buscarMateria(busqueda:str):    
    hoja = 'materia'
    id = 'codigo'
    result = recuperarInfoExcel(hoja, busqueda, id)
    print(result)
    return result
    
def buscarProfesores(busqueda:str):
    hoja = 'profes'
    id = 'legajo'
    
    return recuperarInfoExcel(hoja, id, busqueda)

def buscarCurso(busqueda:str):
    hoja = 'curso'
    id = 'numero'
    
    return recuperarInfoExcel(hoja,id,busqueda)
    

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

