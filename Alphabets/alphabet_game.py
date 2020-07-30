from tkinter import *
import pygame
import pyttsx3

pygame.init()
engine = pyttsx3.init()
root = Tk()
root.title('Alphabet Application')
root.geometry('1352x652+100+100')
root.config(background='black')

str1 = StringVar()
str1.set('WELCOME!!!')
frame1 = Frame(root,bg='white')
frame1.grid()

Disp = Canvas(frame1, width=160,height=120,bg='black')
Disp.grid(row=1,column=3)
img = PhotoImage(file='gp.png')
image = Disp.create_image(85,62,image = img)

imgClear = PhotoImage(file='gp.png')
def Clear():
    str1.set('WELCOME!!!')
    Disp.create_image(85,62,image = imgClear)
    engine.say('WELCOME!!!')
    engine.runAndWait()

imgA = PhotoImage(file='Apple.png')
def Alphabet_A():
    str1.set('A is for Apple')
    Disp.create_image(85,62,image=imgA)
    engine.say('A is for Apple')
    engine.runAndWait()

imgB = PhotoImage(file='Banana.png')
def Alphabet_B():
    str1.set('B is for Banana')
    Disp.create_image(85,62,image=imgB)
    engine.say('B is for Banana')
    engine.runAndWait()

imgC = PhotoImage(file='Cocoa.png')
def Alphabet_C():
    str1.set('C is for Cocoa')
    Disp.create_image(85,62,image=imgC)
    engine.say('C is for Cocoa')
    engine.runAndWait()

imgD = PhotoImage(file='Damson.png')
def Alphabet_D():
    str1.set('D is for Damson')
    Disp.create_image(85,62,image=imgD)
    engine.say('D is for Damson')
    engine.runAndWait()

imgE = PhotoImage(file='Elderberry.png')
def Alphabet_E():
    str1.set('E is for Elderberry')
    Disp.create_image(85,62,image=imgE)
    engine.say('E is for Elderberry')
    engine.runAndWait()

imgF = PhotoImage(file='Fig.png')
def Alphabet_F():
    str1.set('F is for Fig')
    Disp.create_image(85,62,image=imgF)
    engine.say('F is for Fig')
    engine.runAndWait()

imgG = PhotoImage(file='Guava.png')
def Alphabet_G():
    str1.set('G is for Guava')
    Disp.create_image(85,62,image=imgG)
    engine.say('G is for Guava')
    engine.runAndWait()

imgH = PhotoImage(file='HuckleBerry.png')
def Alphabet_H():
    str1.set('H is for HuckleBerry')
    Disp.create_image(85,62,image=imgH)
    engine.say('H is for HuckleBerry')
    engine.runAndWait()

imgI = PhotoImage(file='Ita palm.png')
def Alphabet_I():
    str1.set('I is for Ita palm')
    Disp.create_image(85,62,image=imgI)
    engine.say('I is for Ita palm')
    engine.runAndWait()

imgJ = PhotoImage(file='Jujube.png')
def Alphabet_J():
    str1.set('J is for Jujube')
    Disp.create_image(85,62,image=imgJ)
    engine.say('J is for Jujube')
    engine.runAndWait()

imgK = PhotoImage(file='Kumquat.png')
def Alphabet_K():
    str1.set('K is for Kumquat')
    Disp.create_image(85,62,image=imgK)
    engine.say('K is for Kumquat')
    engine.runAndWait()

imgL = PhotoImage(file='Lime.png')
def Alphabet_L():
    str1.set('L is for Lime')
    Disp.create_image(85,62,image=imgL)
    engine.say('L is for Lime')
    engine.runAndWait()

imgM = PhotoImage(file='Mango.png')
def Alphabet_M():
    str1.set('M is for Mango')
    Disp.create_image(85,62,image=imgM)
    engine.say('M is for Mango')
    engine.runAndWait()

imgN = PhotoImage(file='Nance.png')
def Alphabet_N():
    str1.set('N is for Nance')
    Disp.create_image(85,62,image=imgN)
    engine.say('N is for Nance')
    engine.runAndWait()

imgO = PhotoImage(file='Orange.png')
def Alphabet_O():
    str1.set('O is for Orange')
    Disp.create_image(85,62,image=imgO)
    engine.say('O is for Orange')
    engine.runAndWait()

imgP = PhotoImage(file='Papaya.png')
def Alphabet_P():
    str1.set('P is for Papaya')
    Disp.create_image(85,62,image=imgP)
    engine.say('P is for Papaya')
    engine.runAndWait()

imgQ = PhotoImage(file='Quince.png')
def Alphabet_Q():
    str1.set('Q is for Quince')
    Disp.create_image(85,62,image=imgQ)
    engine.say('Q is for Quince')
    engine.runAndWait()

imgR = PhotoImage(file='RaspBerry.png')
def Alphabet_R():
    str1.set('R is for RaspBerry')
    Disp.create_image(85,62,image=imgR)
    engine.say('R is for RaspBerry')
    engine.runAndWait()

imgS = PhotoImage(file='StrawBerry.png')
def Alphabet_S():
    str1.set('S is for StrawBerry')
    Disp.create_image(85,62,image=imgS)
    engine.say('S is for StrawBerry')
    engine.runAndWait()

imgT = PhotoImage(file='Tamarind.png')
def Alphabet_T():
    str1.set('T is for Tamarind')
    Disp.create_image(85,62,image=imgT)
    engine.say('T is for Tamarind')
    engine.runAndWait()

imgU = PhotoImage(file='Ugli.png')
def Alphabet_U():
    str1.set('U is for Ugli')
    Disp.create_image(85,62,image=imgU)
    engine.say('U is for Ugli')
    engine.runAndWait()

imgV = PhotoImage(file='Vanilla.png')
def Alphabet_V():
    str1.set('V is for Vanilla')
    Disp.create_image(85,62,image=imgV)
    engine.say('V is for Vanilla')
    engine.runAndWait()

imgW = PhotoImage(file='Watermelon.png')
def Alphabet_W():
    str1.set('W is for Watermelon')
    Disp.create_image(85,62,image=imgW)
    engine.say('W is for Watermelon')
    engine.runAndWait()

imgX = PhotoImage(file='Xigua.png')
def Alphabet_X():
    str1.set('X is for Xigua')
    Disp.create_image(85,62,image=imgX)
    engine.say('X is for Xigua')
    engine.runAndWait()

imgY = PhotoImage(file='Yuzu.png')
def Alphabet_Y():
    str1.set('Y is for Yuzu')
    Disp.create_image(85,62,image=imgY)
    engine.say('Y is for Yuzu')
    engine.runAndWait()

imgZ = PhotoImage(file='Zucchini.png')
def Alphabet_Z():
    str1.set('Z is for Zucchini')
    Disp.create_image(85,62,image=imgZ)
    engine.say('Z is for Zucchini')
    engine.runAndWait()


#============================Main Screen==========================
Display = Entry(frame1, textvariable=str1, font=('arial',44,'bold'),bg='#FF4F00',fg='black',bd=34,width=39,justify=CENTER)
Display.grid(row=0,column=0,columnspan=7,pady=1)

#===========================Row 1================================
btnA=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_A,width=10,height=3,text='A',bg='orange',fg='black')\
    .grid(row=1,column=0)
btnB=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_B,width=10,height=3,text='B',bg='orange',fg='black')\
    .grid(row=1,column=1)
btnC=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_C,width=10,height=3,text='C',bg='orange',fg='black')\
    .grid(row=1,column=2)
btnD=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_D,width=10,height=3,text='D',bg='orange',fg='black')\
    .grid(row=1,column=4)
btnE=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_E,width=10,height=3,text='E',bg='orange',fg='black')\
    .grid(row=1,column=5)
btnF=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_F,width=10,height=3,text='F',bg='orange',fg='black')\
    .grid(row=1,column=6)

#===========================Row 2===============================
btnG=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_G,width=10,height=3,text='G',bg='orange',fg='black')\
    .grid(row=2,column=0)
btnH=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_H,width=10,height=3,text='H',bg='#FF4F00',fg='black')\
    .grid(row=2,column=1)
btnI=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_I,width=10,height=3,text='I',bg='#FF4F00',fg='black')\
    .grid(row=2,column=2)
btnJ=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_J,width=10,height=3,text='J',bg='#FF4F00',fg='black')\
    .grid(row=2,column=3)
btnK=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_K,width=10,height=3,text='K',bg='#FF4F00',fg='black')\
    .grid(row=2,column=4)
btnL=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_L,width=10,height=3,text='L',bg='#FF4F00',fg='black')\
    .grid(row=2,column=5)
btnM=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_M,width=10,height=3,text='M',bg='orange',fg='black')\
    .grid(row=2,column=6)

#============================Row 3================================
btnN=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_N,width=10,height=3,text='N',bg='orange',fg='black')\
    .grid(row=3,column=0)
btnO=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_O,width=10,height=3,text='O',bg='#FF4F00',fg='black')\
    .grid(row=3,column=1)
btnP=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_P,width=10,height=3,text='P',bg='#FF4F00',fg='black')\
    .grid(row=3,column=2)
btnQ=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_Q,width=10,height=3,text='Q',bg='#FF4F00',fg='black')\
    .grid(row=3,column=3)
btnR=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_R,width=10,height=3,text='R',bg='#FF4F00',fg='black')\
    .grid(row=3,column=4)
btnS=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_S,width=10,height=3,text='S',bg='#FF4F00',fg='black')\
    .grid(row=3,column=5)
btnT=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_T,width=10,height=3,text='T',bg='orange',fg='black')\
    .grid(row=3,column=6)

#============================Row 4================================
btnU=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_U,width=10,height=3,text='U',bg='orange',fg='black')\
    .grid(row=4,column=0)
btnV=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_V,width=10,height=3,text='V',bg='orange',fg='black')\
    .grid(row=4,column=1)
btnW=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_W,width=10,height=3,text='W',bg='orange',fg='black')\
    .grid(row=4,column=2)
btnX=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_X,width=10,height=3,text='X',bg='orange',fg='black')\
    .grid(row=4,column=4)
btnY=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_Y,width=10,height=3,text='Y',bg='orange',fg='black')\
    .grid(row=4,column=5)
btnZ=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Alphabet_Z,width=10,height=3,text='Z',bg='orange',fg='black')\
    .grid(row=4,column=6)
btnClear=Button(frame1,pady=1,bd=4,font=('arial',21,'bold'),command=Clear,width=10,height=3,text='Reset',bg='green',fg='black')\
    .grid(row=4,column=3)

root.mainloop()