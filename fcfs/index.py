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
	name,w,b = map(str,input().split())
	w = int(w)
	b = int(b)
	new_processes.append(Process(name,w,b))

new_processes = sorted(new_processes,key=lambda process: process.get_arrival_time())
instant = new_processes[0].get_arrival_time()
for process in new_processes:
	process.set_starting(instant)
	instant+= process.get_burst_time()
print("The output from FCFS rule:")
for process in new_processes:
	print(process.get_name(),"   ",process.get_starting(),"----",process.get_complete())



