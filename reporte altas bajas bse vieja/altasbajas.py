import xlwt
import mysql.connector as mysql

def conect(query):
    conexion = mysql.connect(user="root", password='luchi', host='127.0.0.1', db="new_schema")
    cursor = conexion.cursor()
    cursor.execute(query)
    resultado = cursor.fetchall()
    total = 0
    for i in resultado:
        total += 1
    return total
    cursor.close()
    conexion.close()


def titact(prov, mes):
    query = "SELECT * FROM titulares WHERE titulares.procede between '1' and '4' AND titulares.fecing <= '%s' AND titulares.provincia = %s" % (
        mes, prov)

    return conect(query)


def famact(prov, mes):
    query = "SELECT * FROM familia f JOIN titulares ON titulares.nroben = f.nroben AND titulares.procede between '1' and '4' AND titulares.fecing <='%s'AND titulares.provincia = %s" % (
        mes, prov)

    return conect(query)


def titbaj(prov, mes):
    a = mes.split('/')
    query = "SELECT * FROM bajtit t WHERE t.procede between '1' and '4' AND t.fecbaja between '%s/%s/01' and '%s' AND t.provincia = %s" % (
        a[0], a[1], mes, prov)

    return conect(query)


def fambaj(prov, mes):
    b = mes.split('/')
    query = "SELECT * FROM bajfam f join bajtit on bajtit.nroben = f.nroben AND bajtit.procede between '1' and '4' AND bajtit.fecbaja between '%s/%s/01' and '%s' AND bajtit.provincia = %s" % (
        b[0], b[1], mes, prov)

    return conect(query)


meses = (
    '2012/10/31',
    '2012/11/30',
    '2012/12/31',
    '2013/01/31',
    '2013/02/28',
    '2013/03/31',
    '2013/04/30',
    '2013/05/31',
    '2013/06/30',
    '2013/07/31',
    '2013/08/31',
    '2013/09/30',
    '2013/10/31',
    '2013/11/30',
    '2013/12/31',
)

provincias = {
        'Capital Federal': 1,
        'Buenos Aires': 2,
        'Catamarca': 3,
        'Cordoba': 4,
        'Corrientes': 5,
        'Entre Rios': 6,
        'Jujuy': 7,
        'Mendoza': 8,
        'La Rioja': 9,        
        'Salta': 10,
        'San Juan': 11,
        'San Luis': 12,
        'Santa Fe': 13,
        'Santiago del Estero': 14,
        'Tucuman': 15,
        'Chaco': 16,
        'Chubut': 17,
        'Formosa': 18,
        'Misiones': 19,
        'Neuquen': 20,
        'La Pampa': 21,
        'Rio Negro': 22,
        'Santa Cruz': 23,
        'Tierra del Fuego': 24,
        'Sin Especificar': 25,
    }

def main():
    style0 = xlwt.easyxf('font: bold on')

    wb = xlwt.Workbook()
    ws = wb.add_sheet('actividad', cell_overwrite_ok=True)

    ws.write(0, 0, 'Activos', style0)
    x = 1
    for provincia, i in provincias.iteritems():
        ws.write(x, 0, provincia)

        for contenido in meses:
            tit = titact(i, contenido)
            fam = famact(i, contenido)

            ws.write(x, 1, contenido)
            ws.write(x, 2, tit)
            ws.write(x, 3, fam)
            x += 1
        x += 2

    ws.write(0, 5, 'Bajas', style0)
    x = 1

    for provincia, i in provincias.iteritems():
        ws.write(x, 5, provincia)

        for contenido in meses:
            titb = titbaj(i,contenido)
            famb = fambaj(i,contenido)
            ws.write(x, 6, contenido)
            ws.write(x, 7, titb)
            ws.write(x, 8, famb)
            x += 1
        x += 2
    wb.save('ActividadPadron.xls')

main()