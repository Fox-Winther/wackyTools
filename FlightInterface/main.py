from tkinter import *

def throttleToZero():
    throtSlider.set(0)
    # print("throttle 0")

def pitchToZero():
    pitchSlider.set(0)
    # print("pitch neutral")

def yawToZero():
    yawSlider.set(0)
    # print("yaw neutral")

def rollToZero():
    rollSlider.set(0)
    # print("roll neutral")

#plane data:
planeName = "B-57"

window = Tk()

window.title("Interface de Vôo Simples V0.1 - Voando o {}".format(planeName))
window.geometry('640x200')

# sliders for controls (throt, pitch, yaw, rolll)

throtSlider = Scale(window, orient=VERTICAL, label="Throttle/Potência", from_=100, to=00)
throtSlider.grid(column=0, row=1)
throtSlider.set(0)

pitchSlider = Scale(window, orient=VERTICAL, label="Pitch/Arfagem", from_=45, to=-45)
pitchSlider.grid(column=1, row=1)
pitchSlider.set(0)

yawSlider = Scale(window, orient=VERTICAL, label="Yaw/Guinada", from_=45, to=-45)
yawSlider.grid(column=2, row=1)
yawSlider.set(0)

rollSlider = Scale(window, orient=VERTICAL, label="Roll/Rolagem", from_=45, to=-45)
rollSlider.grid(column=3, row=1)
rollSlider.set(0)

# reset buttons

throtReseter = Button(window, text="0%", bg="red", command=throttleToZero)
throtReseter.grid(column=0, row=2)

pitchReseter = Button(window, text="reset (0°)", bg="red", command=pitchToZero)
pitchReseter.grid(column=1, row=2)

yawReseter = Button(window, text="reset (0°)", bg="red", command=yawToZero)
yawReseter.grid(column=2, row=2)

rollReseter = Button(window, text="reset (0°)", bg="red", command=rollToZero)
rollReseter.grid(column=3, row=2)

footNote = Label(text="ChaoticFurry @ 2022 for school project")
footNote.grid(column=0, row=5)


window.mainloop()