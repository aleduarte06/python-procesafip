import mysql.connector as mysql
import config
from Tkinter import *
import datetime

def consultar(cuil):
    conexion = mysql.connect(user=config.user_a, password=config.passwd_a, host=config.host_a, db=config.db_a)
    cursor = conexion.cursor()
    query = "SELECT * FROM titulares WHERE cuil = %s " %cuil
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado
    cursor.close()
    conexion.close()
def update():
    #print cuil_in.get()
    cuil=cuil_in.get()
    mov=mov_in.get()
    f = datetime.datetime.strptime(fecha_in.get(),'%d-%m-%Y')
    fecha = f.strftime('%Y-%m-%d')
    motivo=motivo_in.get()
    informar=informar_in.get()
    print "movimiento :%s  fecha :%s   motivo:%s  cuil:%s " %(mov,fecha,motivo,cuil)
    conexion = mysql.connect(user=config.user_a, password=config.passwd_a, host=config.host_a, db=config.db_a)
    cursor = conexion.cursor()
    query_update="UPDATE titulares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(mov,fecha,informar,cuil)
    query_insert="INSERT INTO altasbajas(cuil,accion,fecha,motivo) values(%s,%s,\'%s\',\'%s\')" %(cuil,mov,fecha,motivo) 
    print query_update
    print query_insert
    
    try:
        cursor.execute(query_update)
        conexion.commit()
        cursor.execute(query_insert)
        conexion.commit()
        print "ok"
        
    except Exception, e:
        print 'No es valido'
        print e

    print "Actualizacion Correcta"


    cursor.close()
    conexion.close()
    root.mainloop()

 

root = Tk()
root.geometry("500x300+0+0") #Aca le decimos a tk que tenemos una ventana de 800 x 600
root.title('formulario Update')
# row 1 : Cuil
cuil_label = Label(root,text="Cuil :")
cuil_label.grid(row=1,column=1)
cuil_in = StringVar()
cuil_entry = Entry(root,textvariable=cuil_in)
cuil_entry.grid(row=1,column=2)
#row 2 : Alta baja
mov_label= Label(root,text="alta/baja : ")
mov_label.grid(row=2,column=1)
mov_in = StringVar()
mov_entry = Entry(root,textvariable=mov_in)
mov_entry.grid(row=2,column=2)
#row 3 : Fecha
fecha_label = Label(root,text="Fecha : ")
fecha_label.grid(row=3,column=1)
fecha_in = StringVar()
fecha_entry = Entry(root,textvariable=fecha_in)
fecha_entry.grid(row=3,column=2)
#row 4 : motivo
motivo_label = Label(root,text="Motivo : ")
motivo_label.grid(row=4,column=1)
motivo_in = StringVar()
motivo_entry = Entry(root,textvariable=motivo_in)
motivo_entry.grid(row=4,column=2)
#row 4 : informar ssss  con chk box

informar_label = Label(root,text="Informar a la super : ")
informar_label.grid(row=5,column=1)
informar_in = IntVar()

informar_chk = Checkbutton(root,onvalue=1,offvalue=0,variable=informar_in)
informar_chk.grid(row=5,column=2)


#row 4 : boton update
btn = Button(root,text="Actualizar",relief=FLAT,command = update)
btn.grid(row=6,column=1)
root.mainloop()


 

def exmain():
    print "############################# update altas bajas padron #########################"


    print "\t ingrese un CUIL para editar"
    cuil = input('>')
    beneficiario = conect(cuil)
    print "vamos a editar el siguiente beneficiario"
    print beneficiario
    print "\n"
    print "ingrese tipo de movimiento 0 baja 1 alta "
    mov = input('>')
    print "ingrese fecha de alta o baja con formatp dd-mm-aaaa"
    fecha_in = raw_input('>')
    f = datetime.datetime.strptime(fecha_in,'%d-%m-%Y')
    fecha = f.strftime('%Y-%m-%d')

    print "\n"
    print "ingrese un motivo de alta o baja"
    motivo = raw_input('>')
    print "##################################################################################"
    print "\n"
    print "se esta por alcualizar el cuil : %s" %cuil
    print "con los siguientes datos" 
    print "movimiento :%s  fecha :%s   motivo:%s  " %(mov,fecha,motivo)
    print "\n hay q informar a la super? 1 = si o 0 = no"
    sss = input('>')
    print "confirma s o n"
    confirma = raw_input('>')
    e=''

