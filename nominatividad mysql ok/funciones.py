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
	
	guardar = open('../../log.txt','a')
	guardar.write('%s %s %s ,%s %s'%(txt,i,mes_carga,fecha,hora))
	guardar.close
def a(i,quincena,mes_carga):
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
		