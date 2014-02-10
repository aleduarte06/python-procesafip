# -*- enconding: utf-8 -*-
import glob
dgi = 'm:\dgi'
loncarica = 'm:\loncarica'


def nominatividad(directorio,mes_carga):
	print mes_carga
	id_nom=''
	archivos = glob.glob("OS1113*.txt")
	nomi = glob.glob("nominatividad.csv")
	print nomi
	if not nomi:

		for i in archivos:
			archivo = open(directorio+i,'r')
			header = archivo.readline()
			if header[0:8] == "HFTRANSF":
				while True:
					linea =  archivo.readline()
					if linea[0:2] == "TN":
						break
					coma = ","
					guardar2 = open(directorio+'nominatividad%s.csv'%mes_carga,'a')
					guardar2.write(linea[0:4]+','+linea[4:7]+','+linea[7:22]+','+linea[22:23]+','+linea[23:33]+','+linea[33:43]+','+linea[43:54]+','+linea[54:58]+','+linea[58:70]+','+linea[70:73]+','+linea[73:84]+','+linea[84:87]+','+linea[87:90]+','+linea[90:92]+','+linea[92:94]+','+linea[94:95]+','+linea[95:96]+','+linea[96:98]+','+linea[98:99]+','+linea[99:100]+','+mes_carga+','+id_nom+'\n')
					guardar2.close
					archivo.close
	else:
		print "El archivo ya existe"

def nominatividadsql(directorio,mes_carga):
	print mes_carga
	id_nom=''
	archivos = glob.glob("OS1113*.txt")
	nomi = glob.glob("nominatividad.csv")
	print nomi
	if not nomi:
		guardar2 = open(directorio+'nominatividad%s.sql'%mes_carga,'a')
		guardar2.write("LOCK TABLES `nominatividad` WRITE;\n")
		guardar2.close
		guardar2.write("INSERT INTO `nominatividad` (`Renos`, `Concepto_Transf`, `Importe`, `Cred_Deb`, `Fecha_Transf`, `Fecha_Recauda`, `Cuit_Contribuyente`, `Periodo`, `Nro_Obligacion`, `Sec_Obligacion`, `Cuit_Aportante`, `Banco`, `Sucursal`, `Zona`, `Porcentaje_Reduccion`, `Porcentaje_Reduccion2`, `Porcentaje_Reduccion3`, `Grupo_Famliar`, `Tipo_Pago`, `Marca_Apropiacion`, `Mes_Carga`, `id`)\n")
		guardar2.close
		guardar2.write('VALUES\n')
		guardar2.close
		
		for i in archivos:

			archivo = open(directorio+i,'r')
			header = archivo.readline()
			if header[0:8] == "HFTRANSF":
				while True:
					linea =  archivo.readline()
					if linea[0:2] == "TN":
						break
					coma = ","
					guardar2.write('\t'+'('+linea[0:4]+','+linea[4:7]+','+linea[7:22]+','+linea[22:23]+','+linea[23:33]+','+linea[33:43]+','+linea[43:54]+','+linea[54:58]+','+linea[58:70]+','+linea[70:73]+','+linea[73:84]+','+linea[84:87]+','+linea[87:90]+','+linea[90:92]+','+linea[92:94]+','+linea[94:95]+','+linea[95:96]+','+linea[96:98]+','+linea[98:99]+','+linea[99:100]+','+mes_carga+','+id_nom+')'+'\n')
					guardar2.close
					archivo.close
		guardar2.write('UNLOCK TABLES;')
		guardar2.close 			
	else:
		print "El archivo ya existe"


def nomina(directorio): #ddjj - nominas para obras sociales
	print directorio
	archivos = glob.glob("ddjjredu*.txt")
	nomi = glob.glob("nomina.csv")
	if not nomi:

		for i in archivos:
			archivo = open(directorio+i,'r')
			header = archivo.readline()
			if header[0:22] == "HFOS111308DDJJ-NOMINAS":
				while True:
					linea =  archivo.readline()
					if linea[0:2] == "TF":
						break
					coma = ","
					guardar2 = open(directorio+'nomina.csv','a')
					guardar2.write(linea[0:6]+','+linea[6:10]+','+linea[10:21]+','+linea[21:32]+','+linea[32:44]+','+linea[44:52]+','+linea[52:54]+','+linea[54:56]+','+linea[56:58]+','+linea[58:61]+','+linea[61:63]+','+linea[63:65]+','+linea[65:68]+','+linea[68:71]+','+linea[71:73]+','+linea[73:81]+','+linea[81:83]+','+linea[83:94]+','+linea[94:95]+','+linea[95:107]+','+linea[107:108]+','+linea[108:109]+','+linea[109:119]+','+linea[119:129]+','+linea[129:130]+','+linea[130:164]+','+linea[164:175]+','+linea[175:177]+','+linea[177:200]+'\n')
					guardar2.close
					archivo.close


def nomina2(directorio): #ddjj - nominas para obras sociales
	archivos = glob.glob("ddjjredu*.txt")
	nomi = glob.glob("nomina.csv")
	if not nomi:

		for i in archivos:
			archivo = open(directorio+i,'r')
			header = archivo.readline()
			if header[0:22] == "HFOS111308DDJJ-NOMINAS":
				while True:
					linea =  archivo.readline()
					if linea[0:2] == "TF":
						break
					coma = ","
					guardar2 = open(directorio+'nomina7campos.csv','a')
					guardar2.write(linea[0:6]+','+linea[6:10]+','+linea[10:21]+','+linea[21:32]+','+linea[32:44]+','+linea[109:119]+','+linea[119:129]+'\n')
					guardar2.close
					archivo.close
def suma(directorio): #subsidio suma
	archivos = glob.glob("SUMA_OS*.txt")
	nomi = glob.glob("suma.csv")
	if not nomi:

		for i in archivos:
			archivo = open(directorio+i,'r')
			header = archivo.readline()
			if header[0:6] == "HFSUMA":
				while True:
					linea =  archivo.readline()
					if linea[0:2] == ' ':
						break
					coma = ","
					guardar2 = open(directorio+'suma.csv','a')
					guardar2.write(linea[0:6]+','+linea[6:12]+','+linea[12:19]+','+linea[19:34]+','+linea[34:49]+','+linea[49:64]+','+linea[64:79]+','+linea[79:94]+','+linea[94:110]+','+linea[110:125]+','+linea[125:151]+'\n')
					guardar2.close
					archivo.close					

def relaciones(directorio): 
	print directorio
	archivos = glob.glob("Relaciones_Laborales_*.txt")
	nomi = glob.glob("relaciones.csv")
	if not nomi:

		for i in archivos:
			archivo = open(directorio+i,'r')
			header = archivo.readline()
			if header[0:18] == "HFABTEMP-DGI111308":
				while True:
					linea =  archivo.readline()
					if linea[0:8] == "TFABTEMP":
						break
					coma = ","
					guardar2 = open(directorio+'relaciones.csv','a')
					guardar2.write(linea[0:11]+','+linea[11:22]+','+linea[22:77]+','+linea[77:87]+','+linea[87:97]+','+linea[97:103]+','+linea[103:123]+','+linea[123:133]+','+linea[133:134]+','+linea[134:139]+','+linea[139:159]+','+linea[159:169]+','+linea[169:170]+','+linea[170:175]+','+linea[175:178]+','+linea[178:180]+','+linea[180:182]+','+linea[182:184]+','+linea[184:189]+','+linea[189:199]+','+linea[199:200]+','+linea[200:208]+','+linea[208:210]+','+linea[210:221]+','+linea[221:222]+','+linea[222:227]+','+linea[227:233]+','+linea[233:237]+','+linea[237:247]+','+linea[247:251]+','+linea[251:252]+','+linea[252:300]+','+header[21:30]+'\n')
					guardar2.close
					archivo.close

def autogestion(directorio): #ddjj - nominas para obras sociales
 
	archivos = glob.glob("0*.txt")
	

	for i in archivos:
		archivo = open(directorio+i,'r')
		header = archivo.readline()
		if header[0:5] == "HFTEX":
			while True:
				linea =  archivo.readline()
				if linea[0:2] == "TF":
					break
				coma = ","
				guardar2 = open('autogestion.csv','a')
				guardar2.write(linea[0:4]+','+linea[4:13]+','+linea[13:23]+','+linea[23:33]+','+linea[33:35]+','+linea[35:50]+','+linea[50:54]+','+linea[54:69]+','+linea[69:70]+','+linea[70:76]+','+linea[76:85]+','+linea[85:93]+','+linea[93:123]+','+linea[123:173]+','+linea[173:273]+','+linea[273:323]+','+linea[323:1347]+','+linea[1347:1547]+','+linea[1547:1600]+','+header[22:30]+'\n')
				guardar2.close
				archivo.close
