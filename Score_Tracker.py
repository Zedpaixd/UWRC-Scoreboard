from tkinter import *
import json
from tkinter import messagebox

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

global resetMinutes
resetMinutes = 15

global resetSeconds
resetSeconds = 0

def normalizeTime(resetMinutes,resetSeconds):
    if(resetMinutes<10):
        resetMinutes = str(0)+str(resetMinutes)
    else:
        resetMinutes = str(resetMinutes)

    if(resetSeconds<10):
        resetSeconds=str(0)+str(resetSeconds)
    else:
        resetSeconds=str(resetSeconds)
    resetTime=resetMinutes+":"+resetSeconds
    return resetTime

def gameStatUpdater():
    global team1ScoreTemp
    global team2ScoreTemp

    currentStats = {
        "Time":stopw.get(),
        "Team1score":team1ScoreTemp,
        "Team2score":team2ScoreTemp
        }

    with open('game.json', 'w') as stats:
        json.dump(currentStats, stats, indent = 0)

def incremTeam1():
    global team1ScoreTemp
    team1ScoreTemp+=1
    team1Score.set(team1ScoreTemp)
    gameStatUpdater()

def decremTeam1():
    global team1ScoreTemp
    team1ScoreTemp-=1
    team1Score.set(team1ScoreTemp)
    gameStatUpdater()

def incremTeam2():
    global team2ScoreTemp
    team2ScoreTemp+=1
    team2Score.set(team2ScoreTemp)
    gameStatUpdater()

def decremTeam2():
    global team2ScoreTemp
    team2ScoreTemp-=1
    team2Score.set(team2ScoreTemp)
    gameStatUpdater()

def resetTimer():
    global switch
    switch = 0
    global count
    count=1
    global resetMinutes
    global resetSeconds

    resetTime=normalizeTime(resetMinutes,resetSeconds)

    stopw.set(resetTime)
    gameStatUpdater()
        
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
    gameStatUpdater()

def timer():

    global count

    if(count==0):
        d = str(stopw.get())
        m,s = map(int,d.split(":"))
            
        m=int(m)
        s= int(s)

        #if(s<59):
        #    s+=1
        #elif(s==59):
        #    s=0
        #    m += 1

        if(s>0):
            s-=1
        elif(m>0):
            m-=1
            s=59


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
        gameStatUpdater()
        if(count==0):
            mainWindow.after(930,start_timer)

def swapScores():
    global lr
    lr = (lr + 1) % 2
    if (lr == 1):
        team1ScoreLabel.place(x = 1200, y = 650, anchor="center")   
        team2ScoreLabel.place(x = 400, y = 650, anchor="center")
    else:
        team1ScoreLabel.place(x = 400, y = 650, anchor="center")
        team2ScoreLabel.place(x = 1200, y = 650, anchor="center")

global mainWindow
mainWindow=Tk()
mainWindow.title("Program Name Here")
mainWindow.geometry("1600x900")
mainWindow.resizable(False,False)

global controlsWindow
controlsWindow = Tk()
controlsWindow.geometry("760x500")
controlsWindow.title("Control Panel")

stopw = StringVar()
stopw.set("15:00")

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

currentResetTime = Label(controlsWindow, text = "Current reset time:", font=("Courier 14 bold"))
currentResetTime.place(x=260,y=140)

lb.place(x = 800, y = 200, anchor = "center")    # IF YOU RESIZE THE WINDOW THEN x = X size / 2    ALSO EDIT swapScores() IN THAT CASE
team1ScoreLabel.place(x = 400, y = 650, anchor="center")   # x = X size / 4
team2ScoreLabel.place(x = 1200, y = 650, anchor="center")   # x = X size * 3 / 4


startTimer = Button(controlsWindow,text="Start Timer",command=startStopwatch,font=("Courier 12 bold"))
pauseTimer = Button(controlsWindow,text="Pause Timer",command=pauseTimer,font=("Courier 12 bold"))
resetTimer = Button(controlsWindow,text="Reset Timer",command=resetTimer,font=("Courier 12 bold"))
pointToT1 = Button(controlsWindow,text="Add point to team 1", command=incremTeam1,font=("Courier 12 bold"))
minusPointToT1 = Button(controlsWindow,text="Subtract point from team 1", command=decremTeam1,font=("Courier 12 bold"))
pointToT2 = Button(controlsWindow,text="Add point to team 2", command=incremTeam2,font=("Courier 12 bold"))
minusPointToT2 = Button(controlsWindow,text="Subtract point from team 2", command=decremTeam2,font=("Courier 12 bold"))
swapTeamScores = Button(controlsWindow,text="Swap team scores", command=swapScores, font=("Courier 12 bold"))

startTimer.place(x=15,y=10)
pauseTimer.place(x=15,y=50)
resetTimer.place(x=15,y=90)
pointToT1.place(x=195,y=10)
minusPointToT1.place(x=165,y=50)
pointToT2.place(x=495,y=10)
minusPointToT2.place(x=465,y=50)
swapTeamScores.place(x=350,y=90)



controlsWindow.mainloop()
mainWindow.mainloop()
