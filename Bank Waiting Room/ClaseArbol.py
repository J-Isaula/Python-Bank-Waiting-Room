import tkinter as tk
import tkinter.messagebox as msg
import tkinter.font as font
from Nodo import Nodo
# ****************************************************************
#                     CLASE ÁRBOL 
# ****************************************************************
class ArbolSufijos:
    def __init__(self, cadena):
        self.raiz = Nodo(0, None)
        tam = len(cadena)
        index = tam - 1
        while(index >= 0):
            key = cadena[index:tam]
            self.agregar(key, index)
            index = index - 1
    
    def agregar(self, key, n):
        raiz = self.raiz
        while key in raiz.hijos.keys():
            raiz = raiz.hijos.get(key)
        raiz.hijos[key] = Nodo(n, raiz)
        
    def recorrer(self, raiz, cadena):
        for key in raiz.hijos.keys():
            cadena = cadena + key + "\n"
            if raiz.hijos[key] != {}:                
                self.recorrer(raiz.hijos[key], cadena)
        return cadena
    
    def sufijo(self, raiz, sub, cadena):
        for key in raiz.hijos.keys():
            cadena = cadena + key + "\n"
            if raiz.hijos[key] != {}:                
                self.recorrer(raiz.hijos[key], cadena)
        return cadena
# ****************************************************************
#                FUNCIONES A UTILIZAR
# ****************************************************************
def limpiar():
    txtcadena.delete('1.0', tk.END)
    txtSubcadena.delete('1.0', tk.END)
    txtresultado.delete('1.0', tk.END)
    
    
def verSufijos():
    INPUT = limpiarCadena(txtcadena.get("1.0", "end-1c"))
    Arbol = ArbolSufijos(INPUT)
    txtresultado.delete('1.0', tk.END)
    txtresultado.insert(tk.END ,Arbol.recorrer(Arbol.raiz, ""))

def buscar():
    cadena = limpiarCadena(txtcadena.get("1.0", "end-1c"))
    subcadena = limpiarCadena(txtSubcadena.get("1.0", "end-1c"))
    txtresultado.delete('1.0', tk.END)
    index = 0
    tam = len(subcadena)
    aux = ""
    if tam > 0:
        for i in range(len(cadena)):   
            c = cadena[i]
            if c == subcadena[index]:            
                aux = aux + c
                index = index + 1
                if index >= tam:
                    txtresultado.insert(tk.END, aux) 
                    txtresultado.tag_add("hg", "1." + str( i - tam + 1), "1." + str(i + 1))
                    txtresultado.tag_config("hg", foreground='#FF0000')
                    index = 0
                    aux = ""
            else:
                if index > 0 and index < tam:
                    txtresultado.insert(tk.END, aux) 
                txtresultado.insert(tk.END, c) 
                index = 0
                aux = ""
    else:
        msg.showwarning('Advertencia', 'La subcadena no puede ser vacía')
            
def limpiarCadena(texto):
    cadena = ""
    for c in texto:
        if c == '\t' or c == '\n':
            cadena = cadena + " "
        else:
            cadena = cadena + c
    return cadena   
# ****************************************************************
#                         VENTANA 
# ****************************************************************
frm = tk.Tk()
frm.geometry('785x445')

myFont = font.Font(family='Helvetica', size=12)

pRoot = tk.PanedWindow(frm, orient=tk.HORIZONTAL, bg='#41413C')
pRoot.place(x=0,y=0)

#Panel datos
pDatos = tk.PanedWindow(pRoot, orient=tk.VERTICAL, bg='#41413C')
pDatos.grid(row=0, column=1, padx=10, pady=20)

l1 = tk.Label(pDatos, text='Cadena', fg='white', bg='#41413C')
l1['font'] = myFont
l1.grid(row=1, column=1)
txtcadena = tk.Text(pDatos, width=50, height=7)
txtcadena['font'] = myFont
txtcadena.insert(tk.END, "")
txtcadena.grid(row=2, column=1, padx=0)

l2 = tk.Label(pDatos, text='Sub Cadena', fg='white', bg='#41413C')
l2.grid(row=3, column=1)
l2['font'] = myFont
txtSubcadena = tk.Text(pDatos, width=50, height=7)
txtSubcadena['font'] = myFont
txtSubcadena.grid(row=4, column=1)

#Panel botones
pDatosBotones = tk.PanedWindow(pDatos, orient=tk.HORIZONTAL, bg='#41413C')
pDatosBotones.grid(row=7, column=1)

btnLimpiar = tk.Button(pDatosBotones, text="Limpiar", command=limpiar, fg='black', bg='#F9937D', width=24)
btnLimpiar.grid(row=8, column=1, pady=10)
btnLimpiar['font'] = myFont

btnBuscar = tk.Button(pDatosBotones, text="Buscar", command=buscar, fg='black', bg='#F9F77D', width=25)
btnBuscar.grid(row=8, column=2, pady=10)
btnBuscar['font'] = myFont

btnVer = tk.Button(pDatos, text="Ver lista de Sufijos", command=verSufijos, fg='black', bg='#5BD574', width=50)
btnVer.grid(row=9, column=1)
btnVer['font'] = myFont

#Panel resultado
pResultado = tk.PanedWindow(pRoot, orient=tk.VERTICAL, bg='#41413C')
pResultado.grid(row=0, column=2, padx=10, pady=20)

txtresultado = tk.Text(pResultado, width=30, height=22)
txtresultado['font'] = myFont
txtresultado.grid(row=2, column=0, padx=0)

frm.mainloop()          