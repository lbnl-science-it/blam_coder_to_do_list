"""
Main entry point for the To-Do List application.
Supports both GUI and CLI modes of operation.
"""

# Standard library imports
import argparse
import tkinter as tk

# Local application imports
from gui import TodoGUI
from tasks import TaskManager


def main():
    """
    Main function that handles program execution flow.
    Parses command line arguments to determine operation mode (GUI/CLI).
    """
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="To-Do List Application")
    parser.add_argument('--gui', action='store_true', help='Run the application in GUI mode')
    args = parser.parse_args()

    # Determine and execute appropriate mode
    if args.gui:
        # Initialize and run GUI mode
        root = tk.Tk()
        gui = TodoGUI(root)
        root.mainloop()
    else:
        # Initialize and run CLI mode
        print("Running in CLI mode")
        task_manager = TaskManager()

        # Main CLI interaction loop
        while True:
            print("\nTo-Do List CLI")
            print("1. Add Task")
            print("2. List Tasks")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                # Handle task addition
                task_description = input("Enter task description: ")
                if task_description.strip() == "":
                    print("Error: Task cannot be empty")
                else:
                    task_manager.add_task(task_description)
                    print("Task added successfully.")
            elif choice == '2':
                # Display all tasks
                tasks = task_manager.list_tasks(show_numbers=True)
                print("\nTasks:")
                print(tasks)
            elif choice == '3':
                # Exit the application
                print("Exiting CLI mode.")
                break
            else:
                # Handle invalid input
                print("Invalid choice. Please try again.")


# Execute only if run as a script
if __name__ == '__main__':
    main()
