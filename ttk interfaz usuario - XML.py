from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()
raiz.title("Club Deportivo CDV - Formulario de inscripción")
raiz.geometry("850x850+500+50")
raiz.configure(bg="#5FD4E2")
raiz.iconbitmap("CDV.ico")

archivo = open ("interfaz.xml","r")
contenido = archivo.read()
xml = BeautifulSoup (contenido)

#Funcion para salir
def salir():
    raiz.destroy()

#Ventana que se abre tras pulsar continuar.
def continuar():

    continuar = tk.Toplevel(raiz) #Creo un a ventana secundaria
    continuar.title("Club Deportivo CDV - Formulario de inscripción")
    continuar.geometry("850x850+500+50")
    continuar.configure(bg="#5FD4E2")
    continuar.iconbitmap("CDV.ico")
    def volver():
        continuar.destroy()
            
    for campo_continuar in xml.find_all("campo_continuar"):
        tipo = campo_continuar.get("tipo")
        texto = campo_continuar.get("texto")
        if tipo == "etiqueta":
            ttk.Label(continuar, text=texto,background="#AC1D4D").pack(padx=20, pady=20)
        elif tipo == "combobox":
            valores = campo_continuar.get("values").split(',')
            ttk.Combobox(continuar, values=valores).pack(padx=20, pady=20)
        elif tipo == "etiqueta":
            ttk.Label(continuar, text=texto,background="#AC1D4D").pack(padx=20, pady=20)
        elif tipo == "check":
            ttk.Checkbutton(continuar, text=texto).pack(padx=20, pady=20)
        elif tipo == "check":
            ttk.Checkbutton(continuar, text=texto).pack(padx=20, pady=20)
        elif tipo == "etiqueta":
            ttk.Label(continuar, text=texto,background="#AC1D4D").pack(padx=20, pady=20)
        elif tipo == "nota":
            tk.Text(continuar,height=10, width=25).pack(padx=20, pady=20)
        elif tipo == "boton_volver":
            ttk.Button(continuar, text=texto, command= volver).pack(padx=20, pady=20)
        elif tipo == "boton2":
            ttk.Button(continuar, text=texto, command= salir).pack(padx=20, pady=20)     
 
for campo in xml.find_all("campo"):
    tipo = campo.get("tipo")
    texto = campo.get("texto")
    if tipo == "entrada":
        ttk.Entry(raiz).pack(padx=20,pady=20)
    elif tipo == "etiqueta":
        ttk.Label(raiz, text=texto,background="#AC1D4D").pack(padx=10,pady=10)
    elif tipo == "boton1":
        ttk.Button(raiz, text=texto, command=continuar).pack(padx=10,pady=10)
    elif tipo == "check":
        ttk.Checkbutton(raiz, text=texto).pack(padx=10,pady=10)
    elif tipo == "nota":
        tk.Text(raiz,height=10, width=25).pack(padx=10,pady=10)

    
    


#Añado un menú
def contacto():
      #creo una nueva ventana con los contactos
      contacto = tk.Toplevel(raiz)
      contacto.title("CDV")
      contacto.configure(bg="#5FD4E2")
      contacto.geometry("850x650+500+50")
      
     #contacto.iconbitmap("CDV.ico")
      marco = tk.Frame(contacto,padx=30,pady=30,background="#F33571")
      
      for campo in xml.find_all("campo_marco"):
          tipo = campo.get("tipo")
          texto = campo.get("texto")
          if tipo == "etiqueta":
              ttk.Label(marco, text=texto).pack(padx=20,pady=20)
          elif tipo == "etiqueta":
              ttk.Label(marco, text=texto,background="#AC1D4D").pack(padx=10,pady=10)
          elif tipo == "etiqueta":
              ttk.Label(marco, text=texto,background="#AC1D4D").pack(padx=10,pady=10)    
          
      marco.pack()
      
      #Inserto y cumplimento tabla
      
      arbol =ttk.Treeview(contacto,columns=('deporte','nombre','email'))
      arbol.heading("#0",text="Id")
      arbol.heading("deporte",text="deporte")
      arbol.heading("nombre",text="Coordinador")
      arbol.heading("email",text="Correo electrónico")

      arbol.insert('','0','elemento1',text="1", values=("Fútbol 11","Juan Alvarez","info@juanalvarez.com"))
      arbol.insert('','1','elemento2',text="2", values=("Balonmano","Demi Cano","info@demicano.com"))
      arbol.insert('','2','elemento3',text="3", values=("Fútbol sala","Juan Alvarez","info@juanalvarez.com"))
      arbol.insert('','3','elemento4',text="4", values=("Voleybol","Alejandra Torres","info@alejandraTorres.com"))
      arbol.insert('','4','elemento5',text="5", values=("Voley playa","Abril León","info@abrilleon.com"))
      arbol.insert('','5','elemento6',text="6", values=("Balonmano playa","Demi Cano","info@demicano.com"))
      arbol.insert('','6','elemento7',text="7", values=("Hockey","Aaron García","info@aarongarcia.com"))


      arbol.pack(padx=10,pady=10)
      
      def cerrar():
                
         contacto.destroy()
         
      for campo in xml.find_all("campo_contacto"):
          tipo = campo.get("tipo")
          texto = campo.get("texto")
          if tipo == "boton3":
              ttk.Button(contacto, text=texto, command=cerrar).pack(padx=20,pady=20)
      #ttk.Button (contacto, text="Cerrar", command=cerrar).pack(padx=10,pady=10)

             

def comentarios():
    #creo una nueva ventana para escribir y enviar el comentario
    comentarios = tk.Toplevel(raiz)
    comentarios.title("CDV")
    comentarios.iconbitmap("CDV.ico")
    comentarios.configure(bg="#5FD4E2")
    comentarios.geometry("550x550+500+50")
    def enviar():
        comentarios.destroy()

    for campo in xml.find_all("campo_comentarios"):
          tipo = campo.get("tipo")
          texto = campo.get("texto")
          if tipo == "etiqueta":
              ttk.Label(comentarios, text=texto, background="#AC1D4D").pack(padx=20,pady=20)
          elif tipo == "nota":
              tk.Text(comentarios, height=20, width=50).pack(padx=10,pady=10)
          elif tipo == "boton4":
              ttk.Button(comentarios, text=texto, command= enviar).pack(padx=10,pady=10)    
     
    
barramenu= tk.Menu(raiz)
raiz.config(menu=barramenu)
ayuda = tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Ayuda",menu=ayuda)

ayuda.add_command(label="Contacto",command=contacto)
ayuda.add_command(label="comentarios",command=comentarios)

#Inicio el bucle de la interfaz
tk.mainloop()
