from Tkinter import *

def main():
	root = Tk()
	root.geometry("500x300+0+0") #Aca le decimos a tk que tenemos una ventana de 800 x 600
	root.title('formulario Update')
	# row 1 : Cuil
	cuil_label = Label(root,text="Cuil :")
	cuil_label.grid(row=1,column=1)
	cuil = IntVar()
	cuil_entry = Entry(root,textvariable=cuil)
	cuil_entry.grid(row=1,column=2)
	#row 2 : Alta baja
	mov_label= Label(root,text="alta/baja : ")
	mov_label.grid(row=2,column=1)
	mov = IntVar()
	mov_entry = Entry(root,textvariable=mov)
	mov_entry.grid(row=2,column=2)
	#row 3 : Fecha
	fecha_label = Label(root,text="Fecha : ")
	fecha_label.grid(row=3,column=1)
	fecha = StringVar()
	fecha_entry = Entry(root,textvariable=fecha)
	fecha_entry.grid(row=3,column=2)
	#row 4 : motivo
	motivo_label = Label(root,text="Motivo : ")
	motivo_label.grid(row=4,column=1)
	motivo = StringVar()
	motivo_entry = Entry(root,textvariable=motivo)
	motivo_entry.grid(row=4,column=2)
	#row 4 : motivo
	informar_label = Label(root,text="Informar sss : ")
	informar_label.grid(row=5,column=1)
	informar = IntVar()
	informar_entry = Entry(root,textvariable=informar)
	informar_entry.grid(row=5,column=2)
	
	#row 4 : boton update
	update = Button(root,text="Actualizar",relief=FLAT)
	update.grid(row=6,column=1)
	root.mainloop()

main()	