import tkinter as tk
from tkinter.messagebox import *

win=tk.Tk()
win.geometry("250x160")
win.title("登录程序（Made by Sinkorty）")

lab_tooltip=tk.Label(win,text="请登录")
lab_user=tk.Label(win,text="用户名：")
lab_psw=tk.Label(win,text="密码：")
ent_user=tk.Entry(win)
ent_psw=tk.Entry(win,show="*")

def Login():
    if ent_user.get() == "abc" and ent_psw.get() == "123":
        showinfo("登录系统","登录成功1")
        win.destroy()
        win.quit()
    else:
        showwarning("登录系统","登录失败，账号或密码错误！")
btn_login=tk.Button(win,text="登录",command=Login)
def Quit():
    win.destroy()
    win.quit()
btn_quit=tk.Button(win,text="退出",command=Quit)

lab_tooltip.place(x=45,y=10,width=120,height=20)
lab_user.place(x=20,y=45,width=50,height=15)
lab_psw.place(x=20,y=90,width=50,height=15)
ent_user.place(x=80,y=43,width=120,height=25)
ent_psw.place(x=80,y=87,width=120,height=25)
btn_login.place(x=50,y=125,width=55,height=25)
btn_quit.place(x=150,y=125,width=55,height=25)


win.mainloop()
