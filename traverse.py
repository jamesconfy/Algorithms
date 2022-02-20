# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:03:58 2020

@author: IFEANYI
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:42:41 2020

@author: IFEANYI
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 00:02:09 2020

@author: IFEANYI
"""

import tkinter as tk
from tkinter import *
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from pandastable import Table, TableModel
import geopandas as gpd
from geopandas import GeoDataFrame
from shapely.geometry import Point, LineString, Polygon

#---------------------------Define the GUI--------------------------------------
master = Tk()
master.geometry('700x400')
master['bg'] = 'DarkGoldenrod1'
master.title('Traverse Computation')

frametraverse0 = Frame(master,bd=5,relief='groove',bg='DarkGoldenrod1') 
frametraverse00 = Frame(frametraverse0,relief='flat',bg='DarkGoldenrod1') 
frametraverse1 = LabelFrame(frametraverse00, text='Notes for your data file!!!',bg = 'DarkGoldenrod1',bd=5,padx=10,pady=10 , fg="red2",font=('times new roman', 12, 'bold','italic'))   
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
labeltraverse1.config(font=('helvetica', 10,'bold','italic'),bg = 'gold', justify = 'left')
labeltraverse1.grid(row=0,column=0,sticky='nw')

frametraverse4 = LabelFrame(frametraverse00, text='Open File!!!',bg = 'DarkGoldenrod1',padx=10,pady=10 , font=('times new roman', 12, 'bold','italic'),relief = 'flat')

labeltraverse6 = Label(frametraverse4,font=('Times', 12, 'bold'),bg = 'DarkGoldenrod1',fg = 'red')
labeltraverse6['text'] = 'No file Selected'
labeltraverse6.grid()      
frametraverse5 = LabelFrame(frametraverse00,bg = 'DarkGoldenrod1',bd=5,padx=250,)
checkvartraverse = IntVar()
plottraverse = Checkbutton(frametraverse5, text='Plot the Traverse Network',variable=checkvartraverse,bg = 'DarkGoldenrod1', cursor='hand2') 
plottraverse.grid()
checkvartraverse1 = IntVar()
sheet = Checkbutton(frametraverse5, text='Show Computation Sheet',variable=checkvartraverse1,bg = 'DarkGoldenrod1', cursor='hand2') 
sheet.grid()

traversemethod = StringVar()
traversemethod.set('Method')
traverseoption = OptionMenu(frametraverse5,traversemethod,"Bowditch Rule","Transit Rule")
traverseoption.grid(column = 0)


#--------------------Function to Open File dialog box to select data file from your system--------------------
def find():
    master.filename = tk.filedialog.askopenfilename()
    labeltraverse6['text'] = master.filename
    labeltraverse6.config(font=('Times', 12, 'bold'),bg = 'DarkGoldenrod1',fg = 'green4')
    frametraverse4.grid(row=1,column=0,columnspan=2,sticky='nw')
    if master.filename == '': 
        labeltraverse6['text'] = 'No file Selected'
        labeltraverse6['fg'] = 'red'
    return master.filename


frametraverse0.grid(row=0,column=0,sticky=NW)
frametraverse00.grid(row=0,column=0,sticky=NW)
frametraverse1.grid(row=0,column=0,sticky='nw')
frametraverse5.grid(row=2,column=0)
frametraverse4.grid(row=1,column=0,columnspan=2,sticky='nw')
    
def traverseforget():
    frametraverse0.grid_forget()
    

def Exit():
    exit = messagebox.askyesno('Close all Windows', 'Are you sure of this action?')
    if exit>0:
        try: 
            master.destroy()
            try: 
                window.destroy()
            except:''
        except:''
            
        
    
#----------------Function to compute change in easting(given the distance and bearing)----------------------------        
def easting_compt(distance, bearing):
    departure = distance * math.sin(math.radians(bearing))
    return departure    

#----------------Function to compute change in northing(given the distance and bearing)----------------------------        
def northing_compt(distance, northing):
    latitude = distance * math.cos(math.radians(northing))
    return latitude

#---------------------Function to sum the items in a list(given a list with same type items)--------------------------------
def sum_list(list1):
    sum = 0
    for i in list1:
        sum += i
    return sum

def distance(change_easting,change_northing):
    dist = math.sqrt(change_easting**2+change_northing**2)
    return dist

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
    

#---------------------Function to compute bearing(given change in easting and change in northings)--------------------------------    
def first_bearing(change_easting, change_northing):
    if change_easting > 0 and change_northing > 0:
        B_B = math.atan(change_easting/change_northing)
        B_B = math.degrees(B_B)
        return B_B
        
    if change_easting < 0 and change_northing > 0:
        B_B = math.atan(abs(change_easting)/change_northing)
        B_B = math.degrees(B_B)
        B_B = 360 - B_B
        return B_B
            
    if change_easting < 0 and change_northing < 0:
        B_B = math.atan(abs(change_easting)/abs(change_northing))
        B_B = math.degrees(B_B)
        B_B = 180 + B_B
        return B_B
        
    if change_easting > 0 and change_northing < 0:
        B_B = math.atan(change_easting/abs(change_northing))
        B_B = math.degrees(B_B)
        B_B = 180 - B_B
        return B_B
    
#---------------------Function to convert angle from deg,min,sec to decimal degrees(given the angle as a string in the format 'deg min sec')--------------------------------        
def dms_to_dgs(string):
    angle = str(string)
    degrees, minutes, seconds = angle.split()
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    return dd

def dgs_to_radians(angle):
    return math.radians(angle)

def radians_to_dgs(angle):
    return math.degrees(angle)

#---------------------Function to convert angle from decimal degrees to deg,min,sec(given the angle)--------------------------------     
def dgs_to_dms(angle):
    mnt,sec = divmod(abs(angle)*3600,60)
    deg,mnt = divmod(mnt,60)
    if angle<0:
        return '-'+str(int(deg))+'° '+str(int(mnt))+'\' '+str(float('{:.2f}'.format(sec)))+'\"'
    else:
        return str(int(deg))+'° '+str(int(mnt))+'\' '+str(float('{:.2f}'.format(sec)))+'\"'

#---------------------Function to round up a float to 3 decimal places------------------------------
def rd3(value):
    return float('{:.3f}'.format(value))

#---------------------Function to round up a float to 7 decimal places------------------------------
def rd6(value):
    return float('{:.6f}'.format(value))

def center(widget):
    widget.tag_configure('center', justify='center')
    widget.tag_add('center', 1.0,'end')
    widget.configure(state="disabled")
    
def exportexcel():
    export_file_path = tk.filedialog.asksaveasfilename(defaultextension='.xlsx')
    df4.to_excel (export_file_path, index = False, header=True)
    
def exportcsv():         
    export_file_path = tk.filedialog.asksaveasfilename(defaultextension='.csv')
    df4.to_csv (export_file_path, index = False, header=True)
    
##-----------------------------Function to Adjust the traverse--------------------------------------  
def traverse_calculation():
    try:
        file = labeltraverse6['text']
        fil = pd.read_excel(file)
        etf = fil.loc[0:(len(fil)-1), 'EASTINGS']
        ntf = fil.loc[0:(len(fil)-1), 'NORTHINGS']
        sta_id = fil.loc[0:(len(fil)), 'STATION ID']
        observed_angle = fil.iloc[0:(len(fil)), 2]
        dist = fil.iloc[0:(len(fil)), 3]
        stn = fil.iloc[0:(len(fil)), 0]
        stn_to = fil.iloc[0:(len(fil)), 4]
        
        method = traversemethod.get()
        if method == 'Method':
            messagebox.showwarning("Error","Please select the method of\nTraverse Adjustment to use")
            
        #----------------Reducing the face left and face right angles to obtain the mean angles--------------------------
        Mean_angle=[]
        increment=0
        while increment < len(observed_angle):
            firstfl=dms_to_dgs(observed_angle.iloc[increment])
            secondfl=dms_to_dgs(observed_angle.iloc[increment+1])
            firstfr=dms_to_dgs(observed_angle.iloc[increment+2])
            secondfr=dms_to_dgs(observed_angle.iloc[increment+3])
            firstdiff=secondfl-firstfl
            if firstdiff < 0: firstdiff += 360
            seconddiff=firstfr-secondfr
            if seconddiff < 0: seconddiff += 360
            mean_angle=(firstdiff+seconddiff)/2
            Mean_angle.append(mean_angle)
            increment += 4
               
        #-----------------------Computing the opening bearing of the network--------------------       
        Opening_DE = etf[1] - etf[0]
        Opening_DN = ntf[1] - ntf[0]
        firstB_B = first_bearing(Opening_DE, Opening_DN)
          
        #----------------------Computing the closing bearing of the network-----------------------------
        Closing_DE = etf[3] - etf[2]
        Closing_DN = ntf[3] - ntf[2]
        Closing_bearing = first_bearing(Closing_DE, Closing_DN)
        
        #------------------------Computing the backward and forward bearings of the traverse legs--------------------------
        Back_Bearings = []
        Back_Bearings.append(firstB_B) 
        Forward_Bearings = []
        increment2=0
        for angle in Mean_angle:
            forward_bearing=(angle+Back_Bearings[increment2])%360
            Forward_Bearings.append(forward_bearing)
            if forward_bearing < 180: new_back_bearing = forward_bearing + 180
            else : new_back_bearing = forward_bearing - 180
            Back_Bearings.append(new_back_bearing)
            increment2 += 1
        
        #--------------------------Computing the corresponding corrections to the bearings of the traverse legs----------------------------    
        Corrections = []
        Bearing_misclosure = Closing_bearing - Forward_Bearings[len(Forward_Bearings)-1]
        increment3 = 1
        while increment3 <= len(Forward_Bearings):
            correction = ((increment3)/(len(Forward_Bearings)))*(Bearing_misclosure)
            Corrections.append(correction)
            increment3 += 1
            
        #--------------------------Computing the corresponding corrected bearings of the traverse legs----------------------------  
        Corrected_bearing = [sum(pair) for pair in zip(Forward_Bearings,Corrections)]
        
        #---------------------------Compiling the distance list and removing empty cells in distance---------------------------
        Distance = []
        for distance in dist:
            distance = str(distance)
            if distance == "nan": distance = int("-1")
            else: distance = float(distance)
            Distance.append(distance)
            for distance in Distance:
                if distance == -1:
                    Distance.remove(distance)
        lastdist = Distance[len(Distance)-1]
        
        #--------------------------Computing the total distance of the traverse network---------------------------
        Total_distance = sum(Distance)
        if len(Distance) == len(Mean_angle):
            Total_distance = Total_distance - Distance[len(Distance)-1]
            Distance.remove(Distance[len(Distance)-1])
        
        #---------------------------Compiling the station id list and removing empty cells in station id---------------------------
        Station_ID = []
        for station_id in stn:
            station_id = str(station_id)
            if station_id == "nan": station_id = int("-1")
            else: distance = str(station_id)
            Station_ID.append(station_id)
            for station_id in Station_ID:
                if station_id == -1:
                    Station_ID.remove(station_id)
        Station_ID.remove(Station_ID[0])
        
        #---------------------------Compiling the station_to list and removing---------------------------
        Station_To = []
        incrementa = 1
        while incrementa < len(stn_to):
            station_to = stn_to[incrementa]
            Station_To.append(station_to)
            incrementa += 4
        
        #------------------------Computing and compiling the change in eastings into a list-----------------------
        Change_in_Eastings = []            
        for distance,bearing in zip(Distance,Corrected_bearing):
            Change_in_easting = easting_compt(distance,bearing)
            Change_in_Eastings.append(Change_in_easting) 
        Sum_Change_in_Eastings = sum(Change_in_Eastings)
        
        total_east = 0
        for value in Change_in_Eastings:
            total_east += abs(value)
            
        #------------------------Computing and compiling the corresponding corrections to change in eastings into a list-----------------------
        Closing_Easting = etf[2] - etf[0]
        correction_to_eastings = Sum_Change_in_Eastings - Closing_Easting
        
        if method == 'Bowditch Rule':
            Correction_to_Eastings = []
            for distance in Distance:
                correction = (distance/Total_distance)*correction_to_eastings
                Correction_to_Eastings.append(correction)
        if method == 'Transit Rule':
            Correction_to_Eastings = []
            for east in Change_in_Eastings:
                correction = (abs(east)/total_east)*correction_to_eastings
                Correction_to_Eastings.append(correction)
    
        #------------------------Computing and compiling the corresponding corrected change in eastings into a list-----------------------
        Corrected_Eastings = []   
        for change_in_easting,correction in zip(Change_in_Eastings,Correction_to_Eastings):
            corrected_easting = change_in_easting - correction
            Corrected_Eastings.append(corrected_easting)
        
        #------------------------Computing and compiling the change in northings into a list-----------------------
        Change_in_Northings = []            
        for distance,bearing in zip(Distance,Corrected_bearing):
            Change_in_northing = northing_compt(distance,bearing)
            Change_in_Northings.append(Change_in_northing)
        Sum_Change_in_Northings = sum(Change_in_Northings)
        
        total_north = 0
        for value in Change_in_Northings:
            total_north += abs(value)
            
        #------------------------Computing and compiling the corresponding corrections to change in northings into a list-----------------------    
        Closing_Northing = ntf[2] - ntf[0]
        correction_to_northings = Sum_Change_in_Northings - Closing_Northing
        
        if method == 'Bowditch Rule':
            Correction_to_Northings = []
            for distance in Distance:
                correction = (distance/Total_distance)*correction_to_northings
                Correction_to_Northings.append(correction)
        if method == 'Transit Rule':
            Correction_to_Northings = []
            for north in Change_in_Northings:
                correction = (abs(north)/total_north)*correction_to_northings
                Correction_to_Northings.append(correction)
        
        #------------------------Computing and compiling the corresponding corrected change in northings into a list-----------------------
        Corrected_Northings = []   
        for change_in_northing,correction in zip(Change_in_Northings ,Correction_to_Northings):
            corrected_northing = change_in_northing - correction
            Corrected_Northings.append(corrected_northing)
        
        linear_misclosure = math.sqrt((correction_to_eastings)**2 + (correction_to_northings)**2)
        
        #-----------------------Computing the Adjusted Easting and Northing coordinates---------------------------  
        Eastings = [etf[0]]
        Northings = [ntf[0]]
        Station_IDs = [sta_id[0]]
        Easting = etf[0]
        Northing = ntf[0]
        for station_id,easting,northing in zip(Station_ID,Corrected_Eastings,Corrected_Northings):
            Easting += easting
            Northing += northing 
            Eastings.append(round(Easting,3))   
            Northings.append(round(Northing,3))
            Station_IDs.append(station_id)
        
        #----------------------Presenting the result in a tabular data frame---------------------
        data = {'Station_IDs':Station_IDs , 'Eastings':Eastings , 'Northings':Northings}
        df = DataFrame(data, columns = ['Station_IDs','Eastings','Northings'])
        
        #-------------------------Presenting the result in a graph-----------------------------
        Starting_Easting = [etf[0],etf[1]]
        Starting_Northing = [ntf[0],ntf[1]]
        Closing_Easting = [etf[2],etf[3]]   
        Closing_Northing = [ntf[2],ntf[3]]  
        
        ID_group1 = []
        IDs1 = [sta_id[0],sta_id[1]]
        ID_group2 = []
        IDs2 = [sta_id[0]]
        for i in Station_ID: IDs2.append(i)
        ID_group3 = []
        IDs3 = [sta_id[2],sta_id[3]]
        
        i = 0
        for value in Starting_Easting: ID_group1.append('Start')
        for value in Eastings: ID_group2.append('Traverse Station')
        for value in Closing_Easting: ID_group3.append('End')
        
        dataframe1 = DataFrame({'ID_Group':ID_group1,'Station_ID':IDs1})
        dataframe2 = DataFrame({'ID_Group':ID_group2,'Station_ID':IDs2})
        dataframe3 = DataFrame({'ID_Group':ID_group3,'Station_ID':IDs3})
        
        points1 = [Point(xy) for xy in zip(Starting_Easting,Starting_Northing)]
        points2 = [Point(xy) for xy in zip(Eastings,Northings)]
        points3 = [Point(xy) for xy in zip(Closing_Easting,Closing_Northing)]
        gdf = GeoDataFrame(dataframe1,geometry = points1)#,Close_geometry,Traverse_geometry))
        gdf2 = gdf.groupby(['ID_Group'])['geometry'].apply(lambda x:          LineString(x.tolist()))
        gdf2 = GeoDataFrame(gdf2,geometry = 'geometry')
        
        gdf1 = GeoDataFrame(dataframe2,geometry = points2)#,Close_geometry,Traverse_geometry))
        gdf21 = gdf1.groupby(['ID_Group'])['geometry'].apply(lambda x:          LineString(x.tolist()))
        gdf21 = GeoDataFrame(gdf21,geometry = 'geometry')
            
        gdf3 = GeoDataFrame(dataframe3,geometry = points3)#,Close_geometry,Traverse_geometry))
        gdf33 = gdf3.groupby(['ID_Group'])['geometry'].apply(lambda x:          LineString(x.tolist()))
        gdf33 = GeoDataFrame(gdf33,geometry = 'geometry')
            
        global fig1
        fig1, ax = plt.subplots(figsize = (7.5,7.5))
        gdf2.plot(ax = ax, color = 'red', legend = True)#, facecolor='blue' )
        gdf21.plot(ax = ax, color = 'blue', legend = True)
        gdf33.plot(ax = ax, color = 'orange', legend = True)
        
        gdf.plot(ax = ax, color = 'blue',marker='s')
        gdf1.plot(ax = ax, color = 'blue',marker='s')
        gdf3.plot(ax = ax, color = 'blue',marker='s')
        
        ax.set_title('Graph of the Traverse Network')
        ax.legend(['Starting Controls', 'Traverse Legs','Closing Controls'],title='Legend')
        ax.grid(True,linewidth=0.5)
        ax.set_xlabel('Eastings')
        ax.set_ylabel('Northings')
        
        gdf.apply(lambda x: ax.annotate(s=x.Station_ID,xy=x.loc['geometry'].coords[0]),axis=1)
        gdf1.apply(lambda x: ax.annotate(s=x.Station_ID,xy=x.loc['geometry'].coords[0]),axis=1)
        gdf3.apply(lambda x: ax.annotate(s=x.Station_ID,xy=x.loc['geometry'].coords[0]),axis=1)
            
        if checkvartraverse.get() == 1:
            createplot()
        
        #------------------------Creating the output tables---------------------
        Back_Bearings.remove(Back_Bearings[len(Back_Bearings)-1])
        Station_ID.insert(0,stn[0])
        
        #-------------------Making the lists needed to have the same length
        if len(Distance) <= len(Mean_angle):
            Change_in_Eastings.append('-----')
            Change_in_Northings.append('-----')
            Correction_to_Eastings.append('-----')
            Correction_to_Northings.append('-----')
            Corrected_Eastings.append('-----')
            Corrected_Northings.append('-----')
            Distance.append(lastdist) 
         
        
        #---------------------------filling in the values in the computation sheet-----------------------------
        for numbers in range(len(Station_ID)):
            Station_ID[numbers] = str(Station_ID[numbers])
            Distance[numbers] = str(Distance[numbers])
            Back_Bearings[numbers] = str(dgs_to_dms(Back_Bearings[numbers]))
            Mean_angle[numbers] = str(dgs_to_dms(Mean_angle[numbers]))
            Forward_Bearings[numbers] = str(dgs_to_dms(Forward_Bearings[numbers]))
            Corrections[numbers] = str(dgs_to_dms(Corrections[numbers]))
            Corrected_bearing[numbers] = str(dgs_to_dms(Corrected_bearing[numbers]))
            if Change_in_Eastings[numbers] == '-----': Change_in_Eastings[numbers] = str(Change_in_Eastings[numbers])
            else: Change_in_Eastings[numbers] = str(rd3(Change_in_Eastings[numbers]))
            if Change_in_Northings[numbers] == '-----': Change_in_Northings[numbers] = str(Change_in_Northings[numbers])
            else: Change_in_Northings[numbers] = str(rd3(Change_in_Northings[numbers]))
            if Correction_to_Eastings[numbers] == '-----': Correction_to_Eastings[numbers] = str(Correction_to_Eastings[numbers])
            else: Correction_to_Eastings[numbers] = str(rd6(Correction_to_Eastings[numbers]))
            if Correction_to_Northings[numbers] == '-----': Correction_to_Northings[numbers] = str(Correction_to_Northings[numbers])
            else: Correction_to_Northings[numbers] = str(rd6(Correction_to_Northings[numbers]))
            if Corrected_Eastings[numbers] == '-----': Corrected_Eastings[numbers] = str(Corrected_Eastings[numbers])
            else: Corrected_Eastings[numbers] = str(rd6(Corrected_Eastings[numbers]))
            if Corrected_Northings[numbers] == '-----': Corrected_Northings[numbers] = str(Corrected_Northings[numbers])
            else: Corrected_Northings[numbers] = str(rd6(Corrected_Northings[numbers]))
            Eastings[numbers] = str(Eastings[numbers])
            Northings[numbers] = str(Northings[numbers])
            Station_To[numbers] = str(Station_To[numbers])
        
        
        frametraverse6 = LabelFrame(frametraverse0, text="**Adjusted Coordinates**", bd=5, bg="gold", fg="green4",font=('Times', 14, 'bold', 'italic'))
        frametraverse6.grid(row=0, column=1,sticky = NW)
        #----------------------------Creating the default output ----------------------------     
        global df4
        if checkvartraverse1.get() == 1: 
            Station_ID.insert(0,' ')
            Distance.insert(0,' ')
            Back_Bearings.insert(0,' ')
            Mean_angle.insert(0,' ')
            Forward_Bearings.insert(0,' ')
            Corrections.insert(0,' ')
            Corrected_bearing.insert(0,' ')
            Change_in_Eastings.insert(0,' ')
            Change_in_Northings.insert(0,' ')
            Correction_to_Eastings.insert(0,' ')
            Correction_to_Northings.insert(0,' ')
            Corrected_Eastings.insert(0,' ')
            Corrected_Northings.insert(0,' ')
            Eastings.insert(0,' ')
            Northings.insert(0,' ')
            Station_To.insert(0,stn_to[0])
            
            data1 = {'Station At':Station_ID,'Distance':Distance , 'Back Bearing':Back_Bearings, "Mean Angle":Mean_angle,"Forward Bearing":Forward_Bearings,"corr. to Bearing":Corrections, "Corr. Bearing":Corrected_bearing,"ΔE(LsinƟ)":Change_in_Eastings,"ΔN(LcosƟ)":Change_in_Northings,"corr. to ΔE":Correction_to_Eastings,"corr. to ΔN":Correction_to_Northings,"Corr. ΔE":Corrected_Eastings,"Corr. ΔN":Corrected_Northings, 'Eastings':Eastings , 'Northings':Northings,"Station To":Station_To}
            df4 = DataFrame(data1, columns = ['Station At','Distance' , 'Back Bearing', "Mean Angle","Forward Bearing","corr. to Bearing", "Corr. Bearing","ΔE(LsinƟ)","ΔN(LcosƟ)","corr. to ΔE","corr. to ΔN","Corr. ΔE","Corr. ΔN",'Eastings','Northings',"Station To"])
            frametraverse6['text'] = "**Computation Sheet**"
            table = Table(frametraverse6,dataframe=df4,showtoolbar=True,showstatusbar=True)
            table.show()
        else:
            Station_To.insert(0,sta_id[1])
            Station_To.insert(1,sta_id[0])
            Eastings.insert(0,etf[1])
            Eastings.append(etf[3])
            Northings.insert(0,ntf[1])
            Northings.append(ntf[3])
               
            data2 = {'Station_IDs':Station_To , 'Eastings':Eastings , 'Northings':Northings}
            df4 = DataFrame(data2, columns = ['Station_IDs','Eastings','Northings'])
            table = Table(frametraverse6,dataframe=df4,showtoolbar=True,showstatusbar=True)
            table.show()
        
        #-----------------------Creating the button to prompt exporting output file to excel--------------------------------- 
        #Savetoexcel = Button(frametraverse6,text='Export Excel', command=exportexcel, bg='green4', fg='white', font=('verdana', 11, 'bold'),cursor='hand2')
        
        labelbrmis = Label(frametraverse6, text='**Misclosure in Bearing** = ', bg='gold',fg='green4',font=('Times', 12,'bold'))
        if Bearing_misclosure<0: labelbrmis['fg'] = 'red3'
        br_misclosure = labelbrmis['text'] + str(dgs_to_dms(Bearing_misclosure))
        labelbrmis['text'] = br_misclosure
        labelbrmis.grid(row=4,column=1,sticky='w')
        #Savetoexcel.grid(column=4) 
        
        labelli_mis = Label(frametraverse6, text='**Linear Misclosure** = ', bg='gold',fg='green4',font=('Times', 12,'bold'))
        if linear_misclosure<0: labelli_mis['fg'] = 'red3'
        li_misclosure = labelli_mis['text'] + str(rd3(linear_misclosure)) + 'm'
        labelli_mis['text'] = li_misclosure
        labelli_mis.grid(row=5,column=1,sticky='w')
        #Savetoexcel.grid(column=4) 
        
        labelrel_pre = Label(frametraverse6, text='**Relative Precision** = ', bg='gold',fg='green4',font=('Times', 12,'bold'))
        
        relative_precision = labelrel_pre['text'] + '1 : ' + str(round(Total_distance/linear_misclosure))
        labelrel_pre['text'] = relative_precision 
        labelrel_pre.grid(row=6,column=1,sticky='w')
        #Savetoexcel.grid(column=4) 
    except ValueError:
        messagebox.showwarning("Error","Please confirm that all fields in your data file\nare valid or check for missing values")
    except KeyError:
        messagebox.showerror("Error","Please confirm that column headers for your\ncontrols in your data file match 'STATION ID',\n'EASTINGS' and 'NORTHINGS' in this order \n\nOr reconfirm your open data file")
    except TypeError:
        messagebox.showwarning("Error","Please confirm that all fields in your data file\nare valid or check for missing values")
    except FileNotFoundError:
        messagebox.showwarning("Error","Please select a data file to process")
    #except :
        #messagebox.showwarning("Error","Oops!!!\nSomething went wrong\nPlease confirm your opened data file")


#-----------------------Creating the button to prompt data file selection---------------------------------


#-----------------------Creating the button to prompt running of the traverse---------------------------------        
computetraverse = Button(frametraverse5, text='COMPUTE', command=traverse_calculation, bg='green4', fg='white', font=('verdana', 11, 'bold'),cursor='hand2')
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



#-------------------Running the entire GUI-----------------------------
master.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    