import os
import getpass
import socket
import subprocess
import threading
import webbrowser
from re import sub
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from ..Fileop import Fileserver, getip
from ..FTP import Ftpserver
from ..SMTP import Smtpop


def check_port_using_bind(host: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((host, port))
        s.close()
        return True
    except OSError:
        return False


def check_port_using_connect_ex(host: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((host, port))
    s.close()
    if result == 0:
        return True
    return False


class ListboxManager:
    def __init__(self, parent, label_text: str, initboxes: list[str] = None,
                 entrywidth=12, listboxwidth=12,
                 list_max: int = 5, add_true_text: str = "添加成功", add_false_text: str = "添加失败",
                 delete_text: str = "已删除"):
        """
        添加、删除元素组件

        :param parent: 父组件
        :param label_text: Label 信息
        :param initboxes: 初始元素列表
        :param list_max: 最大元素数
        :param add_true_text: 添加成功显示
        :param add_false_text: 添加失败显示
        :param delete_text: 删除显示
        """
        self.parent = parent

        self.boxes = []
        for ib in initboxes:
            if str(ib):
                self.boxes.append(str(ib))

        self.list_max = int(list_max)
        self.add_true_text = add_true_text
        self.add_false_text = add_false_text
        self.delete_text = delete_text

        self.label = ttk.Label(self.parent, text=label_text)
        self.entry = ttk.Entry(self.parent, width=entrywidth)
        self.add_button = ttk.Button(self.parent, text="添加", command=self.add_list)

        self.label.grid(row=0, column=2)
        self.entry.grid(row=1, column=2)
        self.add_button.grid(row=1, column=3)

        self.listbox = tk.Listbox(self.parent, height=5, width=listboxwidth, selectmode=tk.SINGLE)
        self.delete_button = ttk.Button(self.parent, text="删除", command=self.delete_box, state=tk.DISABLED)

        self.listbox.grid(row=2, column=2)
        self.delete_button.grid(row=2, column=3)

        self.status_label = ttk.Label(self.parent, text="")
        self.status_label.grid(row=4, column=1, columnspan=3)

        self.update_listbox()  # 更新初始值列表
        self.listbox.bind('<<ListboxSelect>>', self.check_selection)  # 绑定事件

    def check_selection(self, event):
        """
        检测是否已选中元素

        :param event:
        :return:
        """
        if self.listbox.curselection():  # 如果有选中的元素 则删除按钮可用
            self.delete_button.config(state=tk.NORMAL)
        else:
            self.delete_button.config(state=tk.DISABLED)

    def add_list(self):
        """
        添加元素 不可见字符包括空格制表符等均清除

        :return:
        """
        box = sub(r'[ \t\r\n\f\v\u00A0\u1680\u2000-\u200A\u2028\u2029\u202F\u205F\u3000]+',
                  '', self.entry.get().lower())  # 清除不可见字符
        if not box:
            self.status_label.config(text="输入为空, 添加失败!")
            return

        if self.list_max != 0 and len(self.boxes) == self.list_max:
            self.status_label.config(text=self.add_false_text + "[名单已满]")
            return
        elif box in self.boxes:
            self.status_label.config(text=self.add_false_text + "[名单重复]")
            return

        self.boxes.append(box)
        self.update_listbox()
        self.clear_entry()
        self.status_label.config(text=self.add_true_text)


    def delete_box(self):
        """
        删除元素

        :return:
        """
        index = self.listbox.curselection()[0]
        self.boxes.pop(index)
        self.update_listbox()
        self.status_label.config(text=self.delete_text)
        if self.boxes:
            if index > 1:
                self.listbox.selection_set(index - 1)
            else:
                self.listbox.selection_set(0)
            self.check_selection(None)

    def update_listbox(self):
        """
        更新元素

        :return:
        """
        self.listbox.delete(0, tk.END)
        for box in self.boxes:
            self.listbox.insert(tk.END, box)
        self.check_selection(None)

    def clear_entry(self):
        """
        清除 Entry 输入框的值

        :return:
        """
        self.entry.delete(0, tk.END)

    def get(self):
        """
        返回 元素列表

        :return:
        """
        return self.boxes

class FileServerGUI:
    COMMONWIDTH = 15  # 宽度
    def __init__(self, parent):
        self.frame = parent

        # 共享目录路径
        tk.Label(self.frame, text="共享目录路径", width=self.COMMONWIDTH).grid(row=0, column=0)

        self.path_text = tk.Text(self.frame, width=30, height=4)
        self.path_text.config(state=tk.DISABLED)
        self.path_text.grid(row=0, column=2, rowspan=2)

        def select_directory():
            dir_path = filedialog.askdirectory()
            if dir_path:
                self.path_text.config(state=tk.NORMAL)
                self.path_text.delete("1.0", "end")
                self.path_text.insert(tk.END, dir_path)
                self.path_text.config(state=tk.DISABLED)

        tk.Button(self.frame, text="选择目录", command=select_directory, width=self.COMMONWIDTH).grid(row=0, column=1)

        # 主机端IP
        tk.Label(self.frame, text="主机端IP", width=self.COMMONWIDTH).grid(row=1, column=0)
        ip_list = getip()
        self.host_var = tk.StringVar()
        self.host_var.set(ip_list[-1])
        tk.OptionMenu(self.frame, self.host_var, *ip_list).grid(row=1, column=1)

        # 端口
        tk.Label(self.frame, text="端口", width=self.COMMONWIDTH).grid(row=2, column=0)
        self.port_entry = tk.Entry(self.frame, width=self.COMMONWIDTH)
        self.port_entry.insert(0, "5001")
        self.port_entry.grid(row=2, column=1)

        self.start_button = tk.Button(self.frame, text="启动文件服务器", command=self.toggle_fileserver, width=self.COMMONWIDTH)
        self.start_button.grid(row=3, column=1)

        self.link_text = tk.Label(self.frame, text='', fg='blue', cursor='hand2')
        self.link_text.bind('<Button-1>', lambda e: self.open_link())
        self.link_text.grid(row=3, column=2)

        self.server_thread = None

    def open_link(self):
        webbrowser.open(self.link_text.cget("text"))

    def start_fileserver_thread(self):
        path = self.path_text.get("1.0", tk.END).strip()
        if not path:
            messagebox.showerror("错误", "请选择共享目录路径")
            return
        host = self.host_var.get()
        port = int(self.port_entry.get())
        if 0 < port < 65535:
            if not check_port_using_bind(host, port):
                messagebox.showerror("错误", f"端口{port}被占用，请选择其他端口")
                return
            self.server_thread = threading.Thread(target=self.run_fileserver, args=(path, host, port))
            self.server_thread.start()
            self.link_text.config(text=f"http://{host}:{port}")
        else:
            messagebox.showerror("错误", "端口号必须在0到65535之间")
            return

    def run_fileserver(self, path, host, port):
        self.fs_httpd = None
        def start_fileserver_inner():
            if not self.fs_httpd:
                self.fs_httpd = Fileserver(path, host, port)

        fs_thread = threading.Thread(target=start_fileserver_inner)
        fs_thread.start()

    def stop_fileserver(self):
        if self.server_thread:
            print(f"HTTP service is being shut down")
            self.link_text.config(text="")
            self.fs_httpd.shutdown()
            del self.fs_httpd
            self.server_thread.join()
            self.server_thread = None
            self.start_button.config(text="启动文件服务器")
            print(f"HTTP service is down")

    def toggle_fileserver(self):
        if not self.server_thread:
            self.start_fileserver_thread()
            self.start_button.config(text="关闭文件服务器")
        else:
            self.stop_fileserver()

class FTPServerGUI:
    COMMONWIDTH = 15
    def __init__(self, parent):
        self.frame = parent

        tk.Label(self.frame, text="FTP目录路径 ", width=self.COMMONWIDTH).grid(row=0, column=0)
        self.path_text = tk.Text(self.frame, width=30, height=4)
        self.path_text.config(state=tk.DISABLED)
        self.path_text.grid(row=0, column=2, rowspan=2)

        def select_directory():
            dir_path = filedialog.askdirectory()
            if dir_path:
                self.path_text.config(state=tk.NORMAL)
                self.path_text.delete("1.0", "end")
                self.path_text.insert(tk.END, dir_path)
                self.path_text.config(state=tk.DISABLED)

        tk.Button(self.frame, text="选择目录", command=select_directory, width=self.COMMONWIDTH).grid(row=0, column=1)

        # 主机端IP
        tk.Label(self.frame, text="主机端IP", width=self.COMMONWIDTH).grid(row=1, column=0)
        ip_list = getip()
        self.host_var = tk.StringVar()
        self.host_var.set(ip_list[-1])
        tk.OptionMenu(self.frame, self.host_var, *ip_list).grid(row=1, column=1)

        # 端口
        tk.Label(self.frame, text="端口", width=self.COMMONWIDTH).grid(row=2, column=0)
        self.port_entry = tk.Entry(self.frame, width=self.COMMONWIDTH)
        self.port_entry.insert(0, "2121")
        self.port_entry.grid(row=2, column=1)

        # 账号
        tk.Label(self.frame, text="账号", width=self.COMMONWIDTH).grid(row=3, column=0)
        self.username_entry = tk.Entry(self.frame, width=self.COMMONWIDTH)
        self.username_entry.insert(0, getpass.getuser())
        self.username_entry.grid(row=3, column=1)

        # 密码
        tk.Label(self.frame, text="密码", width=self.COMMONWIDTH).grid(row=4, column=0)
        self.password_entry = tk.Entry(self.frame, width=self.COMMONWIDTH)
        self.password_entry.insert(0, getpass.getuser())
        self.password_entry.grid(row=4, column=1)

        # 权限
        tk.Label(self.frame, text="权限", width=self.COMMONWIDTH).grid(row=5, column=0)
        self.perm_entry = tk.Entry(self.frame, width=self.COMMONWIDTH)
        self.perm_entry.insert(0, "elradfmwMT")
        self.perm_entry.grid(row=5, column=1)


        self.start_button = tk.Button(self.frame, text="启动FTP服务器", command=self.toggle_fileserver,
                                      width=self.COMMONWIDTH)
        self.start_button.grid(row=6, column=1)

        self.server_thread = None

    def start_fileserver_thread(self):
        path = self.path_text.get("1.0", tk.END).strip()
        if not path:
            messagebox.showerror("错误", "请选择共享目录路径")
            return
        host = self.host_var.get()
        port = int(self.port_entry.get())

        username = self.username_entry.get()
        password = self.password_entry.get()
        perm = self.perm_entry.get()
        if 0 < port < 65535:
            if not check_port_using_bind(host, port):
                messagebox.showerror("错误", f"端口{port}被占用，请选择其他端口")
                return
            self.server_thread = threading.Thread(target=self.run_fileserver, args=(path, host, port, username, password, perm))
            self.server_thread.start()
        else:
            messagebox.showerror("错误", "端口号必须在0到65535之间")
            return

    def run_fileserver(self, path, host, port, username, password, perm):
        self.ftp_sr = None

        def start_fileserver_inner():
            if not self.ftp_sr:
                self.ftp_sr = Ftpserver()
                self.ftp_sr.add_user(path, username=username, password=password, perm=perm)
                self.ftp_sr.start(host_res=host, port=port)

        fs_thread = threading.Thread(target=start_fileserver_inner)
        fs_thread.start()

    def stop_fileserver(self):
        if self.server_thread:
            print(f"FTP service is being shut down")
            self.ftp_sr.shutdown()
            del self.ftp_sr
            self.server_thread.join()
            self.server_thread = None
            self.start_button.config(text="启动FTP服务器")
            print(f"FTP service is down")

    def toggle_fileserver(self):
        if not self.server_thread:
            self.start_fileserver_thread()
            self.start_button.config(text="关闭FTP服务器")
        else:
            self.stop_fileserver()

class SMTPClientGUI:
    COMMONWIDTH = 15
    def __init__(self, parent):
        self.frame = parent

        tk.Label(self.frame, text="SMTP服务器地址", width=self.COMMONWIDTH).grid(row=0, column=0)
        self.host_entry = tk.Entry(self.frame, width=self.COMMONWIDTH + 5)
        self.host_entry.insert(0, "smtp.qq.com")
        self.host_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="SMTP服务器端口", width=self.COMMONWIDTH - 2).grid(row=0, column=2)
        self.port_entry = tk.Entry(self.frame, width=self.COMMONWIDTH - 5)
        self.port_entry.insert(0, "587")
        self.port_entry.grid(row=0, column=3)

        tk.Label(self.frame, text="SMTP用户名", width=self.COMMONWIDTH - 2).grid(row=1, column=0)
        self.user_entry = tk.Entry(self.frame, width=self.COMMONWIDTH + 5)
        self.user_entry.insert(0, "")
        self.user_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="SMTP授权码", width=self.COMMONWIDTH - 2).grid(row=1, column=2)
        self.passwd_entry = tk.Entry(self.frame, width=self.COMMONWIDTH + 5, show="*")
        self.passwd_entry.insert(0, "")
        self.passwd_entry.grid(row=1, column=3)

        tk.Label(self.frame, text="邮件主题", width=self.COMMONWIDTH - 2).grid(row=2, column=0)
        self.subject_entry = tk.Entry(self.frame, width=self.COMMONWIDTH + 5)
        self.subject_entry.insert(0, "")
        self.subject_entry.grid(row=2, column=1)

        # 添加附件按钮
        self.add_file_button = tk.Button(self.frame, text="添加附件", command=self.add_files, width=self.COMMONWIDTH)
        self.add_file_button.grid(row=2, column=3)
        self.selected_files = None

        tk.Label(self.frame, text="邮件内容", width=self.COMMONWIDTH - 2).grid(row=2, column=2)
        self.mail_text = tk.Text(self.frame)
        self.mail_text.grid(row=3, column=0, columnspan=3, rowspan=2)

        boxframe = tk.Frame(self.frame)
        boxframe.grid(row=3, column=3, columnspan=1)
        self.lcbobox = ListboxManager(boxframe, "接收邮箱列表", initboxes=[""], entrywidth=self.COMMONWIDTH, listboxwidth=self.COMMONWIDTH, list_max=0)

        self.start_button = tk.Button(self.frame, text="发送邮件", command=self.send_mail, width=self.COMMONWIDTH)
        self.start_button.grid(row=4, column=3)

    def add_files(self):
        file_paths = filedialog.askopenfilenames(title="选择附件", filetypes=[("所有文件", "*.*")])
        if file_paths:
            self.selected_files = file_paths

    def send_mail(self):
        host = self.host_entry.get()
        port = int(self.port_entry.get())
        user = self.user_entry.get()
        passwd = self.passwd_entry.get()
        subject = self.subject_entry.get()
        mail_content = self.mail_text.get("1.0", tk.END)
        if not mail_content:
            messagebox.showerror("错误", "请输入邮件内容")
            return

        recipients = self.lcbobox.get()
        if not recipients:
            messagebox.showerror("错误", "请输入接收邮箱")
            return

        try:
            with Smtpop(host, port, user, passwd) as smtp:
                smtp.add_recipient(recipients)
                for file_path in self.selected_files:
                    smtp.add_file(file_path)
                smtp.send(subject=subject, body=mail_content)
                messagebox.showinfo("成功", "邮件发送成功")
        except Exception as err:
            messagebox.showerror("错误", f"邮件发送失败\n{err}")



class HZGTGUI:
    def __init__(self):
        self.width = 500
        self.height = 300

        self.root = tk.Tk()
        self.root.title("HZGT")
        # self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False, False)

        self.create_notebook()
        self.root.mainloop()

    def create_notebook(self, default_dict=None):
        # 创建选项卡
        notebook = ttk.Notebook(self.root)

        # 创建页面框架
        fs_frame = ttk.Frame(notebook)
        if not default_dict:
            self.fs_interface(fs_frame)
        else:
            self.fs_interface(fs_frame, default_dict["fs"])
        notebook.add(fs_frame, text='文件服务器')

        # 创建页面框架
        ftp_frame = ttk.Frame(notebook)
        if not default_dict:
            self.ftp_interface(ftp_frame)
        else:
            self.ftp_interface(ftp_frame, default_dict["ftp"])
        notebook.add(ftp_frame, text='FTP 服务器')

        # 创建页面框架
        smtp_frame = ttk.Frame(notebook)
        if not default_dict:
            self.smtp_interface(smtp_frame)
        else:
            self.smtp_interface(smtp_frame, default_dict["smtp"])
        notebook.add(smtp_frame, text='SMTP 客户端')

        notebook.grid(column=0, row=0)

    def fs_interface(self, frame, default_dict=None):
        FileServerGUI(frame)

    def ftp_interface(self, frame, default_dict=None):
        FTPServerGUI(frame)

    def smtp_interface(self, frame, default_dict=None):
        SMTPClientGUI(frame)
