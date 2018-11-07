from PIL import Image as Img
from tkinter import *
from tkinter.filedialog import *

opfile={'path' : []}
#out_path=StringVar()  #这话一定要放在app=Tk()之后 因为StringVar()需要一个master 既他需要一个_root


#pack()直接把组件放到其父窗口上,grid()按行列控制组件的具体位置
def make_app() :
    #app=Tk()
    Label(app,text='图片压缩工具',font=('Helvetica',35,'bold')).grid(row=0,columnspan=3)
    Listbox(app,name='lbox').grid(row=1,columnspan=3)
    Label(app,text='选择图片',font=('Helvetica',35,'bold')).grid(row=2,column=0)
    Button(app,text='open',command=gt_file).grid(row=2,column=2)
    Label(app,text='选择输出文件夹',font=('Helvetica',35,'bold')).grid(row=3,column=3)
    Entry(app,textvariable=out_path).grid(row=3,column=4)  # Entry对象是产生一个动态可以输入的条框
    Button(app,text='select',command=gt_output).grid(row=3,column=7)
    Button(app,text='压缩图片',command=compress).grid(row=4,column=4)
    app.geometry('400x400')   #app=Tk()实例化最顶层的父窗口,但是它并不能像之后的子控件一样可以在()内部传送参数来改变他的属性,只能通过实例化后的对象app调用不同属性修改方法来修改这个父窗口的属性
    return app


def gt_file() :
    files=askopenfilenames()
    opfile['path']=files
    lbox=app.children['lbox']
    for file in files :
        fname=file.split('/')[-1]
        lbox.insert(END,fname)
    

def gt_output() :
    path=askdirectory()
    out_path.set(path)  #out_path是一个对象,用set方法来设置值


def compress() :
    if opfile['path'] :
        for path in opfile['path'] :
            out=out_path.get()  # 使用get方法来获取对象中存的路径
            filename='%s/c_%s'%(str(out),path.split('/')[-1])  # 对输出路径进行类型转换
            image=Img.open(path)
            image.save(filename,quality=60)



app=Tk()
out_path=StringVar()  #输出路径用一个实例化的StringVar对象来动态存储输出路径的字符串
app=make_app()
app.mainloop()