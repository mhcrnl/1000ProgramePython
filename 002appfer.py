from tkinter import *

class Aplicatie(Frame):

    def salut(self):
        print ("Te salut din python.")

    def createWidgets(self):
        self.Quit = Button(self)
        self.Quit["text"]= "Quit"
        self.Quit["fg"]="red"
        self.Quit["command"]= self.quit

        self.Quit.pack({"side":"left"})


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root=Tk()
app=Aplicatie(master=root)
app.mainloop()
root.destroy()
