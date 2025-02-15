"""
GUI implementation for the To-Do List application.
Provides a graphical interface for task management using tkinter.
"""

# Standard library imports
import tkinter as tk
from tkinter import ttk, messagebox

# Local application imports
from tasks import TaskManager


class TodoGUI:
    """
    Graphical user interface for the To-Do List application.
    Handles all GUI elements and their interactions.
    """

    def __init__(self, root):
        """
        Initialize the GUI window and all its components.
        
        Args:
            root: The main window Tk instance
        """
        # Configure main window
        self.root = root
        self.root.title("To-Do List")
        self.task_manager = TaskManager()
        
        # Create and configure the task entry frame
        self.entry_frame = ttk.Frame(self.root)
        self.entry = ttk.Entry(self.entry_frame, width=40)
        self.add_button = ttk.Button(self.entry_frame, text="Add Task", 
                                   command=self.add_task)
        self.clear_button = ttk.Button(self.entry_frame, text="Clear", 
                                     command=self.clear_entry)
        
        # Create checkbox for numbering options
        self.show_numbers_var = tk.BooleanVar()
        self.show_numbers_checkbox = ttk.Checkbutton(
            self.entry_frame, 
            text="Show Numbers", 
            variable=self.show_numbers_var,
            command=self.update_task_display
        )
        
        # Create and configure the task display area
        self.display_frame = ttk.Frame(self.root)
        self.display = tk.Text(self.display_frame, width=50, height=20)
        self.scrollbar = tk.Scrollbar(self.display_frame, 
                                    command=self.display.yview)
        self.display.configure(yscrollcommand=self.scrollbar.set)
        
        # Arrange entry frame components
        self.entry.pack(side=tk.LEFT, padx=5, pady=5)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.show_numbers_checkbox.pack(side=tk.LEFT, padx=5, pady=5)
        self.entry_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Arrange display frame components
        self.display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.display_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Update task display
        self.update_task_display()

    def add_task(self):
        """
        Add a new task from the entry field to the task list.
        Validates input and shows error message if empty.
        """
        # Get and validate task description
        task = self.entry.get()
        if task.strip() == "":
            messagebox.showerror("Error", "Task cannot be empty")
            self.entry.delete(0, tk.END)
            self.entry.focus_set()
            return
        
        # Add task and update display
        self.task_manager.add_task(task)
        self.entry.delete(0, tk.END)
        self.update_task_display()

    def clear_entry(self):
        """Clear the contents of the entry field."""
        self.entry.delete(0, tk.END)

    def update_task_display(self):
        """
        Update the task display area with the current list of tasks.
        Handles numbered/unnumbered display based on checkbox state.
        """
        # Clear current display and show updated task list
        self.display.delete(1.0, tk.END)
        tasks = self.task_manager.list_tasks(self.show_numbers_var.get())
        self.display.insert(tk.END, tasks)
