#-----@Wilson11-----#

from tkinter import Button, Entry, Frame, Label, PhotoImage, StringVar, Tk, Toplevel, messagebox, ttk, HORIZONTAL,END
from matplotlib.pyplot import grid
import time

from connection_login import Registro_Usuarios

    
class Interfaz(Frame):

    
    def __init__(self, master, *args):
        super().__init__(master,*args)
        self.usuario = 'Nombre de Usuario'
        self.contrasenia = 'Ingrese su Contraseña'
        self.fila1 = ''
        self.fila2 = ''
        self.entry1_usuario=StringVar()
        self.entry2_contrasenia=StringVar()

        self.base_datos=Registro_Usuarios()
        self.widgets()

    def entry_out(self, event, event_text):

        if event['fg'] == 'black' and len(event.get()) == 0:
            event.delete(0, END)
            event['fg']='grey'
            event.insert(0,event_text)

        if self.entry2_contrasenia.get() != 'Ingrese su Contraseña':
            self.entry2_contrasenia['show'] = ''

        if self.entry2_contrasenia.get() != 'Nombre de Usuario':
            self.entry2_contrasenia['show'] = '*'

    def entry_in(self, event):

        if event['fg'] == 'grey':
            event['fg'] = 'black'
            event.delete(0, END)
        
        if self.entry2_contrasenia.get() != 'Ingrese su Contraseña':
            self.entry2_contrasenia['show'] = '*'
        
        if self.entry2_contrasenia.get() == 'Ingrese su Contraseña':
            self.entry2_contrasenia['show'] = ''

    def agregar_usuario(self):

        r_usuario=self.entry1_usuario.get()
        r_password=self.entry2_contrasenia.get()
        if r_usuario != self.usuario and r_password != self.contrasenia:
            self.base_datos.registra_usuario(r_usuario,r_password)
            messagebox.showinfo('!Atencion!','Usuario Registrado correctamente')
          
        else:
            messagebox.showinfo('!Atencion!','No a Ingresado Informacion')

        self.limpiar_campos()

    def accerder_ventana_dos(self):

        for i in range(101):
            self.barra['value'] += 1
            self.master.update()
            time.sleep(0.01)
        
        self.master.withdraw()
        self.ventana_dos=Toplevel()
        self.ventana_dos.geometry('500x500')
        self.ventana_dos.title('Servicios del Sistema')
        self.ventana_dos.protocol('WM_DELETEWINDOW',self.salir)
        self.ventana_dos.config(bg='#1d2127')
        self.ventana_dos.state('zoomed')

        Label(self.ventana_dos, text='Sistema en Desarrollo', font=('Arial',12,'bold'),bg='white').pack(expand=True)
        Button(self.ventana_dos, text='Salir',font='Arial 10', bg='red',command=self.salir).pack(expand=True)

    def verificar_usuario(self):
        self.mensaje1['text'] = ''
        self.mensaje2['text'] = ''
        usurario_entry=self.entry1_usuario.get()
        password_entry=self.entry2_contrasenia.get()

        if usurario_entry != self.usuario or self.contrasenia != password_entry:
            usurario_entry = str("'"+usurario_entry+"'")
            password_entry = str("'"+password_entry+"'")

            dato1=self.base_datos.buscar_usuario(usurario_entry)
            dato2=self.base_datos.buscar_password(password_entry)

            self.fila1 = dato1
            self.fila2 = dato2

            if self.fila1 == self.fila2:
                if dato1 == [] and dato2 ==[]:
                    self.mensaje2['text'] = 'Contrasenia incorrecta'
                    self.mensaje1['text'] = 'Usuario incorrecto'
                else:
                    if dato1 == []:
                        self.mensaje1['text'] = 'Usuario Incorrecto'
                    else:
                        dato1 = dato1[0][1]
                    if dato2 ==[]:
                        self.mensaje2['text'] = 'Contasenia Incorrecta'
                    else:
                        dato2=dato2[0][2]
                    if dato1 != [] and dato2 != []:
                        self.accerder_ventana_dos()
        else:
            self.mensaje1['text'] = 'Usuario Incorrecto'
            self.mensaje2['text'] = 'Contrasenia Incorrecta'   
        
        self.limpiar_campos()
   

    def salir(self):
        self.master.destroy()
        self.master.quit()
        

    def widgets(self):

        self.login = PhotoImage(file=r'./img/login.png')

        #-----Ingreso de Usuario-----#

        Label(self.master, image=self.login, bg='#1d2127').grid(column=0,row=0,padx=125,pady=10)
        Label(self.master, text='Usuario',bg='#1d2127',fg='white', font=('Overpass Mono',12,'bold')).grid(column=0,row=1,padx=150,pady=10)
        self.entry1_usuario=Entry(self.master,font=('Overpass Mono',12),justify='center',fg='grey',highlightbackground='#E65561',
        highlightcolor='green2')
        self.entry1_usuario.insert(0, self.usuario)
        self.entry1_usuario.bind('<FocusIn>',lambda args:self.entry_in(self.entry1_usuario))
        self.entry1_usuario.bind('<FocusOut>',lambda args:self.entry_out(self.entry1_usuario,self.usuario))
        self.entry1_usuario.grid(column=0,row=2,padx=100,pady=10)

        self.mensaje1 = Label(self.master, bg='#1d2127',fg='white',font=('Overpass Mono',12))
        self.mensaje1.grid(column=0,row=3)

        #-----Ingreso de Contrasenia-----#

        Label(self.master, text='Contraseña',bg='#1d2127',fg='white', font=('Overpass Mono',12,'bold')).grid(column=0,row=4,padx=150,pady=10)
        self.entry2_contrasenia=Entry(self.master,font=('Overpass Mono',12),justify='center',fg='grey',highlightbackground='#E65561',
        highlightcolor='green2')
        self.entry2_contrasenia.insert(0,self.contrasenia)
        self.entry2_contrasenia.bind('<FocusIn>',lambda args: self.entry_in(self.entry2_contrasenia))
        self.entry2_contrasenia.bind('<FocusOut>',lambda args:self.entry_out(self.entry2_contrasenia, self.contrasenia))
        self.entry2_contrasenia.grid(column=0,row=5,padx=100,pady=10)

        self.mensaje2 = Label(self.master, bg='#1d2127',fg='white',font=('Overpass Mono',12))
        self.mensaje2.grid(column=0,row=6)

        Button(self.master, text='Registrar',activebackground='magenta',bg='#D64E40',font=('Overpass Mono',12),command=self.agregar_usuario).place(x=100,y=415)
        Button(self.master, text='Iniciar Secion',activebackground='magenta',bg='#D64E40',font=('Overpass Mono',12),command=self.verificar_usuario).place(x=200,y=415)

        estilo =  ttk.Style()
        estilo.theme_use('clam')
        estilo.configure('TProgressbar',foreground='red',background='black',troughcolore='DarkOrechid1',
        bordercolor='#970BD9',lightcolor='#970BD9', darkcolor='black')
        self.barra = ttk.Progressbar(self.master, orient=HORIZONTAL, length=208, mode='determinate', maximum=100, style='TProgressbar')
        self.barra.place(x=100,y=470)
       
if __name__ == '__main__':
    ventana = Tk()
    ventana.title('Gestion de Pedidos')
    ventana.config(bg='#1d2127')
    ventana.geometry('400x500')
    ventana.resizable(0,0)
    app=Interfaz(ventana)
    app.mainloop()





