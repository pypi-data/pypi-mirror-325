import gui_creater as gc
import gui_easily as ge
import upload as up
def Create_new_widget():
    def onbd():
        up.tkinter_running(root.run("inp","-get","1.0","end-1c"))
    def onb():
        dir=ge.openafileasdir()
        with open(dir,mode="r") as f:
            data=f.read()
            root.run("inp","-insert","insert",data)
    root = gc.Windows()
    root.add("-Window","root")
    root.run("root","-geometry","600x500")
    root.run("root","-title","控件设计")
    root.add("-Text","txt","root",args={"text":"请输入程序"})
    root.add("-Button","b","root",placewhere=("pack",{"side":gc.UP}),args={"text":"打开","command":onb})
    root.add("-Button","bt","root",placewhere=("pack",{"side":gc.UP}),args={"text":"上传","command":onbd})
    root.add("-Input","inp","root",placewhere=("pack",{"side":gc.LEFT}),args={"width":80,"height":30})
    root.add("-Scrollbar","scb","root",placewhere=("pack",{"side":gc.RIGHT,"fill":"y"}),args={"command":
                                                                                            root.get_attr("inp","-yview")})
    root.run("inp","-configure",yscrollcommand=root.get_attr("scb","-set"))
    root.start()
