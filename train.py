from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np








class Train:
  def __init__(self, root):
    self.root=root
    self.root.geometry("1400x650+0+0")
    self.root.title("face recognition system")
    

    img4 = Image.open(r"C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\project pics\4a93f546-f0be-4165-93ff-c5c0f95c7abe.jpg")
    img4 = img4.resize((1270,650),Image.LANCZOS)
    self.photoimg4=ImageTk.PhotoImage(img4) 

    bg_imgT= Label(self.root,image=self.photoimg4)
    bg_imgT.place(x=0, y=0,width=1270, height=650)

    title_lbl= Label(bg_imgT, text="TRAIN DATA SET", font=("times new roman",30, "bold"),bg="white", fg="black")
    title_lbl.place(x=0, y=0, width=1300, height=65)

    

    b1=Button(bg_imgT,text="TRAIN DATA",cursor="hand2",command=self.train_classifier,font=("times new roman",15, "bold"),bg="cyan", fg="black")
    b1.place(x=5,y=100,width=1260,height=50)



    #===train function
  def train_classifier(self):
    data_dir=(r"C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\face recognition system\data")
    path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
    faces=[]
    ids=[]

    for image in path:
      img=Image.open(image).convert("L")#gray scale image
      imageNP=np.array(img,"uint8")
      id=int(os.path.split(image)[1].split('.')[1])
      faces.append(imageNP)
      ids.append(id)
      cv2.imshow("training",imageNP)
      cv2.waitKey(1)==13
    ids=np.array(ids)  


    #=====TRAIN THE CLASSIFIER AND SAVE===
    clf= cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces,ids)
    clf.write(r"C:\Users\priya\OneDrive\Pictures\Desktop\face recognition attendsance system\face recognition system\classifier.xml")
    cv2.destroyAllWindows()
    messagebox.showinfo("Result","Training Dataset Completed!!")






















if __name__=="__main__":
  root=Tk()
  obj=Train(root)
  root.mainloop()