import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Salut TK")

        label = tk.Label(self,text="Salut!")
        label.pack(fill=tk.BOTH, expand=1,padx=100, pady=50)



if __name__ == "__main__" :
    window = Window()
    window.mainloop()