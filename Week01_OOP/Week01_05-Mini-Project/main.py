from tracker.task import Task
from tracker.tracker import TaskTracker
from tracker.utils import log_time

@log_time
def main():
    tracker = TaskTracker()

    while True:
        print("\n📌 Commands: add, list, done, undone, delete, exit")
        cmd = input(">> ").strip().lower()
        
        if cmd == "add":
            title = input("Title: ")
            due = input("Due date: ")
            desc = input("Description (optional): ")
            tracker.add_task(Task(title, due, desc))
            print("✅ Task added.")
    
        elif cmd == "list":
            tasks = tracker.list_tasks()
            if not tasks:
                print("No tasks found.")
                continue
            for i, t in enumerate(tasks):
                status = "✅" if t.completed else "❌"
                print(f"{i+1}. {t.title} (Due: {t.due_date}) [{status}]")

        elif cmd == "done":
            index = int(input("Enter task number to mark as complete: ")) - 1
            tracker.mark_task_done(index)
            # print("🎉 Task marked as complete.")
 
        elif cmd == "undone":
            index = int(input("Enter task number to mark as complete: ")) - 1
            tracker.mark_task_undone(index)

        elif cmd == "delete":
            index = int(input("Enter task number to delete: ")) - 1
            tracker.delete_task(index)
            # print("🗑️  Task deleted.")

        elif cmd == "exit":
            print("👋 Exiting Task Tracker.")
            break

        else:
            print("⚠️ Unknown command.")

if __name__ == "__main__":
    main()
