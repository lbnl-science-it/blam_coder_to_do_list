# main.py
import argparse
from tasks import TaskManager

def main():
    parser = argparse.ArgumentParser(description='To-Do List App')
    subparsers = parser.add_subparsers(dest='command')

    # Add command
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('task', type=str, help='Task description')

    # List command
    list_parser = subparsers.add_parser('list')
    list_parser.add_argument('-n', '--number', action='store_true', help='Show task numbers')

    args = parser.parse_args()

    task_manager = TaskManager()

    if args.command == 'add':
        task_manager.add_task(args.task)
    elif args.command == 'list':
        output = task_manager.list_tasks(args.number)
        print(output)

if __name__ == '__main__':
    main()

