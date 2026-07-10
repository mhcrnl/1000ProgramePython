#!/usr/bin/env python3
import flet as ft

class TodoItem(ft.Container):
    """Represents a single task row with alternating background colors."""
    def __init__(self, text: str, index: int):
        # Alternating background scheme logic inspired by the original script
        bg_color = ft.Colors.SURFACE_CONTAINER_HIGHEST if index % 2 == 0 else ft.Colors.SURFACE_CONTAINER_LOW
        
        super().__init__(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.CHECK_BOX_OUTLINE_BLANK, color=ft.Colors.PRIMARY, size=18),
                    ft.Text(value=text, size=15, weight=ft.FontWeight.W_500, expand=True),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=12,
            bgcolor=bg_color,
            border_radius=6,
            animate=ft.Animation(200, ft.AnimationCurve.EASE_OUT),
        )

class TodoApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Modern To-Do App"
        self.page.window_width = 360
        self.page.window_height = 500
        self.page.window_resizable = False
        self.page.theme_mode = ft.ThemeMode.SYSTEM
        
        # Scrollable area for tasks
        self.tasks_list = ft.ListView(
            expand=True,
            spacing=6,
            auto_scroll=True,
        )
        
        # User input field
        self.task_input = ft.TextField(
            hint_text="What needs to be done?",
            expand=True,
            border_color=ft.Colors.OUTLINE,
            focused_border_color=ft.Colors.PRIMARY,
            on_submit=self.add_task,
            content_padding=12,
        )
        
        self.build_ui()

    def build_ui(self):
        # Header equivalent to the original "--- Add Items Here ---" banner
        header = ft.Container(
            content=ft.Text(
                "Your Tasks",
                size=14,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.ON_SURFACE_VARIANT,
                letter_spacing=1.2,
            ),
            alignment=ft.alignment.center,
            padding=ft.padding.only(bottom=10),
            border=ft.Border(bottom=ft.BorderSide(1, ft.Colors.OUTLINE_VARIANT)),
        )

        # Assemble layout
        self.page.add(
            ft.Column(
                controls=[
                    header,
                    self.tasks_list,
                    ft.Divider(height=1, color=ft.Colors.TRANSPARENT),
                    ft.Row(
                        controls=[
                            self.task_input,
                            ft.IconButton(
                                icon=ft.Icons.ADD_ROUNDED,
                                icon_color=ft.Colors.ON_PRIMARY,
                                bgcolor=ft.Colors.PRIMARY,
                                on_click=self.add_task,
                            ),
                        ],
                    ),
                ],
                expand=True,
            )
        )
        self.task_input.focus()

    def add_task(self, e):
        task_text = self.task_input.value.strip()
        
        if task_text:
            # Determine alternating scheme index based on current items list length
            current_index = len(self.tasks_list.controls)
            
            # Create and append new task item
            new_item = TodoItem(text=task_text, index=current_index)
            self.tasks_list.controls.append(new_item)
            
            # Clear layout inputs and refresh view
            self.task_input.value = ""
            self.page.update()

def main(page: ft.Page):
    TodoApp(page)

if __name__ == "__main__":
    ft.app(target=main)