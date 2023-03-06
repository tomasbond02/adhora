from tkinter import * 
from app import *

db_nombre = 'baseDatos.xlsx'

class app:

  def __init__(self, window):
    self.wind = window
    self.wind.title('Generador de clases')

    frame = LabelFrame(self.wind, text = 'Elige una opción')
    frame.grid(row= 0, column= 0 , columnspan= 3, pady= 20)
    
    self.botonMaterias = Button(frame,text="Buscar materias", command=lambda: materias(self))
    self.botonMaterias.grid(row=1, column=1)  
  
if __name__ == '__main__':
    window = Tk()
    application = app(window)
    window.mainloop()