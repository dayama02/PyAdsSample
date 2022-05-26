#! python3
# # -*- coding: utf8 -*-

from cgitb import text
from tkinter import *
from tkinter import ttk
from turtle import width
import pyads


def write_value():
    print("write value")
    net_id = net_id_text.get()
    port = int(port_text.get())
    value = int(value_text.get())
    ads_client = pyads.Connection(net_id, port)
    ads_client.open()
    ads_client.write_by_name("Untitled1_Obj1 (Module1).Inputs.Value",value)
    ads_client.close()

root = Tk()
root.title("pyads sample")
frm = ttk.Frame(root,padding=10)
frm.grid()

# default value
ads_net_id_default  = StringVar(frm, value="192.168.50.172.1.1")
port_number_default = StringVar(frm, value="340")
value_default       = StringVar(frm, value="0")

# place widgets
ttk.Label(frm, text="net id").grid(column=0, row=0)
net_id_text = ttk.Entry(frm, textvariable=ads_net_id_default, width=20)
net_id_text.grid(column=1, row=0)
ttk.Label(frm, text="port").grid(column=0, row=1)
port_text = ttk.Entry(frm, textvariable=port_number_default, width=20)
port_text.grid(column=1, row=1)

ttk.Label(frm, text="value").grid(column=0, row=2)
value_text = ttk.Entry(frm, textvariable=value_default,width=20)
value_text.grid(column=1, row=2)
ttk.Button(frm, text="write", command=write_value).grid(column=2, row=2)

root.mainloop()