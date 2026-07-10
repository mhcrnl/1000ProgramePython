#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "tasks.json"

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Todo App v2 (Complete Tasks)")
        self.geometry("380x500")
        self.configure(bg="#f5f5f5")

        # Color Palette for Alternating Rows
        self.color_schemes = [
            {"bg": "#ffffff", "fg": "#2c3e50"},
            {"bg": "#fdfefe", "fg": "#2c3e50"}
        ]
        
        self.task_count = 0
        self.build_menu()
        self.build_ui()
        self.load_tasks()

    def build_menu(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def build_ui(self):
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
            bg="#2c3e50", 
            fg="#ffffff", 
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            command=self.add_task_from_input
        )
        add_btn.pack(side=tk.RIGHT, ipady=3, ipadx=15)

        self.bind("<Return>", lambda event: self.add_task_from_input())

    def create_task_ui(self, task_text):
        """Creates a task container row with text and a completion button."""
        scheme = self.color_schemes[self.task_count % 2]
        
        # Main container row for this specific task
        task_card = tk.Frame(
            self.task_container, 
            bg=scheme["bg"], 
            highlightbackground="#e2e8f0", 
            highlightthickness=1,
            pady=4,
            padx=10
        )
        task_card.pack(side=tk.TOP, fill=tk.X, pady=3)

        # Task Text Description
        lbl = tk.Label(
            task_card, 
            text=task_text, 
            bg=scheme["bg"], 
            fg=scheme["fg"], 
            font=("Arial", 11),
            anchor="w"
        )
        lbl.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=4)

        # Complete/Close Button (Passing the specific task card wrapper to the deletion function)
        done_btn = tk.Button(
            task_card,
            text="✓",
            bg=scheme["bg"],
            fg="#27ae60",
            activeforeground="#ffffff",
            activebackground="#27ae60",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            bd=0,
            cursor="hand2",
            command=lambda: self.close_task(task_card)
        )
        done_btn.pack(side=tk.RIGHT, padx=2)

        self.task_count += 1
        
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

    def add_task_from_input(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.create_task_ui(task_text)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()

    def close_task(self, task_card):
        """Removes the task component row from view and rewrites the data archive file."""
        # Visual clean up from UI window
        task_card.destroy()
        
        # Defer layout recalculations slightly to let Tkinter finish widget updates safely
        self.after(50, self.save_tasks)

    def save_tasks(self):
        """Scans surviving active layouts and overwrites the JSON file."""
        tasks_to_save = []
        for task_card in self.task_container.winfo_children():
            # Ensure we only pick frames that haven't been marked for destruction
            if task_card.winfo_exists():
                for widget in task_card.winfo_children():
                    if isinstance(widget, tk.Label):
                        tasks_to_save.append(widget.cget("text"))
        
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(tasks_to_save, f, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save tasks: {e}")

    def load_tasks(self):
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