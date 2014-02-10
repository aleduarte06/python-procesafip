import mysql.connector as mysql
import time
import sys
import config



def conect():
    conexion = mysql.connect(user= config.user_a, password= config.passwd_a, host= config.host_a, db= config.db_a)
    cursor = conexion.cursor()
    query = "SELECT * FROM bajtit group by cuil"
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado
    cursor.close()
    conexion.close()


def main():
    print "arranco a insetar registros"
    conexion = mysql.connect(user= config.user_b, password= config.passwd_b , host= config.host_b , db=config.db_b)
    cursor = conexion.cursor()

    doc = ('0', 'DU', 'CI', 'LC', 'LE', 'PA')
    ben = (0, 0, 5, 4, 8, 7)
    nacion = (0, 12, 170, 36, 24, 132, 39, 133, 73, 89, 51, 0, 0)
    prov = (0, 1, 2, 3, 4, 5, 6, 7, 9, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 19, 22, 23, 24, 99)
    civil = (0, 1, 2, 6, 5, 7, 3)
 
    a = conect()
    contar = 0

    for persona in a:
        #print persona
        calle = persona[9]
        #print calle
        if persona[2] == 4:
            query = "INSERT IGNORE INTO titulares(cuil,empresa,parentesco,nro_beneficiario,apellido,nombre,tipo_doc,nro_doc,sexo_id,estado_civil,fecha_nac,nacionalidad_id,provincia_id,localidad,calle,codigo_postal,tipo_domicilio,incapacidad,ingreso_os,tipo_beneficiario,mov,fecha_mov,prestador,situacion_revista_id)VALUES(%s,%s,%s,%s,\"%s\",\"%s\",\'%s\',%s,\'%s\',%s,\'%s\',%s,%s,\'%s\',\"%s\",\'%s\',%s,%s,\'%s\',%s,%s,\'%s\',%s,%s)"%(
                persona[21], persona[27], 0, persona[0], persona[5], persona[6], doc[persona[19]],persona[20],
                persona[7], civil[persona[18]], persona[14], nacion[persona[22]], prov[persona[13]], persona[10],
                calle.replace('"',"'") , persona[11], 0, 0, persona[15], 
                0, 0, persona[37],1, 0)
            cursor.execute(query)
            conexion.commit()
            querymov = "INSERT IGNORE INTO altasbajas(cuil,accion,motivo,fecha) values(%s,%s,\'%s\',\'%s\')" % (persona[21],0, persona[36],persona[37])
            cursor.execute(querymov)
            conexion.commit()
            # print query
            # print persona
        else:
            query = "INSERT IGNORE INTO titulares(cuil,empresa,parentesco,nro_beneficiario,apellido,nombre,tipo_doc,nro_doc,sexo_id,estado_civil,fecha_nac,nacionalidad_id,provincia_id,localidad,calle,codigo_postal,tipo_domicilio,incapacidad,ingreso_os,tipo_beneficiario,mov,fecha_mov,prestador,situacion_revista_id)VALUES(%s,%s,%s,%s,\"%s\",\"%s\",\'%s\',%s,\'%s\',%s,\'%s\',%s,%s,\'%s\',\"%s\",\'%s\',%s,%s,\'%s\',%s,%s,\'%s\',%s,%s)"%(
                persona[21], persona[27], 0, persona[0], persona[5], persona[6], doc[persona[19]],persona[20],
                persona[7], civil[persona[18]], persona[14], nacion[persona[22]], prov[persona[13]], persona[10],
                calle.replace('"',"'"), persona[11], 0, 0, persona[15], 
                ben[persona[2]], 0, persona[37],0, 0)
            cursor.execute(query)
            conexion.commit()        
            querymov = "INSERT IGNORE INTO altasbajas(cuil,accion,motivo,fecha) values(%s,%s,\'%s\',\'%s\')" % (persona[21],0, persona[36],persona[37])
            cursor.execute(querymov)
            conexion.commit()
            # print query
            # print persona

        if persona[24] != 0:
            querytel = "INSERT IGNORE INTO telefono(cuil,telefono,tipo_telefono)values(%s,%s,%s)" % (persona[21], persona[24], 1)
            cursor.execute(querytel)
            conexion.commit()

        if persona[25] != 0:
            querytel2 = "INSERT IGNORE INTO telefono(cuil,telefono,tipo_telefono)values(%s,%s,%s)" % (persona[21], persona[25], 1)
            cursor.execute(querytel2)
            conexion.commit()

        if persona[26] != 0:
            querytel3 = "INSERT IGNORE INTO telefono(cuil,telefono,tipo_telefono)values(%s,%s,%s)" % (persona[21], persona[26], 2)
            cursor.execute(querytel3)
            conexion.commit()               
        contar +=1
        sys.stdout.write(". ")
        time.sleep(0.02)     

    cursor.close()
    conexion.close()
    print "\n se han procesado  %s registros" %contar

main()
