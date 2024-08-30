def task():
    tasks = []
    print('Welcome to our Task Management app')
    total_task = int(input('How many task you want to add Today'))
    for i in range(total_task):
        task_name = input(f'enter {i} task')
        tasks.append(task_name)
    
    print(f'Today tasks are:\n {tasks}')

    while True:
        operation = int(input(f'what you want to Enter 1-Add\n 2-Delete\n 3-Update\n 4-View\n 5-Exit\n'))

        if operation == 1:
            take_task_name = input('Enter a task')
            tasks.append(take_task_name)
            print(f'Task {take_task_name} added successfully..')
        
        elif operation == 2:
            take_delete_task = input('Enter a task which you want to delete')
            tasks.remove(take_delete_task)
            print(f'task {take_delete_task} deleted successfully..')

        elif operation == 3:
            update_task = input('Enter which task you want to update')
            for task in tasks:
                if update_task == task:
                    ind = tasks.index(update_task)
                    updates_task = input('Enter a New task')
                    tasks.update(ind,updates_task)
                    print(f'Task {updates_task} update successfully')

        elif operation == 4:
            print(f'{tasks}')
        
        elif operation == 5:
            print('Closing the app')
            break
    
        else:
            print(' Invalid Input ')
  
task()






