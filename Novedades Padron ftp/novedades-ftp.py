import mysql.connector as mysql
import calendar
# import time
# import sys
import config
import datetime
import glob



conexion = mysql.connect(user= config.user_a, password= config.passwd_a, host= config.host_a, db= config.db_a)
cursor = conexion.cursor()

# def fecha(a):
#     #convertir texto a fecha 01122012
#     fn = datetime.datetime.strptime(a,'%d%m%Y')
#     fecha = fn.strftime('%Y-%m-%d')
#     return fecha
def DiasMes(periodo):
    firstweekday,days=calendar.monthrange(int(periodo[0:4]),int(periodo[4:6]))
    a ='%s-%02d-%s' %(periodo[0:4],int(periodo[4:6]),days)
    return a

def ab(cuil,ab,movtxt,fecha,movsss):

    query = "INSERT INTO altasbajas(cuil,accion,motivo,fecha,abm_sss) values(\'%s\',%s,\'%s\',\'%s\',\'%s\')" % (cuil,ab,movtxt,DiasMes(fecha),movsss)
    cursor.execute(query)
def consulta_cuil(cuil):
    query = "SELECT* FROM titulares WHERE cuil = %s" %cuil 
    cursor.execute(query)
    a=cursor.fetchone()
    return a<0
def consulta_cuil_fam(cuil):
    query = "SELECT* FROM familiares WHERE cuil = %s" %cuil 
    cursor.execute(query)
    a.cursor.fetchone()
    return a<0    

def movimiento(movimiento,linea,per):
    
    if movimiento =='BT':
        # detectar detalle
        # detalle = linea[27]
        # fecha = DiasMes(per)
        # if detalle == 'T':

        #     query="UPDATE titulares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(0,fecha,0,linea[4])
        # else:
        #     query="UPDATE familiares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(0,fecha,0,linea[4])

        # #ejecutar query
        # cursor.execute(query)
        # ab(linea[04],0,'Monotributista dado de baja, informafo por AFIP',per,'BT')
        
        print movimiento
    elif movimiento =='AO':
        # Llamar a funcion 
        print movimiento
    elif movimiento =='BO':
        # fecha = DiasMes(per)
        # if linea[3] != '00':
        #     query="UPDATE familiares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(0,fecha,0,linea[4])
        # else:
        #     query="UPDATE titulares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(0,fecha,0,linea[4])
        # #ejecutar query
        # cursor.execute(query)
        # ab(linea[04],0,'Baja por Proceso de Opcion de Cambio INF SSS',per,'BO')

        
        print movimiento
    elif movimiento =='BE':
        # Llamar a funcion
        print movimiento

    elif movimiento =='BJ':
        # fecha = DiasMes(per)
        # if linea[3] != '00':
        #     query="UPDATE familiares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(0,fecha,0,linea[4])
        # else:
        #     query="UPDATE titulares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(0,fecha,0,linea[4])
        # #ejecutar query
        # cursor.execute(query)
        # ab(linea[04],0,'Baja por no tener ddjj ultimos 6 meses, para titular y grupo familiar. INF SSS',per,'BJ')        
        # # Llamar a funcion
        print movimiento
    elif movimiento =='MT':
        # if linea[3] != '00':
        #     query="UPDATE familiares SET cuit_empresa=%s WHERE cuil = %s" %(linea[27],linea[4])
        # else:
        #     query="UPDATE titulares SET cuit_empresa=%s WHERE cuil = %s" %(linea[27],linea[4])
        # cursor.execute(query)
        # ab(linea[04],2,'Modificacion de CUIT del empleador. INF SSS',per,'MT')
        # Llamar a funcion
        print movimiento
    elif movimiento =='AA':
        # cuil=linea[4]
        # cons = consulta_cuil(cuil)

        # fecha1 = DiasMes(per)
        # #print calle
        # if cons == True:
        #         archivo=open('Novedades_manuales.txt','a')
        #         archivo.write('|'.join(linea))
        #         archivo.close
        # else:
        #     query="UPDATE titulares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(0,fecha1,0,linea[4])
        #     cursor.execute(query)
        #     query="UPDATE familiares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil_titular = %s" %(1,fecha1,0,linea[4])
        #     cursor.execute(query)
        #     ab(linea[04],0,'Alta automatica de titular en relacion de dependencia que no figura en SSS, Beneficiario declarado por empleador en DDJJ SIJP y los aportes son derivados a esta OS',per,'AA')
        # # Llamar a funcion
        print movimiento
    elif movimiento =='BY':
        # fecha = DiasMes(per)        
        # if linea[3] != '00':
        #     query="UPDATE familiares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(0,fecha,0,linea[4])
        # else:
        #     query="UPDATE titulares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(0,fecha,0,linea[4])
        # cursor.execute(query)
        # ab(linea[04],0,'Monotributista Inexistente en el padron de Contribuyentes, No pago por 1 año INF SSS',per,'BY')
        print movimiento

    elif movimiento =='BQ':
        # fecha = DiasMes(per)        
        # if linea[3] != '00':
        #     query="UPDATE familiares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(0,fecha,0,linea[4])
        # else:
        #     query="UPDATE titulares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(0,fecha,0,linea[4])
        # cursor.execute(query)
        # ab(linea[04],0,'El empleador declarado en la ddjj es diferente y la OS tambien INF SSS',per,'BQ')
        
        print movimiento
    
    elif movimiento =='BM':
        # Llamar a funcion
        print movimiento
    elif movimiento =='BF':
        # Llamar a funcion
        print movimiento
    elif movimiento =='JR':
        # Llamar a funcion
        print movimiento
    elif movimiento =='AD':
        # Llamar a funcion

        Hasta aca llegue me fui a dormir 

        
        print movimiento
    elif movimiento =='BD':
        # fecha = DiasMes(per)        
        # if linea[3] != '00':
        #     query="UPDATE familiares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(0,fecha,0,linea[4])
        # else:
        #     query="UPDATE titulares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(0,fecha,0,linea[4])
        # cursor.execute(query)
        # ab(linea[04],0,'El empleador declarado en la ddjj es diferente y la OS tambien INF SSS',per,'BD')

        # Llamar a funcion
        print movimiento
    elif movimiento =='DA':
        print movimiento
        # Llamar a funcion
    else:
        aa=open('log.txt','a')
        aa.write('|'.join(linea))
        aa.close
        return 0
        

print "Novedades"

archivos = glob.glob("Novedades_*.txt")
for x in archivos:
    archivo = open(x,'r')
    n=0
    while True:
            
        a = archivo.readline()
    
        if a == '':
            break
        
        linea=a.split('|')
        enviar=movimiento(linea[26],linea,'201311')
        n+=1    

conexion.commit()        
cursor.close()
conexion.close()
