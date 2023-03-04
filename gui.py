from tkinter import * 
from app import *

db_nombre = 'baseDatos.xlsx'

class app:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Generador de clases')
        ######################## Materias ##########################################
        #creando contenedor
        frame = LabelFrame(self.wind, text = 'selecciona una materia')
        frame.grid(row= 0, column= 0 , columnspan= 3, pady= 20)
        
        #entrada de materia
        Label(frame, text= 'Pon el codigo de la materia: ').grid(row=1, column=0)
        self.materia = Entry(frame)
        self.materia.focus()
        self.materia.grid(row=1, column=1)
        
        #boton para materias
        self.boton = Button(frame,text="Enter", command=lambda: buscarMateria(self))
        self.boton.grid(row=1, column=3)
        
        
        ############################# Profesores #############################
        #creando contenedor
        frame = LabelFrame(self.wind, text = 'selecciona un Profesor')
        frame.grid(row= 0, column= 4, columnspan= 3, pady= 20)
        
        #entrada de legajo profes
        Label(frame, text= 'Pon el legajo del profesor: ').grid(row=1, column=0)
        self.profe = Entry(frame)
        self.profe.grid(row=1, column=1)
        
        #boton para materias
        self.boton = Button(frame,text="Enter", command=lambda: buscarProfesores(self))
        self.boton.grid(row=1, column=3)
        
        
        ################################ Cursos ############################
        
          #creando contenedor
        frame = LabelFrame(self.wind, text = 'selecciona Un curso')
        frame.grid(row= 0, column= 8 , columnspan= 3, pady= 20)
        
        #entrada de curso
        Label(frame, text= 'Pon el codigo del curso: ').grid(row=1, column=0)
        self.cur = Entry(frame)
        self.cur.grid(row=1, column=1)
        
        #boton para curso
        self.boton = Button(frame,text="Enter", command=lambda: buscarCurso(self))
        self.boton.grid(row=1, column=3)
    

if __name__ == '__main__':
    window = Tk()
    application = app(window)
    window.mainloop()