import xlwt
import mysql.connector as mysql


def conect(query):
    conexion = mysql.connect(user="root", password='luchi', host='127.0.0.1', db="testluchi")
    cursor = conexion.cursor()
    header = ('Concepto', 'Descripcion', 'Importe')

    cursor.execute(query)
    resultado = cursor.fetchall()

    reportes(header, resultado)

    cursor.close()
    conexion.close()


def reportes(header, lista):
    style0 = xlwt.easyxf('font: bold on')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Hoja 1', cell_overwrite_ok=True)

    x = 0
    for i in header:
        ws.write(9, x, i, style0)
        x += 1

    x = 10
    for datos in lista:
        y = 0
        for dato in datos:
            ws.write(x, y, dato)
            y += 1
        x += 1

    wb.save('reporte.xls')

query = """SELECT Concepto_Transf,Descripcion,sum(Importe)
    FROM nominatividad, codigo_tranferencia
    where Mes_Carga = '1113'
    and nominatividad.Concepto_Transf= codigo_tranferencia.Codigo_Concepto
    group by Concepto_Transf"""

conect(query)