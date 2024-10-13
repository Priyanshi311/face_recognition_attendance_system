from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Student:
  def __init__(self, root):
    self.root=root
    self.root.geometry("1400x650+0+0")
    self.root.title("face recognition system")

    # =======variables==============
    self.var_dep=StringVar()
    self.var_course=StringVar()
    self.var_year=StringVar()
    self.var_sem=StringVar()
    self.var_stdid=StringVar()
    self.var_name=StringVar()
    self.var_dob=StringVar()
    self.var_gender=StringVar()
    self.var_pno=StringVar()
    self.var_address=StringVar()
    self.var_email=StringVar()
    self.var_teacher=StringVar()
    

   
    img = Image.open(r'C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\project pics\ll3GLmS.webp')
    img = img.resize((1400,650),Image.LANCZOS)
    self.photoimg=ImageTk.PhotoImage(img) 

    firstlabel= Label(self.root,image=self.photoimg)
    firstlabel.place(x=0, y=0,width=1400, height=650)


    img3 = Image.open(r'C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\project pics\ll3GLmS.webp')
    img3 = img3.resize((1400,650),Image.LANCZOS)
    self.photoimg3=ImageTk.PhotoImage(img3) 

    bg_img= Label(self.root,image=self.photoimg3)
    bg_img.place(x=0, y=60,width=1400, height=650)
    
    title_lbl= Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",30, "bold"),bg="white", fg="black")
    title_lbl.place(x=0, y=0, width=1300, height=65)

#LEFT LABEL FRAME
    left_frame = LabelFrame(bg_img,bd=2, relief=RIDGE, text="Student Details", font=("times new roman",20,"bold"))
    left_frame.place(x=30, y=90, width=580, height= 480)
    
#department
    dep_label=Label(left_frame,text="Department",font=("times new roman",13,"bold")) 
    dep_label.grid(row=0, column=0,padx=10,sticky='W')

    dep_combo=ttk.Combobox(left_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),width=15,state="readonly")
    dep_combo["values"]=("select department","CSE","IT","ECE","EE","ME","CE")
    dep_combo.current(0)
    dep_combo.grid(row=0, column=1, padx=1, pady=20)


    #course
    course_label=Label(left_frame,text="Course",font=("times new roman",13,"bold")) 
    course_label.grid(row=0, column=2, padx=10,sticky='W')

    course_combo=ttk.Combobox(left_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),width=15,state="readonly")
    course_combo["values"]=("select course","DBMS","EM","COA","DSP","DSA","EDC","FOP","DAA","DSD","CCS")
    course_combo.current(0)
    course_combo.grid(row=0, column=3, padx=2, pady=20,sticky='W')


    #year
    yr_label=Label(left_frame,text="Year", font=("times new roman",13,"bold")) 
    yr_label.grid(row=1, column=0,padx=10,sticky='W')

    yr_combo=ttk.Combobox(left_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),width=15,state="readonly")
    yr_combo["values"]=("select year","1","2","3","4")
    yr_combo.current(0)
    yr_combo.grid(row=1, column=1, padx=2, pady=20, sticky='W')

    #semester
    sem_label=Label(left_frame,text="Semester",font=("times new roman",13,"bold")) 
    sem_label.grid(row=1, column=2,padx=10,sticky='W')

    sem_combo=ttk.Combobox(left_frame,textvariable=self.var_sem,font=("times new roman",13,"bold"),width=15,state="readonly")
    sem_combo["values"]=("select semester","1","2")
    sem_combo.current(0)
    sem_combo.grid(row=1, column=3, padx=2, pady=20,sticky=W)
     
#STUDENT ID
    student_id_label=Label(left_frame,text="StudentID",font=("times new roman",13,"bold")) 
    student_id_label.grid(row=2, column=0,padx=10,sticky='W')

    StudentID_entry=ttk.Entry(left_frame,textvariable=self.var_stdid, width=15,font=("times new roman",13,"bold"))
    StudentID_entry.grid(row=2, column=1,padx=10,pady=10,sticky='W')
   
   #name
    student_name_label=Label(left_frame,text="Name",font=("times new roman",13,"bold")) 
    student_name_label.grid(row=2, column=2,padx=10,sticky='W')

    Name_entry=ttk.Entry(left_frame,textvariable=self.var_name, width=15,font=("times new roman",13,"bold"))
    Name_entry.grid(row=2, column=3,padx=10,pady=10,sticky='W')

    #dob
    dob_label=Label(left_frame,text="DOB",font=("times new roman",13,"bold")) 
    dob_label.grid(row=3, column=0,padx=10,sticky='W')

    DOB_entry=ttk.Entry(left_frame,textvariable=self.var_dob, width=15,font=("times new roman",13,"bold"))
    DOB_entry.grid(row=3, column=1,padx=10,pady=10,sticky='W')
    
    
  #gender
    gender_label=Label(left_frame,text="Gender",font=("times new roman",13,"bold")) 
    gender_label.grid(row=3, column=2,padx=10,sticky='W')

    Gender_entry=ttk.Entry(left_frame, textvariable=self.var_gender,width=15,font=("times new roman",13,"bold"))
    Gender_entry.grid(row=3, column=3,padx=10,pady=10,sticky='W')

    #phone number
    phone_label=Label(left_frame,text="Phone_No",font=("times new roman",13,"bold")) 
    phone_label.grid(row=4, column=0,padx=10,sticky='W')

    Phone_No_entry=ttk.Entry(left_frame,textvariable=self.var_pno, width=15,font=("times new roman",13,"bold"))
    Phone_No_entry.grid(row=4, column=1,padx=10,pady=10,sticky='W')


   #address
    address_label=Label(left_frame,text="Address",font=("times new roman",13,"bold")) 
    address_label.grid(row=4, column=2,padx=10,sticky='W')

    Address_entry=ttk.Entry(left_frame,textvariable=self.var_address, width=15,font=("times new roman",13,"bold"))
    Address_entry.grid(row=4, column=3,padx=10,pady=10,sticky='W')

    #email
    email_label=Label(left_frame,text="Email",font=("times new roman",13,"bold")) 
    email_label.grid(row=5 ,column=0,padx=10,sticky='W')

    Email_entry=ttk.Entry(left_frame,textvariable=self.var_email, width=15,font=("times new roman",13,"bold"))
    Email_entry.grid(row=5, column=1,padx=10,pady=10,sticky='W')
    #teachers name
    Teacher_label=Label(left_frame,text="Teacher",font=("times new roman",13,"bold")) 
    Teacher_label.grid(row=5, column=2,padx=10,sticky='W')

    Teacher_entry=ttk.Entry(left_frame,textvariable=self.var_teacher,width=15,font=("times new roman",13,"bold"))
    Teacher_entry.grid(row=5, column=3,padx=10,pady=10,sticky='W')
    #radio button
    self.var_r1=StringVar()
    radionbtn1=ttk.Radiobutton(left_frame,variable=self.var_r1,text="Take photo Sample",value="Yes")
    radionbtn1.grid(row=6,column=0 ,padx=10,pady=10)

    
    radionbtn2=ttk.Radiobutton(left_frame,variable=self.var_r1,text="No photo Sample",value="no")
    radionbtn2.grid(row=6,column=1 ,padx=10,pady=10)
    #button
    save_btn=Button(left_frame,text="Save",command=self.add_data, width=10,font=("times new roman",13,"bold"),bg="cyan")
    save_btn.grid(row=7,column=0 ,pady=10)

    save_btn1=Button(left_frame,text="Delete",command=self.delete_data,width=10,font=("times new roman",13,"bold"),bg="cyan")
    save_btn1.grid(row=7,column=1 ,pady=10)

    save_btn2=Button(left_frame,text="Update",command=self.update_data,width=10,font=("times new roman",13,"bold"),bg="cyan")
    save_btn2.grid(row=7,column=2 ,pady=10)

    save_btn3=Button(left_frame,text="Reset",command=self.reset_data,width=10,font=("times new roman",13,"bold"),bg="cyan")
    save_btn3.grid(row=7,column=3 ,pady=10)


    take_photo_btn=Button(left_frame,text="Take Photo",command=self.generate_dataset,width=13,font=("times new roman",13,"bold"),bg="cyan")
    take_photo_btn.grid(row=8,column=0 ,pady=5)

    update_photo_btn=Button(left_frame,text="Update Photo",command=self.generate_dataset,width=13,font=("times new roman",13,"bold"),bg="cyan")
    update_photo_btn.grid(row=8,column=1 ,pady=5)

    #right LABEL FRAME
    right_frame = LabelFrame(bg_img,bd =2, relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
    right_frame.place(x=630, y=90, width=600, height= 480)

    search_label=Label(right_frame,text="Search By:",font=("times new roman",13,"bold")) 
    search_label.grid(row=0, column=0,padx=10,sticky='W')

    search_combo=ttk.Combobox(right_frame,font=("times new roman",13,"bold"),width=15,state="readonly")
    search_combo["values"]=("select ","StudentID","Phone number")
    search_combo.current(0)
    search_combo.grid(row=0, column=1, padx=1, pady=20)

    search_btn3=Button(right_frame,text="Search",width=10,font=("times new roman",13,"bold"),bg="cyan")
    search_btn3.grid(row=0,column=2 ,padx=5,pady=10)

    showall_btn3=Button(right_frame,text="Show All",width=10,font=("times new roman",13,"bold"),bg="cyan")
    showall_btn3.grid(row=0,column=3 ,padx=5,pady=10)

     #TABLE_FRAME

    table_frame = Frame(right_frame,bd =2, relief=RIDGE)
    table_frame.place(x=5, y=100,width=585, height= 350)

    scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
    self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","ID","name","DOB","Gender","phoneno","email","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=self.student_table.xview)
    scroll_y.config(command=self.student_table.yview)

    
    self.student_table.heading("dep", text="Department")
    self.student_table.heading("course", text="Course")
    self.student_table.heading("year", text="Year")
    self.student_table.heading("sem", text="Semester")
    self.student_table.heading("ID", text="ID")
    self.student_table.heading("name", text="Name")
    self.student_table.heading("DOB", text="DOB")
    self.student_table.heading("Gender", text="Gender")
    self.student_table.heading("phoneno", text="Phoneno")
    self.student_table.heading("email", text="E-mail")
    self.student_table.heading("address", text="Address")
    self.student_table.heading("teacher", text="Teacher")
    self.student_table.heading("photo", text="Photo")
    self.student_table["show"]="headings"

    
      
    self.student_table.column("dep", width=80)
    self.student_table.column("course", width=80)
    self.student_table.column("year", width=80)
    self.student_table.column("sem", width=80)
    self.student_table.column("ID", width=80)
    self.student_table.column("name", width=80)
    self.student_table.column("DOB", width=80)
    self.student_table.column("Gender", width=80)
    self.student_table.column("phoneno", width=80)
    self.student_table.column("email",width=80)
    self.student_table.column("address", width=80)
    self.student_table.column("teacher",width=80) 
    self.student_table.column("photo",width=130) 
    self.student_table["show"]="headings"

    self.student_table.pack(fill=BOTH,expand=1)
    self.student_table.bind("<ButtonRelease>",self.get_cursor)
    self.fetch_data()
  #func declaration
  def add_data(self):
    if self.var_dep.get()=="Select Department" or  self.var_stdid.get()=="" or  self.var_name.get()=="":
      messagebox.showerror("Error","All fields are required", parent=self.root)
    else:
      try:
        conn=mysql.connector.connect(host="localhost",username="root", password="Prachi123@",database="facereco1")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into student_det values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                     self.var_dep.get(),
                                                                                                     self.var_course.get(),
                                                                                                     self.var_year.get(),
                                                                                                     self.var_sem.get(),
                                                                                                     self.var_stdid.get(),
                                                                                                     self.var_name.get(),
                                                                                                     self.var_dob.get(),
                                                                                                     self.var_gender.get(),
                                                                                                     self.var_pno.get(),
                                                                                                     self.var_email.get(),
                                                                                                     self.var_address.get(),
                                                                                                     self.var_teacher.get(),
                                                                                                     self.var_r1.get()



                                                                                                    ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Student details have been submitted successfully",parent=self.root)
      except Exception as es:
        messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
  #fetch data
  def fetch_data(self):
    conn=mysql.connector.connect(host="localhost",username="root", password="Prachi123@",database="facereco1")
    my_cursor=conn.cursor()
    my_cursor.execute("select*from student_det")
    data= my_cursor.fetchall()
    if len(data)!=0:
      self.student_table.delete(*self.student_table.get_children())
      for i in data:
        self.student_table.insert("",END,values=i)
      conn.commit()
    conn.close()    
  #get cursor
  def get_cursor(self,event=""):
    cursor_focus=self.student_table.focus()
    content = self.student_table.item(cursor_focus)
    data=content["values"]
    
    self.var_dep.set(data[0])
    self.var_course.set(data[1])
    self.var_year.set(data[2])
    self.var_sem.set(data[3])
    self.var_stdid.set(data[4])
    self.var_name.set(data[5])
    self.var_dob.set(data[6])
    self.var_gender.set(data[7])
    self.var_pno.set(data[8])
    self.var_email.set(data[9])
    self.var_address.set(data[10])
    self.var_teacher.set(data[11])
    self.var_r1.set(data[12])

#update function

  def update_data(self):
    if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_stdid.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
        return

    try:
        update = messagebox.askyesno("Update", "Do you want to update student details?", parent=self.root)
        if update:
            conn = mysql.connector.connect(host="localhost", username="root", password="Prachi123@", database="facereco1")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE student_det SET dep=%s, course=%s, year=%s, sem=%s, name=%s, dob=%s, gender=%s, phone_no=%s, email=%s, address=%s, teacher=%s, photosample=%s WHERE std_id=%s", (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_name.get(),
                self.var_dob.get(),
                self.var_gender.get(),
                self.var_pno.get(),
                self.var_email.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_r1.get(),
                self.var_stdid.get()  # std_id for the WHERE clause
            ))
            conn.commit()
            messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
            self.fetch_data()
    except Exception as es:
        messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    finally:
        if conn:
            conn.close()


  #delete function
  def delete_data(self):
     if self.var_stdid.get()=="":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
     else:
        try:
           delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
           if delete:
            conn = mysql.connector.connect(host="localhost", username="root", password="Prachi123@", database="facereco1")
            my_cursor = conn.cursor()
            sql="delete from student_det where std_id=%s"
            val=(self.var_stdid.get(),)
            my_cursor.execute(sql,val) 
           else:
              if not delete:
                 return
           conn.commit()
           self.fetch_data()
           conn.close()
           messagebox.showinfo("delete","Successfully deleted student details")  
        except Exception as es:
           messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
        finally:
           if conn:
            conn.close()

#reset function
  def reset_data(self):
    self.var_dep.set("Select Department")
    self.var_course.set("Select Course")
    self.var_year.set("select year")
    self.var_sem.set("select semester")
    self.var_stdid.set("")
    self.var_name.set("")
    self.var_dob.set("")
    self.var_gender.set("")
    self.var_pno.set("")
    self.var_email.set("")
    self.var_address.set("")
    self.var_teacher.set("")
    self.var_r1.set("")
   
  # generate data set or take photo samples
  def generate_dataset(self):
     if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_stdid.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
     else: 
      try:
         conn = mysql.connector.connect(host="localhost", username="root", password="Prachi123@", database="facereco1")
         my_cursor = conn.cursor()
         my_cursor.execute("select * from  student_det")
         myresult=my_cursor.fetchall()
         id=0
         for x in myresult:
            id+=1
         my_cursor.execute("UPDATE student_det SET dep=%s, course=%s, year=%s, sem=%s, name=%s, dob=%s, gender=%s, phone_no=%s, email=%s, address=%s, teacher=%s, photosample=%s WHERE std_id=%s", (
                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_pno.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                        self.var_r1.get(),
                                                                                                                                                                        self.var_stdid.get()  # std_id for the WHERE clause
                                                                                                                                                                    ))
         conn.commit()
         self.fetch_data()
         self.reset_data()
         conn.close()

  #load predefined data on face frontals from opencv
         face_classifier =cv2.CascadeClassifier(r"C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\face recognition system\haarcascade_frontalface_default.xml")
         def face_cropped(img):
          gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
          faces=face_classifier.detectMultiScale(gray,1.3,5)
            #scalling factor = 1.3
            #minimum neighbour=5

          for (x,y,w,h) in faces:
            face_cropped=img[y:y+h,x:x+w]
            return face_cropped

         cap=cv2.VideoCapture(0)
         img_id=0
         while True:
          ret,myframe=cap.read()
          if face_cropped(myframe) is not None:
            img_id+=1
            face=cv2.resize(face_cropped(myframe),(450,450))
            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
            file_name_path=r"C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\face recognition system\data\user."+str(id)+"."+str(img_id)+".jpg"
            cv2.imwrite(file_name_path,face)
            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
            cv2.imshow("Crooped Face",face)

          if cv2.waitKey(1)==13 or int(img_id)==100:
            break
         cap.release()
         cv2.destroyAllWindows()
         messagebox.showinfo("Result","Generating data sets completed!!!")
      except Exception as es:
           messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
      finally:
        if conn:
          conn.close()
            



      


        
     
                                                                                                                                                                
                                                                                                                                                                           
                                                                                                                                                                           
                                                                                                                                                                           
                                                                                                                                                                           
                                                                                                                                                                           
                                                                                                                                                   
 


    

    
if __name__=="__main__":
  root=Tk()
  obj=Student(root)
  root.mainloop()
      