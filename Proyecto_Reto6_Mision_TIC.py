from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext as st

class Aplicacion:
    def __init__(self):
        self.ventana=Tk()
        self.ventana.geometry('780x325')
        self.ventana.title('Base de datos de la empresa')
        self.marco=Frame(self.ventana)
        self.marco.config(bg='#1C992A', width=900, height=700)
        self.marco.place(x=0,y=0)
        self.datos=[]
        self.nombre=StringVar()
        self.apellido=StringVar()
        self.nacimiento=StringVar()
        self.ingreso=StringVar()
        self.egreso=StringVar()
        self.genero=StringVar()
        self.salario=StringVar()
        self.labelframe()
        self.labels()
        self.textbox()
        self.combobox()
        self.boton()
        self.scrolledtext()
        self.sacarArchivos()
        self.ventana.mainloop()

    def labels(self):

        self.label1 = Label(self.lfe, text='Base de datos')
        self.label1.config(bg='#1C992A', fg='white', font=('Calibri',10,'bold'))
        self.label1.grid(column=0,row=0, padx=0, pady=5)
        self.label2 = Label(self.lfe, text='Nombre:')
        self.label2.config(bg='#1C992A', fg='white', font=('Calibri',10,'bold'))
        self.label2.grid(column=0,row=1, padx=0, pady=5)
        self.label3 = Label(self.lfe, text='Apellido:')
        self.label3.config(bg='#1C992A', fg='white', font=('Calibri',10,'bold'))
        self.label3.grid(column=0,row=2, padx=0, pady=5)
        self.label4 = Label(self.lfe, text='Sexo:')
        self.label4.config(bg='#1C992A', fg='white', font=('Calibri',10,'bold'))
        self.label4.grid(column=0,row=3, padx=0, pady=5)
        self.label5 = Label(self.lfe, text='Fecha de Nacimiento:')
        self.label5.config(bg='#1C992A', fg='white', font=('Calibri',10,'bold'))
        self.label5.grid(column=0,row=4, padx=0, pady=5)
        self.label6 = Label(self.lfe, text='Fecha de Ingreso:')
        self.label6.config(bg='#1C992A', fg='white', font=('Calibri',10,'bold'))
        self.label6.grid(column=0,row=5, padx=0, pady=5)
        self.label7 = Label(self.lfe, text='Fecha de Egreso:')
        self.label7.config(bg='#1C992A', fg='white', font=('Calibri',10,'bold'))
        self.label7.grid(column=0,row=6, padx=0, pady=5)
        self.label8 = Label(self.lfe, text='Salario:')
        self.label8.config(bg='#1C992A', fg='white', font=('Calibri',10,'bold'))
        self.label8.grid(column=0,row=7, padx=0, pady=5)
    
    def textbox(self):
        self.txt1=Entry(self.lfe, textvariable=self.nombre)
        self.txt1.config(justify='left',font=('Calibri',10,'bold'))
        self.txt1.grid(column=1,row=1, padx=0, pady=0)
        self.txt1.bind("<Key>", self.letricas)
        self.txt1.bind("<BackSpace>", lambda _:self.txt1.delete(END))
        self.txt1.focus()

        self.txt2=Entry(self.lfe, textvariable=self.apellido)
        self.txt2.config(justify='left',font=('Calibri',10,'bold'))
        self.txt2.grid(column=1,row=2, padx=0, pady=0)
        self.txt2.bind("<Key>", self.letricas)
        self.txt2.bind("<BackSpace>", lambda _:self.txt2.delete(END))

        self.txt3 = Entry(self.lfe, textvariable=self.nacimiento)
        self.txt3.config(font=('Calibri',10,'bold'))
        self.txt3.grid(column=1, row=4)
        self.txt3.bind("<Key>",self.mientrasEscribe)
        self.txt3.bind("<BackSpace>",lambda _:self.txt3.delete(END))

        self.txt4 = Entry(self.lfe, textvariable=self.ingreso)
        self.txt4.config(font=('Calibri',10,'bold'))
        self.txt4.grid(column=1, row=5)
        self.txt4.bind("<Key>", self.mientrasEscribe)
        self.txt4.bind("<BackSpace>", lambda _:self.txt4.delete(END))

        self.txt5 = Entry(self.lfe, textvariable=self.egreso)
        self.txt5.config(font=('Calibri',10,'bold'))
        self.txt5.grid(column=1, row=6)
        self.txt5.bind("<Key>", self.mientrasEscribe)
        self.txt5.bind("<BackSpace>", lambda _:self.txt5.delete(END))

        self.txt6 = Entry(self.lfe, textvariable=self.salario)
        self.txt6.config(justify='right',font=('Calibri',10,'bold'))
        self.txt6.grid(column=1, row=7)
        self.txt6.bind("<Key>", self.numeritos)
        self.txt6.bind("<BackSpace>", lambda _:self.txt6.delete(END))

    def combobox(self):
        self.cbx = ttk.Combobox(self.lfe, state='readonly', textvariable=self.genero)
        self.cbx['values']=('No binario','Masculino', 'Femenino')
        self.cbx.config(width=9, height=7,font=('Calibri',10,'bold'))
        self.cbx.current(0)
        self.cbx.grid(column=1,row=3, padx=0, pady=0)

    def boton(self):
        self.boton1=ttk.Button(self.lfe, text='Registrar al empleado',command=self.mensaje)
        self.boton1.config(width=25)
        self.boton1.grid(column=0,row=8, padx=0, pady=0)


        self.boton2=ttk.Button(self.lfe, text='Calcula las prestaciones',command=self.calculoSalario)
        self.boton2.config(width=25)
        self.boton2.grid(column=1,row=8, padx=0, pady=0)

    def scrolledtext(self):
        self.scroltext=st.ScrolledText(self.lfe1, width=50, height=17)
        self.scroltext.grid(column=1,row=1, padx=10, pady=10)

    def labelframe(self):
        self.lfe=LabelFrame(self.ventana,bg="#1C992A",text="Ingresa los datos solicitados del empleado",font=('Calibri',10,'bold'),fg="white",height=800,width=400)
        self.lfe.grid(column=0,row=0, padx=0, pady=0)
        self.lfe1=LabelFrame(self.ventana,bg="#1C992A",text="Vista de la base de datos",font=('Calibri',10,'bold'),fg="white",height=800,width=400)
        self.lfe1.grid(column=1,row=0, padx=5, pady=0)

    def calculoSalario(self):
        cont=0
        try:
            self.numsalario = int(self.salario.get())
            self.numegreso=str(self.egreso.get())
            self.numingreso=str(self.ingreso.get())
            self.numegresoano=[]
            self.numingresoano=[]
            while cont <= 9:
                if cont >= 6:
                    try:
                        self.numegresoano.append(list(self.numegreso)[cont])
                        self.numingresoano.append(list(self.numingreso)[cont])
                        cont+=1
                    except IndexError: 
                        break
                else:
                    cont+=1
            self.estadia = int(''.join(self.numegresoano)) - int(''.join(self.numingresoano))
            self.cesantias = ((self.numsalario*self.estadia)/12)
            messagebox.showinfo('Prestaciones', f'Las prestaciones son:  $ {int(self.cesantias)}')
        except:
            messagebox.showerror('Error del sistema', 'Hay espacios en blanco')

    def mensaje(self):   
        if self.nombre.get() != '' and self.apellido.get() != '' and self.genero.get() != '' and self.nacimiento.get() != '' and self.ingreso.get() != '' and self.egreso.get() and self.salario.get() != '':
            self.overwrite=0
            self.datos.clear()
            self.datos.extend([self.nombre.get(),self.apellido.get(),self.genero.get(),self.nacimiento.get(),self.ingreso.get(),self.egreso.get(),self.salario.get(),'\n'])
            with open('ListaEmpleados.txt','rt', encoding='utf-8') as self.data:
                self.ardatos=self.data.readlines()
                self.data.seek(0)
                for i in self.ardatos:
                    self.divdatos=(i).split(',')
                    self.num=int(len(self.ardatos))
                    if self.divdatos[0]==self.datos[0] and self.divdatos[1]==self.datos[1]:
                        message=messagebox.askyesnocancel('Hay una incongruencia', 'Este empleado esta repetido en la base de datos, deseas, modificarlo(Si), añadirlo(No) o no hacer nada(Cancel)')
                        if message == True:
                            for j in range(self.num):
                                self.divdatos=(self.ardatos[j]).split(',')
                                if self.divdatos[0]==self.datos[0] and self.divdatos[1]==self.datos[1]:
                                    message1=messagebox.askyesno('Modificaciones', f'El siguente empleado esta repetido, \nNombre:  {self.divdatos[0]}\nApellido:  {self.divdatos[1]}\nGenero:  {self.divdatos[2]}\nFecha Nacimiento:  {self.divdatos[3]}\nFecha de Ingreso:  {self.divdatos[4]}\nFecha de Egreso:  {self.divdatos[5]}\nSalario:  {self.divdatos[6]}\nlo deseas modificar?')
                                    if message1 == True:
                                        self.moddatos = f'{self.nombre.get()},{self.apellido.get()},{self.genero.get()},{self.nacimiento.get()},{self.ingreso.get()},{self.egreso.get()},{self.salario.get()},\n'
                                        self.index=self.ardatos.index(self.ardatos[j])
                                        self.ardatos.remove(self.ardatos[j])
                                        self.ardatos.insert(self.index,self.moddatos)
                                        continue
                                    if message1 == False:
                                        continue
                            with open('ListaEmpleados.txt','wt', encoding='utf-8') as self.data:
                                for i in self.ardatos:
                                    self.data.write(i)
                        elif message == False:
                            self.baseDeDatos()
                        else:
                            messagebox.showinfo('Aviso', 'No hiciste nada')
                        self.overwrite +=1
                        break

            if self.overwrite == 0:
                self.baseDeDatos()
        
        else:
            messagebox.showerror('Error del sistema', 'Hay espacios en blanco')
        
        self.sacarArchivos()
    
    def baseDeDatos(self):
        with open ('ListaEmpleados.txt','at', encoding='utf-8') as self.data:
            for i in range(int(len(self.datos))-1):
                self.data.write(self.datos[i])
                self.data.write(',')
            self.data.write('\n')
        messagebox.showinfo('Base de Datos', f'Nombre:  {self.nombre.get()}\nApellido:  {self.apellido.get()}\nGenero:  {self.genero.get()}\nFecha Nacimiento:  {self.nacimiento.get()}\nFecha de Ingreso:  {self.ingreso.get()}\nFecha de Egreso:  {self.egreso.get()}\nSalario:  {self.salario.get()}')

    def mientrasEscribe(self, fecha):
        if fecha.char.isdigit():
            texto1 = self.txt3.get()
            texto2 = self.txt4.get()
            texto3 = self.txt5.get()
            letras1 = 0
            letras2 = 0
            letras3 = 0
            for i in texto1:
                letras1 +=1
            if letras1 == 2:
                self.txt3.insert(2,"/")
            elif letras1 == 5:
                self.txt3.insert(5,"/")

            for j in texto2:
                letras2 +=1
            if letras2 == 2:
                self.txt4.insert(2,"/")
            elif letras2 == 5:
                self.txt4.insert(5,"/")

            for k in texto3:
                letras3 +=1
            if letras3 == 2:
                self.txt5.insert(2,"/")
            elif letras3 == 5:
                self.txt5.insert(5,"/")
        else:
            return "break"
            
    def numeritos(self,numero):
        if numero.char.isdigit():
            texto4 = self.txt6.get()
            letras4 = 0
        else:
            return "break"

    def letricas(self,letras):
        if letras.char.isalpha():
            pass
        else:
            return "break"

    def sacarArchivos(self):
        try:
            with open('ListaEmpleados.txt','rt', encoding='utf-8') as self.data:
                self.l = self.data.readlines()
                self.scroltext.config(state='normal')
                self.scroltext.delete("1.0",END)
                for i in range(len(self.l)):
                    self.scroltext.insert(END,'Nombre: '+(self.l[i].split(','))[0] +'\n')
                    self.scroltext.insert(END,'Apellido: '+(self.l[i].split(','))[1] +'\n') 
                    self.scroltext.insert(END,'Genero: '+(self.l[i].split(','))[2] +'\n') 
                    self.scroltext.insert(END,'Fecha de nacimiento: '+(self.l[i].split(','))[3] +'\n') 
                    self.scroltext.insert(END,'Fecha de ingreso: '+(self.l[i].split(','))[4] +'\n') 
                    self.scroltext.insert(END,'Fecha de egreso: '+(self.l[i].split(','))[5] +'\n') 
                    self.scroltext.insert(END,'Saldo: '+(self.l[i].split(','))[6] +'\n')
                    self.scroltext.insert(END,'\n')
                self.scroltext.config(state='disabled')
                self.data.seek(0)
        except:
            with open ('ListaEmpleados.txt','xt', encoding='utf-8') as self.data:
                pass
        



if __name__ == '__main__':
    App = Aplicacion()