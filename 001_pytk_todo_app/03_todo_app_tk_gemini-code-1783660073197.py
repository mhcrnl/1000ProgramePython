#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import json
import os

# Name of the file where tasks will be permanently stored
DATA_FILE = "tasks.json"

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Todo App v2 (Persistent)")
        self.geometry("360x500")
        self.configure(bg="#f5f5f5")

        # Color Palette for Alternating Rows
        self.color_schemes = [
            {"bg": "#ffffff", "fg": "#2c3e50"},  # Light row
            {"bg": "#fdfefe", "fg": "#2c3e50"}   # Slightly tinted row
        ]
        
        self.task_count = 0
        self.build_menu()
        self.build_ui()
        
        # Load any existing tasks from previous sessions
        self.load_tasks()

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
        self.canvas = tk.Canvas(self, bg="#f5f5f5", highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        
        self.task_container = tk.Frame(self.canvas, bg="#f5f5f5")
        
        self.canvas_window = self.canvas.create_window((0, 0), window=self.task_container, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.task_container.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        # --- Bottom Input Area ---
        input_frame = tk.Frame(self, bg="#f5f5f5", pady=10, padx=10)
        input_frame.pack(side=tk.BOTTOM, fill=tk.X)

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
        
        add_btn = tk.Button(
            input_frame, 
            text="Add", 
            bg="#27ae60", 
            fg="#ffffff", 
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            command=self.add_task_from_input
        )
        add_btn.pack(side=tk.RIGHT, ipady=3, ipadx=15)

        self.bind("<Return>", lambda event: self.add_task_from_input())

    def create_task_ui(self, task_text):
        """Helper to physically draw the task card in the window."""
        scheme = self.color_schemes[self.task_count % 2]
        
        task_card = tk.Frame(
            self.task_container, 
            bg=scheme["bg"], 
            highlightbackground="#e2e8f0", 
            highlightthickness=1,
            pady=8,
            padx=10
        )
        task_card.pack(side=tk.TOP, fill=tk.X, pady=3)

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
        
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

    def add_task_from_input(self):
        """Triggered when user clicks 'Add' or presses Enter."""
        task_text = self.task_entry.get().strip()

        if task_text:
            # Draw it on screen
            self.create_task_ui(task_text)
            # Clear input bar
            self.task_entry.delete(0, tk.END)
            # Permanently save it to the file
            self.save_tasks()

    def save_tasks(self):
        """Gathers text from all current UI tasks and saves them to a JSON file."""
        tasks_to_save = []
        # Loop through all child frames inside the task container to get their labels
        for task_card in self.task_container.winfo_children():
            for widget in task_card.winfo_children():
                if isinstance(widget, tk.Label):
                    tasks_to_save.append(widget.cget("text"))
        
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(tasks_to_save, f, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save tasks: {e}")

    def load_tasks(self):
        """Loads tasks from the JSON file on startup if the file exists."""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    saved_tasks = json.load(f)
                    for task in saved_tasks:
                        self.create_task_ui(task)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load saved tasks: {e}")

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()