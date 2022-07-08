from tkinter import *
from Hotel import *
from tkinter import messagebox as mb
from basededatos import *
class Interfaz(Frame):
    def __init__(self,master):
        super().__init__(master,width=700,height=700)
        self.master=master
        self.pack(fill=BOTH,expand=True)


        frameprincipal = Frame(self)
        frameprincipal.place(x=0,y=0,width=700,height=700)

        frameopcionesprincipales=Frame(frameprincipal,bg="#e3e7b3")
        frameopcionesprincipales.place(x=0,y=0,width=200,height=700)
        botonRegistrar =Button(frameopcionesprincipales,bg="#d77948",relief=RAISED,bd=6,activebackground="#e3e7b3",font=("cambria",11),text="REGISTRAR CLIENTE",command=lambda:IrARegistrar())
        botonRegistrar.place(x=20,y =175,width=160,height=40)
        botonVerRegistro=Button(frameopcionesprincipales,bg="#d77948",relief=RAISED,bd=6,activebackground="#e3e7b3",font=("cambria",11),text="REGISTRO",command=lambda:IrARegistro())
        botonVerRegistro.place(x=20,y=370,width=160,height=40)

        frameinicio=Frame(frameprincipal,bg="#e4ce8e")
        frameinicio.place(x=200,y=0,width=500,height=700)
        self.fondoimagen = PhotoImage(file="PORTADA.gif")
        lblfondo=Label(frameinicio,image=self.fondoimagen,bg="#e4ce8e")
        lblfondo.place(x=0,y=0,width=500,height=700)
        

        def IrARegistrar():
            frameregistrar=Frame(frameprincipal,bg="#e4ce8e")
            frameregistrar.place(x=200,y=0,width=500,height=700)
            
            self.imagentitulo1 =PhotoImage(file="REGISTRO DE CLIENTE.GIF")
            etiquetaRegistrarCliente=Label(frameregistrar,image=self.imagentitulo1 ,bg="#e4ce8e")
            etiquetaRegistrarCliente.place(x=20,y=20,width=460,height=40)

            lblHoraEntrada = Label(frameregistrar,bg="#f6ffe2",text="HORA DE ENTRADA",font=("cambria",11),relief=RIDGE,bd=5)
            lblHoraEntrada.place(x=40,y=100,width=200,height=40)
            entryHoraEntrada =Entry(frameregistrar,bg="#f6ffe2")
            entryHoraEntrada.place(x=260,y=100,width=200,height=40)

            lblFechaEntrada = Label(frameregistrar,bg="#f6ffe2",text="FECHA DE ENTRADA",font=("cambria",11),relief=RIDGE,bd=5)
            lblFechaEntrada.place(x=40,y=160,width=200,height=40)
            entryFechaEntrada=Entry(frameregistrar,bg="#f6ffe2")
            entryFechaEntrada.place(x=260,y=160,width=200,height=40)

            lblMarcaVehiculo = Label(frameregistrar,bg="#f6ffe2",text="MARCA DE VEHICULO",font=("cambria",11),relief=RIDGE,bd=5)
            lblMarcaVehiculo.place(x=40,y=220,width=200,height=40)
            entryMarcaVehiculo =Entry(frameregistrar,bg="#f6ffe2")
            entryMarcaVehiculo.place(x=260,y=220,width=200,height=40)

            lblPatente =Label(frameregistrar,bg="#f6ffe2",text="PATENTE",font=("cambria",11),relief=RIDGE,bd=5)
            lblPatente.place(x=40,y=280,width=200,height=40)
            entryPatente =Entry(frameregistrar,bg="#f6ffe2")
            entryPatente.place(x=260,y=280,width=200,height=40)

            lblHabitacion =Label(frameregistrar,bg="#f6ffe2",text="HABITACION",font=("cambria",11),relief=RIDGE,bd=5)
            lblHabitacion.place(x=40,y=340,width=200,height=40)
            entryHabitacion=Entry(frameregistrar,bg="#f6ffe2")
            entryHabitacion.place(x=260,y=340,width=200,height=40)

            lblCantidadHoras =Label(frameregistrar,bg="#f6ffe2",text="CANTIDAD DE HORAS",font=("cambria",11),relief=RIDGE,bd=5)
            lblCantidadHoras.place(x=40,y=400,width=200,height=40)
            entryCantidadHoras =Entry(frameregistrar,bg="#f6ffe2")
            entryCantidadHoras.place(x=260,y=400,width=200,height=40)

            lblImporte =Label(frameregistrar,bg="#f6ffe2",text="IMPORTE",font=("cambria",11),relief=RIDGE,bd=5)
            lblImporte.place(x=40,y=460,width=200,height=40)
            entryImporte=Entry(frameregistrar,bg="#f6ffe2")
            entryImporte.place(x=260,y=460,width=200,height=40)

            botonRegistrarCliente =Button(frameregistrar,font=("cambria",11),text="REGISTRAR CLIENTE",bg="#d77948",relief=RAISED,bd=6,activebackground="#e4ce8e",command=lambda:AgregarNuevoCliente())
            botonRegistrarCliente.place(x=40,y=540,width=200,height=60)
            botonNuevoCliente=Button(frameregistrar,text="NUEVO CLIENTE",bg="#d77948",font=("cambria",11),relief=RAISED,bd=6,activebackground="#e4ce8e",command=lambda:NuevoCliente())
            botonNuevoCliente.place(x=260,y=540,width=200,height=60)

            def AgregarNuevoCliente():
                miHotel = Hotel()
                nuevaHora=entryHoraEntrada.get()
                nuevaFecha=entryFechaEntrada.get()
                nuevaMarca=entryMarcaVehiculo.get()
                nuevamarcaM = nuevaMarca.upper()
                nuevaPatente=entryPatente.get()
                nuevapatenteM=nuevaPatente.upper()
                nuevaHabitacion=entryHabitacion.get()
                nuevaCantidadHoras=entryCantidadHoras.get()
                nuevoImporte=entryImporte.get()
                miHotel.registrar(nuevaHora,nuevaFecha,nuevamarcaM,nuevapatenteM,nuevaHabitacion,nuevaCantidadHoras,nuevoImporte)
                mb.showinfo('REGISTRO COMPLETO', 'EL CLIENTE SE REGISTRO CORRECTAMENTE')

            def NuevoCliente():
                entryHoraEntrada.delete(0,"end")
                entryFechaEntrada.delete(0,"end")
                entryMarcaVehiculo.delete(0,"end")
                entryPatente.delete(0,"end")
                entryHabitacion.delete(0,"end")
                entryCantidadHoras.delete(0,"end")
                entryImporte.delete(0,"end")
        def IrARegistro():
            frameregistro =Frame(frameprincipal,bg="#e4ce8e")
            frameregistro.place(x=200,y=0,width=500,height=700)
            
            self.imagentitulo2 =PhotoImage(file="REGISTRO.gif")
            etiquetamostrarRegistro =Label(frameregistro,image=self.imagentitulo2,bg="#e4ce8e")
            etiquetamostrarRegistro.place(x=20,y=20,width=460,height=40)

            botonMostrarRegistroCompleto =Button(frameregistro,text="MOSTRAR REGISTRO COMPLETO",bg="#d77948",font=("cambria",11),relief=RAISED,bd=6,activebackground="#e4ce8e",command=lambda:botonregistro())
            botonMostrarRegistroCompleto.place(x=40,y=100,width=420,height=60)

            lblMostrarRegistroFecha =Label(frameregistro,text="MOSTRAR REGISTRO POR FECHA",anchor="w",bg="#e4ce8e",font=("cambria",10))
            lblMostrarRegistroFecha.place(x=40,y=200,width=200,height=40,)

            botonborrarregistro=Button(frameregistro,text="BORRAR LISTA",bg="#d77948",relief=RAISED,bd=6,activebackground="#e4ce8e",font=("cambria",11),command=lambda:borrar())
            botonborrarregistro.place(x=260,y=200,width=200,height=40)

            entryIngresoFecha =Entry(frameregistro,bg="#f6ffe2")
            entryIngresoFecha.place(x=40,y=250,width=200,height=40)
            botonMostrarRegistroFecha=Button(frameregistro,text="MOSTRAR REGISTRO",font=("cambria",11),bg="#d77948",relief=RAISED,bd=6,activebackground="#e4ce8e",command=lambda:botonregistrofecha())
            botonMostrarRegistroFecha.place(x=260,y=250,width=200,height=40)

            informaciondeTablas=Label(frameregistro,text="HORA | FECHA | MARCA VEHICULO | PATENTE | HABITACION | C/HORAS | IMPORTE ",bg="#e4ce8e",relief=RIDGE,bd=5,font=("cambria",9) )
            informaciondeTablas.place(x=20,y=300,width=460,height=40)
            mostrarlista =Listbox(frameregistro,bg="#e4ce8e",relief=RIDGE,bd=5,font=("cambria",13))
            mostrarlista.place(x=20,y=340,width=460,height=340)
            scrollbar =Scrollbar(frameregistro, bg="#e4ce8e")
            scrollbar.place(x=455,y=345,width=20,height=330)
        

            def botonregistro():
                mostrarconusultas =consultas(basededato)
                i= 1
                for persona in mostrarconusultas:
                    mostrarlista.insert(i,persona)
                    i=i + 1
            def botonregistrofecha():
                nuevoregistroporfecha =entryIngresoFecha.get()
                cur=basededato.cursor()
                cur.execute("select * from nuevo_hotel where FECHA = %s" %nuevoregistroporfecha)
                datosporfecha=cur.fetchall()
                index =1
                for personas in datosporfecha:
                    mostrarlista.insert(index,personas)
                    index=index +1
            def borrar():
                mostrarlista.delete(0,"end")
           


        
