mainloc = input('Where is your tasks at?\n')
class Task:
    tasks = []
    with open(mainloc,'r') as file:
        for line in file:
            tasks.append(line.strip())

class Add:
    def __init__(self,task):
        self.addedtask = task

    def add(self):
        Task.tasks.append(self.addedtask)
        print("Task is added")
class Remove:

    def __init__(self,index):
        
        self.removedtask = index
    
    def remove(self):
        if len(Task.tasks)==0:
            return None
        else:
            Task.tasks.remove(Task.tasks[self.removedtask])
            print("Task is removed!")
while True:
    print("What do you want to do?(Type help for more) \n1)Add tasks\n2)Remove tasks.\n3)Show tasks.")
    command  = input()
    if command == '1'or command == 'add' or command  == 'add tasks' or command == "Add tasks": 
        print("Adding tasks!.To quit type q.")
        while True:
            task = input()
            if task == "q":
                break
            task=Add(task)
            task.add()
    elif command  == "2" or command  == "remove" or command== "Remove" or command =="Remove tasks":
        while True:
            print("Removing tasks!.\nWhich task do you want to remove?")
            input_index = input()
            if input_index == 'q':
                break
            elif input_index>='9':
                print("Please enter the line number of your task!")
            elif input_index>str(len(Task.tasks)):
                print("Line number doesn't exist")
            else:
                removetask=Remove(int(input_index)-1)
                removetask.remove()
    elif command == '3' or command  == 'show' or command == 'Show' or command == 'Show tasks':
        row = 1
        for task in Task.tasks:
            print(row,".",task,sep="")
            row+=1
    elif command == "save":
        print("Your tasks are saved!Byeeee...")
        with open(mainloc,'w') as file:
            for task in Task.tasks:
                task+="\n"
                file.write(task)
        break
    elif command == "help":
        print("Command lines for adding tasks: add, add tasks,Add tasks\nCommand lines for removing tasks: remove,Remove,Remove tasks\nCommand lines for showing tasks: show, Show, Show tasks\nCommand line to execute program and save your tasks: save")
    else:
        print("Invalid option")





    
