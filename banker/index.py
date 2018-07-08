import numpy as np
print("Enter number of processes")
processes = int(input())
print("Enter number of resources")
resources = int(input())
allocation = np.zeros((processes,resources))
max_values = np.zeros((processes,resources))
available = np.zeros((1,resources))

temp = []
print("Enter resources for each process sequentially")
for i in range(processes):
    x = input()
    x = list(int(value) for value in x.split())
    temp.append(x)
allocation = np.array(temp)

temp = []
print("Enter the maximum resources for each process sequentially")
for i in range(processes):
    x = input()
    x = list(int(value) for value in x.split())
    temp.append(x)
max_values = np.array(temp)

print("Enter the available resources")
x = input()
x = list(int(value) for value in x.split())
   
    
available = np.array(x)

need = max_values-allocation

ans = []
for i in range(processes):
    available_need = available-need[i]
    init = True
    for x in available_need:
        temp =True
        if x < 0:
            temp = False
        else:
            temp = True
        init= init and temp
            
    if (init):
        ans.append(i)
        available+= allocation[i]
remaining = []
for x in range(processes):
    if x not in ans:
        remaining.append(x)

for remaining_process in remaining:
    available_need = available-need[remaining_process]
    init = True
    for x in available_need:
        temp =True
        if x < 0:
            temp = False
        else:
            temp = True
        init= init and temp
            
    if (init):
        ans.append(remaining_process)
        available+= allocation[remaining_process]

if(len(ans) != processes):
    print("Not safe")
else:
    print("Safe")
    final_output = []
    for process in ans:
        final_output.append("p"+str(process))
    for x in final_output:
        print(x)
