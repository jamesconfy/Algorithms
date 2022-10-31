# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:08:31 2020

@author: IFEANYI
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:59:31 2020

@author: IFEANYI
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 23:46:31 2020

@author: IFEANYI
"""
import tkinter.filedialog
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import math
import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import geopandas as gpd
from geopandas import GeoDataFrame
from shapely.geometry import Point, LineString, Polygon

master = Tk()
master.geometry('670x400')
master.title('Area Computation') 

framearea0 = Frame(master,bd=5,relief='groove',bg='DarkGoldenrod1') 
framearea1 = LabelFrame(framearea0, text='Notes for your data file!!!',bg = 'DarkGoldenrod1',bd=5,padx=10,pady=10 , fg="red2",font=('times new roman', 12, 'bold','italic'))   
framearea1.grid(row=0,column=0,sticky=NW)
labelarea1 = Label(framearea1, text='''**Instructions for Users!!!

(i) This program computes the area of an enclosed region
using the coordinates of the vertices of the region.
(ii) This program either accepts coordinate inputs directly
or reads coordinates from files in .xlsx, .csv and .txt file
extensions.
(iii) The coordinates should be filled in consecutively either
in a clockwise or anti-clockwise manner without repeating the
first point.
(iv) For excel files in .xlsx or .csv extensions, enter the
coordinates in two differnt columns, eastings(x) and northings(y)
(one for each).
(v) For direct input and text files in .txt extension, separate
the coordinates (easting and northing) with a comma eg. 1234,9876.
Each vertex coordinate in a new line.
(vi) To show a plot of the enclosed region, kindly check the box.
(vii) Click the 'Compute' button to calculate the area.
 ''')
labelarea1.config(font=('helvetica', 10,'bold','italic'),padx=25,bg = 'gold', justify = 'left')
labelarea1.grid(row=0,column=0)


framearea2 = LabelFrame(framearea0, text='Data Input', bg='gold',bd=5,font=('times new roman', 12, 'bold','italic'))
labelarea4 = Label(framearea2, text='Enter your coordinates below: ',bg = 'DarkGoldenrod1')
labelarea4.config(font=('times new roman', 12, 'bold'))
labelarea4.grid(row=0,column=0,sticky='w')

entry = Text(framearea2,height=19, width=25)
entry.grid(row=1,column=0,sticky='nw')


framearea4 = LabelFrame(framearea0, text='Open File!!!',bg = 'DarkGoldenrod1',pady=10 , font=('times new roman', 12, 'bold','italic'), width=200000, relief='flat')
labelarea6 = Label(framearea4,font=('Times', 12, 'bold'),bg = 'DarkGoldenrod1',fg = 'red')
labelarea6['text'] = 'No file Selected'
labelarea6.grid()

framearea5 = LabelFrame(framearea0,bg = 'DarkGoldenrod1',bd=5,padx=275)
framearea5.grid(row=2,column=0,columnspan=2)

frameareaoutput = LabelFrame(framearea0,text='Computed Results',bg='gold',bd=2, padx=10,pady=10,relief=RIDGE, fg="green4",font=('Times', 14, 'bold', 'italic'))
labelareaoutput = Text(frameareaoutput, width=40)
checkvararea = IntVar()
plot = Checkbutton(framearea5, text='Plot the Enclosed Region',variable=checkvararea,bg = 'DarkGoldenrod1', cursor='hand2') 
plot1 = Checkbutton(framearea5, text='Plot the Enclosed Region',variable=checkvararea,bg = 'DarkGoldenrod1', cursor='hand2')  
 
def find():
    master.filename = tk.filedialog.askopenfilename()
    labelarea6['text'] = master.filename
    labelarea6.config(font=('Times', 12, 'bold'),bg = 'DarkGoldenrod1',fg = 'green4')
    framearea4.grid(row=1,column=0,columnspan=2, sticky=NW)
    if master.filename == '': 
        labelarea6['text'] = 'No file Selected'
        labelarea6['fg'] = 'red'
    return master.filename
framearea0.grid(row=0,column=0,sticky=NW)
def area1():
    
    framearea2.grid_forget()
    plot1.grid_forget()
    computearea1.grid_forget()
    framearea4.grid(row=1,column=0,columnspan=2, sticky=NW)
    plot.grid()
    computearea.grid()
    
def area2():
    
    framearea4.grid_forget()
    plot.grid_forget()
    computearea.grid_forget()
    framearea2.grid(row=0,column=1, sticky = 'nw')
    plot1.grid()
    computearea1.grid()
    
def areaforget():
    framearea0.grid_forget()
    
def createplot():
    window = Toplevel()
    window.title("Graph of the Traverse Network")
    window.geometry("600x600")
    window['bg'] = 'DarkGoldenrod1'
    canvas = FigureCanvasTkAgg(fig1, master = window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    toolbar.pack()
    canvas.get_tk_widget().pack()

def Area_Computation():
    try:
        labelareaoutput.configure(state = 'normal')
        labelareaoutput.delete('1.0','end')
        global fig1
        def gettext():
            coordinates = entry.get('1.0', 'end') 
            return coordinates
        if len(gettext()) > 1:
            file = gettext()
            files = file.strip().split('\n')
            
            forward=0
            backward=0
            firstx=float(files[0].split(",")[0])
            firsty=float(files[0].split(",")[1])
            oldx=float(files[0].split(",")[0])
            oldy=float(files[0].split(",")[1])
            
            if len(files) < 3: messagebox.showerror("Error","Area cannot be bounded by less than 3 lines")
                                
            area_ans = 'The area bounded by the coordinates: \n'
            X_values = []
            Y_values = []
            for coordinate in files:
                if coordinate == "close" or coordinate == "c":
                    break
                else:
                    newx=float(coordinate.split(",")[0])
                    newy=float(coordinate.split(",")[1])
                    X_values.append(newx)
                    Y_values.append(newy)
                    area_ans = area_ans + str(newx) + ' , ' + str(newy) + '\n'
                    forward=forward+(oldx*newy)
                    backward=backward+(oldy*newx)
                    oldx=newx
                    oldy=newy
            X_values.append(firstx)
            Y_values.append(firsty)
            forward=forward+(oldx*firsty)
            backward=backward+(oldy*firstx)
            Area=(forward-backward)/2
            Area=abs(Area)
            area_ans = area_ans + " Equals " +  str(Area) + " sqrunits\n"
            labelareaoutput.insert(tk.END,area_ans)
            labelareaoutput.configure(state = 'disable')
            entry.delete('1.0','end')
            
            ID_group1 = []
            for value in X_values: ID_group1.append('vertex')
            dataframe1 = DataFrame({'ID_Group':ID_group1, 'X':X_values,'Y':Y_values})
            points1 = [Point(xy) for xy in zip(X_values,Y_values)]
            gdf = GeoDataFrame(dataframe1,geometry = points1)#,Close_geometry,Traverse_geometry))
            gdf2 = gdf.groupby(['ID_Group'])['geometry'].apply(lambda x:          LineString(x.tolist()))
            gdf2 = GeoDataFrame(gdf2,geometry = 'geometry')
            
        else:
            file = labelarea6['text'] 
            directory,file_extension = file.split('.')
            filee = directory +'.'+ file_extension
            if file_extension == 'txt' or file_extension == 'csv':
                open_filee = open(filee)
                fil = open_filee.read()
                files = fil.strip().split('\n')
                #print(files)
                if len(files) < 3: messagebox.showerror("Error","Area cannot be bounded by less than 3 lines")
                 
                forward=0
                backward=0
                firstx=float(files[0].split(",")[0])
                firsty=float(files[0].split(",")[1])
                oldx=float(files[0].split(",")[0])
                oldy=float(files[0].split(",")[1])
                
                area_ans = 'The area bounded by the coordinates: \n'
                
                X_values = []
                Y_values = []
                for coordinate in files:
                    if coordinate == "close" or coordinate == "c":
                        break
                    else:
                        newx=float(coordinate.split(",")[0])
                        newy=float(coordinate.split(",")[1])
                        X_values.append(newx)
                        Y_values.append(newy)
                        area_ans = area_ans + str(newx) + ' , ' + str(newy) + '\n'
                        forward=forward+(oldx*newy)
                        backward=backward+(oldy*newx)
                        oldx=newx
                        oldy=newy
                X_values.append(firstx)
                Y_values.append(firsty)
                forward=forward+(oldx*firsty)
                backward=backward+(oldy*firstx)
                Area=(forward-backward)/2
                Area=abs(Area)
                area_ans = area_ans + " Equals " +  str(Area) + " sqrunits\n"
                labelareaoutput.insert(tk.END,area_ans)
                labelareaoutput.configure(state = 'disable')
                        
            else :
                fil = pd.read_excel(filee)
                x = fil.iloc[0:(len(fil)-1), 0]
                y = fil.iloc[0:(len(fil)-1), 1]
                
                X = []
                Y = []
                forward=0
                backward=0
                
                area_ans = 'The area bounded by the coordinates: \n'
                for value in x:
                    value = str(value)
                    if value == "nan": value = str("empty")
                    else: value = float(value)
                    X.append(value)
                    for value in X:
                        if value == "empty":
                            X.remove(value)         
                for value in y:
                    value = str(value)
                    if value == "nan": value = str("empty")
                    else: value = float(value)
                    Y.append(value)
                    for value in Y:
                        if value == "empty":
                            Y.remove(value)
                if len(X) < 3 or len(Y) < 3: messagebox.showerror("Error","Area cannot be bounded by less than 3 lines")
                
                firstx=float(X[0])
                firsty=float(Y[0])
                oldx=float(X[0])
                oldy=float(Y[0]) 
                count=0  
                for easting,northing in zip(X,Y):
                    newx=float(X[count])
                    newy=float(Y[count])
                    area_ans = area_ans + str(newx) + ' , ' + str(newy) + '\n'
                    forward=forward+(oldx*newy)
                    backward=backward+(oldy*newx)
                    oldx=newx
                    oldy=newy
                    count += 1
                forward=forward+(oldx*firsty)
                backward=backward+(oldy*firstx)
                Area=(forward-backward)/2
                Area=abs(Area)
                area_ans = area_ans + " Equals " +  str(Area) + " sqrunits\n"
                labelareaoutput.insert(tk.END,area_ans)
                labelareaoutput.configure(state = 'disable')
                X.append(firstx)
                Y.append(firsty)
                X_values = X
                Y_values = Y
            ID_group1 = []
            for value in X_values: ID_group1.append('vertex')
            dataframe1 = DataFrame({'ID_Group':ID_group1, 'X':X_values,'Y':Y_values})
            points1 = [Point(xy) for xy in zip(X_values,Y_values)]
            gdf = GeoDataFrame(dataframe1,geometry = points1)#,Close_geometry,Traverse_geometry))
            gdf2 = gdf.groupby(['ID_Group'])['geometry'].apply(lambda x:          LineString(x.tolist()))
            gdf2 = GeoDataFrame(gdf2,geometry = 'geometry')
        
        frameareaoutput.grid(row=0, column=2,sticky = NW)
        labelareaoutput.grid(sticky='w')
        
        if checkvararea.get() == 1:
            fig1, ax = plt.subplots(figsize = (7.5,7.5))
            gdf2.plot(ax = ax, color = 'red', legend = True)#, facecolor='blue' )
            gdf.plot(ax = ax, color = 'blue',marker='s')
            ax.set_title('Area of the Region')
            ax.legend(['Bounding lines of the region','Vertices'],title='Legend')
            ax.grid(True,linewidth=0.5)
            ax.set_xlabel('Eastings')
            ax.set_ylabel('Northings')
            createplot()
    except ValueError:
        messagebox.showwarning("Error","Please enter a valid coordinate value\nOr check for missing fields")
    except IndexError:
        messagebox.showwarning("Error","Please confirm that every x_coordinate\nhas a corresponding y_coordinate")
    except FileNotFoundError:
        messagebox.showwarning("Error","Please select a data file to process")
    except FileNotFoundError:
        messagebox.showwarning("Error","Please select a data file to process")

        
computearea = Button(framearea5, text='COMPUTE', command=Area_Computation, bg='blue', fg='white', font=('verdana', 11, 'bold'), cursor='hand2', relief='raised')
computearea1 = Button(framearea5, text='COMPUTE', command=Area_Computation, bg='blue', fg='white', font=('verdana', 11, 'bold'), cursor='hand2', relief='raised')



#============================================menu==========================================
menubar=Menu(master)
filemenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open Data file",command=find)
submenu = Menu(filemenu)
submenu.add_command(label='Export to excel')#,command=exportexcel)
submenu.add_command(label='Export to csv')#,command=exportcsv)
filemenu.add_cascade(label='Export output',menu=submenu)
filemenu.add_separator()
filemenu.add_command(label="Exit"), #command=Exit)

traversemenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label='Traverse',menu=traversemenu)

areamenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label='Area',menu=areamenu)
areasubmenu = Menu(areamenu)
areasubmenu.add_command(label='Read coordinates from file',command=area1)
areasubmenu.add_command(label='Input coordinates directly',command=area2)
areamenu.add_cascade(label='Compute Area',menu=areasubmenu)

levelmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label='Level',menu=levelmenu)


master.config(menu=menubar)



#-------------------Running the entire GUI-----------------------------
master.mainloop()
    









































































