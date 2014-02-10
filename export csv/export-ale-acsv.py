import mysql.connector as mysql


def conect():
    conexion = mysql.connect(user="aleduarte", password='aleduarte', host='192.168.10.8', db="mauro")
    cursor = conexion.cursor()
    query = "SELECT * FROM titulares GROUP BY cuil"

    cursor.execute(query)
    resultado = cursor.fetchall()
    return resultado
    cursor.close()
    conexion.close()


def main():
    doc = (0, 'DU', 'CI', 'LC', 'LE', 'PA')
    ben = (0, 0, 5, 4, 7, 7)
    nacion = (0, 12, 170, 36, 24, 132, 39, 133, 73, 89, 51, 0, 0)
    prov = (0, 1, 2, 3, 4, 5, 6, 7, 9, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 19, 22, 23, 24, 99)
    civil = (0, 1, 2, 6, 5, 7, 3)


    a = conect()
    for persona in a:
        if persona[2] == 4:
            c1= persona[21]
            c2= persona[27]
            c3= 0
            c4= persona[0]
            c5= persona[5]
            c6= persona[6]
            c7= doc[persona[19]]    
            c8= persona[20]
            c9= persona[7]
            c10= civil[persona[18]]
            c11= persona[14]
            c12= nacion[persona[22]]
            c13= prov[persona[13]]
            c14= persona[10]
            c15= persona[9]
            c16= persona[11]
            c17= 0
            c18= 0
            c19= persona[15]
            c20= ben[persona[2]]
            c21= 1
            c22= persona[15]
            c23= 0
            c24= 0

            print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24 )
            guardar2 = open('titulares.csv','a')
            guardar2.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24 )) 
            guardar2.close
            
            print '%s,%s,%s\n'%(c1,1,c19)
            guardar3 = open('mov.csv','a')
            guardar3.write('%s,%s,%s\n'%(c1,1,c19))
            guardar3.close
            

        else:
            c1= persona[21]
            c2= persona[27]
            c3= 0
            c4= persona[0]
            c5= persona[5]
            c6= persona[6]
            c7= doc[persona[19]]    
            c8= persona[20]
            c9= persona[7]
            c10= civil[persona[18]]
            c11= persona[14]
            c12= nacion[persona[22]]
            c13= prov[persona[13]]
            c14= persona[10]
            c15= persona[9]
            c16= persona[11]
            c17= 0
            c18= 0
            c19= persona[15]
            c20= ben[persona[2]]
            c21= 1
            c22= persona[15]
            c23= 0
            c24= 0
            print "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24 )
            guardar2 = open('titulares.csv','a')
            guardar2.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24 )) 
            guardar2.close
            print '%s,%s,%s\n'%(c1,1,c19)
            guardar3 = open('mov.csv','a')
            guardar3.write('%s,%s,%s\n'%(c1,1,c19))
            guardar3.close

        if persona[24] != 0:
            guardar4 = open('telefono.csv','a')
            guardar4.write("%s,%s,%s\n" %(persona[21], persona[24], 1))
            guardar4.close

        if persona[25] != 0:
            guardar5 = open('telefono.csv','a')
            guardar5.write("%s,%s,%s\n" %(persona[21], persona[25], 1))
            guardar5.close
        if persona[26] != 0:
            guardar6 = open('telefono.csv','a')
            guardar6.write("%s,%s,%s\n" %(persona[21], persona[26], 2))
            guardar6.close             
             

    
    


main()
