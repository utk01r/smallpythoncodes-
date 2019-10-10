from tkinter import*
import hashlib
from tkinter import messagebox
#user_name = 'vividha'
#user_name_hash = hashlib.md5(user_name.encode()).hexdigest()
#print(user_name_hash)
user_name_hash = 'af808b18084a93de1765466e7927ffb1'

# pass_word = 'galaxy'
# pass_word_hash = hashlib.md5(pass_word.encode()).hexdigest()
# print(pass_word_hash)
pass_word_hash = 'e03239b27e34a5f7f3bde739459dd537'

v = Tk()
v.title('LOGIN PAGE')
v.geometry('600x600')
v.config(bg='white')

l1 = Label(v, text='LOGIN PAGE', bg='white', fg='black', relief=RAISED, bd=6, font=('ariel', 30))
l1.place(x=100, y=100)
l1.pack()

e1 = Entry(v, width=50)
e1.place(x=100, y=100)
e1.pack()

l2 = Label(v, text='Enter Username', bg='white', fg='black', bd=12, font=('ariel', 15))
l2.place(x=100, y=100)
l2.pack()

e2 = Entry(v, width=50)
e2.place(x=100, y=100)
e2.pack()

l3 = Label(v, text='Enter Password', bg='white', fg='black', bd=12, font=('ariel', 15))
l3.place(x=100, y=50)
l3.pack()

def check():
    t = e1.get()
    t_hash = hashlib.md5(t.encode()).hexdigest()
    a = e2.get()
    a_hash = hashlib.md5(a.encode()).hexdigest()
    if t_hash != user_name_hash:
        messagebox.showinfo(title='Message box', message='Access Denied')
    else:
        if a_hash != pass_word_hash:
            messagebox.showinfo(title='Message box', message='Access Denied')
    if user_name_hash == t_hash and pass_word_hash == a_hash:
        v.destroy()
        window = Tk()
        window.title('Welcome Page')
        window.geometry('600x600')
        window.config(bg='green')
        Label(window, text='WELCOME VIVIDHA', relief=RAISED, font=('calibri', 20)).pack()
        window.mainloop()

Button(v, text='Verify', font=('ariel', 20), command=check).pack()
v.mainloop()



