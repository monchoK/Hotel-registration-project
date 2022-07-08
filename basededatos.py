from Hotel import *
import mysql.connector
passwordhotel ="ee2zgozxyg" #es la contraseña de mi localhost, poner la de su localhost que hizo cuando creo su base de datos
basededato=mysql.connector.connect(host="localhost", user="root",password=passwordhotel,database="hotel")
    

def consultas(basededato):
    cur=basededato.cursor()
    cur.execute("select * from nuevo_hotel")
    datos=cur.fetchall()
    return datos

