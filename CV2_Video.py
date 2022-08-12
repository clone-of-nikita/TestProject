from tkinter import *
import cv2 
import numpy as np
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import PIL.Image, PIL.ImageTk
import time

class Application(Frame):
    def __init__(self, root):
        super(Application, self).__init__(root)
        self.root = root
        self.config()
        self.wigets()


    def wigets(self):
    	self.btn1 = Button(text = 'Video',height = 2,width = 14,bg = 'grey',padx = '8',pady = '6',command = self.prosto)
    	self.btn1.place(x = '1',y = '470')
    	self.btn2 = Button(text = 'Webcam',height = 2,width = 14,bg = 'grey',padx = '8',pady = '6',command = self.webcam)
    	self.btn2.place(x = '1',y = '410')

    	self.chkbtn = Checkbutton(variable = self.var1,command = self.click,height = 1,bg = 'black')
    	self.chkbtn.place(x = '735',y = '40')
    	self.chkbtn2 = Checkbutton(variable = self.var2,command = self.click2,height = 1,bg = 'black')
    	self.chkbtn2.place(x = '735',y = '110')
    	self.chkbtn3 = Checkbutton(variable = self.var3,command = self.prosto2,height = 1,bg = 'black')
    	self.chkbtn3.place(x = '735',y = '180')
    	self.chkbtn4 = Checkbutton(variable = self.var4,command = self.click4,height = 1,bg = 'black')
    	self.chkbtn4.place(x = '735',y = '250')
    	self.chkbtn5 = Button(text = None,command = self.click3,height = 0,bg = 'red',padx = '5',pady = '5')
    	self.chkbtn5.place(x = '820',y = '500')

    	self.lbl1 = Label(text = '|----Perenos----|')
    	self.lbl1.place(x = '703',y = '10')
    	self.lbl2 = Label(text = '|-----LAB----|')
    	self.lbl2.place(x = '710',y = '80')
    	self.lbl3 = Label(text = '|----Razmitie----|')
    	self.lbl3.place(x = '700',y = '150')
    	self.lbl4 = Label(text = '|--Podcherkivanie granitz--|')
    	self.lbl4.place(x = '680',y = '220')

    	self.canvas = Canvas(width = self.canwidth, height = self.canhight,bg = 'black')
    	self.canvas.place(x = '1',y = '1')

    def config(self):
    	self.canwidth = 650
    	self.canhight = 400
    	self.breakvar = False
    	self.strcreate = False
    	self.delay = 15
    	self.var1 = BooleanVar()
    	self.var2 = BooleanVar()
    	self.var3 = BooleanVar()
    	self.var4 = BooleanVar()
    	self.str0 = BooleanVar()
    	self.var10 = IntVar()
    	self.var11 = IntVar()
    	self.var12 = IntVar()
    	self.var13 = IntVar()
    	self.var14 = IntVar()
    	self.var15 = IntVar()
    	self.var16 = IntVar()
    	self.layervar = IntVar()


    def click(self):
    	if self.var1.get() == 1:
    		self.num_rows, self.num_cols = self.frame.shape[:2]
    		self.translation_matrix = np.array([ [1,0,0], [0,1,0] ])
    		self.frame = cv2.warpAffine(self.frame, self.translation_matrix, (self.num_cols + 250,self.num_rows + 50))
    	else:
    		pass

    def click2(self):
    	if self.var2.get() == 1:
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_RGB2LAB)

    def click3(self):
    	self.breakvar = True

    def click4(self):
    	if self.var4.get() == 1:
    		self.scl = Scale(orient=HORIZONTAL,width=14,length=300,from_=1,to=5,tickinterval=1,resolution=1,variable = self.layervar, bd = 0, showvalue = 0)
    		self.scl.place(x = '350',y = '420')
    		hsv_min = np.array((2,28,65),np.uint8)
    		hsv_max = np.array((26,238,255),np.uint8)
    		layer = self.layervar.get()
    		hsv = cv2.cvtColor(self.frame,cv2.COLOR_RGB2HSV)
    		thresh = cv2.inRange(hsv ,hsv_min, hsv_max)
    		contours0,hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    		self.frame = cv2.drawContours( self.frame, contours0, -1 , (255,0,0), 2, cv2.LINE_AA, hierarchy, layer)
    	else:
    		pass

    		


    def prosto2(self):
    	if self.var3.get() == 1:
    		self.strscale= Scale(orient=HORIZONTAL,width=14,length=300,from_=1,to=10,tickinterval=1,resolution=1,variable = self.var10, bd = 0, showvalue = 0)
    		self.strscale.place(x = '350',y = '420')
    	else:
    		self.strscale.destroy()


    def prosto3(self):
    	if self.var3.get() == 1:
    		if self.var10.get() == 5:
    			self.frame = cv2.GaussianBlur(self.frame,(9,9),5)
    		else:
    			pass


    def prosto(self):
        self.open()
        self.breakvar = False
        self.func()


    def webcam(self):
        self.vid = cv2.VideoCapture(0)
        self.breakvar = False
        self.func()



    def func(self):
    	self.ret,self.frame = self.vid.read()
    	if self.ret:
    		self.frame = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)
    		self.click()
    		self.click2()
    		self.click4()
    		self.prosto3()
    		self.frame = cv2.resize(self.frame,(self.canwidth,self.canhight))
    		self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.frame))
    		self.canvas.create_image(1,1,image = self.photo,anchor = 'nw')

    	if self.breakvar == False:
    		self.root.after(self.delay,self.func)
    	else:
    		self.canvas.delete(ALL)


    def open(self):
    	self.fopen = askopenfile(mode='rb', defaultextension=".mp4", filetypes=(("Video files", "*.mp4"), ("All files", "*.*")))
    	if self.fopen == None:
    		return
    	else:
    		self.vid = cv2.VideoCapture(self.fopen.name)


root = Tk()
root.title("blablabla")
root.geometry('850x530')
root.resizable(False, False)
app = Application(root)
app.configure(background = 'mediumturquoise')
root.mainloop()