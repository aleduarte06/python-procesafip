import mysql.connector as mysql
import time
import sys
import config
import datetime



def conect():
    conexion = mysql.connect(user= config.user_a, password= config.passwd_a, host= config.host_a, db= config.db_a)
    cursor = conexion.cursor()
    query = """SELECT * FROM alta_fam group by c7 """
    cursor.execute(query)
    resultado = cursor.fetchall()
    print resultado
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

        fecha_mov=persona[25]
        f = datetime.datetime.strptime(fecha_mov,'%d%m%Y')
        fecha1 = f.strftime('%Y-%m-%d')

        #print persona
        calle = persona[12]
        #print calle
        query = """INSERT INTO os111308_old.familiares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                        nombre,sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                        depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                        ingreso_os,mov,fecha_mov)VALUES(
                                                        \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                        \'%s\',\'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                        \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                        \'%s\',%s,\'%s\')""" %(
                                                        persona[0], persona[1],persona[2],persona[3], persona[4], persona[5],persona[6],persona[7],
                                                        persona[27],persona[8],persona[9],fecha_nac,persona[11], calle.replace('"',"'"), persona[13],persona[14],
                                                        persona[15],persona[16],persona[17],persona[18],persona[19],persona[21],persona[22],persona[23],
                                                        fecha , 1,fecha1)
        print query
               
        querymov = "INSERT INTO os111308_old.altasbajas(cuil,accion,motivo,fecha) values(\'%s\',%s,\'%s\',\'%s\')" % (persona[2],1, 'Alta os',fecha1)

        querytel = "INSERT INTO os111308_old.telefono(cuil,telefono,tipo_telefono)values(\'%s\',\'%s\',%s)" % (persona[2], persona[20], 1)
        
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
