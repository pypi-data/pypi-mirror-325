import gui_creater as gc
def labelbox(title,label):
    root=gc.Windows()
    root.add("-Window","1")
    root.run("1","-title",title)
    root.add("-Text","2","1",args={"text":label})
    root.add("-Button","3","1",args={"text":"确定","command":lambda:root.run("1","-destroy")})
    root.start()
def buttonsbox(title,text,texts=[],value=[]):
    def show(value,i):
        return lambda:print(value[i])
    root=gc.Windows()
    root.add("-Window","1")
    root.run("1","-title",title)
    root.add("-Text","2","1",args={"text":text})
    for i in range(len(texts)):
        d=show(value,i)
        root.add("-Button",f"{i}","1",args={"text":texts[i],"command":d})
    root.start()
def listbox(title,text,texts=[]):
    def show(event):
        w=event.widget
        selected_item = w.get(w.curselection())
        print(selected_item)
        return selected_item
    root=gc.Windows()
    root.add("-Window","1")
    root.run("1","-title",title)
    root.add("-Text","2","1",args={"text":text})
    root.add("-Listbox","3","1")
    for i in range(len(texts)):
        root.run("3","-insert",i,texts[i])
    root.run("3","-bind","<<ListboxSelect>>",show)
    root.start()
showinfo=gc.Messagebox.showinfo
showerror=gc.Messagebox.showerror
showwarning=gc.Messagebox.showwarning
askyesno=gc.Messagebox.askyesno
askyesnocancel=gc.Messagebox.askyesnocancel
askokcancel=gc.Messagebox.askokcancel
askquestion=gc.Messagebox.askquestion
askretrycancel=gc.Messagebox.askretrycancel
openafile=gc.Filedialog.askopenfile
openfiles=gc.Filedialog.askopenfiles
openafileasdir=gc.Filedialog.askopenfilename
openfilesasdir=gc.Filedialog.askopenfilenames
opendir=gc.Filedialog.askdirectory
saveafile=gc.Filedialog.asksaveasfile
saveafileasdir=gc.Filedialog.asksaveasfilename