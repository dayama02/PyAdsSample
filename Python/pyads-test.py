#! python3
# # -*- coding: utf8 -*-

from cgitb import text
from tkinter import *
from tkinter import ttk
import tkinter
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

def read_value():
    print("read value")
    net_id = net_id_text.get()
    port = int(port_text.get())
    ads_client = pyads.Connection(net_id, port)
    ads_client.open()
    value = ads_client.read_by_name("Untitled1_Obj1 (Module1).Outputs.Value")
    ads_client.close()
    count_text.delete(0, tkinter.END)
    count_text.insert(0, value)

    
root = Tk()
root.title("pyads sample")
frm = ttk.Frame(root,padding=10)
frm.grid()

# default value
ads_net_id_default  = StringVar(frm, value="192.168.50.179.1.1")
port_number_default = StringVar(frm, value="340")
write_value_default = StringVar(frm, value="0")
read_value_default  = StringVar(frm, value="0")

# place widgets
ttk.Label(frm, text="net id").grid(column=0, row=0)
net_id_text = ttk.Entry(frm, textvariable=ads_net_id_default, width=20)
net_id_text.grid(column=1, row=0)
ttk.Label(frm, text="port").grid(column=0, row=1)
port_text = ttk.Entry(frm, textvariable=port_number_default, width=20)
port_text.grid(column=1, row=1)

ttk.Label(frm, text="value").grid(column=0, row=2)
value_text = ttk.Entry(frm, textvariable=write_value_default,width=20)
value_text.grid(column=1, row=2)
ttk.Button(frm, text="write", command=write_value).grid(column=2, row=2)

ttk.Label(frm, text="count").grid(column=0, row=3)
count_text = ttk.Entry(frm, textvariable=read_value_default, width=20)
count_text.grid(column=1, row=3)
ttk.Button(frm, text="read", command=read_value).grid(column=2, row=3)
root.mainloop()