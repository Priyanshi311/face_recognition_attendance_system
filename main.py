from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance1 import Attendance
import tkinter
from time import strftime
from datetime import datetime


class Face_recognition_system:
  def __init__(self, root):
    self.root=root
    self.root.geometry("1400x650+0+0")
    self.root.title("face recognition system")

   
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
    
    title_lbl= Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman",30, "bold"),bg="white", fg="black")
    title_lbl.place(x=0, y=0, width=1300, height=65)
    
    def time():
      string=strftime("%H:%M:%S %p")
      lbl.config(text=string)
      lbl.after(1000,time)
    lbl=Label(title_lbl,font=('times new roman',14,"bold"),bg="white",fg="red")
    lbl.place(x=50,y=10,width=100,height=50)
    time() 

    #firstimg
    img4 = Image.open(r'C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\project pics\6dfb0805-d79b-4ba7-a659-d97e06f2ca80.jpg')
    img4 = img4.resize((150,150),Image.LANCZOS)
    self.photoimg4=ImageTk.PhotoImage(img4) 

    b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.student_details)
    b1.place(x=250,y=100,width=150,height=150)

    b1_1=Button(bg_img,text="Student Details",cursor="hand2",command=self.student_details,font=("times new roman",15, "bold"),bg="white", fg="black")
    b1_1.place(x=250,y=250,width=150,height=40)

    #secondimg
    img5 = Image.open(r'C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\project pics\b1123b3d-401f-4f7d-a6f6-0d0f4c8a06ad.jpg')
    img5 = img5.resize((150,150),Image.LANCZOS)
    self.photoimg5=ImageTk.PhotoImage(img5) 

    
    b2=Button(bg_img,command= self.face_data,image=self.photoimg5)
    b2.place(x=560,y=100,width=150,height=150)

    b2_2=Button(bg_img,text="Face Recognition",cursor="hand2",command= self.face_data,font=("times new roman",15, "bold"),bg="white", fg="black")
    b2_2.place(x=560,y=250,width=150,height=40)

    #thirdimg
    img6 = Image.open(r'C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\project pics\096c36da-65c2-4c51-beb6-4b1d7cb35dd4.jpg')
    img6 = img6.resize((150,150),Image.LANCZOS)
    self.photoimg6=ImageTk.PhotoImage(img6) 

    b3=Button(bg_img,image=self.photoimg6,command=self.attendance_data)
    b3.place(x=880,y=100,width=150,height=150)

    b3_3=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15, "bold"),bg="white", fg="black")
    b3_3.place(x=880,y=250,width=150,height=40)

    



    img8 = Image.open(r"C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\project pics\000c38d6-d2d7-4bb0-ba01-a8f8e8654e4f.jpg")
    img8 = img8.resize((150,150),Image.LANCZOS)
    self.photoimg8=ImageTk.PhotoImage(img8) 

    b5=Button(bg_img,image=self.photoimg8,command=self.train_data)
    b5.place(x=250,y=350,width=150,height=150)
    b5_5=Button(bg_img,text="Training model",cursor="hand2",command=self.train_data,font=("times new roman",15, "bold"),bg="white", fg="black")
    b5_5.place(x=250,y=500,width=150,height=40)





    img9 = Image.open(r'C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\project pics\08673cf7-f343-48a2-ba37-52f0207b8b90.jpg')
    img9 = img9.resize((150,150),Image.LANCZOS)
    self.photoimg9=ImageTk.PhotoImage(img9) 

    b6=Button(bg_img,image=self.photoimg9,command=self.open_image)
    b6.place(x=560,y=350,width=150,height=150)
    b6_6=Button(bg_img,text="Photos",cursor="hand2",command=self.open_image,font=("times new roman",15, "bold"),bg="white", fg="black")
    b6_6.place(x=560,y=500,width=150,height=40)








    img11 = Image.open(r'C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\project pics\dc94e539-0e94-4948-958a-4b7bb2ac7208.jpg')
    img11 = img11.resize((150,150),Image.LANCZOS)
    self.photoimg11=ImageTk.PhotoImage(img11) 

    b8=Button(bg_img,image=self.photoimg11,command=self.iexit)
    b8.place(x=880,y=350,width=150,height=150)
    b8_8=Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("times new roman",15, "bold"),bg="white", fg="black")
    b8_8.place(x=880,y=500,width=150,height=40)


  def open_image(self):
    os.startfile(r"C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\face recognition system\data")
  #function buttons
  def student_details(self):
    self.new_window=Toplevel(self.root)
    self.app=Student(self.new_window)  

  def train_data(self):
    self.new_window=Toplevel(self.root)
    self.app=Train(self.new_window)       

  def face_data(self):
    self.new_window=Toplevel(self.root)
    self.app=Face_Recognition(self.new_window)    

  def attendance_data(self):
    self.new_window=Toplevel(self.root)
    self.app=Attendance(self.new_window) 

  def iexit(self):
    self.iexit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit?",parent=self.root)
    if self.iexit>0:
      self.root.destroy()
    else:
      return

        








    

    



 


if __name__=="__main__":
  root=Tk()
  obj=Face_recognition_system(root)
  root.mainloop()
      