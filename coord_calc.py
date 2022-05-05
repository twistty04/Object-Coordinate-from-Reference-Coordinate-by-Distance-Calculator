from email.header import Header
from tkinter import *
from tkinter import ttk
import math

root = Tk()

frm = ttk.Frame(root, padding=30)
frm.grid()




#final_lat = ((float(obj_lat)/101)/3600) + ref_lat
#long_ref = ((math.cos(final_lat * math.pi/180.0 ) * 24902.0/360.0) * 5280)/3600
#final_long = ((float(obj_lon)/long_ref)/3600) + ref_lon


ttk.Label(frm, text="Latitude/Longitude Calculator").grid(column=0, row=0)
ttk.Label(frm, text="Reference Latitude").grid(column=0, row=1)
ttk.Label(frm, text="Reference Longitude").grid(column=0, row=2)
ttk.Label(frm, text="").grid(column=0, row=3)
ttk.Label(frm, text="Vertical Distance from Reference Latitude").grid(column=0, row=4)
ttk.Label(frm, text="Horizontal Distance from Reference Longitude").grid(column=0, row=5)
ttk.Entry(frm, ).grid(column=1, row=1)
ttk.Entry(frm).grid(column=1, row=2)
ttk.Entry(frm).grid(column=1, row=4)
ttk.Entry(frm).grid(column=1, row=5)
ttk.Label(frm, text="").grid(column=0, row=6)
ttk.Label(frm, text="").grid(column=0, row=7)


ttk.Button(frm, text="Calculate", command=root.destroy).grid(column=0, row=8)


root.mainloop()