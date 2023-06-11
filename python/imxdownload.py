#coding=utf-8
import struct
import subprocess
import tkinter as tk

imx6_512mb_ivtdcd_table = [
    0X402000D1, 0X87800000, 0X00000000, 0X877FF42C, 0X877FF420, 0X877FF400, 0X00000000, 0X00000000,
    0X877FF000, 0X00200000, 0X00000000, 0X40E801D2, 0X04E401CC, 0X68400C02, 0XFFFFFFFF, 0X6C400C02,
    0XFFFFFFFF, 0X70400C02, 0XFFFFFFFF, 0X74400C02, 0XFFFFFFFF, 0X78400C02, 0XFFFFFFFF, 0X7C400C02,
    0XFFFFFFFF, 0X80400C02, 0XFFFFFFFF, 0XB4040E02, 0X00000C00, 0XAC040E02, 0X00000000, 0X7C020E02,
    0X30000000, 0X50020E02, 0X30000000, 0X4C020E02, 0X30000000, 0X90040E02, 0X30000000, 0X88020E02,
    0X30000C00, 0X70020E02, 0X00000000, 0X60020E02, 0X30000000, 0X64020E02, 0X30000000, 0XA0040E02,
    0X30000000, 0X94040E02, 0X00000200, 0X80020E02, 0X30000000, 0X84020E02, 0X30000000, 0XB0040E02,
    0X00000200, 0X98040E02, 0X30000000, 0XA4040E02, 0X30000000, 0X44020E02, 0X30000000, 0X48020E02,
    0X30000000, 0X1C001B02, 0X00800000, 0X00081B02, 0X030039A1, 0X0C081B02, 0X0B000300, 0X3C081B02,
    0X44014801, 0X48081B02, 0X302C4040, 0X50081B02, 0X343E4040, 0X1C081B02, 0X33333333, 0X20081B02,
    0X33333333, 0X2C081B02, 0X333333F3, 0X30081B02, 0X333333F3, 0XC0081B02, 0X09409400, 0XB8081B02,
    0X00080000, 0X04001B02, 0X2D000200, 0X08001B02, 0X3030331B, 0X0C001B02, 0XF3526B67, 0X10001B02,
    0X630B6DB6, 0X14001B02, 0XDB00FF01, 0X18001B02, 0X40172000, 0X1C001B02, 0X00800000, 0X2C001B02,
    0XD2260000, 0X30001B02, 0X23106B00, 0X40001B02, 0X4F000000, 0X00001B02, 0X00001884, 0X90081B02,
    0X00004000, 0X1C001B02, 0X32800002, 0X1C001B02, 0X33800000, 0X1C001B02, 0X31800400, 0X1C001B02,
    0X30802015, 0X1C001B02, 0X40800004, 0X20001B02, 0X00080000, 0X18081B02, 0X27020000, 0X04001B02,
    0X2D550200, 0X04041B02, 0X06100100, 0X1C001B02, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000
]

imx6_256mb_ivtdcd_table = [
    0X402000D1, 0X87800000, 0X00000000, 0X877FF42C, 0X877FF420, 0X877FF400, 0X00000000, 0X00000000,
    0X877FF000, 0X00076000, 0X00000000, 0X40E801D2, 0X04E401CC, 0X68400C02, 0XFFFFFFFF, 0X6C400C02,
    0XFFFFFFFF, 0X70400C02, 0XFFFFFFFF, 0X74400C02, 0XFFFFFFFF, 0X78400C02, 0XFFFFFFFF, 0X7C400C02,
    0XFFFFFFFF, 0X80400C02, 0XFFFFFFFF, 0XB4040E02, 0X00000C00, 0XAC040E02, 0X00000000, 0X7C020E02,
    0X30000000, 0X50020E02, 0X30000000, 0X4C020E02, 0X30000000, 0X90040E02, 0X30000000, 0X88020E02,
    0X30000C00, 0X70020E02, 0X00000000, 0X60020E02, 0X30000000, 0X64020E02, 0X30000000, 0XA0040E02,
    0X30000000, 0X94040E02, 0X00000200, 0X80020E02, 0X30000000, 0X84020E02, 0X30000000, 0XB0040E02,
    0X00000200, 0X98040E02, 0X30000000, 0XA4040E02, 0X30000000, 0X44020E02, 0X30000000, 0X48020E02,
    0X30000000, 0X1C001B02, 0X00800000, 0X00081B02, 0X030039A1, 0X0C081B02, 0X04000000, 0X3C081B02,
    0X3C013C01, 0X48081B02, 0X38324040, 0X50081B02, 0X28304040, 0X1C081B02, 0X33333333, 0X20081B02,
    0X33333333, 0X2C081B02, 0X333333F3, 0X30081B02, 0X333333F3, 0XC0081B02, 0X09409400, 0XB8081B02,
    0X00080000, 0X04001B02, 0X2D000200, 0X08001B02, 0X3030331B, 0X0C001B02, 0XF352433F, 0X10001B02,
    0X630B6DB6, 0X14001B02, 0XDB00FF01, 0X18001B02, 0X40172000, 0X1C001B02, 0X00800000, 0X2C001B02,
    0XD2260000, 0X30001B02, 0X23104300, 0X40001B02, 0X47000000, 0X00001B02, 0X00001883, 0X90081B02,
    0X00004000, 0X1C001B02, 0X32800002, 0X1C001B02, 0X33800000, 0X1C001B02, 0X31800400, 0X1C001B02,
    0X30802015, 0X1C001B02, 0X40800004, 0X20001B02, 0X00080000, 0X18081B02, 0X27020000, 0X04001B02,
    0X2D550200, 0X04041B02, 0X06100100, 0X1C001B02, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
    0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000, 0X00000000,
]

BIN_OFFSET = 768


# linux系统下运行命令
def run_command_with_password(dd_command, password_flag, info):
    # 首次打开需要输入密码，再次运行则不需要
    if password_flag == "False":
        # 创建tkinter窗口
        window = tk.Tk()

        # 设置窗口标题
        window.title("输入密码")

        # 创建标签和密码输入框
        label = tk.Label(window, text="请输入密码:")
        label.pack()
        password_entry = tk.Entry(window, show='*')
        password_entry.pack()

        def execute_command():
            # 获取输入的密码
            password = password_entry.get()

            # 关闭tkinter窗口
            window.destroy()

            # 在Bash中执行需要密码的命令
            command = f"echo '{password}' | sudo -S {dd_command}"
            process = subprocess.Popen(command, shell=True)
            process.wait()
            info.insert("end", '\n' + "Successful...")

        # 创建按钮
        button = tk.Button(window, text="确定", command=execute_command)
        button.pack()
    else:
        command = f"sudo {dd_command}"
        process = subprocess.Popen(command, shell=True)
        process.wait()
        info.insert("end", '\n' + "Successful...")
        return


def write_file(argv: list, info, flag):
    # 打开bin文件
    fp = open(argv[1], "rb")

    fp.seek(0, 2)
    file_len = fp.tell()
    fp.seek(0, 0)
    info.insert("end", f"bin文件:{argv[1]}\nbin文件大小:{file_len}Bytes\n")

    buf = fp.read(file_len)
    # 关闭bin文件
    fp.close()

    # 选择DDR的大小
    if argv[3] == "ddr256mb":
        ivtdcd_table = imx6_256mb_ivtdcd_table
    elif argv[3] == "ddr512mb":
        ivtdcd_table = imx6_512mb_ivtdcd_table
    info.insert("end", f"DDR:{argv[3]}\n")

    # 将ivtdcd_table插入到bin文件前面
    buf = struct.pack("I" * BIN_OFFSET, *(ivtdcd_table + [0] * (BIN_OFFSET - len(ivtdcd_table)))) + buf

    # 将bin文件和头部写入到文件load.imx中
    with open("load.imx", "wb") as fp:
        fp.write(buf)

    # 判断在参数是否够
    if argv[2] == '':
        info.delete(1.0, "end")
        info.insert("end", "请选择SD卡的盘符.....")
        return

    info.insert("end", "烧录结果:")
    # dd命令
    command = f"dd iflag=dsync oflag=dsync if=load.imx of={argv[2]} seek=2"
    run_command_with_password(command, flag, info)