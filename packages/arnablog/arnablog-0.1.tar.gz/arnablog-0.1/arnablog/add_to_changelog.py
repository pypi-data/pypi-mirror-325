import argparse
import datetime

def add_entry(file_path, name, task, status, improvement, total_time_taken):
    date = datetime.datetime.today().strftime('%d-%m-%Y')
    entry = f"\n| {date.ljust(10)} | {name.ljust(22)} | {task.ljust(22)} | {status.ljust(24)} | {improvement.ljust(29)} | {total_time_taken.ljust(33)} |"

    with open(file_path, 'a') as file:
        file.write(entry)
        file.write("\n---------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Entry added successfully!")

def main():
    parser = argparse.ArgumentParser(description="Add an entry to changelog.txt")
    parser.add_argument("--file_path", type=str, required=True, help="Path to the changelog file")
    parser.add_argument("--name", type=str, required=True, help="Name of the person")
    parser.add_argument("--task", type=str, required=True, help="Task description")
    parser.add_argument("--status", type=str, required=True, help="Task status (e.g., DONE, PENDING)")
    parser.add_argument("--improvement", type=str, required=True, help="Improvements made")
    parser.add_argument("--total_time_taken", type=str, required=True, help="Time taken for the task")
    
    args = parser.parse_args()
    add_entry(args.file_path, args.name, args.task, args.status, args.improvement, args.total_time_taken)

if __name__ == "__main__":
    main()
