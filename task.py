Tasks=[]
def add_task():
     print("Adding New Task...")
     task_id =int(input("Enter your task id.."))
     title = input("Enter task title..")
     category=input("Enter category..")
     priority = input("Enter Priority: ")
     notes = input("Enter Notes: ")
     task = {
    "id": task_id,
    "title": title,
    "category": category,
    "priority": priority,
    "is_completed": False,
    "notes": notes
     }  
     Tasks.append(task)

def view_tasks():
    for task in Tasks:
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Category: {task['category']}")
        print(f"Priority: {task['priority']}")
        print(f"Completed: {task['is_completed']}")
        print(f"Notes: {task['notes']}")
        print("--------------------")
def marktask():
   
    task_id = int(input("Enter task ID: "))

    for task in Tasks:
        if task["id"] == task_id:
            task["is_completed"] = True
            print("Task marked as completed!")
            return

    print("Task not found!")

def ViewCategories():
   categories=set()
   for task in Tasks :
       categories.add(task['category'])
   for  category in categories :
       print (category)  


while True :
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. View Categories")
    print("5. Exit")
   
    choice= int(input("Enter your choice : "))
    match choice :
        case 1 :
           add_task()
        case 2 :    
             view_tasks()
        case 3 :
          marktask()
        case 4 :
           ViewCategories()     
        case 5 :
            print("Goodbye..!") 
            break    
