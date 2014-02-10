import mysql.connector as mysql
import time
import sys
import config
import datetime



def conect():
    conexion = mysql.connect(user= config.user_a, password= config.passwd_a, host= config.host_a, db= config.db_a)
    cursor = conexion.cursor()
    query = """SELECT * FROM comparacion.alta AS s WHERE s.c5 IN (SELECT DISTINCT c.c5 FROM  os111308.titulares AS t right outer join comparacion.sss AS c ON t.cuil = c.c5 WHERE t.cuil IS NULL ORDER BY cuil) GROUP BY s.c5 """
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado
    cursor.close()
    conexion.close()


def main():
    print "arranco a insetar registros"
    conexion = mysql.connect(user= config.user_b, password= config.passwd_b , host= config.host_b , db=config.db_b)
    cursor = conexion.cursor()


    a = conect()
    contar = 0

    for persona in a:

        fechanac=persona[10]
        fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
        fecha_nac = fn.strftime('%Y-%m-%d')


        fecha_in=persona[24]
        f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
        fecha = f.strftime('%Y-%m-%d')
        #print persona
        calle = persona[12]
        #print calle
        query = "INSERT IGNORE INTO os111308.titulares(cuil,empresa,parentesco,nro_beneficiario,apellido,nombre,tipo_doc,nro_doc,sexo_id,estado_civil,fecha_nac,nacionalidad_id,provincia_id,localidad,calle,nro,depto,piso,codigo_postal,tipo_domicilio,incapacidad,ingreso_os,tipo_beneficiario,mov,fecha_mov,prestador,situacion_revista_id)VALUES(%s,%s,%s,%s,\"%s\",\"%s\",\'%s\',%s,\'%s\',%s,\'%s\',%s,%s,\'%s\',\"%s\",\"%s\",\"%s\",\"%s\", \'%s\',%s,%s,\'%s\',%s,%s,\'%s\',%s,%s)" %(
            persona[2], 0, 0,0000, persona[7], persona[27],persona[5],persona[6],persona[8],
            persona[9], fecha_nac, persona[11], persona[18], persona[16],
            calle.replace('"',"'"),persona[13],persona[15],persona[14],persona[17], persona[19], persona[22],fecha, 
            persona[23], 1, fecha,99,persona[21])
        print query
               
        querymov = "INSERT INTO os111308.altasbajas(cuil,accion,motivo,fecha) values(%s,%s,\'%s\',\'%s\')" % (persona[2],1, 'Alta os',fecha)

        querytel = "INSERT INTO os111308.telefono(cuil,telefono,tipo_telefono)values(%s,\'%s\',%s)" % (persona[2], persona[20], 1)
        
        cursor.execute(query)
        conexion.commit()
        cursor.execute(querymov)
        conexion.commit() 
        cursor.execute(querytel)
        conexion.commit()
        print querytel

            
        contar +=1
        sys.stdout.write(". ")
        time.sleep(0.02)     

    cursor.close()
    conexion.close()
    print "\n se han procesado  %s registros" %contar

main()
