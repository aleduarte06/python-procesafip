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
    a=cursor.fetchone()
    return a<0    

def movimiento(movimiento,linea,per):
    
    if movimiento =='BT':
        fechap = DiasMes(per)        
        fechanac=linea[10]
        fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
        fecha_nac = fn.strftime('%Y-%m-%d')
        fecha_in=linea[24]
        f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
        fecha = f.strftime('%Y-%m-%d')
        calle = linea[12]
        cuil=linea[4]            
        if linea[3]=='00':
            cons = consulta_cuil(cuil)
            if cons == True:
                query = """INSERT INTO titulares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 0,fechap)
            else:
                query="UPDATE titulares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],0,fechap,0,linea[4])
            ab(linea[04],0,'Baja Titular Monotributista informado por la afip.INF SSS',per,'BT')
        else:
            cons = consulta_cuil_fam(cuil)
            if cons == True:
                query = """INSERT INTO familiares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 0,fechap)
            else:
                query="UPDATE familiares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],0,fechap,0,linea[4])
            ab(linea[04],0,'Baja familiar Monotributista informado por la afip. INF SSS',per,'BT')
        cursor.execute(query) 

        print movimiento
    elif movimiento =='AO':
        
        fechanac=linea[10]
        fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
        fecha_nac = fn.strftime('%Y-%m-%d')
        fecha_in=linea[24]
        f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
        fecha = f.strftime('%Y-%m-%d')
        calle = linea[12]
        cuil=linea[4]            
        if linea[3]=='00':
            cons = consulta_cuil(cuil)
            if cons == True:
                query = """INSERT INTO titulares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 1,fecha)
            else:
                query="UPDATE titulares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],1,fecha,0,linea[4])
            ab(linea[04],1,'Alta Opicon de Cambio. INF SSS',per,'AO')          
        else:
            cons = consulta_cuil_fam(cuil)
            if cons == True:
                query = """INSERT INTO familiares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 1,fecha)
            else:
                query="UPDATE familiares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],1,fecha,0,linea[4])
            ab(linea[04],1,'Alta Opicon de Cambio. INF SSS. INF SSS',per,'AO')             
        cursor.execute(query)        
        
        print movimiento
    elif movimiento =='BO':
        fecha = DiasMes(per)
        if linea[3] != '00':
            query="UPDATE familiares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(0,fecha,0,linea[4])
        else:
            query="UPDATE titulares SET mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(0,fecha,0,linea[4])
        #ejecutar query
        cursor.execute(query)
        ab(linea[04],0,'Baja por Proceso de Opcion de Cambio INF SSS',per,'BO')

        
        print movimiento
    elif movimiento =='BE':
        fechap = DiasMes(per)  
        fechanac=linea[10]
        fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
        fecha_nac = fn.strftime('%Y-%m-%d')
        fecha_in=linea[24]
        f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
        fecha = f.strftime('%Y-%m-%d')
        calle = linea[12]
        cuil=linea[4]            
        cons = consulta_cuil_fam(cuil)
        if cons == True:
            query = """INSERT INTO familiares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                            sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                            depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                            ingreso_os,mov,fecha_mov)VALUES(
                                                            \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                            \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                            \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                            \'%s\',%s,\'%s\')""" %(
                                                            linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                            linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                            linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                            fecha , 0,fechap)
        else:
            query="UPDATE familiares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],0,fechap,0,linea[4])
        ab(linea[04],0,'Baja Familiar por Mayoria de Edad para el tipo de benificiario ',per,'BE')
        cursor.execute(query)
        print movimiento

    elif movimiento =='BJ':
        fechap = DiasMes(per)        
        fechanac=linea[10]
        fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
        fecha_nac = fn.strftime('%Y-%m-%d')
        fecha_in=linea[24]
        f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
        fecha = f.strftime('%Y-%m-%d')
        calle = linea[12]
        cuil=linea[4]            
        if linea[3]=='00':
            cons = consulta_cuil(cuil)
            if cons == True:
                query = """INSERT INTO titulares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 0,fechap)
            else:
                query="UPDATE titulares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],0,fechap,0,linea[4])
            ab(linea[04],0,'Baja por no tener DDJJ en los ultimos 6 meses. pata el titular y su grupo familiar INF SSS',per,'BJ')
        else:
            cons = consulta_cuil_fam(cuil)
            if cons == True:
                query = """INSERT INTO familiares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 0,fechap)
            else:
                query="UPDATE familiares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],0,fechap,0,linea[4])
            ab(linea[04],0,'Baja por no tener DDJJ en los ultimos 6 meses. pata el titular y su grupo familiar INF SSS',per,'BJ')
        cursor.execute(query) 



        print movimiento
    elif movimiento =='MT':
        fechap = DiasMes(per)        
        fechanac=linea[10]
        fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
        fecha_nac = fn.strftime('%Y-%m-%d')
        fecha_in=linea[24]
        f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
        fecha = f.strftime('%Y-%m-%d')
        calle = linea[12]
        cuil=linea[4]            
        if linea[3]=='00':
            cons = consulta_cuil(cuil)
            if cons == True:
                query = """INSERT INTO titulares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[27],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 1,fechap)
            else:
                query="UPDATE titulares SET cuit_empresa=%s,tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[27],linea[23],linea[21],0,fechap,0,linea[4])
            ab(linea[04],2,'Modificacion de CUIT del empleador. INF SSS',per,'MT')         
        else:
            cons = consulta_cuil_fam(cuil)
            if cons == True:
                query = """INSERT INTO familiares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 1,fechap)
            else:
                query="UPDATE familiares SET cuit_empresa=%s,tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[27],linea[23],linea[21],0,fechap,0,linea[4])
            ab(linea[04],2,'Modificacion de CUIT del empleador. INF SSS',per,'MT')             
        cursor.execute(query) 

        # Llamar a funcion
        print movimiento
    elif movimiento =='AA':
        cuil=linea[4]
        cuilt=linea[2]
        cons = consulta_cuil(cuil)
        consf = consulta_cuil_fam(cuilt)
        fechap = DiasMes(per)
        if cons == True:

            fechanac=linea[10]
            fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
            fecha_nac = fn.strftime('%Y-%m-%d')
            fecha_in=linea[24]
            f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
            fecha = f.strftime('%Y-%m-%d')
            calle = linea[12]
            query = """INSERT INTO titulares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                            sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                            depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                            ingreso_os,mov,fecha_mov)VALUES(
                                                            \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                            \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                            \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                            \'%s\',%s,\'%s\')""" %(
                                                            linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                            linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                            linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                            fecha , 1,fechap)
            cursor.execute(query)
            if consf == False:
                query="UPDATE familiares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(1,linea[21],1,fechap,1,linea[4])
                cursor.execute(query)
        else:
            query="UPDATE titulares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(1,linea[21],1,fechap,1,linea[4])
            cursor.execute(query)
            if consf == False:
                query="UPDATE familiares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(1,linea[21],1,fechap,1,linea[4])
                cursor.execute(query)            
        ab(linea[04],1,'Alta automatica de titular en relacion de dependencia que no figura en SSS, Beneficiario declarado por empleador en DDJJ SIJP y los aportes son derivados a esta OS',per,'AA')
      


        print movimiento
    elif movimiento =='BY':
        fechap = DiasMes(per)        
        fechanac=linea[10]
        fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
        fecha_nac = fn.strftime('%Y-%m-%d')
        fecha_in=linea[24]
        f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
        fecha = f.strftime('%Y-%m-%d')
        calle = linea[12]
        cuil=linea[4]            
        if linea[3]=='00':
            cons = consulta_cuil(cuil)
            if cons == True:
                query = """INSERT INTO titulares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 0,fechap)
            else:
                query="UPDATE titulares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],0,fechap,0,linea[4])
            ab(linea[04],0,'Monotributista Inexistente en el padron de Contribuyentes, No pago por 1 año INF SSS',per,'BY')         
        else:
            cons = consulta_cuil_fam(cuil)
            if cons == True:
                query = """INSERT INTO familiares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 0,fechap)
            else:
                query="UPDATE familiares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],0,fechap,0,linea[4])
            ab(linea[04],0,'Monotributista Inexistente en el padron de Contribuyentes, No pago por 1 año INF SSS',per,'BY')             
        cursor.execute(query) 


        print movimiento

    elif movimiento =='BQ':
        fechap = DiasMes(per)        
        fechanac=linea[10]
        fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
        fecha_nac = fn.strftime('%Y-%m-%d')
        fecha_in=linea[24]
        f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
        fecha = f.strftime('%Y-%m-%d')
        calle = linea[12]
        cuil=linea[4]            
        cons = consulta_cuil(cuil)
        if cons == True:
            query = """INSERT INTO titulares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                            sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                            depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                            ingreso_os,mov,fecha_mov)VALUES(
                                                            \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                            \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                            \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                            \'%s\',%s,\'%s\')""" %(
                                                            linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                            linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                            linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                            fecha , 0,fechap)
        else:
            query="UPDATE titulares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],0,fechap,0,linea[4])
        ab(linea[04],0,'El empleador declarado en la ddjj es diferente y la OS tambien INF SSS',per,'BQ')            
        cursor.execute(query)

  
        print movimiento
    
    elif movimiento =='BM':
        detalle = linea[27]
        fechap = DiasMes(per)        
        fechanac=linea[10]
        fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
        fecha_nac = fn.strftime('%Y-%m-%d')
        fecha_in=linea[24]
        f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
        fecha = f.strftime('%Y-%m-%d')
        calle = linea[12]
        cuil=linea[4]            
        cons = consulta_cuil_fam(cuil)
        print detalle
        if cons == True:
            query = """INSERT INTO familiares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                            sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                            depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                            ingreso_os,mov,fecha_mov)VALUES(
                                                            \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                            \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                            \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                            \'%s\',%s,\'%s\')""" %(
                                                            linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                            linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                            linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                            fecha , 0,fechap)
        else:
            query="UPDATE familiares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],0,fechap,0,linea[4])
        ab(linea[04],0,'El familiar EXISTE como %s. INF SSS'%detalle,per,'BM')
        cursor.execute(query)        

        print movimiento
    elif movimiento =='BF':
        fechap = DiasMes(per)
        cuil=linea[4]
        cons = consulta_cuil_fam(cuil)            
        if linea[3]=='00':
            cons = consulta_cuil(cuil)
            if cons == True:
                fechanac=linea[10]
                fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
                fecha_nac = fn.strftime('%Y-%m-%d')
                fecha_in=linea[24]
                f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
                fecha = f.strftime('%Y-%m-%d')
                calle = linea[12]
                query = """INSERT INTO titulares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 0,fechap)
            else:
                query="UPDATE titulares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],0,fechap,0,linea[4])
            ab(linea[04],0,'Baja Titular Fallecido. INF SSS',per,'BF')          
        else:
            cons = consulta_cuil_fam(cuil)
            if cons == True:
                fechanac=linea[10]
                fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
                fecha_nac = fn.strftime('%Y-%m-%d')
                fecha_in=linea[24]
                f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
                fecha = f.strftime('%Y-%m-%d')
                calle = linea[12]
                query = """INSERT INTO familiares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 0,fechap)
            else:
                query="UPDATE familiares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],0,fechap,0,linea[4])
            ab(linea[04],0,'Baja familiar Fallecido. INF SSS',per,'BF')             
        cursor.execute(query)
             


        
        print movimiento
    elif movimiento =='JR':
        fechap = DiasMes(per)        
        fechanac=linea[10]
        fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
        fecha_nac = fn.strftime('%Y-%m-%d')
        fecha_in=linea[24]
        f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
        fecha = f.strftime('%Y-%m-%d')
        calle = linea[12]
        cuil=linea[4]            
        if linea[3]=='00':
            cons = consulta_cuil(cuil)
            if cons == True:
                query = """INSERT INTO titulares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 0,fechap)
            else:
                query="UPDATE titulares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],0,fechap,0,linea[4])
            ab(linea[04],0,'Titular en relacion de dependencia figura como jubilado. Se aplica la baja a todo el grupo familiar. INF SSS',per,'JR')         
        else:
            cons = consulta_cuil_fam(cuil)
            if cons == True:
                query = """INSERT INTO familiares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 0,fechap)
            else:
                query="UPDATE familiares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],0,fechap,0,linea[4])
            ab(linea[04],0,'Titular en relacion de dependencia figura como jubilado. Se aplica la baja a todo el grupo familiar. INF SSS',per,'JR')             
        cursor.execute(query) 
        
        print movimiento
    elif movimiento =='AD':
        fechap = DiasMes(per)
        cuil=linea[4]
        cons = consulta_cuil(cuil)
        tf=linea[3]              
        if tf == '00':
            if cons == True:
                fechanac=linea[10]
                fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
                fecha_nac = fn.strftime('%Y-%m-%d')
                fecha_in=linea[24]
                f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
                fecha = f.strftime('%Y-%m-%d')
                calle = linea[12]
                query = """INSERT INTO titulares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 1,fechap)
            else:

                query="UPDATE titulares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(8,linea[21],1,fechap,0,linea[4])
        
        else:
            if cons == True:
                fechanac=linea[10]
                fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
                fecha_nac = fn.strftime('%Y-%m-%d')
                fecha_in=linea[24]
                f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
                fecha = f.strftime('%Y-%m-%d')
                calle = linea[12]
                query = """INSERT INTO familiares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 1,fechap)
            else:

                query="UPDATE familiares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(8,linea[21],1,fechap,0,linea[4])            

        cursor.execute(query)
        ab(linea[04],1,'Alta beneficiario titulares y familiares, si los tuviera, con prestacion de Desempleo informada por ANSES . INF SSS',per,'AD')       


        
        print movimiento
    elif movimiento =='BD':
        fechap = DiasMes(per)        
        fechanac=linea[10]
        fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
        fecha_nac = fn.strftime('%Y-%m-%d')
        fecha_in=linea[24]
        f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
        fecha = f.strftime('%Y-%m-%d')
        calle = linea[12]
        cuil=linea[4]            
        if linea[3]=='00':
            cons = consulta_cuil(cuil)
            if cons == True:
                query = """INSERT INTO titulares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 0,fechap)
            else:
                query="UPDATE titulares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],0,fechap,0,linea[4])
            ab(linea[04],0,'El empleador declarado en la ddjj es diferente y la OS tambien INF SSS. INF SSS',per,'BD')
        else:
            cons = consulta_cuil_fam(cuil)
            if cons == True:
                query = """INSERT INTO familiares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                                sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                                depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                                ingreso_os,mov,fecha_mov)VALUES(
                                                                \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                                \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                                \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                                \'%s\',%s,\'%s\')""" %(
                                                                linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                                linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                                linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                                fecha , 0,fechap)
            else:
                query="UPDATE familiares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(linea[23],linea[21],0,fechap,0,linea[4])
            ab(linea[04],0,'El empleador declarado en la ddjj es diferente y la OS tambien INF SSS. INF SSS',per,'BD')             
        cursor.execute(query) 


        print movimiento
    elif movimiento =='DA':
        fechap = DiasMes(per)
        cuil=linea[4]
        cons = consulta_cuil_fam(cuil)            
        if cons == True:
            fechanac=linea[10]
            fn = datetime.datetime.strptime(fechanac,'%d%m%Y')
            fecha_nac = fn.strftime('%Y-%m-%d')
            fecha_in=linea[24]
            f = datetime.datetime.strptime(fecha_in,'%d%m%Y')
            fecha = f.strftime('%Y-%m-%d')
            calle = linea[12]
            query = """INSERT INTO familiares(cod_os,cuit_empresa,cuil_titular,parentesco,cuil,tipo_doc,nro_doc,apellido,
                                                            sexo_id,estado_civil,fecha_nac,nacionalidad_id,calle,nro,piso,
                                                            depto,localidad,codigo_postal,provincia_id,tipo_domicilio,situacion_revista_id,incapacidad,tipo_beneficiario,
                                                            ingreso_os,mov,fecha_mov)VALUES(
                                                            \'%s\',\'%s\',\'%s\',%s,\"%s\",\"%s\",\'%s\',\'%s\',
                                                            \'%s\', %s ,\'%s\', %s ,\'%s\',\"%s\",\"%s\",
                                                            \"%s\",\"%s\", \'%s\',%s,%s,%s,%s,%s,
                                                            \'%s\',%s,\'%s\')""" %(
                                                            linea[0], linea[1],linea[2],linea[3], linea[4], linea[5],linea[6],linea[7],
                                                            linea[8],linea[9],fecha_nac,linea[11], calle.replace('"',"'"), linea[13],linea[14],
                                                            linea[15],linea[16],linea[17],linea[18],linea[19],linea[21],linea[22],linea[23],
                                                            fecha , 1,fechap)
        else:

            query="UPDATE familiares SET tipo_beneficiario=%s,situacion_revista_id=%s,mov=%s,fecha_mov =\'%s\',informar=%s WHERE cuil = %s" %(8,linea[21],1,fechap,0,linea[4])
        cursor.execute(query)
        ab(linea[04],1,'Alta de familiares que figuran a cargo de un titular con capita de desempleo y no se encuentra en el grupo familiar informado por la OS en el padron. INF SSS',per,'DA')       


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
