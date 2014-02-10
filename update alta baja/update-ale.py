import mysql.connector as mysql
import config
import datetime

def conect(cuil):
    conexion = mysql.connect(user=config.user_a, password=config.passwd_a, host=config.host_a, db=config.db_a)
    cursor = conexion.cursor()
    query = "SELECT * FROM titulares WHERE cuil = %s " %cuil
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado
    cursor.close()
    conexion.close()


def main():
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
    
    if confirma == "s":
        conexion = mysql.connect(user=config.user_a, password=config.passwd_a, host=config.host_a, db=config.db_a)
        cursor = conexion.cursor()
        query_update="UPDATE titulares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(mov,fecha,sss,cuil)
        query_insert="INSERT INTO altasbajas(cuil,accion,fecha,motivo) values(%s,%s,\'%s\',\'%s\')" %(cuil,mov,fecha,motivo) 
        print query_update
        print query_insert
        
        try:
            cursor.execute(query_update)
            conexion.commit()
            cursor.execute(query_insert)
            conexion.commit()
            print "ok"
            
        except Exception, e :
            print 'No es valido'

    print "Actualizacion Correcta"


    cursor.close()
    conexion.close()
 
main()
