from tkinter import *
from tkinter import ttk
import tkinter as tk
from math import cos, pi



root = Tk()
root.title("")
frm = ttk.Frame(root, padding=50)
frm.grid()
txt = Text(root)


ref_lat_input = tk.StringVar()
ref_lon_input = tk.StringVar()
obj_lat_dist_input = tk.StringVar()
obj_lon_dist_input = tk.StringVar()


def calc():
    ref_lat = ref_lat_input.get()
    ref_lon = ref_lon_input.get()
    obj_lat = obj_lat_dist_input.get()
    obj_lon = obj_lon_dist_input.get()

    global final_lat
    final_lat = ((float(obj_lat)/101)/3600) + float(ref_lat)
    long_ref = ((cos(final_lat * pi/180.0 ) * 24902.0/360.0) * 5280)/3600
    global final_lon
    final_lon = ((float(obj_lon)/long_ref)/3600) + float(ref_lon)

    out_lat = ttk.Label(frm, text="Object latitude: " + str(final_lat)).grid(column=1, row=9)
    out_lon = ttk.Label(frm, text="Object Longitude: " + str(final_lon)).grid(column=1, row=10)



def copy():
    root.clipboard_clear()
    root.clipboard_append(str(final_lat) + ", " + str(final_lon))
    root.update()



#HEADER
ttk.Label(frm, text="Latitude/Longitude Calculator", justify=CENTER, font=100).grid(column=0, row=0)

#GAP
ttk.Label(frm, text="").grid(column=0, row=1)

#REFERENCE LABEL
ttk.Label(frm, text="Reference Latitude (decimal):", justify=LEFT).grid(column=0, row=2)
ttk.Label(frm, text="Reference Longitude (decimal):", justify=LEFT).grid(column=0, row=3)

#GAP
ttk.Label(frm, text="").grid(column=0, row=4)

#OBJECT DISTANCE LABEL
ttk.Label(frm, text="Vertical Distance from Reference Latitude (ft):", justify=LEFT).grid(column=0, row=5)
ttk.Label(frm, text="Horizontal Distance from Reference Longitude (ft):", justify=LEFT).grid(column=0, row=6)

#REFERENCE INPUT
ttk.Entry(frm, textvariable=ref_lat_input).grid(column=1, row=2)
ttk.Entry(frm, textvariable=ref_lon_input).grid(column=1, row=3)

#OBJECT DISTANCE INPUT
ttk.Entry(frm, textvariable=obj_lat_dist_input).grid(column=1, row=5)
ttk.Entry(frm, textvariable=obj_lon_dist_input).grid(column=1, row=6)

#GAP
ttk.Label(frm, text="").grid(column=0, row=7)
ttk.Label(frm, text="").grid(column=0, row=8)

#BUTTON
ttk.Button(frm, text="Calculate", command=calc).grid(column=0, row=9)
ttk.Button(frm, text="Copy to Clipboard", command=copy).grid(column=0, row=10)



root.mainloop()