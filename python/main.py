#coding=utf-8
import tkinter as tk
import os
import sys
from tkinter import filedialog, ttk
import imxdownload
import subprocess


class GuiAttribute:
    def __init__(self):
        self.flag = "False"
        self.disk = None
        self.folder_path = "/home/"  # 第一次默认文件夹路径为 /home
        # 顶层窗口
        self.root = tk.Tk()
        self.creat_window()
        # 一些变量
        self.bin_file = tk.StringVar()
        self.ddr = tk.StringVar(value="ddr512mb")  # 默认DDR512MB
        self.comb = ttk.Combobox(self.root, values=self.disk)
        # 工具简介
        self.info = tk.Text(self.root, background="white", foreground="red")
        # self.application()

    def application(self):
        self.window_info()
        # bin文件选择
        self.lbox_bin()
        self.select_sd_card()
        self.select_bin_but()
        self.start_down_but()
        self.select_ddr()
        self.label()
        self.root.mainloop()

    # 新建一个窗口
    def creat_window(self):
        self.root.title("IMX6ULL烧录工具")
        self.root.geometry("350x300")
        self.root.resizable(False, False)

    # 显示窗口信息
    def window_info(self):
        self.info.insert("end", "I.MX6ULL bin download software\n")
        self.info.insert("end", "\n作者:点灯大师")
        self.info.insert("end", "\n日期:2023.6.10")
        self.info.insert("end", "\n版本:V1.0")
        self.info.insert("end", "\n说明:支持512MB/256MB DDR3")
        self.info.insert("end", "\ngit:https://github.com/zleihao/")
        self.info.place(x=0, y=0, width=350, height=130)

    def label(self):
        tk.Label(self.root, text="bin文件:", font=("Arial", 10), height=1).place(x=0, y=150)  # label_file
        tk.Label(self.root, text="SD Card:", font=("Arial", 10), height=1).place(x=0, y=190)  # label_disk

    def lbox_bin(self):
        tk.Listbox(self.root, width=28, height=1, listvariable=self.bin_file).place(x=60, y=150)

    # 选择磁盘
    def select_sd_card(self):
        # 执行命令，并将输出保存到变量中
        output = subprocess.check_output("ls /dev/sd*", shell=True)
        # 打印输出结果
        self.disk = output.decode()
        self.comb.config(values=self.disk)  # 更新下拉框
        self.comb.place(x=60, y=190)

    # 选择bin文件按钮
    def select_bin_but(self):
        tk.Button(self.root, text="...", width=10, height=1, command=self.select_file).place(x=250, y=150)

    # Start按钮
    def start_down_but(self):
        tk.Button(self.root, text="Start", width=10, height=1, command=self.start_down).place(x=100, y=250)

    # 按钮回调函数
    # 选择bin文件
    def select_file(self):
        file_path = filedialog.askopenfilename(initialdir=self.folder_path)
        self.bin_file.set(file_path)
        self.folder_path = os.path.dirname(file_path)
    
    # 选择DDR大小
    def select_ddr(self):
        tk.Radiobutton(self.root, text="DDR256", variable=self.ddr, value="ddr256mb", width=10, height=1,
                       ).place(x=40, y=220)
        tk.Radiobutton(self.root, text="DDR512", variable=self.ddr, value="ddr512mb", width=10, height=1,
                       ).place(x=170, y=220)

    # 开始烧录
    def start_down(self):
        self.info.delete(1.0, "end")
        argv = [sys.argv[0], self.bin_file.get()[2:-3], self.comb.get(), self.ddr.get()]
        imxdownload.write_file(argv, self.info, self.flag)
        self.flag = "True"


if __name__ == "__main__":
    if sys.platform != "linux":
        print("请使用linux系统运行.....")
        sys.exit(-1)
    my_app = GuiAttribute()
    my_app.application()
