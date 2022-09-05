import tkinter as tk
from tkinter import *
from traverse1 import traverse_coord, find, exportexcel, exportcsv, Exit

master = Tk()
master.geometry('700x400')
master['bg'] = 'DarkGoldenrod1'
master.title('Traverse Computation')

# ---------------------------Define the GUI--------------------------------------
frametraverse0 = Frame(master, bd=5, relief='groove', bg='DarkGoldenrod1')
frametraverse00 = Frame(frametraverse0, relief='flat', bg='DarkGoldenrod1')
frametraverse1 = LabelFrame(frametraverse00, text='Notes for your data file!!!', bg='DarkGoldenrod1',
                            bd=5, padx=10, pady=10, fg="red2", font=('times new roman', 12, 'bold', 'italic'))
labeltraverse1 = Label(frametraverse1, text='''Instructions for Users!!!

    (i) This program adjusts a closed traverse network(both loop 
    and connecting traverses)
    (ii) Open your data file from the file menu in the Menu bar 
    (iii) Ensure your data file is saved properly using the .xlsx 
    file extension eg. Datafile.xlsx
    (iv) For your excel data files, fill in the Station_At, Face,
    Horizontal Angles, Distance and Station_To (in this order) in 
    different columns (one for each).
    (v) Your Angular observations have to be separated with a space 
    not the conventional degrees, minutes and seconds symbols.
    (vi) Also provide the Starting and Closing Controls and their
    coordinates
    (vii) To show a plot of the traverse network or the computation 
    Sheet, kindly check the corresponding boxes.
    (viii) Click the 'Compute' button to proceed with the adjustment. 
    ''')
labeltraverse1.config(font=('helvetica', 10, 'bold',
                            'italic'), bg='gold', justify='left')
labeltraverse1.grid(row=0, column=0, sticky='nw')

frametraverse4 = LabelFrame(frametraverse00, text='Open File!!!', bg='DarkGoldenrod1',
                            padx=10, pady=10, font=('times new roman', 12, 'bold', 'italic'), relief='flat')

labeltraverse6 = Label(frametraverse4, font=(
    'Times', 12, 'bold'), bg='DarkGoldenrod1', fg='red')
labeltraverse6['text'] = 'No file Selected'
labeltraverse6.grid()
frametraverse5 = LabelFrame(frametraverse00, bg='DarkGoldenrod1', bd=5, padx=250,)
checkvartraverse = IntVar()
plottraverse = Checkbutton(frametraverse5, text='Plot the Traverse Network',
                           variable=checkvartraverse, bg='DarkGoldenrod1', cursor='hand2')
plottraverse.grid()
checkvartraverse1 = IntVar()
sheet = Checkbutton(frametraverse5, text='Show Computation Sheet',
                    variable=checkvartraverse1, bg='DarkGoldenrod1', cursor='hand2')
sheet.grid()

traversemethod = StringVar()
traversemethod.set('Method')
traverseoption = OptionMenu(
frametraverse5, traversemethod, "Bowditch Rule", "Transit Rule")
traverseoption.grid(column=0)


computetraverse = Button(frametraverse5, text='COMPUTE', command=traverse_coord(master), bg='green4', fg='white', font=('verdana', 11, 'bold'),cursor='hand2')
computetraverse.grid()

#============================================menu==========================================
menubar=Menu(master)
filemenu=Menu(menubar, tearoff=0)

filemenu.add_command(label="Open Data file",command=find)
filesubmenu = Menu(filemenu)
filesubmenu.add_command(label='Export to excel',command=exportexcel)
filesubmenu.add_command(label='Export to csv',command=exportcsv)
filemenu.add_cascade(label='Export output',menu=filesubmenu)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)

# =============================================================================
# traversemenu=Menu(menubar, tearoff=0)
# traversemenu.add_command(label="Compute Traverse",command=traverse)
# menubar.add_cascade(label='Traverse',menu=traversemenu)
# =============================================================================

areamenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label='Area',menu=areamenu)
submenu = Menu(areamenu)
submenu.add_command(label='Read coordinates from file',)#command=area1)
submenu.add_command(label='Input coordinates directly',)#command=area2)
areamenu.add_cascade(label='Compute Area',menu=submenu)

levelmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label='Level',menu=levelmenu)

master.config(menu=menubar)

master.mainloop()
