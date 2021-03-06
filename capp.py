import ast
import math
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import *
from operator import itemgetter
from prettytable import PrettyTable

def ppc():
  operations = []
  operation1 = []
  operation2 = []
  final_sequence = []

  # function that splits the operations 
  def split_opr(coded):
    c=0
    for e in coded:   
      if(e[0]=='D'):
        c = c + 1
      if(e[0]=='ch'):
        c = c + 1
      if(e[0]=='Tr'):
        c = c + 1
      if(e[0]=='Ta'):
        c = c + 1
      if(e[0]=='Tt'):
        c = c + 1
      if(e[0]==('T' or 'K')):
        c = c + 1
        break
    operation2 = code[:c]
    del code[:c]
    return (osm(code) + osm(operation2))

  # function to sequence the opertions
  def osm(coded):
    operations = []
    for i in coded:
      if(i[0]=='T'):
        operations.append(i)
      sequence=sorted(operations, key = itemgetter(3), reverse = True)

    max_dia = sequence[0][3]
    for i in coded:
      if i not in sequence:
        sequence.append(i)
    return sequence

  final_sequence = split_opr(code)

  #2

  # function that selects the tool for corresponding operations
  def tool_m(c):
    if(c[0]=="T"):
      return "Carbide Insert"
    if(c[0]=="ch"):
      return "Carbide Insert"
    if(c[0]=="D"):
      return "Brazed Carbide"
    if(c[0]=="Tt"):
      return "Carbide Insert"

  # function to choose the component number
  def comp_no(c):
    return "NA"

  # function to offset_ number 
  def offset_no(c):
    if(c[0]=="T"):
      return "05"

  # function to choose tool number
  def tool_no(c):
    if(c[0]=="T"):
      t = list(str(ono[-1]))
      return "T11" + str(t[0])
    if(c[0]=="ch"):
      t = list(str(ono[-1]))
      return "T12" + str(t[0])
    if(c[0]=="D"):
      if(c[2]<10):
        return "D10" + str(c[2])
      else:
        return "D1" + str(c[2])

  # function to choose tool
  def tooling(c):
    if(c[0]=="T"):
      return "RH Turn tool"
    if(c[0]=="D"):
      #condition to refer the standard drill size
      return u"\u2300" + str(c[2]) +" carbide twist drill"
    if(c[0]=="ch"):
      return "RH Turn tool"

  # function to calculate machining time
  def m_time(m_allowance, c):
    if(c[0]=="F"):
      return ((c[2]/2)+m_allowance)/(fr[-1]*sp[-1])
    if(c[0]=="P"):
      return ((c[2]/2)+m_allowance)/(fr[-1]*sp[-1])
    if(c[0]=="Tt"):
      l = math.sqrt((c[2]**2)+(c[3]**2))
      return (l+m_allowance)/(fr[-1]*sp[-1])
    if(c[0]=="D"):
      m = int(c[2]/2)
      return (c[3]+(2*m))/(fr[-1]*sp[-1])
    else:
      return (c[3]+m_allowance)/(fr[-1]*sp[-1])

  # function to calculate feed
  def feed(mat, Tool, c, p):

    global rf_feed,ff_feed,d_feed,feed_d,rfr,ffr,dfr

    feed_r_drilling_carbide_HSS =[[2,0.15,0.05]
                                ,[4,0.15,0.10]
                                ,[6,0.15,0.12]
                                ,[8,0.18,0.15]
                                ,[10,0.25,0.18]
                                ,[12,0.25,0.21]
                                ,[14,0.28,0.24]
                                ,[16,0.32,0.26]
                                ,[18,0.32,0.28]
                                ,[20,0.32,0.30]]

    feed_r_turning_carbide_r_f = [["Low carbon steels",0.15,1.1]
                            ,["Medium carbon steels",0.15,0.8]
                            ,["Steel alloys",0.1,0.75]
                            ,["Grey cast iron",0.1,1.0]
                            ,["Stainless Steel",0.2,2.0]
                            ,["Chromium nickel",0.1,1.0]
                            ,["Aluminium",0.2,1.0]
                            ,["Brass",0.15,1.5]
                            ,["Plastics",0.2,1.0]]

    feed_r_turning_HSS_r_f = [["Low carbon steels",0.15,0.45]
                           ,["Medium carbon steels",0.15,0.4]
                           ,["Steel alloys",0.1,0.3]
                           ,["Grey cast iron",0.1,0.4]
                           ,["Stainless Steel",0.2,0.75]
                           ,["Chromium nickel",0.1,0.6]
                           ,["Aluminium",0.2,0.6]
                           ,["Brass",0.15,8.0]
                           ,["Plastics",0.1,0.35]]

    if(Tool == "carbide"):
      feed_t = feed_r_turning_carbide_r_f
    if(Tool == "HSS"):
      feed_t = feed_r_turning_HSS_r_f

    feed_d = feed_r_drilling_carbide_HSS

    if(Tool == "carbide"):
      v = 1
    if(Tool == "HSS"):
      v = 2

    if(c[0]=="T"): 
      for Feeds in feed_t:
        if(material == mat):
          rf_feed = Feeds[1]
          ff_feed = Feeds[2]
          if(p=="r"):
            return rf_feed
          if(p=="f"):
            return ff_feed

    if(c[0]=="D"):
      d = c[2]
      for feeds in feed_d:
        if(feeds[0] <= d):
          d_feed = feeds[v]
          continue   
      return d_feed

    if(c[0]=="ch"):
      return ff_feed

  #Surface cutting speeds in metres per minute
  def velocity(mat,Tool):
    global rm_speed
    global fm_speed

    cutting_speed_carbide = [["Low carbon steels",60,230]
                           ,["Medium carbon steels",45,210]
                           ,["Steel alloys",60,170]
                           ,["Grey cast iron",60,210]
                           ,["Stainless Steel",55,200]
                           ,["Chromium nickel",60,140]
                           ,["Aluminium",60,210]
                           ,["Brass",90,305]
                           ,["Plastics",50,230]]

    cutting_speed_HSS =    [["Low carbon steels",20,110]
                           ,["Medium carbon steels",20,80]
                           ,["Steel alloys",20,80]
                           ,["Grey cast iron",20,50]
                           ,["Stainless Steel",20,50]
                           ,["Chromium nickel",15,60]
                           ,["Aluminium",30,110]
                           ,["Brass",50,110]
                           ,["Plastics",30,150]]

    if(Tool == "carbide"):
      speeds = cutting_speed_carbide
    if(Tool == "HSS"):
      speeds = cutting_speed_HSS

    for speed in speeds:
      if(speed[0]==mat):
        rm_speed = speed[1]
        fm_speed = speed[2]

  # calculating the required rpm values
  def rpm(material, Tool, c, p):
    global fm_rpm,rm_rpm
    velocity(material,Tool)

    if(c[0]!="Tt"):
      rm_rpm = (1000*rm_speed)/(math.pi*c[3])
      fm_rpm = (1000*fm_speed)/(math.pi*c[3])
      if(p=="r"):
        return round(rm_rpm)
      if(p=="f"):
        return round(fm_rpm)
    if(c[0]=="Tt"):
      rm_rpm = (1000*rm_speed)/(math.pi*((c[3]+c[4])/2))
      fm_rpm = (1000*rm_speed)/(math.pi*((c[3]+c[4])/2))

  #3

  route_sheet = []
  operation_sheet = []
  tooling_list = []
  mat = material
  tool = toolm
  m_a = 2 # machining allowance

  # machines and operations
  def machines(c):
    if(c[0] == 'T'):
      return "NC Lathe"
    if(c[0] == "ch"):
      return "NC Lathe"
    if(c[0] == "S"):
      return "Slotting Machine"
    if(c[0] == 'D'):
      if(c[4] == "A"):
        return "NC Lathe"
      if(c[4] =="R"):
        return "Drill Press"

  # main function      
  def process_plan(coded):
    n = 0
    onr.append(op_no)
    des_r.append("Cast Initial Geometry")
    W_centre.append("Foundry")
    M_tool.append("Investment Casting")

    for i in coded:
      if(i[0]=='T'):
        sp.append(rpm(mat,tool,i,"f"))
        f.append(round(feed(mat,tool,i,"f")*sp[-1]/1000,2))
        fr.append(feed(mat,tool,i,"f"))
        t_d.append(tooling(i))
        op_t.append(round(m_time(m_a,i),3))
        des.append("Turn " + u"\u2300" + str(i[3]) + " X " + str(i[2]) + "mm" )
        n = n + 10
        if(des_r[-1]!='Turning'):
          n=10
          des_r.append("Turning")
          onr.append(onr[-1]+100)
          W_centre.append("Machine Shop")
          M_tool.append(machines(i))
        ont.append(onr[-1]+n)
        ono.append(onr[-1]+n)
        t_n.append(tool_no(i))
        of_n.append(offset_no(i))
        c_no.append(comp_no(i))
        t_m.append(tool_m(i))
        M_tool_o.append(machines(i))

      if(i[0]=="ch"):
        sp.append(rpm(mat,tool,i,"f"))
        f.append(round(feed(mat,tool,i,"f")*sp[-1]/1000,2))
        fr.append(feed(mat,tool,i,"f"))
        op_t.append(round(m_time(m_a,i),3))
        t_d.append(tooling(i))
        onr.append(onr[-1]+100)
        ono.append(onr[-1]+10)
        ont.append(onr[-1]+10)
        t_n.append(tool_no(i))
        des.append("Chamfer " + str(i[3]) + u"\u00B0" + " X " + str(i[2]) + "mm")
        des_r.append("Chamfering")
        W_centre.append("Machine Shop")
        M_tool.append("NC Lathe")
        of_n.append(offset_no(i))
        c_no.append(comp_no(i))
        t_m.append(tool_m(i))
        M_tool_o.append(machines(i))

      if(i[0]=='D'):
        sp.append(rpm(mat,tool,i,"f"))
        f.append(round(feed(mat,tool,i,"f")*sp[-1]/1000,2))
        fr.append(feed(mat,tool,i,"f"))
        op_t.append(round(m_time(m_a,i),3))
        t_d.append(tooling(i))
        t_n.append(tool_no(i))
        des.append("Drill " + str(i[1]) + " X " + u"\u2300" + str(i[2]) + " by " + str(i[3]) + "mm deep holes")
        if(des_r[-1]!='Drilling'):
          des_r.append("Drilling")
          onr.append(onr[-1]+100)
          W_centre.append("Machine Shop")
          if(i[4]=="A"):
            M_tool.append(machines(i))
            M_tool_o.append(machines(i))
          if(i[4]=="R"):
            M_tool.append(machines(i))
            M_tool_o.append(machines(i))
        ono.append(onr[-1]+10)
        of_n.append(offset_no(i))
        c_no.append(comp_no(i))
        t_m.append(tool_m(i))
        ont.append(onr[-1]+10)
      if(i[0]=='S'):
        sp.append(rpm(mat,tool,i,"f"))
        f.append(round(feed(mat,tool,i,"f")*sp[-1]/1000,2))
        fr.append(feed(mat,tool,i,"f"))
        op_t.append(round(m_time(m_a,i),3))
        t_d.append(tooling(i))
        onr.append(onr[-1]+100)
        t_n.append(tool_no(i))
        des.append("Machine " + str(i[2]) + " X " + str(i[3]) + " X " + str(i[4]) + "mm slot")
        des_r.append("Slotting")
        W_centre.append("Machine Shop")
        M_tool.append(machines(i))
        M_tool_o.append(machines(i))
        of_n.append(offset_no(i))
        c_no.append(comp_no(i))
        t_m.append(tool_m(i))
        ono.append(onr[-1]+10)
        ont.append(onr[-1]+10)
        
  op_no = 100
  ono = []
  onr = []
  ont = []
  des = []
  sp = []
  f = []
  fr = []
  op_t = []
  t_d = []
  t_n = []
  of_n = []
  c_no = []
  t_m = []
  des_r = []
  W_centre = []
  M_tool = []
  M_tool_o = []
  mhr=[]
  op_time = []
  factory_oh = []
  process_plan(final_sequence)

  onr.append(onr[-1]+100)
  onr.append(onr[-1]+100)
  des_r.append("Finishing")
  des_r.append("Final Inspection")
  W_centre.append("Foundry")
  W_centre.append("Inspection")
  M_tool.append("Shake Down and Finishing")
  M_tool.append("QA Department")
  
  for m in M_tool_o:
    if(m == 'NC Lathe'):
      mhr.append(225)
    if(m == 'Drill Press'):
      mhr.append(40)
  for g in op_t:
    op_time.append(g/3600)
  op_time_sum = sum(op_time)
  
  factory_oh = np.multiply(mhr,op_time)
  factory_OH = sum(factory_oh)
  
  volume = 901555
  volume = volume/1000
  density = 7.8
  d_m_cost = 90
  labour_rate = 50
  batch_quantity = 200
  
  direct_material =(volume * density/1000) * d_m_cost

  total_d_m = direct_material * batch_quantity

  print(total_d_m)

  print("dm=",direct_material)

  direct_labour = labour_rate * op_time_sum

  #direct_expenses 

  prime_cost = direct_material + direct_labour

  factory_cost = prime_cost + factory_OH

  admin_OH = 0.05 * factory_cost

  COP = factory_cost + admin_OH

  selling_OH = 10 * batch_quantity

  selling_cost = COP + selling_OH

  profit = 0.15 * selling_cost

  selling_price = profit + selling_cost
  
  print(selling_price)
  
  for j in range(len(onr)):
    route_sheet.append([onr[j], des_r[j], W_centre[j], M_tool[j]])
  for k in range(len(ono)):
    operation_sheet.append([ono[k], des[k], M_tool_o[k], t_d[k], sp[k], f[k], op_t[k]])
  for l in range(len(ont)):
    tooling_list.append([ont[l], t_n[l], of_n[l], c_no[l], t_d[l], t_m[l]])

  #4
  global r,o,t

  r = PrettyTable()
  o = PrettyTable()
  t = PrettyTable()

  start = "\033[1m"
  end = "\033[0m"

  r.field_names = ["Operation No", "Description", "Work Centre", "Machine Tool"]
  o.field_names = ["Operation No", "Description", "Machine Tool", "Tooling", "Speed (rev/min)", "Feed (mm/min) ", "Op. Time (min)"]
  t.field_names = ["Operation No", "Tool No", "Offset No", "Comp. No", "Tooling Description", "Tool Material"]

  for item in route_sheet:
    r.add_row(item)
  for items in operation_sheet:
    o.add_row(items)
  for items in tooling_list:
    t.add_row(items)

  print("\n\n" + start + "ROUTE SHEET".center(150,"-") + end + "\n")
  print(r)
  print("\n\n" + start + "OPERATION SHEET".center(150,"-") + end + "\n")
  print(o)
  print("\n\n" + start + "TOOLING LIST".center(150,"-") + end + "\n")
  print(t)
  
  name_r = tk.Label(frame, text="ROUTE SHEET", bg='#50c878')
  name_r.place(relx=0.01, rely=0.32, relwidth=0.2)
  label_code_r = tk.Label(frame, text=r, bg='#50c878')
  label_code_r.place(relx=0.01, rely=0.35,relwidth=0.5)
  
  name_o = tk.Label(frame, text="OPERATION SHEET", bg='#50c878')
  name_o.place(relx=0.4,rely=0.32,relwidth=0.2)
  label_code_o = tk.Label(frame, text=o, bg='#50c878')
  label_code_o.place(relx=0.5, rely=0.35,relwidth=0.5)
  
  name_t = tk.Label(frame, text="TOOLING LIST", bg='#50c878')
  name_t.place(relx=0.01, rely=0.625, relwidth=0.2)
  label_code_t = tk.Label(frame, text=t, bg='#50c878')
  label_code_t.place(relx=0.01, rely=0.65,relwidth=0.5)
  return True

window = tk.Tk()

window.title("PROCESS PLANNING ASSIGNMENT")

canvas = tk.Canvas(window, height=700, width=800)
canvas.pack()

frame = tk.Frame(window, bg='#50c878')
frame.place(relx=0.005, rely=0.19, relwidth=0.990, relheight=0.8)

label = tk.Label(window, text="CAPP ")
label.config(font=("Ariel",70))
label.place(relx=.5,rely=.1, anchor='center')

label1 = tk.Label(window, text = r"(COMPUTER AIDED PROCESS PLANNING - Generative Type)")
label1.place(relx=.5,rely=0.175, anchor='center')

label_code = tk.Label(frame, text="Component Code : ", bg='#50c878', anchor='n')
label_code.place(relx=0.01, rely=0.02)

code_entry = tk.Entry(frame, font = 40)
code_entry.config(font=("Ariel"))
code_entry.place(relwidth = 0.65, relheight=0.05, relx=0.25, rely=0.01,)

w_var = StringVar(window)
w_materials = {'Low cabon steels','Medium carbon steels', 'Steel alloys', 'Grey cast iron'
              ,'Stainless Steel','Chromium nickel','Aluminium','Brass','Plastics'}
w_var.set('Low carbon steels')

popupMenu1 = OptionMenu(frame, w_var, *w_materials)
menu = tk.Label(frame, text = "Choose the Workpiece Material", bg='#50c878')
menu.place(relx=0.01, rely=0.09)
popupMenu1.place(relx = 0.25, rely=0.085, relwidth=0.3, relheight=0.05)

def change_dropdown(*args):
  w_var.get()

w_var.trace('w', change_dropdown)

t_var = StringVar(window)
t_materials = {'carbide','HSS'}
t_var.set('carbide')

popupMenu2 = OptionMenu(frame, t_var, *t_materials)
menu1 = tk.Label(frame, text="Choose Tool Material", bg="#50c878")
menu1.place(relx=0.01, rely=0.155)
popupMenu2.place(relx=0.25, rely = 0.155, relwidth=0.3, relheight=0.05)

def change_dropdown2(*args):
  t_var.get()

t_var.trace('w', change_dropdown2)

def generate(c, w_mat, t_mat):
  global code
  global material
  global toolm

  code = ast.literal_eval(c)
  material = w_mat
  toolm = t_mat
  ppc()
  
button = tk.Button(frame, text = "Generate", bg='#006400',fg='#ffffff', 
                   command = lambda: generate(code_entry.get(), w_var.get(), t_var.get()))
button.place(relx=0.4, rely=0.250, relwidth=0.2)

window.mainloop()