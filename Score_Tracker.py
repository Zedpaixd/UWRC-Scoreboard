from tkinter import *

global timer 
timer = 0

global switch
switch = 0

global lr 
lr = 0

global team1ScoreTemp
team1ScoreTemp = 0

global team2ScoreTemp
team2ScoreTemp = 0

def incremTeam1():
    global team1ScoreTemp
    team1ScoreTemp+=1
    team1Score.set(team1ScoreTemp)

def decremTeam1():
    global team1ScoreTemp
    team1ScoreTemp-=1
    team1Score.set(team1ScoreTemp)

def incremTeam2():
    global team2ScoreTemp
    team2ScoreTemp+=1
    team2Score.set(team2ScoreTemp)

def decremTeam2():
    global team2ScoreTemp
    team2ScoreTemp-=1
    team2Score.set(team2ScoreTemp)

def resetTimer():
    global switch
    switch = 0
    global count
    count=1
    stopw.set('00:00')
        
def startStopwatch():
    global switch
    if (switch == 0):
        switch = 1
        global count
        count=0
        start_timer()
    
def start_timer():
    global count
    timer()

def pauseTimer():
    global switch
    switch = 0
    global count
    count=1

def timer():

    global count

    if(count==0):
        d = str(stopw.get())
        m,s = map(int,d.split(":"))
            
        m=int(m)
        s= int(s)

        if(s<59):
            s+=1
        elif(s==59):
            s=0
            m += 1


        if(m<10):
            m = str(0)+str(m)
        else:
            m = str(m)

        if(s<10):
            s=str(0)+str(s)
        else:
            s=str(s)
        d=m+":"+s
            
            
        stopw.set(d)
        if(count==0):
            mainWindow.after(930,start_timer)

mainWindow=Tk()
mainWindow.title("Program Name Here")
mainWindow.geometry("1600x900")
mainWindow.resizable(False,False)

stopw = StringVar()
stopw.set("00:00")

lb = Label(mainWindow,textvariable=stopw)
lb.config(font=("Courier 290 bold"))       

team1Score = StringVar()
team1Score.set(team1ScoreTemp)

team2Score = StringVar()
team2Score.set(team2ScoreTemp)

team1ScoreLabel = Label(mainWindow,textvariable=team1Score)
team1ScoreLabel.config(font=("Courier 190 bold"))  

team2ScoreLabel = Label(mainWindow,textvariable=team2Score)
team2ScoreLabel.config(font=("Courier 190 bold"))  



lb.place(x = 800, y = 200, anchor = "center")    # IF YOU RESIZE THE WINDOW THEN x = X size / 2
team1ScoreLabel.place(x = 400, y = 650, anchor="center")   # x = X size / 4
team2ScoreLabel.place(x = 1200, y = 650, anchor="center")   # x = X size * 3 / 4

def swapScores():
    global lr
    lr = (lr + 1) % 2
    if (lr == 1):
        team1ScoreLabel.place(x = 1200, y = 650, anchor="center")   
        team2ScoreLabel.place(x = 400, y = 650, anchor="center")
    else:
        team1ScoreLabel.place(x = 400, y = 650, anchor="center")
        team2ScoreLabel.place(x = 1200, y = 650, anchor="center")

controlsWindow = Tk()
controlsWindow.title("Control Panel")







bt1 = Button(controlsWindow,text="Start Timer",command=startStopwatch,font=("Courier 12 bold"))
bt2 = Button(controlsWindow,text="Pause Timer",command=pauseTimer,font=("Courier 12 bold"))
bt3 = Button(controlsWindow,text="Reset Timer",command=resetTimer,font=("Courier 12 bold"))
bt4 = Button(controlsWindow,text="Add point to team 1", command=incremTeam1,font=("Courier 12 bold"))
bt5 = Button(controlsWindow,text="Subtract point from team 1", command=decremTeam1,font=("Courier 12 bold"))
bt6 = Button(controlsWindow,text="Add point to team 2", command=incremTeam2,font=("Courier 12 bold"))
bt7 = Button(controlsWindow,text="Subtract point from team 2", command=decremTeam2,font=("Courier 12 bold"))
bt8 = Button(controlsWindow,text="Swap team scores", command=swapScores, font=("Courier 12 bold"))

bt1.pack()
bt2.pack()
bt3.pack()
bt4.pack()
bt5.pack()
bt6.pack()
bt7.pack()
bt8.pack()

controlsWindow.mainloop()
mainWindow.mainloop()
