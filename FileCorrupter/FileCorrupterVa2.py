from tkinter import *
from random import randrange

window = Tk()

totalFileSize = 0

window.title("File Corrupter - Version a-2 - by ChaoticFurry @ 2022")
window.geometry('640x50')

fileNameLbl = Label(text="Insert the file's name: ")
fileNameLbl.grid(column=0, row=0)

fileName = Entry(width=50)
fileName.grid(column=1, row=0)

# now we input the size unit

sizeUnits = ["MB", "KB", "B"]

variable = StringVar()
variable.set(sizeUnits[2])

# creating widget
dropdown = OptionMenu(window, variable,*sizeUnits)
dropdown.grid(column=4, row=0)

# now for the actual size

temp1 = Label(text=" with ")
temp1.grid(column=2, row=0)

fileSize = Entry(width=4)
fileSize.grid(column=3, row=0)

#all that was just the file parameter, now its time for the actual logic
    
# here we go, math go brrr

allTheCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=´[~],.;!@#$%¨&*()_+`{^}<>:|'£¢¬§/?°/₢ºª "

def iWannaEndItAll():
    myGodAnotherTemp = open(fileName.get(), 'wt')
    myGodAnotherTemp.write("")
    myGodAnotherTemp.close()
    fileActualUnit = 1
    if variable.get() == 'KB':
        fileActualUnit = 1000
    if variable.get() == 'MB':
        fileActualUnit = 1000000
    totalFileSize =  int(fileSize.get()) * fileActualUnit * 1.011282051282052  # thats the same math from version A-1 , 
                                                                                                                                # but the infamous "Long Number" had to be changed
                                                                                                                                # it still slightly off (4 kb became 4.04 kb) but heh... good enough
    print(totalFileSize)
    finallyTheFile = open(fileName.get(), 'at')
    for i in range(int(totalFileSize)):
        if (randrange(0, 100)) == 0:
            finallyTheFile.write("\n")
        else:
            finallyTheFile.write(allTheCharacters[randrange(0, 100)])
    finallyTheFile.write("\n\nFile Corrupter Version a2 by ChaoticFurry @ 2022")
    finallyTheFile.close
    
theOneThatEndsItAll = Button(window, text="Corrupt!", command=iWannaEndItAll, height=1, width=8, bg='red', fg='white', font=('arial 15'))
theOneThatEndsItAll.grid(column=6, row=0)

# probably my longest functioning code to date, finished on 24/6/2022 at 20:32

window.mainloop()