from tkinter import *
import json
from tkinter import messagebox

global timer,switch,team1ScoreTemp,team2ScoreTemp,resetMinutes,resetSeconds
timer = 0
switch = 0
lr = 0
team1ScoreTemp = 0
team2ScoreTemp = 0
team1ScoreVal = str(team1ScoreTemp)
team2ScoreVal = str(team2ScoreTemp)
resetMinutes = 15
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

def submitValues():
    try:
        tempM = int(minutes.get())
        tempS = int(seconds.get())
    except:
        messagebox.showerror("","Non integers have been inputted") 
        tempM = 15
        tempS = 0

    if tempS > 59:
        tempS = 59

    global resetMinutes,resetSeconds
    resetMinutes = tempM
    resetSeconds = tempS

    minutes.set("")
    seconds.set("")

def gameStatUpdater():
    global team1ScoreTemp,team2ScoreTemp

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
    team1ScoreVal = str(team1ScoreTemp)
    team1Score.set(team1ScoreVal)
    gameStatUpdater()

def decremTeam1():
    global team1ScoreTemp
    team1ScoreTemp-=1
    team1ScoreVal = str(team1ScoreTemp)
    team1Score.set(team1ScoreVal)
    gameStatUpdater()

def incremTeam2():
    global team2ScoreTemp
    team2ScoreTemp+=1
    team2ScoreVal = str(team2ScoreTemp)
    team2Score.set(team2ScoreVal)
    gameStatUpdater()

def decremTeam2():
    global team2ScoreTemp
    team2ScoreTemp-=1
    team2ScoreVal = str(team2ScoreTemp)
    team2Score.set(team2ScoreVal)
    gameStatUpdater()

def resetTimer():
    global switch,count,resetMinutes,resetSeconds
    switch = 0
    count=1

    resetTime=normalizeTime(resetMinutes,resetSeconds)

    stopw.set(" "*7 + resetTime + (" " * 7))
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
    global switch,count
    switch = 0
    count=1
    gameStatUpdater()

def timer():

    global count

    if(count==0):
        d = str(stopw.get())
        m,s = map(int,d.strip().split(":"))
            
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
        d="       "+m+":"+s+"       "
            
            
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
        team1ScoreTracking.place(x=590,y=310,anchor="center")
        team2ScoreTracking.place(x=450,y=310,anchor="center")
        canvas1.place(x=800,y=0)
        canvas2.place(x=-10,y=0)
    else:
        team1ScoreLabel.place(x = 400, y = 650, anchor="center")
        team2ScoreLabel.place(x = 1200, y = 650, anchor="center")
        team1ScoreTracking.place(x=450,y=310,anchor="center")
        team2ScoreTracking.place(x=590,y=310,anchor="center")
        canvas1.place(x=-10,y=0)
        canvas2.place(x=800,y=0)

global mainWindow
mainWindow=Tk()
mainWindow.title("UWR Scoreboard - © AAB")
mainWindow.geometry("1600x900")
mainWindow.resizable(False,False)

global controlsWindow
controlsWindow = Toplevel(mainWindow)
controlsWindow.geometry("760x500")
controlsWindow.title("Control Panel")
controlsWindow.resizable(False,False)

canvas1 = Canvas(width=810, height=900, bg='#180bd4')
canvas1.place(x=-10,y=0)

canvas2 = Canvas(width=810, height=900, bg='#FFFFFF')
canvas2.place(x=800,y=0)

stopw = StringVar()
stopw.set("   15:00   ")

lb = Label(mainWindow,textvariable=stopw)
lb.config(font=("Courier 300 bold"),bg="#000000",fg="#FFB400")       
lb.place(x = 800, y = 220, anchor = "center")    # IF YOU RESIZE THE WINDOW THEN x = X size / 2    ALSO EDIT swapScores() IN THAT CASE

team1Score = StringVar()
team1Score.set(team1ScoreVal)

team2Score = StringVar()
team2Score.set(team2ScoreVal)

team1ScoreLabel = Label(mainWindow,textvariable=team1Score)
team1ScoreLabel.config(font=("Courier 240 bold"),bg="#180bd4",fg="#FFFFFF")  
team1ScoreLabel.place(x = 400, y = 675, anchor="center")   # x = X size / 4

team2ScoreLabel = Label(mainWindow,textvariable=team2Score)
team2ScoreLabel.config(font=("Courier 240 bold"),bg="#FFFFFF",fg="#000000")  
team2ScoreLabel.place(x = 1200, y = 675, anchor="center")   # x = X size * 3 / 4

startTimer = Button(controlsWindow,text="Start Timer",command=startStopwatch,font=("Courier 12 bold"))
startTimer.place(x=15,y=10)

pauseTimer = Button(controlsWindow,text="Pause Timer",command=pauseTimer,font=("Courier 12 bold"))
pauseTimer.place(x=15,y=50)

resetTimer = Button(controlsWindow,text="Reset Timer",command=resetTimer,font=("Courier 12 bold"))
resetTimer.place(x=15,y=90)

pointToT1 = Button(controlsWindow,text="Add point to team 1", command=incremTeam1,font=("Courier 12 bold"))
pointToT1.place(x=195,y=10)

minusPointToT1 = Button(controlsWindow,text="Subtract point from team 1", command=decremTeam1,font=("Courier 12 bold"))
minusPointToT1.place(x=165,y=50)

pointToT2 = Button(controlsWindow,text="Add point to team 2", command=incremTeam2,font=("Courier 12 bold"))
pointToT2.place(x=495,y=10)

minusPointToT2 = Button(controlsWindow,text="Subtract point from team 2", command=decremTeam2,font=("Courier 12 bold"))
minusPointToT2.place(x=465,y=50)

swapTeamScores = Button(controlsWindow,text="Swap team scores", command=swapScores, font=("Courier 12 bold"))
swapTeamScores.place(x=350,y=90)

timerTracking = Label(controlsWindow, textvariable = stopw)
timerTracking.config(font =("Courier 25 bold"))
timerTracking.place(x=520,y=280, anchor="center")

team1ScoreTracking = Label(controlsWindow,textvariable=team1Score)
team1ScoreTracking.config(font=("Courier 20 bold"))  
team1ScoreTracking.place(x=450,y=310,anchor="center")

team2ScoreTracking = Label(controlsWindow,textvariable=team2Score)
team2ScoreTracking.config(font=("Courier 20 bold"))  
team2ScoreTracking.place(x=590,y=310,anchor="center")

global minutes
minutes=StringVar()
minutesLabel = Label(controlsWindow, text = "Change reset minutes to:", font = ("Courier 12 bold"))
minutesEntry = Entry(controlsWindow, textvariable=minutes, font = ("Courier 12 bold"))
minutesLabel.place(x=15,y=230)
minutesEntry.place(x=35,y=260)

global seconds
seconds=StringVar()
secondsLabel = Label(controlsWindow, text = "Change reset seconds to:", font = ("Courier 12 bold"))
secondsEntry = Entry(controlsWindow, textvariable=seconds, font = ("Courier 12 bold"))
secondsLabel.place(x=15,y=300)
secondsEntry.place(x=35,y=330)

submitButton = Button(controlsWindow,text = "Submit", command = submitValues)
submitButton.place(x=115,y=370)

controlsWindow.mainloop()
mainWindow.mainloop()
