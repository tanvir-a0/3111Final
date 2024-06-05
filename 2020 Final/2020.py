import time
import copy


number_of_cases = int(input())
for case in range(number_of_cases):
    first_line = input().split(" ")
    #print(first_line)
    number_of_tasks = int(first_line[0])
    my_task = int(first_line[1])
    task_priority = input().split(" ")
    task_priority_dict = {}
    for i in range(number_of_tasks):
        task_priority_dict[i] = int(task_priority[i])
    max_priority = max(list(task_priority_dict.values()))
    #print(max_priority)
    tasks = list(task_priority_dict.keys())
    prio = list(task_priority_dict.values())
    result = 0
    while True:
        #time.sleep(2)
        #print('prio 0: ', prio[0])
        if prio[0] != max_priority:
            tasks.append(tasks[0])
            prio.append(prio[0])
            tasks.pop(0)
            prio.pop(0)
            # print(tasks)
            # print(prio)
            continue

        if prio[0] == max_priority:
            if tasks[0] == my_task:
                #print("Found the solution")
                break
            result = result + 1
            tasks.pop(0)
            prio.pop(0)
            max_priority = max(prio)
            # print(tasks)
            # print(prio)
        
        
    print(result + 1)
    
    