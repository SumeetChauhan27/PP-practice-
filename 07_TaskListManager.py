print('Let\'s create a task list')

T1 = input('Enter Task 1: ')
T2 = input('Enter Task 2: ')
T3 = input('Enter Task 3: ')

task_list = [T1, T2, T3]
print('The Tasks Are:', task_list)

print('Adding a new task')
T4 = input('Enter Task 4: ')
task_list.append(T4)
print('Updated Task List:', task_list)
print('---------------------------------')

print('Sorting Task List')
task_list.sort()
print('Sorted Task List:', task_list)
print('---------------------------------')

print('Changing/Updating a task')
no = int(input('Enter the Task number to be updated: '))
newtask = input('Enter the updated value of Task: ')
task_list[no - 1] = newtask
print('Updated Task List:', task_list)
print('---------------------------------')

print('Deleting a task')
rem = input('Enter Task to be deleted: ')
task_list.remove(rem)
print('Updated Task List:', task_list)
