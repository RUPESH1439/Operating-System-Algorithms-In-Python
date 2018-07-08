class Process:
	

	def __init__(self,name,arrival,burst):
		self.name = name
		self.arrival_time = arrival
		self.burst_time = burst
	def get_arrival_time(self):
		return self.arrival_time
	def get_burst_time(self):
		return self.burst_time
	def get_name(self):
		return self.name
	def set_starting(self,time):
		self.starting = time
		self.complete = self.starting+self.burst_time
	def get_starting(self):
		return self.starting
	def get_complete(self):
		return self.complete


print("Enter the number of processes")
new_processes = []
N = int(input())
print("Enter Process's name arrival time and burst time ")
for i in range(N):
	name,a,b = map(str,input().split())
	a = int(a)
	b = int(b)
	new_processes.append(Process(name,a,b))
instant = 0
new_processes = sorted(new_processes,key=lambda process: process.get_arrival_time())
temp = new_processes
count = 0
final = []
while(temp!= []):
	eligible = []
	for process in temp:
		if (process.get_arrival_time() > instant):
			break
		else:
			eligible.append(process)
	if(eligible != []):
		eligible = sorted(eligible,key=lambda process: process.get_burst_time())
		current = eligible[0]
		current.set_starting(instant)
		instant+= current.get_burst_time()
		

	else:
		current = new_processes[count]
		current.set_starting(current.get_arrival_time())
		instant+= current.get_complete()
		count+=1
	final.append(current)
	temp.remove(current)
for process in final:
	print(process.get_name(),"   ",process.get_starting(),"----",process.get_complete())



