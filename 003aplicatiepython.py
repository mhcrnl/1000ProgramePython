#!/usr/bin/env python

import Tkinter as tk
import Tkinter
class Aplication(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton= tk.Button( self, text='Quit',
                                    command= self.quit)
        self.quitButton.grid()
#root=tk()
app= Aplication(tk.Frame)
app.master.title('Aplicatie')
app.mainloop()
#root.destroy()
