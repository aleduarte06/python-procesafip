import mysql.connector as mysql
import config

conexion = mysql.connect(user= config.user_a, password= config.passwd_a, host= config.host_a, db= config.db_a)
cursor = conexion.cursor()

def main():
	query = "SELECT* from altasbajas WHERE cuil = 20362689717"
	
	opcion = input('>')
	
	if opcion == 1:
		try:
			cursor.execute(query)
			a=cursor.fetchone()
		except Exception, e:
			print 'No es valido'
			print e 
			main()
	print  a<0
	return a<0

	
main()
		
