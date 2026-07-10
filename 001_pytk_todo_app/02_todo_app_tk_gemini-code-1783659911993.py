#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Todo App v2")
        self.geometry("360x500")
        self.configure(bg="#f5f5f5")

        # Color Palette for Alternating Rows
        self.color_schemes = [
            {"bg": "#ffffff", "fg": "#2c3e50"},  # Light row
            {"bg": "#fdfefe", "fg": "#2c3e50"}   # Slightly tinted row
        ]
        
        self.build_menu()
        self.build_ui()

    def build_menu(self):
        """Constructs the top menu bar."""
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def build_ui(self):
        """Constructs the application layout."""
        # --- Header Banner ---
        header = tk.Label(
            self, 
            text="YOUR TASKS", 
            bg="#2c3e50", 
            fg="#ffffff", 
            font=("Arial", 10, "bold"), 
            pady=12
        )
        header.pack(side=tk.TOP, fill=tk.X)

        # --- Main Scrollable Canvas Area ---
        # Canvas holds the frame to allow scrolling when the list grows long
        self.canvas = tk.Canvas(self, bg="#f5f5f5", highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        
        self.task_container = tk.Frame(self.canvas, bg="#f5f5f5")
        
        # Configure canvas window and scrolling mechanics
        self.canvas_window = self.canvas.create_window((0, 0), window=self.task_container, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack scrolling elements
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Bind resize events to ensure the inner frame stretches nicely
        self.task_container.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        # --- Bottom Input Area ---
        input_frame = tk.Frame(self, bg="#f5f5f5", pady=10, padx=10)
        input_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Replacing Text with Entry for clean, single-line task inputs
        self.task_entry = tk.Entry(
            input_frame, 
            bg="#ffffff", 
            fg="#2c3e50", 
            font=("Arial", 11),
            relief=tk.SOLID,
            bd=1
        )
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=6, padx=(0, 5))
        self.task_entry.focus_set()
        
        # Submit Button
        add_btn = tk.Button(
            input_frame, 
            text="Add", 
            bg="#27ae60", 
            fg="#ffffff", 
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            command=self.add_task
        )
        add_btn.pack(side=tk.RIGHT, ipady=3, ipadx=15)

        # Keep the original Enter key binding functionality
        self.bind("<Return>", lambda event: self.add_task())

        # Track internal task count to alternate styling accurately
        self.task_count = 0

    def add_task(self):
        task_text = self.task_entry.get().strip()

        if task_text:
            # Pick background scheme based on count parity
            scheme = self.color_schemes[self.task_count % 2]
            
            # Use an internal frame for each task to act as a stylish card
            task_card = tk.Frame(
                self.task_container, 
                bg=scheme["bg"], 
                highlightbackground="#e2e8f0", 
                highlightthickness=1,
                pady=8,
                padx=10
            )
            task_card.pack(side=tk.TOP, fill=tk.X, pady=3)

            # Task Text Label
            lbl = tk.Label(
                task_card, 
                text=task_text, 
                bg=scheme["bg"], 
                fg=scheme["fg"], 
                font=("Arial", 11),
                anchor="w"
            )
            lbl.pack(side=tk.LEFT, fill=tk.X, expand=True)

            self.task_count += 1
            
            # Clear input and automatically scroll to the bottom of the list
            self.task_entry.delete(0, tk.END)
            self.canvas.update_idletasks()
            self.canvas.yview_moveto(1.0)

    def on_frame_configure(self, event):
        """Reset the scroll region to encompass the inner task container."""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        """Dynamically widen the inner frame to match the application window window size."""
        self.canvas.itemconfig(self.canvas_window, width=event.width)

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()