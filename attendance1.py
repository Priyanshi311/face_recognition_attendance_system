from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog



mydata=[]




class Attendance:
  def __init__(self, root):
    self.root=root
    self.root.geometry("1400x650+0+0")
    self.root.title("Attendance system")

    #=====variables=====
    self.var_id=StringVar()
    self.var_name=StringVar()
    self.var_dep=StringVar()
    self.var_time=StringVar()
    self.var_date=StringVar()
    self.var_status=StringVar()


    
    img3 = Image.open(r'C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\project pics\ll3GLmS.webp')
    img3 = img3.resize((1400,650),Image.LANCZOS)
    self.photoimg3=ImageTk.PhotoImage(img3) 

    bg_img= Label(self.root,image=self.photoimg3)
    bg_img.place(x=0, y=60,width=1400, height=650)
    
    title_lbl= Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman",30, "bold"),bg="white", fg="black")
    title_lbl.place(x=0, y=0, width=1300, height=65)


    #LEFT LABEL FRAME
    left_frame = LabelFrame(bg_img,bd=2, relief=RIDGE, text="Attendance Details", font=("times new roman",20,"bold"))
    left_frame.place(x=30, y=90, width=580, height= 480)

    #id
    student_id_label=Label(left_frame,text="StudentID:",font=("times new roman",15,"bold")) 
    student_id_label.grid(row=2, column=0,padx=8,sticky='W')

    StudentID_entry=ttk.Entry(left_frame,textvariable=self.var_id, width=15,font=("times new roman",15,"bold"))
    StudentID_entry.grid(row=2, column=1,padx=8,pady=20,sticky='W')
   
   #name
    student_name_label=Label(left_frame,text="Name:",font=("times new roman",15,"bold")) 
    student_name_label.grid(row=2, column=2,padx=8,sticky='W')

    Name_entry=ttk.Entry(left_frame,textvariable=self.var_name, width=15,font=("times new roman",15,"bold"))
    Name_entry.grid(row=2, column=3,padx=8,pady=20,sticky='W')

    #department
    dep_label=Label(left_frame,text="Department:",font=("times new roman",15,"bold")) 
    dep_label.grid(row=3, column=0,padx=8,sticky='W')

    Dep_entry=ttk.Entry(left_frame,textvariable=self.var_dep,width=15,font=("times new roman",15,"bold"))
    Dep_entry.grid(row=3, column=1,padx=8,pady=20,sticky='W')
    
    
  #time
    time_label=Label(left_frame,text="Time",font=("times new roman",15,"bold")) 
    time_label.grid(row=3, column=2,padx=8,sticky='W')

    Time_entry=ttk.Entry(left_frame,width=15,textvariable=self.var_time,font=("times new roman",15,"bold"))
    Time_entry.grid(row=3, column=3,padx=8,pady=20,sticky='W')

#date
    date_label=Label(left_frame,text="Date:",font=("times new roman",15,"bold")) 
    date_label.grid(row=4, column=0,padx=8,sticky='W')

    Date_entry=ttk.Entry(left_frame,textvariable=self.var_date, width=15,font=("times new roman",15,"bold"))
    Date_entry.grid(row=4, column=1,padx=8,pady=20,sticky='W')


   #Status
    status_label=Label(left_frame,text="Status:",font=("times new roman",15,"bold")) 
    status_label.grid(row=4, column=2,padx=8,sticky='W')

    Status_combo=ttk.Combobox(left_frame,textvariable=self.var_status,font=("times new roman",15,"bold"),width=15,state="readonly")
    Status_combo["values"]=("select status","Present","Absent")
    Status_combo.current(0)
    Status_combo.grid(row=4, column=3, padx=8, pady=20,sticky='W')


    #button
    save_btn=Button(left_frame,text="Importcsv",command=self.importCsv, width=8,font=("times new roman",13,"bold"),bg="lightgreen")
    save_btn.grid(row=5,column=0 ,pady=30)

    save_btn1=Button(left_frame,text="Exportcsv",command=self.exportCsv,width=8,font=("times new roman",13,"bold"),bg="lightgreen")
    save_btn1.grid(row=5,column=1 ,pady=30)

    save_btn2=Button(left_frame,text="Update",width=8,font=("times new roman",13,"bold"),bg="lightgreen")
    save_btn2.grid(row=5,column=2 ,pady=30)

    save_btn3=Button(left_frame,text="Reset",command=self.reset_data,width=8,font=("times new roman",13,"bold"),bg="lightgreen")
    save_btn3.grid(row=5,column=3 ,pady=30)




    
    #right LABEL FRAME
    right_frame = LabelFrame(bg_img,bd =2, relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
    right_frame.place(x=630, y=90, width=600, height= 480)


    table_frame = Frame(right_frame,bd =2, relief=RIDGE)
    table_frame.place(x=5, y=50,width=585, height= 350)

    scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

    self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","name","department","time","date","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=self.AttendanceReportTable.xview)
    scroll_y.config(command=self.AttendanceReportTable.yview)

    self.AttendanceReportTable.heading("id",text="Attendance id")
    self.AttendanceReportTable.heading("name",text="Name")
    self.AttendanceReportTable.heading("department",text="Department")
    self.AttendanceReportTable.heading("time",text="Time")
    self.AttendanceReportTable.heading("date",text="Date")
    self.AttendanceReportTable.heading("status",text="Attendance status")
    self.AttendanceReportTable["show"]="headings"
      
    self.AttendanceReportTable.column("id", width=120)
    self.AttendanceReportTable.column("name", width=120)
    self.AttendanceReportTable.column("department", width=120)
    self.AttendanceReportTable.column("time", width=120)
    self.AttendanceReportTable.column("date", width=120)
    self.AttendanceReportTable.column("status", width=120)
    
    self.AttendanceReportTable.pack(fill=BOTH,expand=1)
    self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


  #=========FETCH DATA====
  def fetchData(self,rows):
    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
    for i in rows:
      self.AttendanceReportTable.insert("",END,values=i)


#import csv
  def importCsv(self):
    global mydata
    mydata.clear()
    fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
    with open(fln) as myfile:
      csvread=csv.reader(myfile,delimiter=",")
      for i in csvread:
        mydata.append(i)
      self.fetchData(mydata)

#export csv
  def exportCsv(self):
    try:
      if len(mydata)<1:
        messagebox.showerror("No Data","No Data Found to Export.", parent=self.root)
        return False
      fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
      with open(fln,mode="w",newline="") as myfile:
        exp_write=csv.writer(myfile, delimiter=",")
        for i in mydata:
          exp_write.writerow(i)
        messagebox.showinfo("Data Export","Data Exported Successfully")
    except Exception as es:
      messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

  def get_cursor(self, event=""):
    cursor_row=self.AttendanceReportTable.focus()
    content=self.AttendanceReportTable.item(cursor_row)
    rows=content["values"]

    self.var_id.set(rows[0])
    self.var_name.set(rows[1])
    self.var_dep.set(rows[2])
    self.var_time.set(rows[3])
    self.var_date.set(rows[4])
    self.var_status.set(rows[5])

#resetdata
  def reset_data(self):
     self.var_id.set("")
     self.var_name.set("")
     self.var_dep.set("")
     self.var_time.set("")
     self.var_date.set("")
     self.var_status.set("")









if __name__=="__main__":
  root=Tk()
  obj=Attendance(root)
  root.mainloop()
      