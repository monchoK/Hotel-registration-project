from tkinter import*
from interfaces import Interfaz
def main():
    root=Tk()
    root.resizable(width=False, height=False)
    root.title("GESTOR DE HOTEL")
    root.iconbitmap("systemfilemanager_94456.ico")
    ventana =Interfaz(root)
    ventana.mainloop()      

if __name__=="__main__":
    main()