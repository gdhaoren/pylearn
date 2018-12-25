#  压缩图片 制作界面

from PIL import Image as Img #由于pillow库中的Image方法和tkinter中的存在名字冲突
from tkinter import *
from tkinter.filedialog import *

# path=
# output=
# image=img.open(path)
# image.save(output,60)

names={'path':[]} #用全局变量来沟通函数之间的数据

def make_app() :
    app=Tk()
    Label(app,text='图片压缩',font=('Hack',25,'bold')).pack()
    Listbox(app,name='lbox',bg='#f2f2f2').pack(fill=BOTH,expand=True)
    Button(app,text='添加图片',command=opfile).pack()
    Button(app,text='压缩',command=compress).pack()
    app.geometry('300x400')
    return app

def opfile() :
    filnames=askopenfilenames()
    lbox=app.children['lbox']   #这里使用了app这个名字 它并不是来自于make_app 中的app 而是在写主循环的时候定义的app=make_app(),改了名字就会报错
#    names=  这个用法是错误的 不要在函数内部为任何全局变量赋值，只能去更新它的元素
    names['path']=filnames
    if names['path'] : #防止没有放入任何文件
        for f in filnames:
            lbox.insert(END, f.split('/')[-1])
            # abc.jpg

def compress() :
    for path in names['path'] :
        output='C:/Users/Jelly/Desktop/'
        name=path.split('/')[-1]
        output='%sc_%s'%(output,name)
        image=Img.open(path)
        image.save(output,quality=30)

app=make_app()
app.mainloop()
