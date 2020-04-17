from tkinter import *
root=Tk()
root.title("simple calci")
num1=0
oper=0


def  clicked_b(numb):
    s1=e.get()
    e.delete(0,END)
    e.insert(0,str(s1)+str(numb))

def  clicked_c():
	e.delete(0,END)


def clicked_add(op):
    global num1 
    num1=int(op) 
    e.delete(0,END)	
    global oper
    oper=ord('+')

def clicked_sub(op):
    global num1 
    num1=int(op) 
    e.delete(0,END)	
    global oper
    oper=ord('-')

def clicked_mul(op):
    global num1 
    num1=int(op) 
    e.delete(0,END)	
    global oper
    oper=ord('*')

def clicked_div(op):
    global num1 
    num1=int(op) 
    e.delete(0,END)	
    global oper
    oper=ord('/')

def clicked_e(op1,opera):
	global num1
	a={43:'add',42:'mul',45:'sub',47:'div'}
	wrd=a[opera]
	sum=0
	if wrd=='add':
		sum=num1+int(op1)
	elif wrd=='sub':
		sum=num1-int(op1)
	elif wrd=='mul':
		sum=num1*int(op1)
	elif wrd=='div':
		sum=num1/int(op1)

	e.delete(0,END)
	e.insert(0,sum)
	num1=0

e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=15)
b1=Button(root,text='1',command=lambda:clicked_b(1),padx=35,pady=10,borderwidth=5)
b2=Button(root,text='2',command=lambda:clicked_b(2),padx=35,pady=10,borderwidth=5)
b3=Button(root,text='3',command=lambda:clicked_b(3),padx=35,pady=10,borderwidth=5)
b4=Button(root,text='4',command=lambda:clicked_b(4),padx=35,pady=10,borderwidth=5)
b5=Button(root,text='5',command=lambda:clicked_b(5),padx=35,pady=10,borderwidth=5)
b6=Button(root,text='6',command=lambda:clicked_b(6),padx=35,pady=10,borderwidth=5)
b7=Button(root,text='7',command=lambda:clicked_b(7),padx=35,pady=10,borderwidth=5)
b8=Button(root,text='8',command=lambda:clicked_b(8),padx=35,pady=10,borderwidth=5)
b9=Button(root,text='9',command=lambda:clicked_b(9),padx=35,pady=10,borderwidth=5)
b0=Button(root,text='0',command=lambda:clicked_b(0),padx=35,pady=10,borderwidth=5)
bc=Button(root,text='C',padx=35,command=clicked_c, pady=10,borderwidth=5)
ba=Button(root,text='+',padx=35,command=lambda:clicked_add(e.get()), pady=10,borderwidth=5)
bs=Button(root,text='-',command=lambda:clicked_sub(e.get()),padx=35,pady=10,borderwidth=5)
bm=Button(root,text='*',command=lambda:clicked_mul(e.get()),padx=35,pady=10,borderwidth=5)
bd=Button(root,text='/',command=lambda:clicked_div(e.get()),padx=35,pady=10,borderwidth=5)
be=Button(root,text='=',padx=175,command=lambda:clicked_e(e.get(),oper), pady=10,borderwidth=5)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b0.grid(row=4,column=0)
bs.grid(row=4,column=1)
bm.grid(row=4,column=2)
ba.grid(row=5,column=0)
bd.grid(row=5,column=1)
bc.grid(row=5,column=2)
be.grid(row=6,column=0,columnspan=3)

root.mainloop()