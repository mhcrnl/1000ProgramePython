import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Salut TK")

        self.label_text = tk.StringVar()
        self.label_text.set("My Name Is: ")

        self.label = tk.Label(self,textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1,padx=100, pady=50)

        hello_butoon = tk.Button(self, text="Say Hello!",
                                 command=self.say_hello)
        hello_butoon.pack(side=tk.LEFT, padx=(20,0), pady=(0,20))

        goodbye_button = tk.Button(self, text="Say_Goodbye",
                                   command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0,20), pady=(0,20))

    def say_hello(self):
        self.label_text.set("hello")

    def say_goodbye(self):
        self.label_text.set("Goodbye! \n (Closing in 2 seconds.)")
        self.after(2000, self.destroy)

if __name__ == "__main__" :
    window = Window()
    window.mainloop()