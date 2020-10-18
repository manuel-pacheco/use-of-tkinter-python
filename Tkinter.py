from tkinter import *

def crear(w):
	global canvas
	global root

	largo = 600
	alto = 300
	largo_s = 200
	abajo = 50
	margen = 50
	s= StringVar() 
	s.set(w)
	#crear ejes
	canvas.create_line(margen, margen, margen, alto + margen ,fill='black',width=3)
	canvas.create_line(margen,margen + alto , largo + margen , alto + margen, fill = 'Black' , width = 3)
	canvas.create_line(margen, margen,margen + 20, margen + 20 , fill = 'black' , width = 3)
	canvas.create_line(margen, margen,margen - 20, margen + 20 , fill = 'black' , width = 3)
	canvas.create_line(largo + margen , alto + margen,largo + margen -20, alto + margen-20 , fill='black' , width=3)
	canvas.create_line(largo + margen , alto + margen,largo + margen -20, alto + margen+20 , fill='black' , width=3)

	#Crear parte superior de los trapecios
	canvas.create_line(margen, margen+50,margen + 100,margen+50, fill ='blue', width  =3)
	canvas.create_line(margen+180,margen+50,margen+330,margen+50, fill = 'green', width  =3)
	canvas.create_line(margen+450,margen+50,margen+600,margen+50, fill = 'red', width = 3)

	#crear /
	canvas.create_line(margen + 120,margen+alto,margen+180,margen+50 , fill = 'green' , width = 3)
	canvas.create_line(margen + 350,margen+alto,margen+450,margen+50 , fill = 'red' , width = 3)

	#crear \
	canvas.create_line(margen + 100,margen+50,margen+180,margen+alto, fill ='blue' , width =3)	
	canvas.create_line(margen + 330,margen+50,margen+450,margen+alto, fill ='green' , width =3)

	#crear text
	canvas.create_text(margen + 620 ,margen + alto,fill="darkblue",font="Times 13 italic bold",text="T")
	canvas.create_text(margen + 600 ,margen + alto +10,fill="darkblue",font="Times 13 italic bold",text="60")
	canvas.create_text(margen + 450 ,margen + alto +10,fill="darkblue",font="Times 13 italic bold",text="45")
	canvas.create_text(margen + 350 ,margen + alto +10,fill="darkblue",font="Times 13 italic bold",text="35")
	canvas.create_text(margen + 330 ,margen + alto +10,fill="darkblue",font="Times 13 italic bold",text="33")
	canvas.create_text(margen + 180 ,margen + alto +10,fill="darkblue",font="Times 13 italic bold",text="18")
	canvas.create_text(margen + 120 ,margen + alto +10,fill="darkblue",font="Times 13 italic bold",text="12")
	canvas.create_text(margen + 100 ,margen + alto +10,fill="darkblue",font="Times 13 italic bold",text="10")
	canvas.create_text(margen + (w*10) ,margen + alto + 10,fill="darkred",font="Times 13 italic bold",text=s.get())
	canvas.create_text(margen,margen - 20,fill="darkblue",font="Times 13 italic bold",text="GP")
	canvas.create_text(margen - 10,margen + 50,fill="darkblue",font="Times 13 italic bold",text="1")

	#crear lineas verticales
	canvas.create_line(margen + 600,margen+alto,margen+600,margen, fill ='black' , width = 2,dash=(5,4))
	canvas.create_line(margen + 450,margen+alto,margen+450,margen, fill ='black' , width = 2,dash=(5,4))
	canvas.create_line(margen + 350,margen+alto,margen+350,margen, fill ='black' , width = 2,dash=(5,4))
	canvas.create_line(margen + 330,margen+alto,margen+330,margen, fill ='black' , width = 2,dash=(5,4))
	canvas.create_line(margen + 180,margen+alto,margen+180,margen, fill ='black' , width = 2,dash=(5,4))
	canvas.create_line(margen + 120,margen+alto,margen+120,margen, fill ='black' , width = 2,dash=(5,4))
	canvas.create_line(margen + 100,margen+alto,margen+100,margen, fill ='black' , width = 2,dash=(5,4))
	canvas.create_line(margen + (w*10),margen+alto,margen+(w*10),margen, fill ='orange' , width = 2,dash=(5,4))
def cerrar():
	root.destroy()

def botones():
	global root
	global entrada
	entrada = Entry(justify='center')
	entrada.place(x = 700 , y = 100)
	Label(root,text="Temperatura",fg="green",font="Times 20 italic bold").place(x = 700 , y = 50)
	Button(root,text='Calcular',command=main,fg="blue").place(x = 700, y = 330)
	Button(root,text='Cerrar',command=cerrar,fg="blue").place(x = 800, y = 330)

def operacion(Temperatura):
	global label1
	global label2
	global label3
	a = blue(Temperatura)
	b = green(Temperatura)
	c = red(Temperatura)
	label1=Label(root,text="GPbaja:        " + str(a),fg="black")
	label1.place(x = 700 , y = 150)
	label2=Label(root,text="GPbaja:        " + str(b),fg="black")
	label2.place(x = 700 , y = 200)
	label3=Label(root,text="GPbaja:        " + str(c),fg="black")
	label3.place(x = 700 , y = 250)
	print("GPbaja: "+ str(a))
	print("GPmedia: "+ str(b))
	print("GPalta: "+ str(c))
	return(Temperatura)

def blue(x):
	if(x>=0 and x<=10):
		GPbaja  = 1
	elif(x>10 and x<= 18):
		GPbaja = (9/4)-(x/8)
	else:
		GPbaja=0
	return(GPbaja)

def green(y):
	if(y>=0 and y<=12):
		GPmedia = 0
	elif(y>12 and y<=18):
		GPmedia = (y/6)-2
	elif(y>18 and y<=33):
		GPmedia = 1
	elif(y>33 and y<=45):
		GPmedia = (15/4)-(y/12)
	else:
		GPmedia = 0
	return(GPmedia)
	
def red(z):
	if(z>=0 and z<=35):
		GPalta = 0
	elif(z>35 and z<=45):
		GPalta = (z/10)-(7/2)
	else:
		GPalta = 1
	return(GPalta)

def main():
	global canvas
	global entrada
	canvas.delete("all")
	val = entrada.get()
	
	try:
		label1.pack(side="bottom")
		label2.pack(side="bottom")
		label3.pack(side="bottom")
		val = float(val)
		print(val)
		t = operacion(val)
		crear(t)
		
		
	except:
		print("Comienzo")
		crear(0)
		operacion(0)
	
if __name__ == '__main__':
	global canvas
	global root

	root = Tk()
	root.geometry("900x400")
	canvas = Canvas(width=700, height=400, bg='white')
	canvas.pack(expand=YES, fill=BOTH)
	botones()
	main()

	root.mainloop()
