from tkinter import * 
from app import *
from tkinter import ttk


db_nombre = 'baseDatos.xlsx'

class app:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Generador de clases')
        
        #creando contenedor
        frame = LabelFrame(self.wind, text = 'selecciona una materia')
        frame.grid(row= 0, column= 0 , columnspan= 3, pady= 20)
        
        #entrada de materia
        Label(frame, text= 'Pon el codigo de la materia: ').grid(row=1, column=0)
        self.materia = Entry(frame)
        self.materia.focus()
        self.materia.grid(row=1, column=1)
        
        
        
        #boton para materias
        self.boton = Button(frame,text="Enter", command=lambda: buscarMateria(self.materia.get()))
        self.boton.grid(row=1, column=3)
        
        
        #recibe los datos
        
        #tabla de materias
        self.tree = ttk.Label('', text='tonta').grid(column=1, row=4)
        

if __name__ == '__main__':
    window = Tk()
    application = app(window)
    window.mainloop()