from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
win = Tk()
win.state('zoomed')
win.config(bg="black")
#=============================Button Function=============================

def pd():
    if e1.get()=="" or e2.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        con = mysql.connector.connect(host="localhost",username="root",password="faiztamboli@0104",database="mydata")
        my_cursor = con.cursor()
        my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            nameoftablets.get(),
            ref.get(),
            dose.get(),
            nooftablets.get(),
            issuedate.get(),
            expdate.get(),
            dailydose.get(),
            sideeffect.get(),
            nameofpatient.get(),
            dob.get(),
            patientaddress.get()
        ))
        con.commit()
        fetch_data()
        con.close()
        messagebox.showinfo("Success","Record has been inserted")
def fetch_data():
    con = mysql.connector.connect(host="localhost", username="root", password="faiztamboli@0104", database="mydata")
    my_cursor = con.cursor()
    my_cursor.execute('select * from hospital')
    rows = my_cursor.fetchall()
    if len(rows)!=0:
        table.delete(* table.get_children())
        for items in rows:
            table.insert('',END,values=items)
            con.commit()
        con.close()
def get_data(event=''):
    cursor_row = table.focus()
    data = table.item(cursor_row)
    row = data['values']
    nameoftablets.set(row[0])
    ref.set(row[1])
    dose.set(row[2])
    nooftablets.set(row[3])
    issuedate.set(row[4])
    expdate.set(row[5])
    dailydose.set(row[6])
    sideeffect.set(row[7])
    nameofpatient.set(row[8])
    dob.set(row[9])
    patientaddress.set(row[10])
#============================Prescription Data=============================
def pre():
    txt_frme.insert(END, 'Name Of Tablets:\t\t\t' + nameoftablets.get() + '\n')
    txt_frme.insert(END, 'Reference No.:\t\t\t' + ref.get() + '\n')
    txt_frme.insert(END, 'Dose:\t\t\t' + dose.get() + '\n')
    txt_frme.insert(END, 'No. of Tablets:\t\t\t' + nooftablets.get() + '\n')
    txt_frme.insert(END, 'Issue Date:\t\t\t' + issuedate.get() + '\n')
    txt_frme.insert(END, 'Exp. Date:\t\t\t' + expdate.get() + '\n')
    txt_frme.insert(END, 'Daily Dose:\t\t\t' + dailydose.get() + '\n')
    txt_frme.insert(END, 'Side Effect:\t\t\t' + sideeffect.get() + '\n')
    txt_frme.insert(END, 'Blood Pressure:\t\t\t' + bloodpressure.get() + '\n')
    txt_frme.insert(END, 'Storage:\t\t\t' + storage.get() + '\n')
    txt_frme.insert(END, 'Medication:\t\t\t' + medication.get() + '\n')
    txt_frme.insert(END, 'Patient Id:\t\t\t' + patientid.get() + '\n')
    txt_frme.insert(END, 'Name of  Patient:\t\t\t' + nameofpatient.get() + '\n')
    txt_frme.insert(END, 'DOB:\t\t\t' + dob.get() + '\n')
    txt_frme.insert(END, 'Patient Address:\t\t\t' + patientaddress.get() + '\n')

#============================Delete======================================
def delete():
    con = mysql.connector.connect(host="localhost", username="root", password="faiztamboli@0104", database="mydata")
    my_cursor = con.cursor()
    querry = ('delete from hospital where Reference = %s')
    value = (ref.get(),)
    my_cursor.execute(querry,value)
    con.commit()
    con.close()
    fetch_data()
    messagebox.showinfo('Delete','Patient data has been deleted')

#===========================Clear==============================================
def clear():
    nameoftablets.set('')
    ref.set('')
    dose.set('')
    nooftablets.set('')
    issuedate.set('')
    expdate.set('')
    dailydose.set('')
    sideeffect.set('')
    bloodpressure.set('')
    storage.set('')
    medication.set('')
    patientid.set('')
    nameofpatient.set('')
    dob.set('')
    patientaddress.set('')
    txt_frme.delete(1.0,END)

#============================Exit========================================
def exit():
    confirm = messagebox.askyesno('confirmation','Are You Sure You Want To Exit')
    if confirm>0:
        win.destroy()

#============================Heading=====================================

Label(win,text='Hospital Management System',font='impact 31 bold',bg='blue',fg='white').pack(fill=X)

#==============================Frame1==============================================

frame1 = Frame(win,bd=15,relief=RIDGE)
frame1.place(x=0,y=54,width=1535,height=310)
#===============================Label Frame for Patient Info=============================

lf1 = LabelFrame(frame1,text='Patient Information',font='ariel 10 bold',bd=10,bg='pink')
lf1.place(x=10,y=0,width=750,height=280)

#LABEL_FOR_PATIENT_INFORMATION
Label(lf1,text='Name of Tablet',bg='pink').place(x=5,y=10)
Label(lf1,text='Refrence No.',bg='pink').place(x=5,y=40)
Label(lf1,text='Dose',bg='pink').place(x=5,y=70)
Label(lf1,text='No. of Tablets',bg='pink').place(x=5,y=100)
Label(lf1,text='Issue Date',bg='pink').place(x=5,y=130)
Label(lf1,text='Exp. Date',bg='pink').place(x=5,y=160)
Label(lf1,text='Daily Dose',bg='pink').place(x=5,y=190)
Label(lf1,text='Side Effect',bg='pink').place(x=5,y=220)
Label(lf1,text='Blood Pressure',bg='pink').place(x=370,y=10)
Label(lf1,text='Storage Device',bg='pink').place(x=370,y=40)
Label(lf1,text='Medication ',bg='pink').place(x=370,y=70)
Label(lf1,text='Patient Id',bg='pink').place(x=370,y=100)
Label(lf1,text='Name Of Patient',bg='pink').place(x=370,y=130)
Label(lf1,text='DOB',bg='pink').place(x=370,y=160)
Label(lf1,text='Patient Address',bg='pink').place(x=370,y=190)
#TEXT_VARIEABLE_FOR_EVERY_ENTRY_FIELD
nameoftablets = StringVar()
ref = StringVar()
dose = StringVar()
nooftablets = StringVar()
issuedate = StringVar()
expdate = StringVar()
dailydose = StringVar()
sideeffect = StringVar()
bloodpressure = StringVar()
storage = StringVar()
medication = StringVar()
patientid = StringVar()
nameofpatient = StringVar()
dob = StringVar()
patientaddress = StringVar()

#ENTRY_FIELD_FOR_ALL_LABELS
e1 = Entry(lf1,bd=4,textvariable=nameoftablets)
e1.place(x=130,y=10,width=200)

e2 = Entry(lf1,bd=4,textvariable=ref)
e2.place(x=130,y=40,width=200)

e3 = Entry(lf1,bd=4,textvariable=dose)
e3.place(x=130,y=70,width=200)

e4 = Entry(lf1,bd=4,textvariable=nooftablets)
e4.place(x=130,y=100,width=200)

e5 = Entry(lf1,bd=4,textvariable=issuedate)
e5.place(x=130,y=130,width=200)

e6 = Entry(lf1,bd=4,textvariable=expdate)
e6.place(x=130,y=160,width=200)

e7 = Entry(lf1,bd=4,textvariable=dailydose)
e7.place(x=130,y=190,width=200)

e8 = Entry(lf1,bd=4,textvariable=sideeffect)
e8.place(x=130,y=220,width=200)

e9 = Entry(lf1,bd=4,textvariable=bloodpressure)
e9.place(x=500,y=10,width=200)

e10 = Entry(lf1,bd=4,textvariable=storage)
e10.place(x=500,y=40,width=200)

e11 = Entry(lf1,bd=4,textvariable=medication)
e11.place(x=500,y=70,width=200)

e12 = Entry(lf1,bd=4,textvariable=patientid)
e12.place(x=500,y=100,width=200)

e13 = Entry(lf1,bd=4,textvariable=nameofpatient)
e13.place(x=500,y=130,width=200)

e14 = Entry(lf1,bd=4,textvariable=dob)
e14.place(x=500,y=160,width=200)

e15 = Entry(lf1,bd=4,textvariable=patientaddress)
e15.place(x=500,y=190,width=200)


#===============================Label Frame for Prescription=============================

lf2 = LabelFrame(frame1,text='Priscription',font='ariel 12 bold',bd=10)
lf2.place(x=770,y=0,width=470,height=280)

#TEXT_BOX_FOR_PRESCRIPTION
txt_frme = Text(lf2,font='impack 10 bold',width=40,height=30,bg='yellow')
txt_frme.pack(fill=BOTH)

#==============================Frame2=============================================

frame2 = Frame(win,bd=15,relief=RIDGE)
frame2.place(x=0,y=360,width=1535,height=400)

#=============================Button==============================================
#DELETE_BUTTON
d_btn = Button(win,text='Delete',font='arial 15 bold',bg='brown',fg='white',bd=6,cursor='hand2',command=delete)
d_btn.place(x=0,y=740,width=270)
#PRESCRIPTION_BUTTION
d_btn = Button(win,text='Prescription',font='arial 15 bold',bg='purple',fg='white',bd=6,cursor='hand2',command=pre)
d_btn.place(x=270,y=740,width=330)
#SAVE_PRESCRIPTION_BUTTON
pd_btn = Button(win,text='Save Prescription Data',font='arial 15 bold',bg='green',fg='white',bd=6,cursor='hand2',command=pd)
pd_btn.place(x=600,y=740,width=340)
#CLEAR_BUTTON
c_btn = Button(win,text='Clear Button',font='arial 15 bold',bg='blue',fg='white',bd=6,cursor='hand2',command=clear)
c_btn.place(x=940,y=740,width=170)
#EXIT_BUTTON
e_btn = Button(win,text='Exit',font='arial 15 bold',bg='brown',fg='white',bd=6,cursor='hand2',command=exit)
e_btn.place(x=1110,y=740,width=170)

#=========================================Scroll Bar For Prescription Data===================================================
scroll_x = ttk.Scrollbar(frame2,orient=HORIZONTAL)
scroll_x.pack(side='bottom',fill='x')

scroll_y = ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side='right',fill='y')

table = ttk.Treeview(frame2,columns=('Name Of Tablets','Reference','Dose','No. of Tablets','Issue Date','Exp. Date','Daily Dose','Side Effect','Patient Name','DOB','Patient Address'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x = ttk.Scrollbar(command=table.xview)
scroll_y = ttk.Scrollbar(command=table.yview)

#=============================================Heading for Prescription Data=======================================================
table.heading('Name Of Tablets',text='Name Of Tablets')
table.heading('Reference',text='Reference')
table.heading('Dose',text='Dose')
table.heading('No. of Tablets',text='No. of Tablets')
table.heading('Issue Date',text='Issue Date')
table.heading('Exp. Date',text='Exp. Date')
table.heading('Daily Dose',text='Daily Dose')
table.heading('Side Effect',text='Side Effect')
table.heading('Patient Name',text='Patient Name')
table.heading('DOB',text='DOB')
table.heading('Patient Address',text='Patient Address')
table['show'] = 'headings'
table.pack(fill=BOTH,expand=1)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6
table.column('Name Of Tablets',width=100)
table.column('Reference',width=100)
table.column('Dose',width=100)
table.column('No. of Tablets',width=100)
table.column('Issue Date',width=100)
table.column('Exp. Date',width=100)
table.column('Daily Dose',width=100)
table.column('Side Effect',width=100)
table.column('Patient Name',width=100)
table.column('DOB',width=100)
table.column('Patient Address',width=100)


table.bind('<ButtonRelease-1>',get_data)
fetch_data()
mainloop()


