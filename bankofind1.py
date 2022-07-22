#importing from library
from tkinter import*
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date


def frame1_login():
    global frame1
    global n1
    global n2
    #creating instances/frame
    frame1=Tk()

    #Title to the Frame
    frame1.title("BANKING MANAGEMENT SYSTEM")

    #Size of the frame and making it non resizable
    frame1.geometry("310x160")
    frame1.resizable(False,False)

    #name=[widget name](root window,properties/configuration)
    #pack method for positioning
    label1=Label(frame1,text="BANK OF INDIA",font="Cambria",fg="blue")
    loginid=Label(frame1,text="Login Id:",font="Cailibri",fg="green")
    password=Label(frame1,text="Password:",font="Cailibri",fg="green")
    n1=Entry(frame1)
    n2=Entry(frame1)
    login=Button(frame1,text="Login",fg="red", command=frame1_loginbutton)
    newus=Button(frame1,text="New User",fg="black",command=f1_to_f2)
    label1.grid(column=3)
    loginid.grid(row=4,sticky=E)
    n1.grid(row=4,column=3)

    password.grid(row=5,sticky=E)
    n2.grid(row=5,column=3)
    login.grid(row=6,column=3)
    newus.grid(row=8,column=10,sticky=E)

    #Strarting the GUI/ creating the main loop
    frame1.mainloop()


def frame1_loginbutton():
    global login2
    global pass2
    login2=n1.get()
    pass2=n2.get()
    r=0
    
    if len(login2) == 0 and len(pass2) == 0:
        messagebox.showinfo(" ","Please fill in the Missing Info")
    elif len(login2) == 0 and len(pass2) != 0 :
        messagebox.showinfo(" ","Please Enter  Username")
    elif len(login2) != 0 and len(pass2) == 0:
        messagebox.showinfo(" ","Please enter a Password")
    else:
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",
                                       database="bankofind")
        mycursor = mydb.cursor()
        query = ("SELECT userid,pass1 FROM bankpass WHERE userid =%s and pass1=%s")
        query_data=(login2,pass2)
        mycursor.execute(query,query_data)
        #connection.commit()
        table_data=mycursor.fetchall()

        for row in table_data:
            r=r+1
        if(r==0):
            messagebox.showinfo(" ","Wrong id and pass")
        else:
            messagebox.showinfo(" ","WELCOME")
            f1_to_f3()

def frame2_newuser():
    global frame2
    global n3
    global n4
    global n5
    frame2=Tk()
    #frame2=Toplevel()
    frame2.title("BANKING MANAGEMENT SYSTEM")
    frame2.geometry("470x200")
    frame2.resizable(False,False)

    labe21=Label(frame2,text="BANK OF INDIA",font="Cambria",fg="blue")
    labe22=Label(frame2,text="New User",font="Cambria",fg="blue")
    atmpin=Label(frame2,text="Enter Atm Pin:",font="Cambria",fg="red")
    loginid=Label(frame2,text="Enter new Login Id:",font="Cailibri",fg="green")
    password=Label(frame2,text="Enter new Password:",font="Cailibri",fg="green")
    n3=Entry(frame2)
    n4=Entry(frame2)
    n5=Entry(frame2)
    
    back=Button(frame2,text="<--",fg="black",command=f2_to_f1)
    newlogin=Button(frame2,text="Create ID/Password",fg="red",command=frame2_newaccbutton)
    back.grid(row=0,column=0,stick=W)
    labe21.grid(row=0,column=1)
    labe22.grid(row=1,column=1)
    loginid.grid(row=3,sticky=E)
    n3.grid(row=3,column=2) 
    password.grid(row=4,sticky=E)
    n4.grid(row=4,column=2)
    atmpin.grid(row=5,sticky=E)
    n5.grid(row=5,column=2)
    newlogin.grid(row=6,column=1)

    #Strarting the GUI/ creating the main loop
    frame2.mainloop()


def frame2_newaccbutton():
    global newuserid 
    global newpassword
    global newatmpin
    newuserid=""
    newpassword=""
    if(n5.get()==""):
        n5.insert(0,0)
    else:
        newatmpin=int(n5.get())
    
    newuserid=n3.get()
    newpassword=n4.get()
    newatmpin=int(n5.get())
    if len(newuserid) == 0 and len(newpassword) == 0:
        messagebox.showinfo(" ","Please fill in the Missing Info")
    elif len(newuserid) == 0 and len(newpassword) != 0:
        messagebox.showinfo(" ","Please Enter  Username")
    elif len(newuserid) != 0 and len(newpassword) == 0:
        messagebox.showinfo(" ","Please enter a Password")
    elif len(newuserid) != 0 and len(newpassword) != 0 and newatmpin>9999 or newatmpin<=999:
        messagebox.showinfo(" ","Please enter a new atmpin of four digit")
    else:
        
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",
                                       database="bankofind")
        mycursor = mydb.cursor()
        query = ("INSERT INTO bankpass (userid,pass1,atmpin) VALUES (%s, %s,%s)")
        query_data=(newuserid,newpassword,newatmpin)
        mycursor.execute(query,query_data)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        
        #to create new instance for message box and delete it 
        master = Tk()
        master.withdraw()

        messagebox.showinfo(" ","Records Inserted")

def frame3():
    global frame3
    
    #creating instances/frame
    frame3=Tk()

    #Title to the Frame
    frame3.title("BANKING MANAGEMENT SYSTEM")

    #Size of the frame and making it non resizable
    frame3.geometry("600x160")
    frame3.resizable(False,False)

    #name=[widget name](root window,properties/configuration)
    #pack method for positioning
    label1=Label(frame3,text="BANK OF INDIA",font="Cambria",fg="blue")
    label2=Label(frame3,text="Select the Options Below",font="Cambria",fg="black")

    add_new_cust=Button(frame3,text="ADD NEW CUSTOMER",fg="orange",command=f3_to_f4)
    check_record_cust=Button(frame3,text="CHECK RECORDS OF CUSTOMER",fg="orange",command=f3_to_f7)
    update_record_cust=Button(frame3,text="UPDATE RECORDS OF CUSTOMER",fg="orange",command=f3_to_f5)
    delete_record_cust=Button(frame3,text="DELETE RECORD OF CUSTOMER",fg="orange",command=f3_to_f6)
    back=Button(frame3,text="<--",fg="black",command=f3_to_f1)
    
    label1.grid(column=2)
    label2.grid(row=1,column=2)
    back.grid(row=0,column=1,sticky=W)
    add_new_cust.grid(row=2,column=1,sticky=W)
    check_record_cust.grid(row=3,column=1,sticky=E)
    update_record_cust.grid(row=2,column=3,sticky=W)
    delete_record_cust.grid(row=3,column=3,sticky=E)
    
    #Strarting the GUI/ creating the main loop
    frame3.mainloop()


def frame4():
    global frame4
    global t1
    global t2
    global t3
    global t4
    global n_branch
    global selected_date
    
    
    #creating instances/frame
    frame4=Tk()

    #Title to the Frame
    frame4.title("BANKING MANAGEMENT SYSTEM")

    #Size of the frame and making it non resizable
    frame4.geometry("500x230")
    frame4.resizable(False,False)

    #name=[widget name](root window,properties/configuration)
    label1=Label(frame4,text="BANK OF INDIA",font="Cambria",fg="blue")
    label2=Label(frame4,text="For New Customers",font="Cambria",fg="black")

    nm=Label(frame4,text="Enter Name",fg="orange")
    ac_no=Label(frame4,text="Enter New Account Number",fg="orange")
    branch=Label(frame4,text="Select Branch",fg="orange")
    date=Label(frame4,text="Enter date",fg="orange")
    address=Label(frame4,text="Enter Address",fg="orange")
    fdeposit=Label(frame4,text="First Deposite",fg="orange")

    # Create a Tkinter variable
    n_branch=StringVar(frame4)
    # Dictionary with options
    choices = { "Baner","Wakad","Shivaji Nagar"}
    c1=ttk.OptionMenu(frame4, n_branch, *choices)
    
    srecords=Button(frame4,text="Submit Records",fg="black")
    back=Button(frame4,text="<--",fg="black",command=f4_to_f3)

    n_date=DateEntry(frame4,width=12,dateformat=3, background='brown',
                  foreground='white', borderwidth=4,Calendar =2019)
    n_date.grid(row=5,column=3,sticky='nsew')

    selected_date = (n_date.get_date())
    
    t1=Entry(frame4)
    t2=Entry(frame4)
    t3=Entry(frame4)
    t4=Entry(frame4)
    
    #grid method for positioning
    label1.grid(row=0,column=2)
    label2.grid(row=1,column=2)
    back.grid(row=0,column=1,sticky=W)
    nm.grid(row=2,column=1)
    ac_no.grid(row=3,column=1)
    branch.grid(row=4,column=1)
    date.grid(row=5,column=1)
    address.grid(row=6,column=1)
    fdeposit.grid(row=7,column=1)
    srecords.grid(row=8,column=2)
    c1.grid(row=4,column=3)

    t1.grid(row=2,column=3)
    t2.grid(row=3,column=3)
    t3.grid(row=6,column=3)
    t4.grid(row=7,column=3)
    
    #Strarting the GUI/ creating the main loop
    frame4.mainloop()

def frame5():
    global frame5
    global t5
    global t6
    global t7
    
    
    #creating instances/frame
    frame5=Tk()

    #Title to the Frame
    frame5.title("BANKING MANAGEMENT SYSTEM")

    #Size of the frame and making it non resizable
    frame5.geometry("550x230")
    frame5.resizable(False,False)

    #name=[widget name](root window,properties/configuration)
    label1=Label(frame5,text="BANK OF INDIA",font="Cambria",fg="blue")
    label2=Label(frame5,text="Update Transaction of Account",font="Cambria",fg="black")

    nm=Label(frame5,text="Enter Name",fg="orange")
    ac_no=Label(frame5,text="Enter Account Number",fg="orange")
    tranc_type=Label(frame5,text="Select transaction type",fg="orange")
    amt=Label(frame5,text="Enter Amount",fg="orange")
    branch=Label(frame5,text="Select Branch",fg="orange")
    date=Label(frame5,text="Select Date",fg="orange")

    update_rec=Button(frame5,text="Update",fg="black")
    back=Button(frame5,text="<--",fg="black",command=f5_to_f3)

    t5=Entry(frame5)
    t6=Entry(frame5)
    t7=Entry(frame5)
    
    #grid method for positioning
    label1.grid(column=2)
    label2.grid(row=1,column=2)
    back.grid(row=0,column=1,sticky=W)
    nm.grid(row=2,column=1)
    ac_no.grid(row=3,column=1)
    tranc_type.grid(row=4,column=1)
    amt.grid(row=5,column=1)
    branch.grid(row=6,column=1)
    date.grid(row=7,column=1)
    update_rec.grid(row=8,column=2)

    t5.grid(row=2,column=3)
    t6.grid(row=3,column=3)
    t7.grid(row=5,column=3)
    
    #Strarting the GUI/ creating the main loop
    frame5.mainloop()

def frame6():
    global frame6
    global t8
    global t9
    
    #creating instances/frame
    frame6=Tk()

    #Title to the Frame
    frame6.title("BANKING MANAGEMENT SYSTEM")

    #Size of the frame and making it non resizable
    frame6.geometry("500x160")
    frame6.resizable(False,False)

    #name=[widget name](root window,properties/configuration)
    label1=Label(frame6,text="BANK OF INDIA",font="Cambria",fg="blue")
    label2=Label(frame6,text="Delete record of a customer",font="Cambria",fg="black")

    nm=Label(frame6,text="Enter Name",fg="orange")
    ac_no=Label(frame6,text="Enter Account Number",fg="orange")

    delete_rec=Button(frame6,text="Delete Record",fg="black")
    back=Button(frame6,text="<--",fg="black",command=f6_to_f3)

    t8=Entry(frame6)
    t9=Entry(frame6)
    
    #grid method for positioning
    label1.grid(column=2)
    label2.grid(row=1,column=2)
    back.grid(row=0,column=1,sticky=W)
    nm.grid(row=2,column=1)
    ac_no.grid(row=3,column=1)
    
    delete_rec.grid(row=8,column=2)

    t8.grid(row=2,column=3)
    t9.grid(row=3,column=3)
    
    #Strarting the GUI/ creating the main loop
    frame6.mainloop()

def frame7():
    global frame7
    global t10
    
    
    #creating instances/frame
    frame7=Tk()

    #Title to the Frame
    frame7.title("BANKING MANAGEMENT SYSTEM")

    #Size of the frame and making it non resizable
    frame7.geometry("500x160")
    frame7.resizable(False,False)

    #name=[widget name](root window,properties/configuration)
    label1=Label(frame7,text="BANK OF INDIA",font="Cambria",fg="blue")
    label2=Label(frame7,text="Check Transaction of a Account",font="Cambria",fg="black")

    ac_no=Label(frame7,text="Enter Account Number",fg="orange")

    check_rec=Button(frame7,text="Check A/C Details",fg="black")
    back=Button(frame7,text="<--",fg="black",command=f7_to_f3)

    t10=Entry(frame7)
    
    #grid method for positioning
    label1.grid(column=2)
    label2.grid(row=1,column=2)
    back.grid(row=0,column=1,sticky=W)
    ac_no.grid(row=2,column=1)
    
    check_rec.grid(row=8,column=2, stick=S)

    t10.grid(row=2,column=3)
    
    #Strarting the GUI/ creating the main loop
    frame7.mainloop()



def f1_to_f3():
    frame1.destroy()
    frame3()

def f1_to_f2():
    frame1.destroy()
    frame2_newuser()

def f2_to_f1():
    frame2.destroy()
    frame1_login()

def f3_to_f1():
    frame3.destroy()
    frame1_login()

def f3_to_f4():
    frame3.destroy()
    frame4()

def f3_to_f5():
    frame3.destroy()
    frame5()

def f3_to_f6():
    frame3.destroy()
    frame6()

def f3_to_f7():
    frame3.destroy()
    frame7()
    
def f4_to_f3():
    frame4.destroy()
    frame3()
    
def f5_to_f3():
    frame5.destroy()
    frame3()

def f6_to_f3():
    frame6.destroy()
    frame3()

def f7_to_f3():
    frame7.destroy()
    frame3()

frame1_login()
