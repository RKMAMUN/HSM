
from tkinter import *
from tkinter import ttk
import time
import datetime
from PIL import ImageTk,Image
import os
import sqlite3
from tkinter import messagebox
now = datetime.datetime.now()

#----------- importing sqlite for server side operations---------------------------------------------------------------------------------

con = sqlite3.Connection('hm_proj.db')
cursor = con.cursor()
cursor.execute("create table if not exists hoteld(t_r number,r_r number,t_s number)")
cursor.execute("create table if not exists roomd(rn number primary key,beds number,ac varchar(10),tv varchar(10),internet varchar(10),price number(10))")



#rstatus extra column
#for i in range (1,21):
#cur.execute("update roomd set tv='Yes' where rn = ? ",(19,))
cursor.execute("create table if not exists payments(id number primary key,dot varchar(15),time varchar(10),amt number,method varchar(10))")
cursor.execute("create table if not exists paymentsf(id number  primary key,f_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,day varchar,month varchar,year varchar,time varchar , method varchar,totalamt varchar)")

con.commit()

con.commit()
cursor.execute("select * from payments")
con.commit()
x = cursor.fetchall()
con.commit()

#-----------splash_screen------------------------------------------------------------------------------------------------------------------
sroot = Tk()
sroot.minsize(height=516, width=1150)
sroot.configure(bg='skyblue')
#chilanka
Label(sroot, text="Hostel Management System", font='Timesnewroman 44', bg='blue', fg='black').place(x=250, y=10)

#Label(sroot,text="9589861196",font='Timesnewroman 40',bg='white',fg='grey').place(x=535,y=450)
#----------- main project------------------------------------------------------------------------------------------------------------------


def mainroot():
	#sroot.destroy()
	root = Tk()
	root.geometry('1080x500')
	root.minsize(width=1080, height=550)
	root.maxsize(width=1080, height=550)
	root.configure(bg='white')
	root.title("Hostel Management System")

	#--------------seperator-------------------------------------------------------------------------------------------------------------------

	#sep = Frame(height=500,bd=1,relief='sunken',bg='white')
	#sep.place(x=20,y=0)
	#----------------Connection with printer-------------------------------------------------------------------------------------------------------------

	# def connectprinter():
	# 	os.startfile("C:/Users/TestFile.txt", "print")
	#---------------top frame------------------------------------------------------------------------------------------------------------------

	top_frame = Frame(root, height=70, width=1080, bg='skyblue')

	top_frame.place(x=0, y=0)
	tf_label = Label(top_frame, text='Hostel Management System', font='msserif 34', fg='black', bg='skyblue', height=70)
	tf_label.pack(anchor='center')
	top_frame.pack_propagate(False)

	#---------------DATE TIME------------------------------------------------------------------------------------------------------------------
	def datetime():
		#while(True):
		localtime = now.strftime("%Y-%m-%d %H:%M")
		#lblinfo = Label(top_frame, font='helvetica 16', text=localtime, bg='blue', fg='white')

		#lblInfo.place(x=333,y=40)

	#----------------bottom frame - hotel status and default page-------------------------------------------------------------------------------
	def hotel_status():
		global b_frame
		b_frame = Frame(root,height=400, width=1080, bg='gray91')
		b_frame.place(x=0, y=120+6+20+60+11)
		b_frame.pack_propagate(False)
		path = "images/newbackg6lf.jpg"
		img = ImageTk.PhotoImage(Image.open(path))
		label = Label(b_frame, image = img , height=400, width=1080)
		label.image = img
		label.place(x=0, y=0)
		cursor.execute("select * from hoteld")

		#print(x)
		cursor.execute("select count(rn) from roomd")
		x = cursor.fetchone()
		print(x)
		cursor.execute("select count(rn) from roomd where rstatus = 'Reserved'")
		y = cursor.fetchone()
		print(y)
		tor = x[0]
		rer = y[0]
		tos = 21
		avr = int(tor)-int(rer)
		avr = str(avr)


	# ------------inner frames of bottom frame-------------------------

		smf1 = Frame(b_frame, height=150, width=175, bg='white')
		tr = Label(smf1, text='Total Rooms:', fg='white', bg='cyan4', width=100, height=2, font='helvetica 16')
		tr.pack(side='top')
		smf1.pack_propagate(False)
		smf1.place(x=0, y=30)
		Label(smf1, text=tor, fg='cyan4', bg='white', font=('Helvetica', 45)).pack(anchor='center')

		smf2 = Frame(b_frame, height=150, width=175, bg='white')
		ar = Label(smf2, text='Available Rooms:', fg='white', bg='cyan4', width=130, height=2, font='helvetica 15')
		ar.pack(side='top')
		smf2.pack_propagate(False)
		smf2.place(x=180+4, y=30)
		Label(smf2, text=avr, fg='cyan4', bg='white', font=('Helvetica', 50)).pack(anchor='center')

		smf3 = Frame(b_frame, height=150, width=175, bg='white')
		tre = Label(smf3, text='Total reservations:', fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
		tre.pack(side='top')
		smf3.pack_propagate(False)
		smf3.place(x=360+6,y=30)
		Label(smf3,text=rer,fg='cyan4',bg='white',font=('Helvetica', 50)).pack(anchor='center')

		smf4 = Frame(b_frame,height=150,width=175,bg='white')
		tc = Label(smf4,text='Total Customers:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
		tc.pack(side='top')
		smf4.pack_propagate(False)
		smf4.place(x=540+8,y=30)
		Label(smf4,text='40',fg='cyan4',bg='white',font=('Helvetica', 50)).pack(anchor='center')

		smf5 = Frame(b_frame,height=150,width=175,bg='white')
		ts = Label(smf5,text='Total Staff:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
		ts.pack(side='top')
		smf5.pack_propagate(False)
		smf5.place(x=720+10, y=30)
		Label(smf5,text=tos, fg='cyan4', bg='white', font=('Helvetica', 50)).pack(anchor='center')
		redf1 = Frame(b_frame, height=8, width=1080, bg='cyan4')

		smf6 = Frame(b_frame, height=150, width=175, bg='white')
		ts = Label(smf6, text='Under renovation:', fg='white', bg='cyan4', width=130, height=2, font='helvetica 15')
		ts.pack(side='top')
		smf6.pack_propagate(False)
		smf6.place(x=915, y=30)
		Label(smf6, text='3', fg='cyan4', bg='white', font=('Helvetica', 50)).place(x=60, y=60)


		#Label(b_frame,text='==================================================================================',fg='cyan4').place(x=0,y=20)
		redf1.place(x=0, y=22)
		Label(b_frame, text='Hotel Status', font=('Helvetica', 12), bg='cyan4', fg='white').pack(anchor='center')
		redf1.pack_propagate(False)
		#b_frame.pack_propagate(False)



	#-------------- Guests --------------------------------------------------------------------------------------------------------------------------
	def staff():
		b_frame = Frame(root, height=400, width=1080, bg='white')
		path = "images/newbackg6lf.jpg"
		img = ImageTk.PhotoImage(Image.open(path))
		label = Label(b_frame, image = img , height=400, width=1080)
		label.image = img
		label.place(x=0, y=0)


		emp1f = Frame(b_frame)
		path1 = "images/newman.jpg"
		img1 = ImageTk.PhotoImage(Image.open(path1))
		emp1 = Label(emp1f, image = img1)
		emp1.image = img1
		emp1.pack()
		emp1f.place(x=0,y=0)
		emp1inf = Frame(b_frame,bg='White',height=122,width=300)
		Label(emp1inf,text="Manager",bg='white',font='msserif 18 bold').place(x=60,y=0)
		Label(emp1inf,text="Mr. Walter Gomez",bg='white',fg="Grey",font='msserif 10').place(x=60,y=37)
		Label(emp1inf,text="Extention : 020",bg='white',fg="Grey",font='msserif 11').place(x=60,y=59)
		Label(emp1inf,text="Mail : walter@gmail.com",bg='white',fg="Grey",font='msserif 10').place(x=60,y=83)
		emp1inf.pack_propagate(False)
		emp1inf.place(x=117,y=1)

		emp1f = Frame(b_frame)
		path2 = "images/recepnew.jpg"
		img2 = ImageTk.PhotoImage(Image.open(path2))
		emp1 = Label(emp1f,image = img2)
		emp1.image=img2
		emp1.pack()
		emp1f.place(x=657,y=0)
		emp1inf = Frame(b_frame,bg='White',height=116,width=310)
		Label(emp1inf,text="Customer Executive",bg='white',font='msserif 16 bold').place(x=45,y=0)#pack(side='top')
		Label(emp1inf,text="Ms. Cindy Camilly",bg='white',fg="Grey",font='msserif 10').place(x=45,y=37)
		Label(emp1inf,text="Extention : 030",bg='white',fg="Grey",font='msserif 10').place(x=45,y=59)
		Label(emp1inf,text="Mail : cindy@gmail.com",bg='white',fg="Grey",font='msserif 10').place(x=45,y=83)
		emp1inf.pack_propagate(False)
		emp1inf.place(x=767,y=2)

		emp1f = Frame(b_frame)
		path3 = "images/fchefnew.jpg"
		img3 = ImageTk.PhotoImage(Image.open(path3))
		emp1 = Label(emp1f,image = img3)
		emp1.image=img3
		emp1.pack()
		emp1f.place(x=0,y=152)
		emp1inf = Frame(b_frame,bg='White',height=121,width=320)
		Label(emp1inf,text="Restaurant",bg='white',font='msserif 17 bold').place(x=72,y=0)#pack(side='top')
		Label(emp1inf,text="Mr. Kim Jung",bg='white',fg="Grey",font='msserif 10').place(x=72,y=37)
		Label(emp1inf,text="Extention : 048",bg='white',fg="Grey",font='msserif 10').place(x=72,y=59)
		Label(emp1inf,text="Mail : kim@gmail.com",bg='white',fg="Grey",font='msserif 10').place(x=72,y=83)
		emp1inf.pack_propagate(False)
		emp1inf.place(x=99,y=153)
		emp1inf.tkraise()

		emp1f = Frame(b_frame)
		path4 = "images/roomservicenew.jpg"
		img4 = ImageTk.PhotoImage(Image.open(path4))
		emp1 = Label(emp1f,image = img4)
		emp1.image = img4
		emp1.pack()
		emp1f.place(x=657, y=152)
		emp1inf = Frame(b_frame,bg='White',height=124,width=315)
		Label(emp1inf,text="Room Service",bg='white',font='msserif 17 bold').place(x=55,y=0)#pack(side='top')
		Label(emp1inf,text="Ms. Juan cordovus",bg='white',fg="Grey",font='msserif 10').place(x=55,y=37)
		Label(emp1inf,text="Extention : 040",bg='white',fg="Grey",font='msserif 10').place(x=55,y=59)
		Label(emp1inf,text="Mail : juan@gmail.com",bg='white',fg="Grey",font='msserif 10').place(x=55,y=83)
		emp1inf.pack_propagate(False)
		emp1inf.place(x=763,y=153)

		Frame(b_frame,height=13,width=250,bg='white').place(x=410,y=2)
		Frame(b_frame,height=13,width=250,bg='white').place(x=410,y=153)
		#Frame(b_frame,height=180,width=13,bg='white').place(x=406,y=20)



		b_frame.place(x=0,y=120+6+20+60+11)
		b_frame.pack_propagate(False)
		b_frame.tkraise()


	#-------------- rooms --------------------------------------------------------------------------------------------------------------------------
	def rooms():
		b_frame = Frame(root,height=400,width=1080,bg='gray91')
		b_frame.place(x=0,y=120+6+20+60+11)
		b_frame.pack_propagate(False)
		b_frame.tkraise()
		path = "images/newbackg6lf.jpg"
		img = ImageTk.PhotoImage(Image.open(path))
		label = Label(b_frame,image = img ,height=400,width=1080)
		label.image=img
		label.place(x=0,y=0)
		sidebuttons = Text(b_frame,width=1,height=19)
		sc = Scrollbar(b_frame,command=sidebuttons.yview,width=10,bg='lightsteelblue3')
		sidebuttons.configure(yscrollcommand=sc.set)
		sc.pack(side='left',fill=Y)
		sidebuttons.place(x=10,y=0)
		def roomdet(rno):
			Label(b_frame,text='Room %s'% rno,font=('Helvetica', 15),fg='white',bg='cyan4',width=10).place(x=535,y=0)
			cursor.execute("select * from roomd where rn = ?",(rno,))
			rdata=cursor.fetchall()
			#print (rdata)
			smf1 = Frame(b_frame,height=120,width=145,bg='white')
			hline = Frame(b_frame,height=10,width=960,bg='cyan4')
			hline.place(x=122,y=27)
			vline = Frame(b_frame,height=400,width=7,bg='lightsteelblue3')
			vline.place(x=122,y=0) 
			tr = Label(smf1,text='Total Bed(s):',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
			tr.pack(side='top')
			smf1.pack_propagate(False)
			smf1.place(x=129+3,y=30)
			Label(smf1,text=str(rdata[0][1]),fg='cyan4',bg='white',font='msserif 36').pack()
			smf2 = Frame(b_frame,height=120,width=145,bg='white')
			tr = Label(smf2,text='AC Available?',fg='white',bg='cyan4',width=100,height=2,font='msserif 16')
			tr.pack(side='top')
			smf2.pack_propagate(False)
			smf2.place(x=140*2+5+3*2,y=30)
			Label(smf2,text=str(rdata[0][2]),fg='cyan4',bg='white',font='msserif 35').pack()
			smf2 = Frame(b_frame,height=120,width=145,bg='white')
			tr = Label(smf2,text='TV Available?',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
			tr.pack(side='top')
			smf2.pack_propagate(False)
			smf2.place(x=140*3+12+5*2+3*3,y=30)
			Label(smf2,text=str(rdata[0][3]),fg='cyan4',bg='white',font=('Helvetica', 35)).pack()
			smf2 = Frame(b_frame,height=120,width=145,bg='white')
			tr = Label(smf2,text='  Wifi ?',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
			tr.pack(side='top')
			smf2.pack_propagate(False)
			smf2.place(x=140*4+12*2+5*3+3*4,y=30)
			Label(smf2,text=str(rdata[0][4]),fg='cyan4',bg='white',font='msserif 35').pack()
			smf2 = Frame(b_frame,height=120,width=145,bg='white')
			tr = Label(smf2,text=' Price ?',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
			tr.pack(side='top')
			smf2.pack_propagate(False)
			smf2.place(x=140*5+12*3+5*4+3*5,y=30)
			Label(smf2,text=str(rdata[0][5]),fg='cyan4',bg='white',font='msserif 35').pack()
			smf2 = Frame(b_frame,height=120,width=145,bg='white')
			tr = Label(smf2,text='Reserved ?',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
			tr.pack(side='top')
			#print (rdata)
			smf2.pack_propagate(False)
			smf2.place(x=140*6+12*4+5*5+3*6,y=30)
			p=''
			if rdata[0][6]=='Unreserved':
				p = 'No'
			else :
				p = 'Yes'
			Label(smf2,text=p,fg='cyan4',bg='white',font='msserif 35').pack()

		roomdet(1)


		sidebuttons.configure(state='disabled')
		'''loop approach will fail when we connect database with button that's why itni mehnat'''
		b1  = Button(b_frame,font='mssherif 10', text="Room 1", bg='white',fg='cyan4',width=10,command=lambda:roomdet(1))
		b2  = Button(b_frame,font='mssherif 10', text="Room 2", bg='white',fg='cyan4',width=10,command=lambda:roomdet(2))
		b3  = Button(b_frame,font='mssherif 10', text="Room 3", bg='white',fg='cyan4',width=10,command=lambda:roomdet(3))
		b4  = Button(b_frame,font='mssherif 10', text="Room 4", bg='white',fg='cyan4',width=10,command=lambda:roomdet(4))
		b5  = Button(b_frame,font='mssherif 10', text="Room 5", bg='white',fg='cyan4',width=10,command=lambda:roomdet(5))
		b6  = Button(b_frame,font='mssherif 10', text="Room 6", bg='white',fg='cyan4',width=10,command=lambda:roomdet(6))
		b7  = Button(b_frame,font='mssherif 10', text="Room 7", bg='white',fg='cyan4',width=10,command=lambda:roomdet(7))
		b8  = Button(b_frame,font='mssherif 10', text="Room 8", bg='white',fg='cyan4',width=10,command=lambda:roomdet(8))
		b9  = Button(b_frame,font='mssherif 10', text="Room 9", bg='white',fg='cyan4',width=10,command=lambda:roomdet(9))
		b10 = Button(b_frame,font='mssherif 10', text="Room 10",bg='white',fg='cyan4',width=10,command=lambda:roomdet(10))
		b11 = Button(b_frame,font='mssherif 10', text="Room 11",bg='white',fg='cyan4',width=10,command=lambda:roomdet(11))
		b12 = Button(b_frame,font='mssherif 10', text="Room 12",bg='white',fg='cyan4',width=10,command=lambda:roomdet(12))
		b13 = Button(b_frame,font='mssherif 10', text="Room 13",bg='white',fg='cyan4',width=10,command=lambda:roomdet(13))
		b14 = Button(b_frame,font='mssherif 10', text="Room 14",bg='white',fg='cyan4',width=10,command=lambda:roomdet(14))
		b15 = Button(b_frame,font='mssherif 10', text="Room 15",bg='white',fg='cyan4',width=10,command=lambda:roomdet(15))
		b16 = Button(b_frame,font='mssherif 10', text="Room 16",bg='white',fg='cyan4',width=10,command=lambda:roomdet(16))
		b17 = Button(b_frame,font='mssherif 10', text="Room 17",bg='white',fg='cyan4',width=10,command=lambda:roomdet(17))
		b18 = Button(b_frame,font='mssherif 10', text="Room 18",bg='white',fg='cyan4',width=10,command=lambda:roomdet(18))
		b19 = Button(b_frame,font='mssherif 10', text="Room 19",bg='white',fg='cyan4',width=10,command=lambda:roomdet(19))
		b20 = Button(b_frame,font='mssherif 10', text="Room 20",bg='white',fg='cyan4',width=10,command=lambda:roomdet(20))
		sidebuttons.window_create("end",window=b1)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b2)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b3)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b4)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b5)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b6)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b7)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b8)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b9)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b10)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b11)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b12)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b13)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b14)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b15)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b16)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b17)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b18)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b19)
		sidebuttons.insert("end","\n")
		sidebuttons.window_create("end",window=b20)

	#--------------- payments-----------------------------------------------------------------------------------------------------------------------

	def payments():
		b_frame = Frame(root,height=400,width=1080,bg='gray89')
		path = "images/newbackg6lf.jpg"
		img = ImageTk.PhotoImage(Image.open(path))
		label = Label(b_frame,image = img ,height=400,width=1080)
		label.image=img
		label.place(x=0,y=0)
		l = Label(b_frame,text='Please Enter The Unique Payment ID',font='msserif 15',bg='cyan4',fg='white')
		l.place(x=245,y=0)
		b_frame.place(x=0,y=120+6+20+60+11)
		b_frame.pack_propagate(False)
		b_frame.tkraise()
		hline = Frame(b_frame,height=42,width=1080,bg='cyan4')
		hline.place(x=0,y=23)
		ef = Frame(hline)
		p_id = Entry(ef)
		p_id.pack(ipadx=25,ipady=3)
		ef.place(x=308,y=6)

		fl1 = Frame(b_frame,height=38, width=308, bg='cyan4')
		fl1.place(x=0, y=68)
		l1 = Label(fl1,text='Transact Date', bg='cyan4', fg='white', font=('Helvetica', 16))
		l1.pack()
		fl1.pack_propagate(False)

		fr1 = Frame(b_frame,height=38,width=1080-308,bg='white')
		fr1.place(x=0+308,y=68)

		fr1.pack_propagate(False)

		fl2=Frame(b_frame,height=38,width=308,bg='cyan4')
		fl2.place(x=0,y=109)
		fl2.pack_propagate(False)

		l1.pack()
		
		fr2=Frame(b_frame,height=38,width=1080-308,bg='white')
		fr2.place(x=0+308,y=109)
		fr2.pack_propagate(False)

		
		fl3=Frame(b_frame,height=38,width=308,bg='cyan4')
		fl3.place(x=0,y=150)
		fl3.pack_propagate(False)
		l1=Label(fl3,text='Amount Paid',bg='cyan4',fg='white',font='msserif 17')
		l1.pack()
		
		fr3=Frame(b_frame,height=38,width=1080-308,bg='white')
		fr3.place(x=0+308,y=150)
		fr3.pack_propagate(False)

		
		fl4=Frame(b_frame,height=38,width=308,bg='cyan4')
		fl4.place(x=0,y=191)
		fl4.pack_propagate(False)
		l1=Label(fl4,text='Payment Method',bg='cyan4',fg='white',font='msserif 17')
		l1.pack()
		
		fr4=Frame(b_frame,height=38,width=1080-308,bg='white')
		fr4.place(x=0+308,y=191)
		fr4.pack_propagate(False)

		def getid(event=None):
			fl1=Frame(b_frame,height=38,width=308,bg='cyan4')
			fl1.place(x=0,y=68)
			l1=Label(fl1,text='Transact Date',bg='cyan4',fg='white',font=('Helvetica', 16))
			l1.pack()
			fl1.pack_propagate(False)

			fr1=Frame(b_frame,height=38,width=1080-308,bg='white')
			fr1.place(x=0+308,y=68)

			fr1.pack_propagate(False)

			fl2=Frame(b_frame,height=38,width=308,bg='cyan4')
			fl2.place(x=0,y=109)
			fl2.pack_propagate(False)
			l1=Label(fl2,text='Transact Time',bg='cyan4',fg='white',font=('Helvetica', 16))
			l1.pack()
		
			fr2=Frame(b_frame,height=38,width=1080-308,bg='white')
			fr2.place(x=0+308,y=109)
			fr2.pack_propagate(False)

		
			fl3=Frame(b_frame,height=38,width=308,bg='cyan4')
			fl3.place(x=0,y=150)
			fl3.pack_propagate(False)
			l1=Label(fl3,text='Amount Paid',bg='cyan4',fg='white',font=('Helvetica', 16))
			l1.pack()
		
			fr3=Frame(b_frame,height=38,width=1080-308,bg='white')
			fr3.place(x=0+308,y=150)
			fr3.pack_propagate(False)
			l1=Label(fl1,text='Transact Date',bg='cyan4',fg='white',font=('Helvetica', 16))
		#l1.pack()
		
			fl4=Frame(b_frame,height=38,width=308,bg='cyan4')
			fl4.place(x=0,y=191)
			fl4.pack_propagate(False)
			l1=Label(fl4,text='Payment Method',bg='cyan4',fg='white',font='msserif 17')
			l1.pack()
		
			fr4=Frame(b_frame,height=38,width=1080-308,bg='white')
			fr4.place(x=0+308,y=191)
			fr4.pack_propagate(False)
			l1=Label(fl1,text='Transaction Date',bg='cyan4',fg='white',font='msserif 17')
			idd = p_id.get()




	#cur.execute("create table if not exists paymentsf(id number  primary key,f_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,day varchar,month varchar,year varchar,time varchar , method varchar,totalamt varchar)")
			cursor.execute("select * from payments where id = ?",(idd,))
			x = cursor.fetchall()
			#print(x)
			cursor.execute("select day,month,year,time,totalamt,r_n from paymentsf where id = ?",(idd,))
			yy = cursor.fetchone()
			print (yy)
			#print (x)
			if(yy!=None):
				dot = yy[0]+'-'+yy[1]+'-'+yy[2]
				tot = yy[3]
				ap = yy[4]
				pm = '--'
				lbl1 = Label(fr1, text=dot, height=38,width=1080-308, font='msserif 15',bg='white',fg='cyan4').pack()
				lbl2 = Label(fr2, text=tot, height=38,width=1080-308, font='msserif 15',bg='white',fg='cyan4').pack()
				lbl3 = Label(fr3, text=ap, height=38,width=1080-308, font='msserif 15',bg='white',fg='cyan4').pack()
				lbl4 = Label(fr4, text=pm, height=38,width=1080-308, font='msserif 15',bg='white',fg='cyan4').pack()
			else:
				lbl1 = Label(fr1, text='No Information Available',height=38, width=1080-308,font='msserif 15',bg='white',fg='cyan4').pack()
				lbl1 = Label(fr2, text='No Information Available',height=38, width=1080-308,font='msserif 15',bg='white',fg='cyan4').pack()
				lbl1 = Label(fr3, text='No Information Available',height=38, width=1080-308,font='msserif 15',bg='white',fg='cyan4').pack()
				lbl1 = Label(fr4, text='No Information Available',height=38, width=1080-308,font='msserif 15',bg='white',fg='cyan4').pack()
		ok = Button(hline,text='OK',font='msserif 10',bg='white', activebackground='steelblue',fg='cyan4', command=getid)
		ok.place(x=530,y=5)
		p_id.bind('<Return>',getid)
		def pr():
			messagebox.askyesno("Print","Do you want to print Reciept")








	#---------------reserve------------------------------------------------------------------------------------------------------------------------

	def reserve():
		b_frame = Frame(root,height=420,width=1080,bg='gray89')
		path = "images/newbackg6lf.jpg"
		img = ImageTk.PhotoImage(Image.open(path))
		label = Label(b_frame,image = img ,height=420,width=1080)
		label.image=img
		label.place(x=0,y=0)
		

		vline = Frame(b_frame,height=400,width=7,bg='lightsteelblue3')
		vline.place(x=700,y=0) 

		Label(b_frame,text='Personal Information',font='msserif 15',bg='gray93').place(x=225,y=0)

		fnf = Frame(b_frame,height=1,width=1)
		first_name = Entry(fnf)
		
		mnf = Frame(b_frame,height=1,width=1)
		middle_name = Entry(mnf)

		lnf = Frame(b_frame,height=1,width=1)
		last_name = Entry(lnf)

		first_name.insert(0, 'First Name *')
		middle_name.insert(0, 'Middle Name')
		last_name.insert(0, 'Last Name *')

		
		def on_entry_click1(event):
			if first_name.get() == 'First Name *' :
				first_name.delete(0,END)
				first_name.insert(0,'')
		def on_entry_click2(event):
			if middle_name.get() == 'Middle Name' :
				middle_name.delete(0,END)
				middle_name.insert(0,'')
		def on_entry_click3(event):
			if last_name.get() == 'Last Name *' :
				last_name.delete(0,END)
				last_name.insert(0,'')
		def on_exit1(event):
			if first_name.get()=='':
				first_name.insert(0,'First Name *')
		def on_exit2(event):
			if middle_name.get()=='':
				middle_name.insert(0,'Middle Name')
		def on_exit3(event):
			if last_name.get()=='':
				last_name.insert(0,'Last Name *')

		first_name.bind('<FocusIn>', on_entry_click1)
		middle_name.bind('<FocusIn>', on_entry_click2)
		last_name.bind('<FocusIn>', on_entry_click3)
		first_name.bind('<FocusOut>',on_exit1)
		middle_name.bind('<FocusOut>',on_exit2)
		last_name.bind('<FocusOut>',on_exit3)

		first_name.pack(ipady=4,ipadx=15)
		middle_name.pack(ipady=4,ipadx=15)
		last_name.pack(ipady=4,ipadx=15)
		fnf.place(x=20,y=42)
		mnf.place(x=235,y=42)
		lnf.place(x=450,y=42)

		Label(b_frame,text='Contact Information',font='msserif 15',bg='gray93').place(x=225,y=90)

		cnf = Frame(b_frame,height=1,width=1)
		contct_number = Entry(cnf)
		
		emf = Frame(b_frame,height=1,width=1)
		email = Entry(emf)

		adf = Frame(b_frame,height=1,width=1)
		address = Entry(adf)

		contct_number.insert(0, 'Contact Number *')
		email.insert(0, 'Email *')
		address.insert(0, "Guest's Address *")
		
		def on_entry_click4(event):
			if contct_number.get() == 'Contact Number *' :
				contct_number.delete(0,END)
				contct_number.insert(0,'')
		def on_entry_click5(event):
			if email.get() == 'Email *' :
				email.delete(0,END)
				email.insert(0,'')
		def on_entry_click6(event):
			if address.get() == "Guest's Address *" :
				address.delete(0,END)
				address.insert(0,'')
		def on_exit4(event):
			if contct_number.get()=='':
				contct_number.insert(0,'Contact Number *')
		def on_exit5(event):
			if email.get()=='':
				email.insert(0,'Email *')
		def on_exit6(event):
			if address.get()=='':
				address.insert(0,"Guest's Address *")

		contct_number.bind('<FocusIn>', on_entry_click4)
		email.bind('<FocusIn>', on_entry_click5)
		address.bind('<FocusIn>', on_entry_click6)
		contct_number.bind('<FocusOut>',on_exit4)
		email.bind('<FocusOut>',on_exit5)
		address.bind('<FocusOut>',on_exit6)

		contct_number.pack(ipady=4,ipadx=15)
		email.pack(ipady=4,ipadx=15)
		address.pack(ipady=4,ipadx=15)
		cnf.place(x=20,y=130)
		emf.place(x=235,y=130)
		adf.place(x=450,y=130)


		Label(b_frame,text='Reservation Information',font='msserif 15',bg='gray93').place(x=210,y=175)
		
		nocf = Frame(b_frame,height=1,width=1)
		no_of_child = Entry(nocf)
		
		noaf = Frame(b_frame,height=1,width=1)
		no_of_adult = Entry(noaf)

		nodf = Frame(b_frame,height=1,width=1)
		no_of_day = Entry(nodf)

		no_of_child.insert(0, 'Number of Children *')
		no_of_adult.insert(0, 'Number of Adults *')
		no_of_day.insert(0, 'Number of Days of Stay *')
		
		def on_entry_click7(event):
			if no_of_child.get() == 'Number of Children *' :
				no_of_child.delete(0,END)
				no_of_child.insert(0,'')
		def on_entry_click8(event):
			if no_of_adult.get() == 'Number of Adults *' :
				no_of_adult.delete(0,END)
				no_of_adult.insert(0,'')
		def on_entry_click9(event):
			if no_of_day.get() == 'Number of Days of Stay *' :
				no_of_day.delete(0,END)
				no_of_day.insert(0,'')
		def on_exit7(event):
			if no_of_child.get()=='':
				no_of_child.insert(0,'Number of Children *')
		def on_exit8(event):
			if no_of_adult.get()=='':
				no_of_adult.insert(0,'Number of Adults *')
		def on_exit9(event):
			if no_of_day.get()=='':
				no_of_day.insert(0,'Number of Days of Stay *')

		no_of_child.bind('<FocusIn>', on_entry_click7)
		no_of_adult.bind('<FocusIn>', on_entry_click8)
		no_of_day.bind('<FocusIn>', on_entry_click9)
		no_of_child.bind('<FocusOut>',on_exit7)
		no_of_adult.bind('<FocusOut>',on_exit8)
		no_of_day.bind('<FocusOut>',on_exit9)

		no_of_child.pack(ipady=4,ipadx=15)
		no_of_adult.pack(ipady=4,ipadx=15)
		no_of_day.pack(ipady=4,ipadx=15)
		nocf.place(x=20,y=220)
		noaf.place(x=235,y=220)
		nodf.place(x=450,y=220)
		
		roomnf = Frame(b_frame,height=1,width=1)
		room_number = Entry(roomnf)
		room_number.insert(0, 'Enter Room Number *')
		def on_entry_click10(event):
			if room_number.get() == 'Enter Room Number *' :
				room_number.delete(0,END)
				room_number.insert(0,'')
		def on_exit10(event):
			if room_number.get()=='':
				room_number.insert(0,'Enter Room Number *')
		room_number.bind('<FocusIn>', on_entry_click10)
		room_number.bind('<FocusOut>',on_exit10)
		room_number.pack(ipady=4,ipadx=15)
		roomnf.place(x=20,y=270)

		pmethod = IntVar()
		def booking():
			if first_name.get() == 'First Name' or last_name.get() == 'Last Name' or contct_number.get() == 'Contact Number *' or email.get() == 'Email' or address.get() == "Guest's Address" or no_of_child.get() == 'Number of Children' or no_of_adult.get() == 'Number of Adults' or no_of_day.get() == 'Number of Days of Stay' or room_number.get() == 'Enter Room Number':
				messagebox.showinfo('Incomplete','Fill All the Fields marked by *')
			elif first_name.get() == '' or last_name.get() == '' or contct_number.get() == '' or email.get() == '' or address.get() == "" or no_of_child.get() == '' or no_of_adult.get() == '' or no_of_day.get() == '' or room_number.get() == '':
				messagebox.showinfo('Incomplete','Fill All the Fields marked by *')
	#cur.execute("create table if not exists paymentsf(id number  primary key,f_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,day varchar,month varchar,year varchar,time varchar , method varchar)")
			else :
				cursor.execute("select rstatus from roomd where rn = ?",(room_number.get(),))
				temp = cursor.fetchone()
				if temp[0] == 'Reserved':
					messagebox.showwarning('Room is Reserved','Room number '+str(room_number.get())+' is Reserved')
				else:
					payroot = Tk()
					payroot.title("Payment")
					payroot.minsize(height=236,width=302)
					payroot.configure(bg='White')
					#global pmethod
					cursor.execute("select price from roomd where rn = (?)",(room_number.get(),))
					rp = cursor.fetchone()
					print (rp)
					amtpd = str(int(rp[0])*int(no_of_day.get()))
					Label(payroot,text='Select an option to pay '+str(int(rp[0])*int(no_of_day.get())),font='msserif 14 bold',bg='White').place(x=0,y=0)
					Frame(payroot,height=4,width=300,bg='cyan4').place(x=0,y=39)
					Radiobutton(payroot,text='Cash  ',bg='White',variable=pmethod,value=1,font='helvetica 15',width=5).place(x=0,y=43+10)
					Radiobutton(payroot,text='Card   ',bg='White',variable=pmethod,value=2,font='helvetica 15',width=5).place(x=0,y=80+10)
					Radiobutton(payroot,text='UPI     ',bg='White',variable=pmethod,value=3,font='helvetica 15',width=5).place(x=0,y=115+10)
					Radiobutton(payroot,text='Paytm ',bg='White',variable=pmethod,value=4,font='helvetica 15',width=5).place(x=0,y=150+10)
					
					def f():
						if pmethod != '':
							print (pmethod.get())
							print ('pmethod value')
							cursor.execute("select id from paymentsf order by id desc")
							x = cursor.fetchone()
							cid = int(x[0])
							cid+=1

							#print (pmethod.get())
							#cur.execute("create table if not exists paymentsf(id number  primary key,f_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,day varchar,month varchar,year varchar,time varchar , method varchar,totalamt varchar)")
							cursor.execute("insert into paymentsf values(?,?,?,?,?,?,?,?,?,?,?,?)",(cid,first_name.get(),last_name.get(),contct_number.get(),email.get(),room_number.get(),str(now.strftime("%d")),str(now.strftime("%b")),str(now.strftime("%Y")),str(now.strftime("%H:%M")),str(pmethod.get()),amtpd))
							cursor.execute("update roomd set rstatus='Reserved' where rn = ? ",(room_number.get(),))
							messagebox.showinfo("Successful","Room Booked successfully")
							con.commit()
							ask = messagebox.askyesno("Successful","Payment Successful\nDo you want to print reciept ?")
							if ask == 'yes':
								def createfile():
									fl = open("reciept.txt","w")
									fl.write("reciept will come here")
							reserve()
							payroot.destroy()
						else :
							messagebox.showwarning("Not selected","Please Select the payment method")
					Button(payroot,text='Pay',font='msserif 12',bg='Green',fg='White',width=28,command=f).place(x=0,y=200)
					Label(payroot,text='Your unique payment id :',font='msserif',bg='White')#.place(x=0,y=25)
					
		def unreserve():
			if (room_number.get() == 'Enter Room Number') or (room_number.get()==''):
				messagebox.showerror('Entries not filled','Kindly Enter room Number')
			else :
				cursor.execute("update roomd set rstatus='Unreserved' where rn = ? ",(room_number.get(),))
				messagebox.showinfo("Successful","Room Unreserved successfully")
				reserve()
				con.commit()
		#--------------------------------------------------------right side---------------------------------------------------
		Label(b_frame,text='Filter',font='msserif 20',bg='gray93').place(x=850,y=0)

		nbb = IntVar()
		acb = IntVar()
		tvb = IntVar()
		wifib = IntVar()

		style = ttk.Style()
		style.map('TCombobox', fieldbackground=[('readonly', 'white')])
		Label(b_frame, text='Bed(s) :', bg='gray93', font='17').place(x=730, y=50)
		#Radiobutton(b_frame,text='1',bg='gray93',variable=nbb,value=1,font='15',width=3).place(x=800,y=50)
		#Radiobutton(b_frame,text='2',bg='gray93',variable=nbb,value=2,font='15',width=3).place(x=880,y=50)
		#Radiobutton(b_frame,text='3',bg='gray93',variable=nbb,value=3,font='15',width=3).place(x=960,y=50)
		nb = ttk.Combobox(b_frame,values=['please select...','1','2','3'],state='readonly',width=22)
		nb.place(x=830, y=50)
		nb.current(0)

		Label(b_frame,text='AC :',font='17',bg='gray93').place(x=732,y=75)
		#Radiobutton(b_frame,text='Yes',bg='gray93',variable=acb,value=1,font='15',width=3).place(x=800,y=90)
		#Radiobutton(b_frame,text='No',bg='gray93',variable=acb,value=0,font='15',width=3).place(x=880,y=90)
		ac = ttk.Combobox(b_frame,values=['please select...','Yes','No'],state='readonly',width=22)
		ac.place(x=830,y=75)
		ac.current(0)


		Label(b_frame,text='TV :',font='17',bg='gray93').place(x=732,y=100)
		#Radiobutton(b_frame,text='Yes',bg='gray93',variable=tvb,value=1,font='15',width=3).place(x=800,y=130)
		#Radiobutton(b_frame,text='No',bg='gray93',variable=tvb,value=0,font='15',width=3).place(x=880,y=130)
		tv = ttk.Combobox(b_frame,values=['please select...','Yes','No'],state='readonly',width=22)
		tv.place(x=830,y=100)
		tv.current(0)

		Label(b_frame,text='Wifi :',font='17',bg='gray93').place(x=732,y=125)
		#Radiobutton(b_frame,text='Yes',bg='gray93',variable=tvb,value=1,font='15',width=3).place(x=800,y=130)
		#Radiobutton(b_frame,text='No',bg='gray93',variable=tvb,value=0,font='15',width=3).place(x=880,y=130)
		wifi = ttk.Combobox(b_frame,values=['please select...','Yes','No'],state='readonly',width=22)
		wifi.place(x=830,y=125)
		wifi.current(0)
		#roomd(rn number primary key,beds number,ac varchar(10),tv varchar(10),internet varchar(10),price number(10))
		listofrooms = Listbox(b_frame,height=6,width=36)
		listofrooms.place(x=735,y=190)
		listofrooms.insert(END,'Rooms of Your Choice will appear Here')
		listofrooms.insert(END,'once you apply filter')
		def findrooms():
			cursor.execute('select rn,price,rstatus from roomd where beds = ? and ac = ? and tv = ? and internet = ? order by price asc',((nb.get()),ac.get(),tv.get(),wifi.get()) )
			x = cursor.fetchall()
			#print (x)
			listofrooms.delete(0,END)
			if x == []:
				listofrooms.insert(END,'No Matching Found')
			for i in x :
				listofrooms.insert(END,'Room Number '+str(i[0])+' - Price - '+str(i[1]))
		res = Button(b_frame,text='Reserve',bg='white',fg='cyan4',font='timenewroman 11',activebackground='green',command=booking).place(x=235,y=270)
		unres = Button(b_frame,text='Unreserve',bg='white',fg='cyan4',font='timenewroman 11',activebackground='green',command=unreserve).place(x=327,y=270)
		findrooms = Button(b_frame,text='Find Rooms',bg='white',fg='cyan4',font='timenewroman 9',activebackground='green',command = findrooms).place(x=830,y=155)
		
		scrollbar = Scrollbar(b_frame, orient="vertical")
		scrollbar.config(command=listofrooms.yview)
		scrollbar.place(x=1014,y=191,height=111)
		listofrooms.config(yscrollcommand=scrollbar.set)



		b_frame.place(x=0,y=120+6+20+60+11)
		b_frame.pack_propagate(False)
		b_frame.tkraise()

		#nl = Label(b_frame,text='www.itsourcecode.com',fg='blue',bg='gray91',font='msserif 8')
		#nl.place(x=955,y=310)
		#nl.tkraise()
	#-------------login module----------------------------------------------------------------------------------------------------------------------
	def login():
		q = messagebox.askyesno("Exit","Do you really want to exit ?")
		if(q):
			root.destroy()
	#---------------2nd top frame-----------------------------------------------------------------------------------------------------------------

	sl_frame = Frame(root,height=130,width=1080,bg='white')
	sl_frame.place(x=0,y=70+6)
	path = "images/rooms.png"
	img = ImageTk.PhotoImage(Image.open(path))
	b1 = Button(sl_frame,image=img,text='b1',bg='white',width=180,command=rooms)
	b1.image = img
	b1.place(x=180,y=0)
	path2 = "images/hotelstatus.png"
	img1 = ImageTk.PhotoImage(Image.open(path2))
	b2 = Button(sl_frame,image=img1,text='b2',bg='white',width=180,command=hotel_status)
	b2.image = img1
	b2.place(x=0,y=0)
	path3='images/guests.png'
	img3 = ImageTk.PhotoImage(Image.open(path3))
	b3 = Button(sl_frame,image=img3,text='b2',bg='white',width=180,command=staff)
	b3.image = img3
	b3.place(x=180*4,y=0)
	path4='images/payments.png'
	img4 = ImageTk.PhotoImage(Image.open(path4))
	b4 = Button(sl_frame,image=img4,text='b2',bg='white',width=180,command = payments)
	b4.image = img4
	b4.place(x=180*3,y=0)
	path5='images/logout.png'
	img5 = ImageTk.PhotoImage(Image.open(path5))
	b5 = Button(sl_frame,image=img5,text='b2',bg='white',width=180,height=100,command=login)
	b5.image = img5
	b5.place(x=180*5,y=0)
	path6='images/Bookroom.png'
	img6 = ImageTk.PhotoImage(Image.open(path6))
	b6 = Button(sl_frame,image=img6,text='b2',bg='white',width=180,height=100,command=reserve)
	b6.image = img6
	b6.place(x=180*2,y=0)
	Label(sl_frame,text='Hotel Status',font='msserif 13',bg='white').place(x=35,y=106)
	Label(sl_frame,text='Rooms',font='msserif 13',bg='white').place(x=248,y=106)
	Label(sl_frame,text='Reserve',font='msserif 13',bg='white').place(x=417,y=106)
	Label(sl_frame,text='Contacts',font='msserif 13',bg='white').place(x=774,y=106)
	Label(sl_frame,text='Payments Info',font='msserif 13',bg='white').place(x=570,y=106)
	Label(sl_frame,text='Exit',font='msserif 13',bg='white').place(x=968,y=106)
	sl_frame.pack_propagate(False)
	#-------------------extra frame------------------------------------------------------------------------------------------------------------------
	redf = Frame(root,height=6,width=1080,bg='lightsteelblue3')
	redf.place(x=0,y=70)
	redf1 = Frame(root,height=40,width=1080,bg='lightsteelblue3')
	redf1.place(x=0,y=210)

	#hotel_status() # calling the bottom frame for default page
	#login()
	#rooms()
	#payments()
	#cur.execute("select * from roomd ")
	#x = cur.fetchall()
	#print (x) 
	reserve()
	#staff()
	datetime()
	mainloop()
def call_mainroot():
	sroot.destroy()
	mainroot()
sroot.after(3000,call_mainroot)
mainloop()