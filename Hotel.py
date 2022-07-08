from basededatos import*
class Hotel():
    def __init__(self):
        self.registros=[]
    def registrar(self,hora_entrada,fecha,marcavehiculo,patente,habitacion,cantidad_horas,importe):
        nuevoregistro=Registro()
        nuevoregistro.hora_entrada=hora_entrada
        nuevoregistro.fecha=fecha
        nuevoregistro.marcavehiculo=marcavehiculo
        nuevoregistro.patente=patente
        nuevoregistro.habitacion=habitacion
        nuevoregistro.cantidad_horas=cantidad_horas
        nuevoregistro.importe=importe
        self.registros.append(nuevoregistro)
        sql="INSERT INTO nuevo_hotel(Hora_de_Entrada,Fecha,Marca_de_Vehiculo,Patente,Habitacion,Cantidad_de_Horas,Importe) values(%s,%s,%s,%s,%s,%s,%s)"
        nuevosdatos=(hora_entrada,fecha,marcavehiculo,patente,habitacion,cantidad_horas,importe)
        cur=basededato.cursor()
        cur.execute(sql,nuevosdatos)
        basededato.commit() 
        
        

    
class Registro():
    def __init__(self):
        self.hora_entrada=0
        self.fecha=0
        self.marcavehiculo=""
        self.patente=""
        self.habitacion=0
        self.cantidad_horas=0
        self.importe=0


   

        


        

   

