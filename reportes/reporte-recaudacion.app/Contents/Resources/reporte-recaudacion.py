import config as cn
import xlwt

from xlwt import *
import mysql.connector as mysql
from xlrd import open_workbook
from xlutils.copy import copy
from datetime import datetime

def conect(query, periodo,plantilla):
    conexion = mysql.connect(user=cn.user, password=cn.password, host=cn.host, db=cn.db)
    cursor = conexion.cursor()

    cursor.execute(query)
    print 'aca'
    resultado = cursor.fetchall()
    print 'ok'
    if plantilla == 1:
        header = ('Efector','Benficiario','Apellido','Nombre','Cuil','Periodo','Importe','Acreditado','Recaudado','Codigo')
        reportes(header, resultado, periodo)
    elif plantilla == 2:    
        header = ('Concepto', 'Descripcion', 'Importe','C/D')
        reportes_plantilla(header, resultado, periodo)
    elif plantilla == 3:
        header = ('Efector','Benficiario','Apellido','Nombre','Cuil','Periodo','Importe','Acreditado','Recaudado','Codigo')
        reportes(header, resultado, periodo)
    cursor.close()
    conexion.close()


def reportes(header, lista, periodo):
    style0 = xlwt.easyxf('font: bold on')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Periodo'+periodo, cell_overwrite_ok=True)
    x = 0
    for i in header:
        
        ws.write(0,x, i, style0)
        x += 1

    x = 1
    for datos in lista:
        y = 0
        for dato in datos:
            ws.write(x, y, dato)
            y += 1
        x += 1

    wb.save('EFECTORES%s.xls'%periodo) 
    main()

def reportes_plantilla_efectores(header, lista, periodo):
    # Ejemplo de modificacion de hoja Excel
    style0 = xlwt.easyxf('font: bold on')
    rb = open_workbook('efectores.xls',formatting_info=True)
    wb = copy(rb)
    ws = wb.get_sheet(0)
    x=0

    for i in header:
        
        ws.write(0,x, i, style0)
        x += 1

    x = 1
    for datos in lista:
        y = 0
        for dato in datos:
            ws.write(x, y, dato)
            y += 1
        x += 1
    

    #ws.write(0,0,"I'm only changing cell A1")
    wb.save('EFECTORES%s.xls' %periodo)
    main()    
def reportes_plantilla(header, lista, periodo):
   
    # Ejemplo de modificacion de hoja Excel
    # style0 = xlwt.easyxf('font: bold on')
    rb = open_workbook('example.xls',formatting_info=True)
    wb = copy(rb)
    ws = wb.get_sheet(0)
    
    x = 8
    for datos in lista:
        if dato[3]=='D':
            dato1=[dato[0],dato[1], ' ' ,dato[2]]
            print dato1
        y=0
        for dato in datos:
            print dato
            ws.write(x, y, dato)
            y += 1
        x += 1
        
    

    #ws.write(0,0,"I'm only changing cell A1")
    wb.save('Recaudacion%s.xls' %periodo)
    main()


def recaudacion_mensual(periodo):
    desde = '20%s-%s-01'%(periodo[2:4],periodo[0:2])
    hasta = '20%s-%s-31'%(periodo[2:4],periodo[0:2])
    plantilla=2
    query = """SELECT Concepto_Transf,Descripcion,sum(Importe)/100,Credito_Debito
    FROM test.afip_nominatividad as n 
    LEFT JOIN test.afip_codigo_tranferencia as c on n.Concepto_Transf= c.Codigo_Concepto
    where Fecha_Transf between \'%s\' and \'%s\'
    group by Concepto_Transf""" %(desde,hasta)
    print query
    conect(query, periodo,plantilla)

def recaudacion_mensual_efectores(periodo,quincena='""'):
    plantilla = 3
    query = """SELECT concat_ws('', t.interno1 ,t.interno) as efector , t.nroben, t.apellido, t.nombre, n.Cuil_Aportante as cuil, Periodo, replace(format(n.importe/100,2),".",",") as importe , n.Fecha_Transf, n.Fecha_Recauda, n.Concepto_Transf  
    FROM osmtt.titulares as t
    LEFT JOIN os111308.afip_nominatividad as n on t.cuil = n.Cuil_Aportante
    WHERE procede = 5
    AND Mes_Carga = %s
    AND n.Concepto_Transf IN ('C14','SEO')""" %periodo
    print 'ok'
    conect(query, periodo,plantilla)

def main():
    print "Eleija una opcion: "
    print "1) recaudacion mensual"
    print "2) recaudacion mensual plantilla"
    print "3) EFECTORES"
    opcion = input('>')
    if opcion == 1:
        print "mm-aa sin guion"
        periodo = raw_input('>')
        print "ingese quincena '1 o 2' "
        quincena = raw_input('>')
        print periodo 
        print quincena
        try:
            recaudacion_mensual(periodo,quincena)
        except Exception, e:
            print 'No es valido'
            main()

    elif opcion == 2:
        print "mm-aa sin guion"
        periodo = raw_input('>')
        print periodo 
        try:
            recaudacion_mensual(periodo)
        except Exception, e:
            print 'No es valido'
            main()        

    if opcion == 3:
        print "mm-aa sin guion"
        periodo = raw_input('>')
        print periodo
        try:
            recaudacion_mensual_efectores(periodo)
        except Exception, e:
            print 'No es valido'
            main()        
main()


    
