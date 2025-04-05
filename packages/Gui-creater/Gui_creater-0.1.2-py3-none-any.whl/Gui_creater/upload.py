import socket
import tkinter
def tkinter_running(data):
    import tkinter as tk
    root=tk.Tk()
    root.title("发送")
    root.geometry("200x200")
    button=tk.Button(root,text="发送并更新扩展控件",command=lambda:start_client(root,mss=data))
    button.pack()
    root.mainloop()
 
def start_client(master:tkinter.Tk,host='192.168.1.8', port=65432,mss:str=""):
    import tkinter.messagebox as ms
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            message = "add"
            client_socket.sendall(message.encode())
            message = mss
            import time
            time.sleep(2)
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(data)
            if data.decode()=="add finish @ code 1":
                ms.showinfo("提示","上传成功")
            else:
                ms.showinfo("提示","上传失败，请重试")
                return
            message = "get"
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            file_string=data.decode()
            with open("widget_data.py",mode="w") as f:
                f.write(file_string)
            ms.showinfo("提示","更新成功")
            client_socket.close()
            master.destroy()
            print("Connection closed.")
    except:
        ms.showerror("提示","服务器未工作，请换个时间再试")  

 
def upgrade(host='192.168.1.8', port=65432):
    import tkinter.messagebox as ms
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            message = "get"
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            file_string=data.decode()
            with open("widget_data.py",mode="w") as f:
                f.write(file_string)
            ms.showinfo("提示","更新成功")
            client_socket.close()
            print("Connection closed.")
    except:
        ms.showerror("提示","服务器未工作，请换个时间再试")

