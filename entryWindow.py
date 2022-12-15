import tkinter as tk
import tkinter.messagebox
import csv
from register import register
from user import User, UserStock
def center_window(root, width, height):
    '''
    窗体居中
    :param root: 窗体对象
    :param width: 窗体宽度
    :param height: 窗体高度
    '''
    screen_width = root.winfo_screenwidth()
    screen_height  = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screen_width - width) / 2, (screen_height - height) / 2)  # 设置窗口居中参数
    root.geometry(size)

def read_account():
    '''
    读取用户账号密码数据
    :return: 字典
    '''
    with open("account.csv", encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        account_dict = {}
        for row in csv_reader:
            if row[1] == "用户名":
                continue
            account_dict[row[1]] = row[2]

    return account_dict

def read_admin_account():
    with open("admin_account.csv", encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)
        admin_account_dict = {}
        for row in csv_reader:
            if row[1] == "用户名":
                continue
            admin_account_dict[row[1]] = row[2]

    return  admin_account_dict

def read_user_w():
    '''
    :return: 列表
    '''
    with open("account.csv", encoding='gbk') as csvfile:
        csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
        user_w_list = []
        for row in csv_reader:
            if row[0] == 'id':
                continue
            user_cur = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            user_w_list.append(user_cur)
    return user_w_list



def enter():

    enterWindow = tk.Tk()  #设置登陆注册对象
    enterWindow.title('欢迎使用你帮我助物品互换系统')
    center_window(enterWindow, 500, 200)

    tk.Label(enterWindow, text="你帮我助物品互换系统",font=("黑体", 24)).place(relx=0.5, rely=0.18, anchor=tk.CENTER)
    tk.Label(enterWindow,text="账号：", font=("宋体",14)).place(relx=0.25, rely=0.35)
    tk.Label(enterWindow,text="密码：", font=("宋体",14)).place(relx=0.25, rely=0.52)
    account_entry = tk.Entry(enterWindow,width=21)
    account_entry.place(relx=0.34, rely=0.35)
    password_entry = tk.Entry(enterWindow,width=21)
    password_entry.place(relx=0.34, rely=0.52)

    account_d = {'acc':''}
    dict_a = {}
    def change_state():
        dict_a['state'] = ad_v.get()
        account_dict = read_account()
        ad_account_dict = read_admin_account()
        account_cur = account_entry.get()
        password_cur = password_entry.get()
        if ad_v.get() == 1:
            if account_cur == "":
                tk.messagebox.showwarning('未输入账号', '请输入账号!')
            else:
                if password_cur == "":
                    tk.messagebox.showwarning('未输入密码', '请输入密码!')
                else:
                    if account_cur not in account_dict.keys():
                        tk.messagebox.showwarning('账号未注册', '账号未注册，请注册账号!')
                    else:
                        if account_dict[account_cur] != password_cur:
                            tk.messagebox.showerror('密码错误', '密码错误，请重新输入密码！')
                        else:
                            account_d['acc'] = account_cur
                            enterWindow.destroy()


        elif ad_v.get() == 0:
            if account_cur == "":
                tk.messagebox.showwarning('未输入账号', '请输入账号!')
            else:
                if password_cur == "":
                    tk.messagebox.showwarning('未输入密码', '请输入密码!')
                else:
                    if account_cur not in ad_account_dict.keys():
                        tk.messagebox.showwarning('无此账号', '无此管理员账号!')
                    else:
                        if ad_account_dict[account_cur] != password_cur:
                            tk.messagebox.showerror('密码错误', '密码错误，请重新输入密码！')
                        else:
                            account_d['acc'] = account_cur
                            enterWindow.destroy()



    log_button = tk.Button(enterWindow,text='登录',command=change_state)
    log_button.place(relx=0.445, rely=0.85, anchor=tk.CENTER)
    reg_button = tk.Button(enterWindow, text='注册', command=register)
    reg_button.place(relx=0.575, rely=0.85, anchor=tk.CENTER)

    #单选框 管理员/普通用户
    ad_v = tk.IntVar()
    tk.Radiobutton(enterWindow, text="管理员", variable=ad_v, value=0).place(relx=0.43, rely=0.72, anchor=tk.CENTER)
    tk.Radiobutton(enterWindow, text="普通用户", variable=ad_v, value=1).place(relx=0.58, rely=0.72, anchor=tk.CENTER)


    def writor():
        wriWin = tk.Tk()
        center_window(wriWin, 300, 100)
        wriWin.title('你帮我助开发者')
        tk.Label(wriWin, text='开发者：胡宇恒   学号：520120910026').place(x=150, y=40, anchor=tk.CENTER)
        tk.Label(wriWin, text='学院：安泰经济管理学院').place(x=150, y=70 , anchor=tk.CENTER)

    wri_Button = tk.Button(enterWindow,text='开发者信息',command=writor).place(x=390, y=155)
    enterWindow.mainloop()


    return dict_a['state'], account_d['acc']

