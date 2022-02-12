# encoding:utf-8
# @Author :ZQY
import os
import shutil
import tkinter as tk
from tkinter import messagebox


# 报错自定义
class error1(BaseException):
    def __init__(self,msg):
        self.msg = msg
    def __repr__(self):
        return self.msg

class error2(BaseException):
    def __init__(self,msg):
        self.msg = msg
    def __repr__(self):
        return self.msg

# 游戏存档文件名
def type_select(type):
    if type == 1:
        file1 = r'savedgames.alt'
        file2 = r'savedgames'
    if type == 2:
        file1 = r'storiessavedgames.alt'
        file2 = r'storiessavedgames'
    return file1,file2


def find_path(input_dir_name,type=1):
    """
    输入大致目录名，找到存档所在目录
    :param input_dir_name: 大致目录名，越详细越好
    :return: 存档所在目录
    """
    file1,file2 = type_select(type)

    # 注意\和/，可能报错
    dir_name = ""
    judge = False
    for root, dirs, files in os.walk(input_dir_name):
        for file in files:
            if file1 == file:
                dir_name = root
                judge = True
                break
    if judge is False:
        raise error1('请开始一个普通模式，以便定位存档路径')
    return dir_name


def save_dir_name(dir_name):
    """
    保存存档的目录名到save\path.txt
    :param dir_name: 目录名
    :return: None
    """
    # 查询是否有save目录，没有就创建一个
    if not os.path.exists(r'.\save'):
        os.mkdir(r'.\save')

    with open(r".\save\save.txt", 'w') as f:
        f.write(dir_name)

def check_dir_name():
    """
    检查是否提交了路径，查看路径下是否有存档
    :return: str
    """
    try:
        with open(r".\save\save.txt", 'r') as f:
            dir_name = f.readline()
    except:
        raise error1('没有提交路径')

    file1,file2 = type_select(1)
    file3,file4 = type_select(2)
    for file in [file1,file2,file3,file4]:
        if os.path.exists(os.path.join(dir_name,file)):
            return "已提交路径，路径下有存档"
    return "已提交路径，路径下没有存档"



def save_file(day,type=1):
    """
    读取save.txt，再目录中找到存档文件，并保存到day\file中
    如果没有save.txt，报错
    :return: None
    """
    file1, file2 = type_select(type)
    # 确定已经搜索存档路径
    if not os.path.exists(r'.\save\save.txt'):
        raise error1('请先搜索存档路径')

    # 确定有游戏存档
    with open(r'.\save\save.txt','r') as f:
        dir_name = f.readline()
    if not os.path.join(dir_name, file1) or not os.path.join(dir_name, file2):
        raise error1('目前没有存档，请开一局普通模式')

    # 保存游戏存档到save
    saved_name = fr'./save/day{day}'
    if not os.path.exists(saved_name):
        os.mkdir(saved_name)
    shutil.copyfile(os.path.join(dir_name, file1), \
                    os.path.join(saved_name, file1))
    shutil.copyfile(os.path.join(dir_name, file2), \
                    os.path.join(saved_name, file2))


def load_file(day,type=1):
    file1, file2 = type_select(type)

    # 确定已经搜索存档路径
    if not os.path.exists(r'.\save\save.txt'):
        raise error1('请先搜索存档路径')

    # 确定有游戏存档
    with open(r'.\save\save.txt') as f:
        dir_name = f.readline()
    saved_name = fr'./save/day{day}'

    if not os.path.exists(os.path.join(saved_name, file1)) \
            or not os.path.exists(os.path.join(saved_name, file2)):
        raise error1("没有存档文件")
    shutil.copyfile(os.path.join(saved_name, file1), \
                    os.path.join(dir_name, file1))
    shutil.copyfile(os.path.join(saved_name, file2), \
                    os.path.join(dir_name, file2))



if __name__ == "__main__":
    # input_dir_name = r'D:\steam\steam1\userdata'
    # path = find_path(input_dir_name)
    # save_dir_name(path)
    # save_file(27)

    load_file(27)
