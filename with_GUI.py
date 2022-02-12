# encoding:utf-8
# @Author :ZQY
import functools
import time
import tkinter as tk
from tkinter import messagebox
from save_games import *


def text0_show(num,msg=""):
    if num==0:
        text0.delete(1.0, 'end')
        text0.insert(1.0,'欢迎使用','center')
    elif num == 1:
        text0.delete(1.0, 'end')
        text0.insert(1.0, '运行中...', 'center')
    elif num == 2:
        text0.delete(1.0, 'end')
        text0.insert(1.0, '运行完成', 'center')
    elif num == 3:
        text0.delete(1.0, 'end')
        text0.insert(1.0, msg, 'center')
    elif num == -1:
        text0.delete(1.0, 'end')

def submit_path():
    """
    提交路径，生成save.txt
    :return:
    """
    path = entry1.get()
    try:
        text0_show(1)
        dir_name = find_path(path)
    except error1 as e:
        text0_show(-1)
        messagebox.showerror(message=e)
    else:
        save_dir_name(dir_name)
        text0_show(2)

def check_path():
    """
    检查路径是否正确，路径下是否有存档
    :return:
    """
    try:
        msg = check_dir_name()
    except error1 as e:
        text0_show(-1)
        messagebox.showerror(message=e)
    else:
        text0_show(3,msg)

def save_games(type=1):
    """
    第二步，保存day天的存档
    :param day:
    :param type: 游戏模式
    :return:
    """
    # 读取day
    day = entry2_l.get()
    if not day:
        text0_show(-1)
        messagebox.showerror(message="请输入天数")
        return
    day = int(day)

    # 保存存档
    try:
        text0_show(1)
        save_file(day,type)
    except error1 as e:
        text0_show(-1)
        messagebox.showerror(e)
    else:
        if type == 1:
            text0_show(3,msg=f"已存档第{day}天----普通模式")
        else:
            text0_show(3, msg=f"已存档第{day}天----故事模式")

def load_games(type=1):
    """
    第二步，读取游戏存档
    :param type: 游戏模式
    :return:
    """
    # 读取day
    day = entry2_r.get()
    if not day:
        text0_show(-1)
        messagebox.showerror(message="请输入天数")
        return
    day = int(day)

    # 读取存档
    try:
        text0_show(1)
        load_file(day, type)
    except error1 as e:
        text0_show(-1)
        messagebox.showerror(message=e)
    else:
        if type == 1:
            text0_show(3,msg=f"已读档第{day}天----普通模式")
        else:
            text0_show(3, msg=f"已读档第{day}天----故事模式")

def button3_click():
    """
    按button3改变游戏模式
    :return:
    """
    global mode
    if mode == 1:
        mode = 2
        button3_text.set('故事模式')
    else:
        mode = 1
        button3_text.set('普通模式')

def save_games_with_type():
    """
    选择模式后的save_games
    :return:
    """
    return functools.partial(save_games,type=mode)()

def load_games_with_type():
    """
    选择模式后的load_games
    :return:
    """
    return functools.partial(load_games,type=mode)()



# 窗口设置
window = tk.Tk()
window.title('This War of Mine自动存档')
window.geometry("800x500")

# 全局变量
mode = 1  # 1为普通模式，2为故事模式


# Frame
frm0 =tk.Frame(window)
frm1 = tk.Frame(window)
frm2 = tk.Frame(window,width=20,height=20)
frm3 = tk.Frame(window)
frm0.pack()
frm1.pack()
frm2.pack()
frm3.pack()

# 状态栏
tk.Label(frm0,text='状态栏',font=('宋体',25)).pack()
text0 = tk.Text(frm0,height=1,font=('宋体',20),width=30,bg='LightYellow')
text0.pack()
text0_show(0)

# 第一步:提交检查地址
tk.Label(frm1, text='第一步：输入地址', font=('宋体', 30)).pack()
entry1 = tk.Entry(frm1,font=('宋体', 20))
entry1.pack()
tk.Button(frm1,text='提交',font=('宋体', 20), command=submit_path).pack(side='left')
tk.Button(frm1, text='检查', font=('宋体', 20),command=check_path).pack(side='right')

# 第二步:保存读取存档
tk.Label(frm2, text='第二步：输入天数', font=('宋体', 30)).pack()
frm2_l = tk.Frame(frm2)
frm2_r = tk.Frame(frm2)
frm2_l.pack(side='left')
frm2_r.pack(side='right')
entry2_l = tk.Entry(frm2_l,font=('宋体', 20),width = 5)
entry2_r = tk.Entry(frm2_r, font=('宋体', 20),width = 5)
entry2_l.pack()
entry2_r.pack()
tk.Button(frm2_l, text='保存', font=('宋体', 20), command=save_games_with_type).pack()
tk.Button(frm2_r, text='读取', font=('宋体', 20), command=load_games_with_type).pack()

# 切换游戏模式
tk.Label(frm3, text='切换游戏模式', font=('宋体', 25)).pack()
button3_text = tk.StringVar()
button3_text.set('普通模式')
button3 = tk.Button(master=frm3, command=button3_click,font=('宋体', 20), textvariable=button3_text)
button3.pack()


# 窗口运行
window.mainloop()











