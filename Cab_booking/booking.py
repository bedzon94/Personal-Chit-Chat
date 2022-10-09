#!/usr/bin/env python3

def __init__(self, master):
    self.master = master
    self.username = StringVar()
    self.password = StringVar()
    self.n_username = StringVar()
    self.n_password = StringVar()
    self.widgets()
def new_user(self):
    with sqlite3.connect('Users.db') as db:
        c = db.cursor()
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!','Username Already Taken')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()
