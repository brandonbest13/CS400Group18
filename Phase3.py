### CS4400 Phase 3 Heavy-Weight Option Source-Code ###
from tkinter import *
import pymysql
import getpass

class GUI:
    db = pymysql.connect(host='academic-mysql.cc.gatech.edu', user='cs4400_Team_18', passwd='hPwvUzZA', db='cs4400_Team_18')
    def __init__(self, win):
        self.win = win
        self.login_page()

    def login_page(self):
        self.win.title("Login")
        self.Frame1 = Frame(self.win)
        self.Frame1.pack()
        Label(self.Frame1, text='Login', fg='gold').grid(row=0, column=3, sticky=W, pady=5)

        self.Username = StringVar()
        Label(self.Frame1, text='Username').grid(row=2, column=1)
        e1 = Entry(self.Frame1, textvariable=self.Username, width=30)
        e1.grid(row=2, column=3, pady=10, columnspan=2)

        self.Password = StringVar()
        Label(self.Frame1, text='Password').grid(row=3, column=1)
        e2 = Entry(self.Frame1, textvariable=self.Password, width=30)
        e2.grid(row=3, column=3, pady=10, columnspan=2)

        b1 = Button(self.Frame1, text='Login', command=self.Login)
        b1.grid(row=4, column=2, sticky=W, pady=5, padx=5)
        b2 = Button(self.Frame1, text='Register', command=self.Register)
        b2.grid(row=4, column=4, pady=10, padx=5)

        #photo = PhotoImage(file='buzz.gif')
        #L1 = Label(self.Frame1, image=photo, height=500, width=400)
        #L1.photo=photo
        #L1.grid(row=5,column=5)


    def Register(self):
        self.Frame1.destroy()
        self.Frame1 = Frame(self.win)
        self.Frame1.pack()
        Label(self.Frame1, text='New Student Registration').pack()
        frameList = []
        labelList = ['Username', 'GT Email Address', 'Password', 'Confirm Password']
        self.entryList = []
        for i in range(4):
            frameList.append(Frame(self.Frame1, width=50))
            frameList[i].pack()
            Label(frameList[i], text=labelList[i]).pack(side=LEFT, anchor=E, padx=25)
            self.entryList.append(StringVar())
            Entry(frameList[i], textvariable=self.entryList[i]).pack(anchor=W, padx=25)
        Button(self.Frame1, text='Create', command=self.TryRegister).pack()

    def MainPage(self):
        self.Frame1.destroy()
        self.Frame1 = Frame(self.win)
        self.Frame1.pack()
        Label(text='Main Page').grid(row=0,column=1)
        Label()






    def Login(self):
        #c = cursor(GUI.db)

        sql = """SELECT GT_Email
            FROM Students
            WHERE Username=? AND Password=?;
            """
        #user = c.execute(sql, (self.Username,self.Password))
        user = None ##delete me
        if user:
            pass ##################### should move to next window
        else:
            showerror('Login Error', 'Username or password incorrect. Try again')

    def TryRegister(self):
        self.Frame1.pack_forget()
        sql = """SELECT * FROM Students
                WHERE Username=? AND Password=?;
            """
        inSys = None ############################## Should be a sql execute statement
        if not inSys:
            sql = """INSERT INTO Students
                    values (?, ?, ?, ?);
            """
            self.login_page()
        else:
            showerror('Registration Error', 'User already in database')












def main(args):
    mainWin = Tk()
    mainGUI = GUI(mainWin)
    mainWin.mainloop()
    print('done')############################

if __name__ == '__main__':
    import sys
    main(sys.argv)
