from tkinter import *
import random

class Game:
    def __init__(self):
        self.number =str(random.randint(1, 10))
        self.chance = 5
        self.label1 = Label(root, text="NUMBER GUESSING", width=300, font="bold 20", fg="#000", bg="red")
        self.label1.pack()


    def start(self):
        btn1.destroy()

        self.ent = Entry(root, width=100, bd=2, font=50)
        self.ent.pack(padx=50, pady=20, anchor=CENTER)
        self.ckbtn = Button(root, text="Check", padx=20, pady=10, fg="#fff", bg="#000", command=self.check)
        self.ckbtn.pack(pady=10,anchor=CENTER)
        self.btl = Label(root,text="Total Chances remaining:"+str(self.chance), fg="red", bg="#fff", font="Times 20")
        self.btl.pack(side=BOTTOM)

    def check(self):
        if self.chance>=1:
            val = self.ent.get()
            if val == self.number:
                self.ent.destroy()
                self.ckbtn.destroy()
                self.btl.destroy()
                self.endgame = Label(root, text="You Won !", font="Times 20", fg="green")
                self.endgame.pack(pady=50)
                self.playagain = Button(root,text="Play Again",command=self.restart,bg="#000",fg="#fff",padx=10,pady=10)
                self.playagain.pack(pady=20, side=BOTTOM)
            else:
                self.chance-=1
                self.btl.config(text=f"Total Chances remaining:{self.chance}")
                if self.chance==0:
                    self.ent.destroy()
                    self.ckbtn.destroy()
                    self.btl.destroy()
                    self.endgame = Label(root, text="You Lost !", font="Times 20", fg="red")
                    self.endgame.pack(pady=50)
                    self.playagain = Button(root, text="Play Again", command=self.restart, bg="#000", fg="#fff", padx=10, pady=10)
                    self.playagain.pack(pady=20, side=BOTTOM)

        else:
            self.ent.destroy()
            self.ckbtn.destroy()
            self.btl.destroy()
            self.endgame = Label(root, text="You Lost !", font="Times 20", fg="red")
            self.endgame.pack(pady=50)
            self.playagain = Button(root, text="Play Again", command=self.restart, bg="#000", fg="#fff", padx=10,pady=10)
            self.playagain.pack(pady=20, side=BOTTOM)


    def restart(self):
        self.endgame.destroy()
        self.playagain.destroy()
        self.number = str(random.randint(1, 10))
        self.chance = 5
        self.start()







root = Tk()
root.geometry("300x300")
root.title("Number Guessing")
sg = Game()
btn1 = Button(root, text="START", command=sg.start, padx=50, pady=10, fg="#fff", bg="#000")
btn1.pack(pady=100, anchor=CENTER)

root.mainloop()
