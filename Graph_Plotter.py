import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import sys
import math
import Tkinter as Tk
import time
import ttk
from PIL import ImageTk,Image

#Setting up the kitchen
root = Tk.Tk()
root.title("Maths is an Art")
root.configure(background="#b3ffb3")

scbar=Tk.Scrollbar(root)

#styling equipments
style = ttk.Style()
style.configure("BW.TLabel",background="#b3ffb3", foreground="#006600",font=('Harrington',50) ,fontstyle="Bold")
style.configure("BW.TButton",background="#70db70", foreground="black",font=('Century Gothic',18) ,fontstyle="Bold")


#recipe goes like this:

#Declaring frames
f1=Tk.Frame(root,bg="#b3ffb3")
f2=Tk.Frame(root,bg="#b3ffb3")
f3=Tk.Frame(root,bg="#b3ffb3")

#Functions to initialise Frames
def _shw1():
    f2.grid_remove()
    f3.grid_remove()
    f1.grid(row=3,column=0,columnspan=4)
   
    
def _shw2():
    f1.grid_remove()
    f3.grid_remove()
    f2.grid(row=3,column=0,columnspan=4)

def _shw3():
    f1.grid_remove()
    f2.grid_remove()
    f3.grid(row=3,column=0,columnspan=4)

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate    
#Name of dish
ltitle=ttk.Label(root,text="Mathematics is an Art!",style="BW.TLabel")
ltitle.grid(row=0,column=0,columnspan=4)
txt=ttk.Label(root,text="Have you ever seen a mathematician dance?",style="BW.TLabel",font=('Candara',25))
txt.grid(row=1,column=0,columnspan=3, sticky='W')


#On the Menu bar
Btn1=ttk.Button(root,text="Home",command=_shw1,style="BW.TButton")
Btn2=ttk.Button(root,text="Plot",command=_shw2,style="BW.TButton")
Btn3=ttk.Button(root,text="Learn",command=_shw3,style="BW.TButton")
Btn1.grid(row=2,column=0)
Btn2.grid(row=2,column=1)
Btn3.grid(row=2,column=2)
button = ttk.Button(master=root, text='Quit', command=_quit,style="BW.TButton")
button.grid(row=2,column=3)

#inside Frame1
f = Figure(figsize=(5,5), dpi=100)
# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=f1)
canvas.show()
canvas.get_tk_widget().grid(row=0, column=0,columnspan=4,rowspan=8)
toolbar = NavigationToolbar2TkAgg(canvas,f1)
toolbar.grid(row=9, column=0, columnspan=4)

#functions for the mathematician
a = f.add_subplot(111)
a.grid(True)
c=np.linspace(-100,100,100)
b=np.linspace(-100,100,100)
A,B=np.meshgrid(c,b)
#character
def ch():
    a.plot([-100,100],[0,0],'y')
    a.plot([0,0],[-100,100],'y')
    F=((A**2))+(((B-7)**2))-49
    a.contour(A,B,F,[0])
    Z=((A**2)/7)+(((B+19)**2)/37)-10
    a.contour(A,B,Z,[0])
    a.plot([5,7,12],[-34,-59,-59],'g',[-5,-7,-12],[-34,-59,-59],'g')

def ch1():
    a.cla()
    a.plot([-100,100],[0,0],'y')
    a.plot([0,0],[-100,100],'y')
    F=((A**2))+(((B-7)**2))-49
    a.contour(A,B,F,[0])
    Z=((A**2)/7)+(((B+19)**2)/37)-10
    a.contour(A,B,Z,[0])
    a.plot([5,9,7,12],[-34,-46,-59,-59],'g',[-5,-7,-12],[-34,-59,-59],'g')
    a.plot([0,-17,-5],[0,-9,-30],'g',[0,15,10],[0,9,30],'g')
    canvas.draw()
    
def ch2():
    a.cla()
    a.plot([-100,100],[0,0],'y')
    a.plot([0,0],[-100,100],'y')
    F=((A**2))+(((B-7)**2))-49
    a.contour(A,B,F,[0])
    Z=((A**2)/7)+(((B+19)**2)/37)-10
    a.contour(A,B,Z,[0])
    a.plot([5,7,12],[-34,-59,-59],'g',[-5,-9,-7,-12],[-34,-46,-59,-59],'g')
    a.plot([0,17,5],[0,-9,-30],'g',[0,-15,-10],[0,9,30],'g')
    canvas.draw()
    
def ch3():
    a.cla()
    a.set_title("Let's do the Maths dance!")
    a.plot([-100,100],[0,0],'y')
    a.plot([0,0],[-100,100],'y')
    F=((A**2))+(((B-7)**2))-49
    a.contour(A,B,F,[0])
    Z=((A**2)/7)+(((B+19)**2)/37)-10
    a.contour(A,B,Z,[0])
    a.plot([5,7,12],[-34,-59,-59],'g',[-5,-9,-7,-12],[-34,-46,-59,-59],'g')
    a.plot([0,17,5],[0,-9,-30],'g',[0,-15,-20],[0,9,30],'g')
    canvas.draw()

#y=x
def _yx():
    a.cla()
    a.set_title('y=x')
    ch()
    x=[i for i in range(-20,20)]
    y=[i for i in x]
    a.plot(x,y,'g')
    canvas.draw()

#y=x^2
def _yx2():
    a.cla()
    a.set_title('y=x^2')
    ch()
    x=[i for i in range(-14,15)]
    y=[(i**2)/5 for i in x]
    a.plot(x,y,'g')
    canvas.draw()

#y=-x^2
def _y_x2():
    a.cla()
    a.set_title('y=-x^2')
    ch()
    x=[i for i in range(-14,15)]
    y=[-(i**2)/5 for i in x]
    a.plot(x,y,'g')
    canvas.draw()

#y=-x^3
def _y_x3():
    a.cla()
    a.set_title('y=-x^3')
    ch()
    x=[i for i in range(-13,14)]
    y=[-(i**3)/65 for i in x]
    a.plot(x,y,'g')
    canvas.draw()

#y=x^3
def _yx3():
    a.cla()
    a.set_title('y=x^3')
    ch()
    x=[i for i in range(-13,14)]
    y=[(i**3)/65 for i in x]
    a.plot(x,y,'g')
    canvas.draw()

#y=-x
def _y_x():
    a.cla()
    a.set_title('y=-x')
    ch()
    x=[i for i in range(-20,20)]
    y=[-i for i in x]
    a.plot(x,y,'g')
    canvas.draw()

#for the dance
def dnc():
    for i in range(6):
        ch2()
        ch3()
    for i in range(3):
        time.sleep(0.08)
        ch1()
        time.sleep(0.08)
        _yx()
        time.sleep(0.08)
        _y_x()
        time.sleep(0.08)
        ch1()
        time.sleep(0.08)
        _yx()
        time.sleep(0.08)
        _y_x()
        time.sleep(0.08)
        ch2()
        time.sleep(0.08)
        _yx2()
        time.sleep(0.08)
        _y_x2()
        time.sleep(0.08)
        ch2()
        time.sleep(0.08)
        _yx2()
        time.sleep(0.08)
        _y_x2()
        time.sleep(0.08)
        ch1()
        time.sleep(0.08)
        _yx3()
        time.sleep(0.08)
        _y_x3()
        time.sleep(0.08)
        ch2()
        time.sleep(0.08)
        _yx3()
        time.sleep(0.08)
        _y_x3()
        time.sleep(0.08)
        ch2()
        time.sleep(0.08)
        sinx()
        time.sleep(0.08)
        _sinx()
        time.sleep(0.08)
        ch1()
        time.sleep(0.08)
        sinx()
        time.sleep(0
                   )
        _sinx()
    ch1()

def sinx():
    a.cla()
    a.set_title('y=sin(x)')
    ch()
    x=[i for i in range(-20,21,10)]
    y=[12*(math.sin(i)) for i in x]
    a.plot(x,y,'g')
    canvas.draw()

def _sinx():
    a.cla()
    a.set_title('y=-sin(x)')
    ch()
    x=[i for i in range(-20,21,10)]
    y=[-12*(math.sin(i)) for i in x]
    a.plot(x,y,'g')
    canvas.draw()

_shw1()

lbl1=Tk.Label(f1,text="Here are some standard graphs",font=('Century Gothic',18),background="#b3ffb3", foreground="#006600")
lbl1.grid(row=0,column=5,columnspan=3,sticky="W")
b1 =Tk.Button(master=f1, text='y=x', command=_yx,font=('Century Gothic',12),background="#85e085", foreground="black",padx="14px",pady="2px")
b1.grid(row=1,column=5,sticky="W")
b3 = Tk.Button(master=f1, text='y=-x', command=_y_x,font=('Century Gothic',12),background="#85e085", foreground="black",padx="12px",pady="2px")
b3.grid(row=1,column=6,sticky="W")
b2 = Tk.Button(master=f1, text='y=x^2', command=_yx2, font=('Century Gothic',12),background="#85e085", foreground="black",padx="4px",pady="2px")
b2.grid(row=1,column=7,sticky="W")
b12 = Tk.Button(master=f1, text='y=-(x^2)', command=_y_x2, font=('Century Gothic',12),background="#85e085", foreground="black",padx="1px",pady="2px")
b12.grid(row=2,column=5,sticky="W")
b10 = Tk.Button(master=f1, text='y=x^3', command=_yx3, font=('Century Gothic',12),background="#85e085", foreground="black",padx="6px",pady="2px")
b10.grid(row=2,column=6,sticky="W")
b11 = Tk.Button(master=f1, text='y=-(x^3)', command=_y_x3, font=('Century Gothic',12),background="#85e085", foreground="black",padx="2px",pady="2px")
b11.grid(row=2,column=7,sticky="W")
b8 = Tk.Button(master=f1, text='y=sin(x)', command=sinx, font=('Century Gothic',12),background="#85e085", foreground="black",padx="2px",pady="2px")
b8.grid(row=3,column=5,sticky="W")
b9 = Tk.Button(master=f1, text='y=-sin(x)', command=_sinx, font=('Century Gothic',12),background="#85e085", foreground="black",padx="1px",pady="2px")
b9.grid(row=3,column=6,sticky="W")
b4 = Tk.Button(master=root, text='Watch Now!', command=dnc,font=('Century Gothic,Bold',17),background="#85e085", foreground="black")
b4.grid(row=1,column=3)
lb1=Tk.Label(f1,text="Algebraic Equation: Help. I lost my 'X' (~_~)",font=('Century Gothic',14),background="#b3ffb3", foreground="#006600")
lb1.grid(row=4,column=4,columnspan=4,sticky="W")
lb2=Tk.Label(f1,text="Coordinate Geometry: I'll figure it out! (*_*)",font=('Century Gothic',14),background="#b3ffb3", foreground="#006600")
lb2.grid(row=5,column=4,columnspan=4,sticky="W")
bp=Tk.Button(f1,text="Let's plot it!",command=_shw2,font=('Century Gothic',14),background="white", foreground="#006600")
bp.grid(row=6,column=7)
f1.grid_columnconfigure(4,minsize=30)
f1.grid_columnconfigure(8,minsize=10)
#inside of Frame2
f_1 = Figure(figsize=(5,5), dpi=100)
# a tk.DrawingArea
canvas_1 = FigureCanvasTkAgg(f_1, master=f2)
canvas_1.show()
canvas_1.get_tk_widget().grid(row=0, column=0, columnspan=4,rowspan=12)
toolbar = NavigationToolbar2TkAgg(canvas_1,f2)
toolbar.grid(row=13, column=0, columnspan=5)


a_1 = f_1.add_subplot(111)
a_1.grid(True)
c_1=np.linspace(-100,100,100)
b_1=np.linspace(-100,100,100)
A_1,B_1=np.meshgrid(c_1,b_1)

def setup():
    a_1.cla()
    a_1.grid(True)
    a_1.set_xlim(-100,100)
    a_1.set_ylim(-100,100)
    a_1.plot([0,0],[-100,100],'g',[-100,100],[0,0],'g')

def xy():
    setup()
    m=mg.get()
    m=int(m)
    c=cg.get()
    c=int(c)
    x=[i for i in range(-70,71)]
    y=[(m*i)+c for i in x]
    setup()
    a_1.plot(x,y)
    canvas_1.draw()

def x2y2():
    setup()
    r=rg.get()
    r=int(r)
    x=xg.get()
    x=int(x)
    y=yg.get()
    y=int(y)
    F_1=((A_1-x)**2)+((B_1-y)**2)-(r**2)
    a_1.contour(A_1,B_1,F_1,[0])
    canvas_1.draw()

def x2x():
    setup()
    a1=ag.get()
    a1=int(a1)
    b=bg.get()
    b=int(b)
    c=gxc.get()
    c=int(b)
    x=[i for i in range(-70,71)]
    y=[(a1*(i**2)+(b*i)+c) for i in x]
    a_1.plot(x,y)
    canvas_1.draw()


#y=mx+c
lbl2=Tk.Label(f2,text='Equation of line:"y=mx+c"',font=('Century Gothic',15),background="#b3ffb3", foreground="#006600")
lbl2.grid(row=0,column=6,columnspan=8,sticky="W")
lm=Tk.Label(f2,text="y=",width=5,font=('Century Gothic',13),background="#b3ffb3")
lm.grid(row=1,column=6)
mg=Tk.Entry(f2,width=5,font=('Century Gothic',13))
mg.grid(row=1,column=7)
lc=Tk.Label(f2,text="x+",width=5,font=('Century Gothic',13),background="#b3ffb3")
lc.grid(row=1,column=8)
cg=Tk.Entry(f2,width=5,font=('Century Gothic',13))
cg.grid(row=1,column=9)
button=Tk.Button(f2,text="Go",width=5,command=xy,font=('Century Gothic',11),background="#b3ffb3")
button.grid(row=1, column=10)

#x2+y2=r2
lbl3=Tk.Label(f2,text='Equation of circle:"(x^2)+(y^2)=(r^2)"',font=('Century Gothic',15),background="#b3ffb3", foreground="#006600")
lbl3.grid(row=2,column=6,columnspan=8,sticky="W")
lx=Tk.Label(f2,text="Enter centre(x,y):",font=('Century Gothic',13),background="#b3ffb3")
lx.grid(row=3,column=6,columnspan=3)
xg=Tk.Entry(f2,width=5,font=('Century Gothic',13))
xg.grid(row=3,column=9)
yg=Tk.Entry(f2,width=5,font=('Century Gothic',13))
yg.grid(row=3,column=10)
lr=Tk.Label(f2,text="Enter radius:",font=('Century Gothic',13),background="#b3ffb3")
lr.grid(row=4,column=6,columnspan=3)
rg=Tk.Entry(f2,width=5,font=('Century Gothic',13))
rg.grid(row=4,column=9)
button1=Tk.Button(f2,text="Go",command=x2y2,font=('Century Gothic',11),background="#b3ffb3")
button1.grid(row=4, column=10)
f2.grid_columnconfigure(8,minsize=5)
f2.grid_columnconfigure(7,minsize=5)

#ax2+bx+c
lbl4=Tk.Label(f2,text='Equation of parabola:"a*(x^2)+b(x)+c"',font=('Century Gothic',15),background="#b3ffb3", foreground="#006600")
lbl4.grid(row=5,column=6,columnspan=8,sticky="W")
ag=Tk.Entry(f2,width=5,font=('Century Gothic',13))
ag.grid(row=6,column=6)
lb=Tk.Label(f2,text="x^2+",font=('Century Gothic',13),background="#b3ffb3")
lb.grid(row=6,column=7)
bg=Tk.Entry(f2,width=5,font=('Century Gothic',13))
bg.grid(row=6,column=8)
lxc=Tk.Label(f2,text="x+",font=('Century Gothic',13),background="#b3ffb3")
lxc.grid(row=6,column=9)
gxc=Tk.Entry(f2,width=5,font=('Century Gothic',13))
gxc.grid(row=6,column=10)
button2=Tk.Button(f2,text="Go",command=x2x,font=('Century Gothic',11),background="#b3ffb3")
button2.grid(row=6, column=11)

f2.grid_columnconfigure(5,minsize=30)
f2.grid_columnconfigure(12,minsize=10)
#getting to next frame
nxtl=Tk.Label(f2,text='Want to see how I do it?',font=('Century Gothic',14),background="#b3ffb3", foreground="#006600")
nxtl.grid(row=7,column=6,columnspan=8,sticky="W")
bl=Tk.Button(f2,text="Come!",command=_shw3,font=('Century Gothic',14),background="white", foreground="#006600")
bl.grid(row=8,column=11)

#inside of Frame3
f_2 = Figure(figsize=(5,5), dpi=100)
# a tk.DrawingArea
canvas_2 = FigureCanvasTkAgg(f_2, master=f3)
canvas_2.show()
canvas_2.get_tk_widget().grid(row=0, column=0,sticky="W", columnspan=5,rowspan=5)
toolbar = NavigationToolbar2TkAgg(canvas_2,f3)
toolbar.grid(row=6, column=0, columnspan=5)

a_2 = f_2.add_subplot(111)
a_2.grid(True)
c_2=np.linspace(-100,100,100)
b_2=np.linspace(-100,100,100)
A_2,B_2=np.meshgrid(c_2,b_2)


#functions in this frame
#point
def _point():
    for x in range(0,4):
        a_2.cla()
        a_2.set_title("Moving 3 units along positive X-axis")
        a_2.plot([-10,10],[0,0],'g',[0,0],[10,-10],'g')
        a_2.plot(x,0,'ro')
        canvas_2.show()
    time.sleep(2)  
    for x in range(0,6):
        a_2.cla()
        a_2.set_title("Moving 5 units along positive Y-axis")
        a_2.plot([-10,10],[0,0],'g',[0,0],[10,-10],'g')
        a_2.plot(3,x,'ro')
        canvas_2.show()
    time.sleep(1)
    a_2.set_title("This is Point P")
    a_2.text(3,4,'P(3,5)',fontsize=10)
    canvas_2.show()
    
    
#line
def _line():
    #Point A
    for x in range(0,11):
        a_2.cla()
        a_2.set_title("Moving 10 units along positive X-axis")
        a_2.plot([-20,20],[0,0],'g',[0,0],[20,-20],'g')
        a_2.plot(x,0,'ro')
        canvas_2.show()
    time.sleep(2)  
    for x in range(0,11):
        a_2.cla()
        a_2.set_title("Moving 10 units along positive Y-axis")
        a_2.plot([-20,20],[0,0],'g',[0,0],[20,-20],'g')
        a_2.plot(10,x,'ro')
        canvas_2.show()
    time.sleep(1)
    a_2.set_title("This is Point A")
    canvas_2.show()
    time.sleep(1)

    #Point B
    for x in range(0,-11,-1):
        a_2.cla()
        a_2.plot(10,10,'ro')
        a_2.set_title("Moving 10 units along negative X-axis")
        a_2.plot([-20,20],[0,0],'g',[0,0],[20,-20],'g')
        a_2.plot(x,0,'ro')
        canvas_2.show()
    time.sleep(2)  
    for x in range(0,-11,-1):
        a_2.cla()
        a_2.plot(10,10,'ro')
        a_2.set_title("Moving 10 units along negative Y-axis")
        a_2.plot([-20,20],[0,0],'g',[0,0],[20,-20],'g')
        a_2.plot(-10,x,'ro')
        canvas_2.show()
    time.sleep(1)
    a_2.set_title("This is Point B")
    canvas_2.show()
    time.sleep(1)
    a_2.set_title("Bridge the gap!")
    a_2.plot([10,-10],[10,-10],'b')
    canvas_2.show()

#Quadrants
a_2.set_title("Quadrants")
a_2.plot([-4,4],[0,0],'g',[0,0],[4,-4],'g')
a_2.text(1.5,2,'I Quadrant', fontsize=10)
a_2.text(1.5,1.5,'(+,+)', fontsize=10)
a_2.text(-3,2,'II Quadrant', fontsize=10)
a_2.text(-3,1.5,'(-,+)', fontsize=10)
a_2.text(-3,-2,'III Quadrant', fontsize=10)
a_2.text(-3,-1.5,'(-,-)', fontsize=10)
a_2.text(1.5,-2,'IV Quadrant', fontsize=10)
a_2.text(1.5,-1.5,'(+,-)', fontsize=10)
a_2.text(0,4,'Y', fontsize=10)
a_2.text(4,0,'X', fontsize=10)
a_2.text(0,-4,'-Y', fontsize=10)
a_2.text(-4,0,'-X', fontsize=10)
a_2.text(0,0,'O', fontsize=10)
canvas_2.draw()

f3.grid_columnconfigure(6,minsize=10)
#getting subframe
sf=Tk.Frame(f3,bg="#b3ffb3")
sf2=Tk.Frame(f3,bg="#b3ffb3")
lst=Tk.Frame(f3,bg="#b3ffb3")

def shwsf():
    sf2.grid_remove()
    lst.grid_remove()
    sf.grid(row=0,column=7,columnspan=5,rowspan=5)

def shwsf2():
    sf.grid_remove()
    lst.grid_remove()
    sf2.grid(row=0,column=7,columnspan=5,rowspan=5)

def shwlst():
    sf.grid_remove()
    sf2.grid_remove()
    smile()
    lst.grid(row=0,column=7,columnspan=5,rowspan=5)

head=Tk.Label(sf,text="Let's get Started!",font=('Century Gothic',18),background="#b3ffb3")
head.grid(row=0,column=0)
h1=Tk.Label(sf,text="Cartesian Plane",font=('Century Gothic',15),background="#b3ffb3")
h1.grid(row=1,column=0)
txt1='''
Cartesian Plane consists of Two perpendicular
lines intersecting each other at thier zeros.
Each perpendicular line is called 'Axis'.
'''
t1=Tk.Label(sf,text=txt1,font=('Century Gothic',12),background="#b3ffb3")
t1.grid(row=2,column=0,sticky="W",columnspan=2,rowspan=3)

h2=Tk.Label(sf,text="Quadrants",font=('Century Gothic',15),background="#b3ffb3")
h2.grid(row=5,column=0)
txt2='''
The axes divides co-ordinate plane into 4 parts.
These are called Quadrants. Starting from OX-
they are named as first,second,third and forth
quadrants in anti-clockwise manner.
'''
t2=Tk.Label(sf,text=txt2,font=('Century Gothic',12),background="#b3ffb3")
t2.grid(row=6,column=0,sticky="W",columnspan=2,rowspan=4)


btnxt=Tk.Button(sf,text="Next->",command=shwsf2,font=('Century Gothic',14),background="white", foreground="#006600")
btnxt.grid(row=10,column=1)


#subframe2

bpoint=Tk.Label(sf2,text="Plotting of Points",font=('Century Gothic',15),background="#b3ffb3")
bpoint.grid(row=1,column=0)
txt3='''
Every point on a plane has an ordered pair
of reference. That is position of point with
reference to co-ordinate axes.
Say point P(3,5). Here, 3 is called abscissa;
distance from X-axis. And 5 is called ordinate;
distance from Y axis.
'''
l_point=Tk.Label(sf2,text=txt3,font=('Century Gothic',12),background="#b3ffb3")
l_point.grid(row=2,column=0,columnspan=4,rowspan=7)
ptshw=Tk.Button(sf2,text="Plot" ,command=_point,font=('Century Gothic',13),background="#b3ffb3")
ptshw.grid(row=1,column=3,sticky="E")


bline=Tk.Label(sf2,text="Plotting Line",font=('Century Gothic',15),background="#b3ffb3")
bline.grid(row=10,column=0)
txt2='''
Ill show you how to plot a line when two
points are given. First Plot the points.
Say A(10,10) and B(-10,-10). Then join them.
'''
l_line=Tk.Label(sf2,text=txt2,font=('Century Gothic',12),background="#b3ffb3")
l_line.grid(row=11,column=0,columnspan=5)
l_bline=Tk.Button(sf2,text="Plot" ,command=_line,font=('Century Gothic',13),background="#b3ffb3")
l_bline.grid(row=10,column=3)

#navigating on subframes
bprev=Tk.Button(sf2,text="<- Prev",command=shwsf,font=('Century Gothic',14),background="white", foreground="#006600")
bprev.grid(row=13,column=0)
bnxt=Tk.Button(sf2,text="Next->",command=shwlst,font=('Century Gothic',14),background="white", foreground="#006600")
bnxt.grid(row=13,column=3)


f3.grid_columnconfigure(13,minsize=30)
sf2.grid_columnconfigure(13,minsize=10)

#last frame
def smile():
    a_2.cla()
    a_2.grid(True)
    x=30
    y=30
    r_2=12
    F_2=((A_2-x)**2)+((B_2-y)**2)-(r_2**2)
    a_2.contour(A_2,B_2,F_2,[0])
    x2=-30
    y2=30
    F_2=((A_2-x2)**2)+((B_2-y2)**2)-(r_2**2)
    a_2.contour(A_2,B_2,F_2,[0])
    r_3=75
    F_2=((A_2)**2)+((B_2)**2)-(r_3**2)
    a_2.contour(A_2,B_2,F_2,[0])
    x=[i for i in range(-45,45)]
    y=[(0.015*(i**2))-45 for i in x]
    a_2.plot(x,y)
    canvas_2.show()

img=ImageTk.PhotoImage(Image.open('thanks.jpg'))
panel=Tk.Label(lst,image=img,width=490,height=490)
panel.grid(row=0,column=0)


shwsf()
Tk.mainloop()