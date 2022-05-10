import threading
import tkinter
from tkinter import *
import socket
import time


class Trigger:
    def __init__(self):
        self.trigger = False

    def setTrigger(self):
        self.trigger = True

    def getTrigger(self):
        return self.trigger


newTrigger = Trigger()


def posaljiNaServer():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.connect((host, port))
    ime = unosIme.get()
    x = var1.get() + ime

    s.sendall(x.encode())
    odgovor = (s.recv(1024).decode())
    if odgovor != "UGASI":
        var = StringVar()
        label = Label(prozorClient, textvariable=var, relief=GROOVE, font=("Arial", 18))
        var.set(odgovor)
        label.pack()
    else:
        print("ugasi")
        newTrigger.setTrigger()

    s.close()


prozorClient = Tk()

prozorClient.geometry("400x900")
posaljiDugme = Button(prozorClient, text="Posalji", command=posaljiNaServer)
posaljiDugme.pack()

f = ("Arial", 19)
var1 = StringVar(value="1")

labelaIme = Label(prozorClient, text="Ime: ", font=f)
labelaIme.pack()
unosIme = Entry(prozorClient, font=f)
unosIme.pack()

radioVreme = Radiobutton(prozorClient, text="Vreme", value="1", variable=var1)
radioUgasi = Radiobutton(prozorClient, text="Ugasi", value="2", variable=var1)
radioVreme.pack()
radioUgasi.pack()


def arkTred():
    extent = 1
    extent2 = 1
    while True and extent2 != -180:
        if newTrigger.getTrigger():
            mojCanvas.delete(ALL)
            mojCanvas.create_arc((150, 150, 250, 250), start=0, extent=180, fill="red", outline="blue")
            # mojCanvas.create_arc((150, 150, 250, 250), start=extent, extent=0)
            mojCanvas.create_arc((150, 150, 250, 250), start=180, extent=extent2, fill="blue", outline="blue")
            # extent += 1
            extent2 -= 1
            # if extent == 180:
            #    extent = 0
            time.sleep(0.00002)
        else:
            mojCanvas.delete(ALL)
            mojCanvas.create_arc((150, 150, 250, 250), start=0, extent=180, fill="red", outline="blue")
            mojCanvas.create_arc((150, 150, 250, 250), start=extent, extent=0)
            # mojCanvas.create_arc((150, 150, 250, 250), start=180, extent=extent2, fill="blue", outline="blue")
            extent += 1
            # extent2 -= 1
            if extent == 180:
                extent = 0
            time.sleep(0.00002)


mojCanvas = Canvas(prozorClient, bg="blue", width=400, height=250)
mojCanvas.pack(anchor=E)
threading.Thread(target=arkTred).start()
prozorClient.mainloop()
