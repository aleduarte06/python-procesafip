# -*- enconding: utf-8 -*-
#! /usr/bin/env python
import funciones
import os
def main():
	print "Eleija una opcion: "
	print "1) Nominatividad_mySQL"
	print "2) Nomina_mysql"
	print "3) Autogestion_mySQL"
	print "4) suma_mysql"
	print '#############################'
	print "8) Domicilio_mysql"
	print "9) Relaciones_mysql"
	print "\n0) Salir"
	
	opcion = input('>')

		
	if opcion == 1:
		print "Ingrese mes carga"
		mes_carga = raw_input('>')
		try:
			a=funciones.nominatividad_mysql(mes_carga)
		except Exception, e:
			print 'No es valido'
			print e
			main()	
		if a==1:
			print os.getcwd()
			main()							
	elif opcion == 2:
		print "Ingrese mes carga"
		mes_carga = raw_input('>')
		try:
			a=funciones.nomina_mysql(mes_carga)
		except Exception, e:
			print 'No es valido'
			print e
			main()
		if a==1:
			print os.getcwd()
			main()								
	elif opcion == 3:
		print "Ingrese mes carga"
		mes_carga = raw_input('>')
		try:
			a=funciones.autogestion_mysql(mes_carga)
		except Exception, e:
			print 'No es valido'
			print e
			main()
		if a==1:
			print os.getcwd()
			main()						
	elif opcion == 4:
		print "Ingrese mes carga"
		mes_carga = raw_input('>')
		try:
			a=funciones.suma_mysql(mes_carga)
		except Exception, e:
			print 'No es valido'
			print e
			main()					
		if a==1:
			print os.getcwd()
			main()				
	elif opcion == 8:
		print "Ingrese mes carga"
		mes_carga = raw_input('>')
		try:
			a=funciones.domicilio_mysql(mes_carga)
		except Exception, e:
			print 'No es valido'
			print e
			main()					
		if a==1:
			print os.getcwd()
			main()		
	elif opcion == 9:
		print "Ingrese mes carga"
		mes_carga = raw_input('>')
		try:
			a=funciones.relaciones_mysql(mes_carga)
		except Exception, e:
			print 'No es valido'
			print e
			main()					
		if a==1:
			print os.getcwd()
			main()
main()
