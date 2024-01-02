import tkinter as tk
from tkinter import ttk
print("Revving up the PyEngine")

def quitScriptum():
	displayData.close()
	quit()

root = tk.Tk()
root.title('3D Display')
root.geometry('600x450+50+50')
root.resizable(False, False)

canvas = tk.Canvas(root, width=600, height=400, bg='black')
canvas.grid(column=0, row=1, sticky=tk.S)

quitButt = ttk.Button(root, text="QUIT", command=lambda : quitScriptum())
quitButt.grid(column=0, row=0, sticky=tk.N)

# displayData.txt file imports:

displayData = open("../displayData.txt", "rt")
lineCoords = []
for x in displayData:
	if x.endswith("\n"):
		x = x[-4:-1]
	lineCoords.append(x)

print(str(len(lineCoords)) + "\n")

i=0
while i+4 <= len(lineCoords):
	print(i+4) 
	# TODO WHAT THE ACTUAL FUCK DO I DO BELOW
	print("{} {} {} {}".format(str(lineCoords[i]+300), str(lineCoords[i+1]+300), str(lineCoords[i+2]+200), str(lineCoords[i+3]+200)))
	canvas.create_line((lineCoords[i]+300), (lineCoords[i+1]+300), (lineCoords[i+2]+200), (lineCoords[i+3]+200), width=3, fill='green')
	i = i+4

# center lines
canvas.create_line((0, 200), (600, 200), width=1, fill='gray')
canvas.create_line((300, 0), (300, 400), width=1, fill='gray')


root.mainloop()