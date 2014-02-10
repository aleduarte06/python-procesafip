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
        header = ('Concepto', 'Descripcion', 'Importe')
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
    #periodo = int(periodo)
    # s=str(periodo)
    # mm=s[0]+s[1]
    # aa=s[2]+s[3]
    # per=mm+'/'+aa
    # dt = datetime.strptime(per, "%m/%y")
    # Ejemplo de modificacion de hoja Excel
    style0 = xlwt.easyxf('font: bold on')
    rb = open_workbook('example.xls',formatting_info=True)
    wb = copy(rb)
    ws = wb.get_sheet(0)


    
    # fmt = 'MMM-YY' #formato de fecha
    # style = XFStyle() #estilo de fecha nov-13
    # style.num_format_str = fmt #convertir al estilo mm-aa
    # ws.write(0, 2,datetime.now()) # graba en la celda la fecha con el estilo
    # # aca restamos un mes a la fecha para indicar el periodo recaudado
    # carry, new_month=divmod(dt.month-1+1, 12)
    # new_month-=1
    # mesdown=dt.replace(year=dt.year+carry, month=new_month)
    # print mesdown

    # aca imprimo el mes de pago y el periodo en posicion 
    
    # ws.write(4,0,dt,style) #mes de pago
    # r = int(periodo)
    # r = r-100
    # ws.write(4,2,mesdown,style) #mes posicion

    x = 8
    for datos in lista:
        y = 0
        for dato in datos:
            ws.write(x, y, dato)
            y += 1
        x += 1
    

    #ws.write(0,0,"I'm only changing cell A1")
    wb.save('Recaudacion%s.xls' %periodo)
    main()


def recaudacion_mensual(periodo):
    plantilla=2
    query = """SELECT Concepto_Transf,Descripcion,sum(Importe)/100
    FROM os111308.afip_nominatividad as n 
    LEFT JOIN os111308.afip_codigo_tranferencia as c on n.Concepto_Transf= c.Codigo_Concepto
    where Mes_Carga = %s
    group by Concepto_Transf"""%periodo
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


    
