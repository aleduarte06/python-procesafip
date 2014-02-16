# -*- enconding: utf-8 -*-
import mysql.connector as mysql
import glob
import sys
import config as cn
import os
from datetime import datetime

def log(txt,i,mes_carga):
	
	ahora = datetime.now()
	fecha = str(ahora.month)+"-"+str(ahora.day)+"-"+str(ahora.year)
	hora = str(ahora.hour)+":"+str(ahora.minute)+":"+str(ahora.second)
	
	guardar = open('../../../log.txt','a')
	guardar.write('%s %s %s ,%s %s'%(txt,i,mes_carga,fecha,hora))
	guardar.close
def a(i,quincena,mes_carga):
	print os.getcwd()
	conexion = mysql.connect(user=cn.user_a, password=cn.passwd_a, host=cn.host_a, db=cn.db_a)
	cursor = conexion.cursor() 
	
	n=0
	archivo = open(i,'r')
	header = archivo.readline()
	if header[0:8] == "HFTRANSF":	
		while True:
			linea =  archivo.readline()
			if linea[0:2] == "TN":
				break
			try:
				query="""INSERT INTO afip_nominatividad (Renos,Concepto_Transf,Importe,Cred_Deb,Fecha_Transf,Fecha_Recauda,Cuit_Contribuyente,Periodo,Nro_Obligacion,Sec_Obligacion,Cuil_Aportante,Banco,Sucursal,Zona,Porcentaje_Reduccion,Porcentaje_Reduccion2,Porcentaje_Reduccion3,Grupo_Famliar,Tipo_Pago,Marca_Apropiacion,Mes_Carga,quincena) VALUES(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%s,%s)""" %(linea[0:4],linea[4:7],linea[7:22],linea[22:23],linea[23:33],linea[33:43],linea[43:54],linea[54:58],linea[58:70],linea[70:73],linea[73:84],linea[84:87],linea[87:90],linea[90:92],linea[92:94],linea[94:95],linea[95:96],linea[96:98],linea[98:99],linea[99:100],mes_carga,quincena)
			except Exception, e:
				print e

			cursor.execute(query)	
			conexion.commit()
			n+=1
			print '\r%s' % n,
			sys.stdout.flush()
			
    		

	txt="\n se han procesado  %s registros" %n		
	print txt 
	log(txt, i, mes_carga)
	archivo.close
	
	return 1
				

def b(i,quincena,mes_carga):
	conexion = mysql.connect(user=cn.user_a, password=cn.passwd_a, host=cn.host_a, db=cn.db_a)
	cursor = conexion.cursor()
	n=0
	archivo = open(i,'r')
	header = archivo.readline()
	if header[0:22] == "HFOS111308DDJJ-NOMINAS":
		while True:
			linea =  archivo.readline()
			if linea[0:2] == "TF":
				break
			try:
				query="""INSERT INTO afip_nomina (codosoc,periodo,cuit,cuil,remosimp,imposad,zona,grpfam,nogrpfam,secoblig,condcuil,sitcuil,actividades,modalidad,codsini,apadios,version,rem5,esposa,excosapo,indret,indexccon,fecpresent,fecproc,origrect,filler,remcont,release_ver,usofut,fecha_carga,quincena)VALUES(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',%s,%s)""" %(linea[0:6],linea[6:10],linea[10:21],linea[21:32],linea[32:44],linea[44:52],linea[52:54],linea[54:56],linea[56:58],linea[58:61],linea[61:63],linea[63:65],linea[65:68],linea[68:71],linea[71:73],linea[73:81],linea[81:83],linea[83:94],linea[94:95],linea[95:107],linea[107:108],linea[108:109],linea[109:119],linea[119:129],linea[129:130],linea[130:164],linea[164:175],linea[175:177],linea[177:200],mes_carga,quincena)
			except Exception, e:
				print e
			cursor.execute(query)
			conexion.commit()
			n+=1
			print '\r%s' % n,
			sys.stdout.flush()
	txt="\n se han procesado  %s registros" %n		
	print txt 
	log(txt, i, mes_carga)
	archivo.close
	
	return 1
	

def nominatividad_mysql(mes_carga):
	os.chdir('20%s'%mes_carga[2:4])	
	os.chdir(mes_carga[0:2])
	archivos = glob.glob("OS1113*.txt")
	for i in archivos:
		if i == "OS1113a.txt":
			quincena=1
		else:
			quincena=2	
		try:
			c=a(i, quincena, mes_carga)
		except Exception, e:
			print e	
	os.chdir('../../')
	return c				

				


def nomina_mysql(mes_carga):
	os.chdir('20%s'%mes_carga[2:4])	
	os.chdir(mes_carga[0:2])
	archivos = glob.glob("ddjjredu*.txt")
	for i in archivos:
		if i == "ddjjredua.txt":
			quincena=1
		else:
			quincena=2	
		try:
			a=b(i, quincena, mes_carga)
		except Exception, e:
			print e	
	os.chdir('../../')
	return a

def autogestion_mysql(mes_carga):	
		os.chdir('20%s'%mes_carga[2:4])
		os.chdir(mes_carga[0:2]) 
		print os.getcwd()
		conexion = mysql.connect(user=cn.user_a, password=cn.passwd_a, host=cn.host_a, db=cn.db_a)
		cursor = conexion.cursor()
		
		n=0
		archivos = glob.glob("0*.txt")
		for i in archivos:
			archivo = open(i,'r')
			header = archivo.readline()
			if header[0:5] == "HFTEX":
				while True:
					linea =  archivo.readline()
					if linea[0:2] == "TF":
						break
					query="""INSERT INTO `afip_autogestion` (`renos`, `nro_exp`, `fecha_proceso`, `fecha_tranf`, `cod_clas`,
					 `importe_exp`, `nro_cuota`, `importe`, `cred_deb`, `periodo`, `nro_exp_orig`, `cod_hospita`, `ref_externa`,
					  `obs`, `juzgado`, `secretaria`, `autos`, `detalle_fact`, `filler`, `fecha`)
					VALUES(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',
						\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',
						\'%s\')"""%(linea[0:4],linea[4:13],linea[13:23],linea[23:33], linea[33:35],linea[35:50],linea[50:54],
						linea[54:69], linea[69:70],linea[70:76],linea[76:85],linea[85:93], linea[93:123],linea[123:173],
						linea[173:273],linea[273:323], linea[323:1347],linea[1347:1547],linea[1547:1600],header[22:30]) 
				
					cursor.execute(query)
					conexion.commit()
					n+=1
					print '\r%s' % n,
					sys.stdout.flush()
		txt="\n se han procesado  %s registros" %n		
		print txt 
		log(txt, i, mes_carga)
		archivo.close
		os.chdir('../../')
		return 1
def suma_mysql(mes_carga):
	os.chdir('20%s'%mes_carga[2:4])
	os.chdir(mes_carga[0:2]) 		
	conexion = mysql.connect(user=cn.user_a, password=cn.passwd_a, host=cn.host_a, db=cn.db_a)
	cursor = conexion.cursor()
	
	n=0
	archivos = glob.glob("SUMA_OS*.txt")
	for i in archivos:
		archivo = open(i,'r')
		header = archivo.readline()
		if header[0:6] == "HFSUMA":
				linea =  archivo.readline()
				if linea[0:8] == "TFABTEMP":
					break
				query="""INSERT INTO `afip_suma` (`renos`, `periodo`, `cant_benef`, `importe_tranf`, `capita`, `art_2_inc_a`, 
					`art_2_inc_b`, `art_2_inc_c`, `art_3_ajuste`, `total_subsidio`, `area_reservada`)
				VALUES(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')""" %(linea[0:6],linea[6:12],linea[12:19],linea[19:34], linea[34:49],linea[49:64],linea[64:79],linea[79:94], linea[94:110],linea[110:125],linea[125:151]) 
				cursor.execute(query)
				conexion.commit()
				n+=1
				print '\r%s' % n,
				sys.stdout.flush()					
	print "\n se han procesado  %s registros" %n 			
	archivo.close
	os.chdir('../../')
def relaciones_mysql(mes_carga):
		os.chdir('20%s'%mes_carga[2:4])
		os.chdir(mes_carga[0:2])
		os.chdir('Relaciones Laborales') 
		print os.getcwd()
		conexion = mysql.connect(user=cn.user_a, password=cn.passwd_a, host=cn.host_a, db=cn.db_a)
		cursor = conexion.cursor()
		
		n=0
		archivos = glob.glob("Relaciones_Laborales_*.txt")
		for i in archivos:
			archivo = open(i,'r')
			header = archivo.readline()
			if header[0:18] == "HFABTEMP-DGI111308":
				while True:
					linea =  archivo.readline()
					if linea[0:8] == "TFABTEMP":
						break
					query="""INSERT INTO `afip_relaciones` (`cuit`, `cuil`, `apellido_nombre`, `fecha_inicio_relacion`, `fecha_fin_relacion`, `renos`, `clave_alta_registro`,
					 `fecha_clave_registro`, `separador`, `hora_clave_alta`, `clave_baja_registro`, `fecha_clave_baja`, `separor2`, `hora_clave_baja`, `codigo_contrato`, `marca_trabajador_agro`,
					  `regimen_aportes`, `codigo_sit_baja`, `filler1`, `fecha_mov`, `separador3`, `hora_mov`, `codigo_mov`, `rem_bruta`, `cod_modalidad_liq`, `cod_sucursal_exp`, `cod_actividad`,
					   `cod_puesto`, `fecha_telegrama_renuncia`, `filler2`, `marca_rectificacion`, `area_reservada`, `fecha`) VALUES(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',
					   \'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')""" %(linea[0:11],
					   linea[11:22],linea[22:77],linea[77:87],linea[87:97],linea[97:103],linea[103:123],linea[123:133],linea[133:134],linea[134:139],linea[139:159],linea[159:169],linea[169:170],linea[170:175],
					   linea[175:178],linea[178:180],linea[180:182],linea[182:184],linea[184:189],linea[189:199],linea[199:200],linea[200:208],linea[208:210],linea[210:221],linea[221:222],linea[222:227],
					   linea[227:233],linea[233:237],linea[237:247],linea[247:251],linea[251:252],linea[252:300],header[22:30])
				
					cursor.execute(query)
					conexion.commit()
					n+=1
					print '\r%s' % n,
					sys.stdout.flush()
		txt="\n se han procesado  %s registros" %n		
		print txt 
		log(txt, i, mes_carga)
		archivo.close
		os.chdir('../../../')
		return 1	
def domicilio_mysql(mes_carga):


	os.chdir('20%s'%mes_carga[2:4])
	os.chdir(mes_carga[0:2])
	d=os.listdir(os.getcwd())
	os.chdir('%s'%d[0]) 
	conexion = mysql.connect(user=cn.user_a, password=cn.passwd_a, host=cn.host_a, db=cn.db_a)
	cursor = conexion.cursor()
	
	n=0
	archivos = glob.glob("Domicilios_Explotacion*.txt")
	for i in archivos:
		archivo = open(i,'r')
		header = archivo.readline()
		if header[0] == 'H':
			while True:
				linea =  archivo.readline()
				if linea[0] == "T":
					break	
				query = 'INSERT INTO afip_domicilio(`cuit`, `cod_mov`, `tipo_externo`, `calle`, `nro`, `torre`, `bloque`, `piso`,`departamento`, `cp`, `localidad`, `provincia`, `sucursal`, `actividad`, `fecha_hora_mov`, `area_reservada`, fecha) VALUES(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')' %(linea[0:11],linea[11:13],linea[13:14],linea[14:74],linea[74:80],linea[80:85],linea[85:90],linea[90:95],linea[95:100],linea[100:108],linea[108:168],linea[168:170],linea[170:175],linea[175:181],linea[181:207],linea[207:250],header[9:17])
				cursor.execute(query)
				conexion.commit()
				n+=1
				print '\r%s' % n,
				sys.stdout.flush()
	txt="\n se han procesado  %s registros" %n		
	print txt 
	log(txt, i, mes_carga)
	archivo.close
	os.chdir('../../../')
	return 1	
