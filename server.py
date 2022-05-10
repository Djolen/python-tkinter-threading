import threading
import tkinter
from tkinter import *
import socket
import time

def srvThread():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host,port))
    s.listen(5)
    while True:
        var = StringVar()
        label = Label(tk, textvariable=var, relief=GROOVE, font=("Arial", 18))
        var.set("Server ceka")
        label.pack()
        conn, addr = s.accept()
        poruka =  conn.recv(1024).decode()
        broj = poruka[0]
        ime = ""
        for i in range (1,len(poruka)):
            ime += poruka[i]
        if broj == "1":
            poruka = "VREME"
            vreme = time.ctime(time.time())
            conn.send(vreme.encode())
        elif broj == "2":
            poruka = "UGASI"
            conn.send(poruka.encode())
        var = StringVar()
        label = Label(tk, textvariable=var, relief=GROOVE, font=("Arial", 18))
        var.set("SERVER PRIMIO:" + ime + " " + poruka)
        label.pack()
        conn.close()

tk = Tk()
tk.geometry("400x900")
threading.Thread(target=srvThread).start()
mainloop()