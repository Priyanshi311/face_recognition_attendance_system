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

class Face_Recognition:
  def __init__(self, root):
    self.root=root
    self.root.geometry("1400x650+0+0")
    self.root.title("face recognition system")

    imgf = Image.open(r"C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\project pics\73a357e0-e136-444e-8df4-57df8ee66673.jpg")
    imgf = imgf.resize((1270,650),Image.LANCZOS)
    self.photoimgf=ImageTk.PhotoImage(imgf) 
    bg_imgf= Label(self.root,image=self.photoimgf)
    bg_imgf.place(x=0, y=0,width=1270, height=650)


    title_lbl1= Label(self.root, text="Face Recognition page", font=("times new roman",30, "bold"),fg="black", bg="cyan")
    title_lbl1.place(x=0, y=0, width=1300, height=65)

    b1=Button(bg_imgf,text="Face Recognition ",cursor="hand2",command=self.face_recog,font=("times new roman",15, "bold"),bg="lightgreen", fg="black")
    b1.place(x=5,y=100,width=200,height=50)


    #attendance
  def mark_attendance(self,i,n,d):
    with open(r"C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\face recognition system\attendance.csv","r+",newline="\n") as f:
      myDataList=f.readlines()
      name_list=[]
      for line in myDataList:
        entry =line.split((","))
        name_list.append(entry[0])
      if((i not in name_list)and (n not in name_list)and(d not in name_list)):
        now=datetime.now()
        d1=now.strftime("%d/%m/%Y")
        dtString=now.strftime("%H:%M:%S")
        f.writelines(f"\n{i},{n},{d},{dtString},{d1},Present")


    #===========face recognition====================
  def face_recog(self):
    def draw_boundary(img, classifier, scalefactor, minNeighbors, color, text, clf):
      gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      features = classifier.detectMultiScale(gray_image, scalefactor, minNeighbors)
      
      coord = []
      for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        id, predict = clf.predict(gray_image[y:y + h, x:x + w])
        confidence = int((100 * (1 - predict / 300)))
        try:
          conn = mysql.connector.connect(host="localhost", username="root", password="Prachi123@", database="facereco1")
          my_cursor = conn.cursor()
          
          my_cursor.execute("select name from student_det where std_id=%s", (id,))
          n=my_cursor.fetchone()
          n = n[0] if n else None 

          my_cursor.execute("select std_id from student_det where std_id=%s", (id,))
          i=my_cursor.fetchone()
          i = i[0] if i else None 

          my_cursor.execute("select dep from student_det where std_id=%s", (id,))
          d=my_cursor.fetchone()
          d= d[0] if d else None 
           
          if confidence > 77 and n is not None and i is not None and d is not None:
            cv2.putText(img,f"std_id:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
            cv2.putText(img,f"name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
            cv2.putText(img,f"dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
            self.mark_attendance(i,n,d)
          else:
            cv2.rectangle(img,(x,y),(x+w, y+h), (0,0,255),3)
            cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
        finally:
            if conn.is_connected():
                my_cursor.close()
                conn.close()

      return coord


    def recognize(img,clf,faceCascade):
      coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf) 
      return img
    
    faceCascade=cv2.CascadeClassifier(r"C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\face recognition system\haarcascade_frontalface_default.xml")
    clf=cv2.face.LBPHFaceRecognizer_create()
    clf.read(r"C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\face recognition system\classifier.xml")
    
    video_cap=cv2.VideoCapture(0)

    while True:
      ret,img=video_cap.read()
      img=recognize(img,clf,faceCascade)
      cv2.imshow("WELCOME TO FACE RECOGNITION",img)

      if cv2.waitKey(1)==13:
        break
    video_cap.release()
    cv2.destroyAllWindows()


if __name__=="__main__":
  root=Tk()
  obj=Face_Recognition(root)
  root.mainloop()
