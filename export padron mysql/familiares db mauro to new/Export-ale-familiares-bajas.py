import mysql.connector as mysql
import time
import sys


def conect():
    conexion = mysql.connect(user="root", password='osmttroot', host='192.168.1.36', db="osmtt")
    cursor = conexion.cursor()
    query = "SELECT * FROM bajfam"
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado
    cursor.close()
    conexion.close()


def main():
    print "arranco a insetar registros FAMILIARES"
    conexion = mysql.connect(user="root", password='osmttroot', host='192.168.1.36', db="os111308")
    cursor = conexion.cursor()

    doc = ('0', 'DU', 'CI', 'LC', 'LE', 'PA')
    ben = (0, 0, 5, 4, 8, 7)
    nacion = (0, 12, 170, 36, 24, 132, 39, 133, 73, 89, 51, 0, 0)
    prov = (0, 1, 2, 3, 4, 5, 6, 7, 9, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 19, 22, 23, 24, 99)
    civil = (0, 1, 2, 6, 5, 7, 3)
 
    a = conect()
    contar = 0

    for persona in a:
        # print persona
        fecha_null='0000-00-00' 
        query = "INSERT IGNORE INTO familiares(cuil,parentesco,nro_beneficiario,nombre,apellido,nro_doc,tipo_doc,sexo_id,fecha_nac,nacionalidad_id,verificado,mov,fecha_mov)VALUES(%i,%i,%i,\"%s\",\"%s\",%i,\"%s\",\'%s\',\'%s\',%i,%i,%i,\"%s\")"%(
            persona[11], persona[2], persona[22], persona[5], persona[6], persona[11], doc[persona[9]],
            persona[7], persona[8], nacion[persona[12]],0,0,fecha_null)
        cursor.execute(query)
        conexion.commit()
        querymov = "INSERT IGNORE INTO altasbajas(cuil,accion,fecha) values(%s,%s,\'%s\')" % (persona[11],0,fecha_null)
        cursor.execute(querymov)
        conexion.commit()
        # print query
        # print querymov
        # print persona
                     
        contar +=1
        sys.stdout.write(".%s "%contar)
        time.sleep(0.0)     

    cursor.close()
    conexion.close()
    print "\n se han procesado  %s registros" %contar

main()
