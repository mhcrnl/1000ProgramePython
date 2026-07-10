#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "tasks.json"

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Todo App v2 (High Visibility)")
        self.geometry("420x550")  # Wider for better text space
        self.configure(bg="#f7fafc")

        # High-Contrast Alternating Color Palette
        self.color_schemes = [
            {"bg": "#ffffff", "fg": "#1a202c"},  # Pure White Row / Dark Charcoal Text
            {"bg": "#edf2f7", "fg": "#1a202c"}   # Light Ice-Blue Row / Dark Charcoal Text
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
        # --- High-Visibility Header ---
        header = tk.Label(
            self, 
            text="CURRENT TO-DO LIST", 
            bg="#1a202c", 
            fg="#ffffff", 
            font=("Segoe UI", 12, "bold"), 
            pady=16
        )
        header.pack(side=tk.TOP, fill=tk.X)

        # --- Main Scrollable Area ---
        self.canvas = tk.Canvas(self, bg="#f7fafc", highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        
        self.task_container = tk.Frame(self.canvas, bg="#f7fafc")
        
        self.canvas_window = self.canvas.create_window((0, 0), window=self.task_container, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=16, pady=10)

        self.task_container.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        # --- Bottom Input Footer Area ---
        input_frame = tk.Frame(self, bg="#edf2f7", pady=16, padx=16)
        input_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Bold, Large Text Entry Field
        self.task_entry = tk.Entry(
            input_frame, 
            bg="#ffffff", 
            fg="#1a202c", 
            insertbackground="#1a202c", # Highly visible typing cursor
            font=("Segoe UI", 12),
            relief=tk.SOLID,
            bd=2
        )
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 10))
        self.task_entry.focus_set()
        
        # Prominent Add Action Button
        add_btn = tk.Button(
            input_frame, 
            text="ADD TASK", 
            bg="#2b6cb0", # Deep clear blue
            fg="#ffffff", 
            font=("Segoe UI", 11, "bold"),
            relief=tk.FLAT,
            activebackground="#2c5282",
            activeforeground="#ffffff",
            cursor="hand2"
        )
        add_btn.configure(command=self.add_task_from_input)
        add_btn.pack(side=tk.RIGHT, ipady=4, ipadx=18)

        self.bind("<Return>", lambda event: self.add_task_from_input())

    def create_task_ui(self, task_text):
        """Creates a highly legible task row with large font and strong element contrast."""
        scheme = self.color_schemes[self.task_count % 2]
        
        # Task Card Border wrapper
        task_card = tk.Frame(
            self.task_container, 
            bg=scheme["bg"], 
            highlightbackground="#cbd5e0", 
            highlightthickness=1,
            pady=8,
            padx=14
        )
        task_card.pack(side=tk.TOP, fill=tk.X, pady=4)

        # High-Legibility Label
        lbl = tk.Label(
            task_card, 
            text=task_text, 
            bg=scheme["bg"], 
            fg=scheme["fg"], 
            font=("Segoe UI", 12, "bold"),  # Large, clean text style
            anchor="w",
            wraplength=280  # Keeps extra-long text inside readable bounds
        )
        lbl.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=6)

        # Highly Visible Close/Delete Action Button
        done_btn = tk.Button(
            task_card,
            text=" ✗ ", 
            bg=scheme["bg"],
            fg="#e53e3e", # High visibility crimson red
            activeforeground="#ffffff",
            activebackground="#e53e3e",
            font=("Arial", 11, "bold"),
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
        task_card.destroy()
        self.after(50, self.save_tasks)

    def save_tasks(self):
        tasks_to_save = []
        for task_card in self.task_container.winfo_children():
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