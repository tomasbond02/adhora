import smtplib
from email.message import EmailMessage


def recuperarInfoExcel():
    pass



def enviarMail():
    
    remitente = "tbond@uade.edu.ar"
    destinatario = "tbond@uade.edu.ar"
    asunto = "Mail html enviado desde python"
    mensaje = EmailMessage()
    
    mensaje['Subject'] = asunto
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
        
    mensaje.set_content("hola estoy mandando esto desde python!")


    mail_smtp = "mail.uade.com"
    server = smtplib.SMTP(mail_smtp, '25')
    
    server.ehlo()
    server.starttls()
    
    mail_envio = "tbond@uade.edu.ar"
    mail_contraseña = "tomasbond07"
    
    server.login(mail_envio, mail_contraseña)
    
    server.send_message(mensaje)
    
    server.quit()
    
    
