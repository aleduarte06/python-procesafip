# -*- enconding: utf-8 -*-
#! /usr/bin/env python
import os
import funciones
actual = os.getcwd()

def main():
	print "Eleija una opcion: "
	print "1) Nominatividad"
	print "2) Autogestion"
	print "3) nomina ddjj"
	print "4) nomina ddjj solo 7 campos"
	print "5) suma"
	print "6) relaciones laborales"
	print "1) NominatividadSQL"
	print "\n0) Salir"
	print actual
	opcion = input('>')

	if opcion == 1:
		print "Ingrese el directorio"
		directorio = raw_input('>')
		print "Ingrese mes carga"
		mes_carga = raw_input('>')
		try:
			funciones.nominatividad(directorio,mes_carga)
		except Exception, e:
			print 'No es valido'
			main()
	elif opcion == 2:
		print "Ingrese el directorio"
		entrada = raw_input('>')
		try:
			funciones.autogestion(entrada)
		except Exception, e:
			print "No es valido"
			main()
	elif opcion == 3:
		print "Ingrese el directorio"
		entrada = raw_input('>')
		try:
			funciones.nomina(entrada)
		except Exception, e:
			print "No es valido"
			main()
	elif opcion == 4:
		print "Ingrese el directorio"
		entrada = raw_input('>')
		try:
			funciones.nomina2(entrada)
		except Exception, e:
			print "No es valido"
			main()

	elif opcion == 5:
		print "Ingrese el directorio"
		entrada = raw_input('>')
		try:
			funciones.suma(entrada)
		except Exception, e:
			print "No es valido"
			main()		
	elif opcion == 6:
		print "Ingrese el directorio"
		entrada = raw_input('>')
		try:
			funciones.relaciones(entrada)
		except Exception, e:
			print "No es valido"
			main()
	elif opcion == 7:
		print "Ingrese el directorio"
		directorio = raw_input('>')
		print "Ingrese mes carga"
		mes_carga = raw_input('>')
		try:
			funciones.nominatividadsql(directorio,mes_carga)
		except Exception, e:
			print 'No es valido'
			main()					

main()
