#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "tasks.json"

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Todo App v2 (Maximum Visibility)")
        self.geometry("460x600")  # Expanded resolution for breathing room
        self.configure(bg="#F1F5F9")

        # Ultra High-Contrast Alternating Color Palette
        self.color_schemes = [
            {"bg": "#FFFFFF", "fg": "#000000"},  # Crisp White Row / Solid Black Text
            {"bg": "#FEF3C7", "fg": "#000000"}   # High-Visibility Amber-Yellow Row / Solid Black Text
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
        # --- High-Contrast Header Banner ---
        header = tk.Label(
            self, 
            text="★ MY ACTIVE TO-DO LIST ★", 
            bg="#000000", 
            fg="#FFFFFF", 
            font=("Arial", 14, "bold"), 
            pady=20
        )
        header.pack(side=tk.TOP, fill=tk.X)

        # --- Main Scrollable List Area ---
        self.canvas = tk.Canvas(self, bg="#F1F5F9", highlightthickness=0)
        
        # Thicker scrollbar layout for quick accessibility tracking
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview, width=20)
        
        self.task_container = tk.Frame(self.canvas, bg="#F1F5F9")
        
        self.canvas_window = self.canvas.create_window((0, 0), window=self.task_container, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=20, pady=15)

        self.task_container.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        # --- Bottom Input Footer Area ---
        input_frame = tk.Frame(self, bg="#000000", pady=20, padx=20)
        input_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Thick, High-Contrast Entry Box
        self.task_entry = tk.Entry(
            input_frame, 
            bg="#FFFFFF", 
            fg="#000000", 
            insertbackground="#000000", # Thick visible cursor line
            insertwidth=3,
            font=("Arial", 14, "bold"),  # Large typing text
            relief=tk.SOLID,
            bd=3
        )
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=10, padx=(0, 12))
        self.task_entry.focus_set()
        
        # Giant Add Button
        add_btn = tk.Button(
            input_frame, 
            text="ADD ITEM", 
            bg="#1D4ED8",  # Vibrant primary blue
            fg="#FFFFFF", 
            font=("Arial", 12, "bold"),
            relief=tk.RAISED,
            bd=2,
            activebackground="#FFFFFF",
            activeforeground="#1D4ED8",
            cursor="hand2"
        )
        add_btn.configure(command=self.add_task_from_input)
        add_btn.pack(side=tk.RIGHT, ipady=6, ipadx=20)

        self.bind("<Return>", lambda event: self.add_task_from_input())

    def create_task_ui(self, task_text):
        """Generates huge, highly isolated row modules for complete visual definition."""
        scheme = self.color_schemes[self.task_count % 2]
        
        # Heavy Border Task Block
        task_card = tk.Frame(
            self.task_container, 
            bg=scheme["bg"], 
            highlightbackground="#000000",  # Dark crisp border lines
            highlightthickness=2,
            pady=12,
            padx=16
        )
        task_card.pack(side=tk.TOP, fill=tk.X, pady=6)

        # Big Bold Text Label
        lbl = tk.Label(
            task_card, 
            text=task_text, 
            bg=scheme["bg"], 
            fg=scheme["fg"], 
            font=("Arial", 14, "bold"),  # Massive text profile
            anchor="w",
            wraplength=300
        )
        lbl.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=4)

        # Clear Contrast Clear/Delete Action Cross
        done_btn = tk.Button(
            task_card,
            text=" ✗ CLOSE ", 
            bg="#DC2626",  # Intense Signal Red
            fg="#FFFFFF", 
            activeforeground="#DC2626",
            activebackground="#FFFFFF",
            font=("Arial", 11, "bold"),
            relief=tk.SOLID,
            bd=1,
            cursor="hand2",
            command=lambda: self.close_task(task_card)
        )
        done_btn.pack(side=tk.RIGHT, padx=2, ipady=4)

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