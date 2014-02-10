import mysql.connector as mysql


def conect():
    conexion = mysql.connect(user="root", password='luchi', host='127.0.0.1', db="new_schema")
    cursor = conexion.cursor()
    query = "SELECT * FROM titulares LIMIT 1"
    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado
    cursor.close()
    conexion.close()


def main():
    conexion = mysql.connect(user="root", password='luchi', host='127.0.0.1', db="test")
    cursor = conexion.cursor()

    doc = (0, 'DU', 'CI', 'LC', 'LE', 'PA')
    ben = (0, 0, 5, 4, 7)
    nacion = (0, 12, 170, 36, 24, 132, 39, 133, 73, 89, 51, 0, 0)
    prov = (0, 1, 2, 3, 4, 5, 6, 7, 9, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 19, 22, 23, 24, 99)
    civil = (0, 1, 2, 6, 5, 7, 3)

    a = conect()
    for persona in a:
        if persona[2] == 4:
            query = """INSERT INTO titulares(cuil,cuit_empleador,parestesco,nro_beneficiario,nombre,apellido,tipo_doc,nro_doc,sexo_id,estado_civil,fecha_nac,nacionalidad_id,provincia_id,localidad,calle,codigo_postal,tipo_domicilio,incapacidad,ingreso_os,tipo_beneficiario,mov,fecha_mov,prestador,situacion_revista_id,tipo_domicilio) VALUES({0:s},{1:s},{2:s},{3:s},{4:s},{5:s},{6:s},{7:s},{8:s},{9:s},{10:s},{11:s},{12:s},{13:s},{14:s},{15:s},{16:s},{17:s},{18:s},{19:s},{20:s},{21:s},{22:s},{23:s},{24:s})""".format(
                persona[21], persona[27], 0, persona[0], persona[5], persona[6], doc[persona[19]],persona[20],
                persona[7], civil[persona[18]], persona[14], nacion[persona[22]], prov[persona[13]], persona[10],
                persona[9], persona[11], 0, 0, persona[15], ben[persona[2]], 'A', persona[15], 1, 0)
            cursor.execute(query)

            if persona[24] != 0:
                querytel = "INSERT INTO telefonos(cuil,telefono,tipo_telefono)values(%s,%s,%s)" % (
                    persona[21], persona[24], 1)
                cursor.execute(querytel)

            if persona[25] != 0:
                querytel2 = "INSERT INTO telefonos(cuil,telefono,tipo_telefono)values(%s,%s,%s)" % (
                    persona[21], persona[25], 1)
                cursor.execute(querytel2)

            if persona[26] != 0:
                querytel3 = "INSERT INTO telefonos(cuil,telefono,tipo_telefono)values(%s,%s,%s)" % (
                    persona[21], persona[26], 2)
                cursor.execute(querytel3)

            querymov = "INSERT INTO altasbajas(cuil,accion,fecha) values(%s,%s,%s)" % (persona[21], 'A', persona[15])
            cursor.execute(querymov)
        else:
            query = "INSERT INTO titulares(cuil,cuit_empleador,parentesco,nro_beneficiario,nombre,apellido,tipo_doc,nro_doc,sexo_id,estado_civil,fecha_nac,nacionalidad_id,provincia_id,localidad,calle,codigo_postal,tipo_domicilio,incapacidad,ingreso_os,tipo_beneficiario,mov,fecha_mov,prestador,situacion_revista_id)VALUES(%s,%s,%s,%s,\'%s\',\'%s\',\'%s\',%s,\'%s\',%s,\'%s\',%s,%s,\'%s\',\'%s\',%s,%s,%s,\'%s\',%s,%s,\'%s\',%s,%s)"%(
                (persona[21]), persona[27], 0, persona[0], persona[5], persona[6], doc[persona[19]],persona[20],
                persona[7], civil[persona[18]], persona[14], nacion[persona[22]], prov[persona[13]], persona[10],
                persona[9], persona[11], 0, 0, persona[15], 
                ben[persona[2]], 1, persona[15], 0, 0)
            print query
            cursor.execute(query)

            querymov = "INSERT INTO altasbajas(cuil,accion,fecha) values(%s,%s,%s)" % (persona[21], 'A', persona[15])
            cursor.execute(querymov)

    cursor.close()
    conexion.close()


main()