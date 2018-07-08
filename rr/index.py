class Process:
	def __init__(self,name,arrival,burst):
		self.name = name
		self.arrival_time = arrival
		self.burst_time = burst
	def set_arrival_time(self,time):
		self.arrival_time = time
	def get_arrival_time(self):
		return self.arrival_time
	def get_burst_time(self):
		return self.burst_time
	def set_burst_time(self,time):
		self.burst_time = time
	def get_name(self):
		return self.name
	def set_starting(self,time):
		self.starting = time
	def get_starting(self):
		return self.starting
	def get_complete(self):
		return self.complete
	def set_complete(self,time):
		self.complete = self.starting+time

print("Enter the number of processes")
new_processes = []
N = int(input())
print("Enter time slice")
timeSlice = int(input())
print("Enter Process's name arrival time and burst time ")
for i in range(N):
	name,a,b = map(str,input().split())
	a = int(a)
	b = int(b)
	new_processes.append(Process(name,a,b))
new_processes = sorted(new_processes,key=lambda process: process.get_arrival_time())
instant = new_processes[0].get_arrival_time()
temp = new_processes
count = 0
final = []
while(temp != []):
	current = temp[0]
	if(current.get_burst_time() > timeSlice):
		current.set_burst_time(current.get_burst_time()-timeSlice)
		constant = timeSlice
	else:
		
		constant= current.get_burst_time()
		current.set_burst_time(0)
	newProcess = Process(current.get_name(),instant,instant+constant)
	instant+= constant
	final.append(newProcess)
	if(current.get_burst_time() <= 0):
		temp.remove(temp[0])
		temp = sorted(temp,key=lambda process: process.get_arrival_time())
		continue
	current.set_arrival_time(instant)
	if(temp != []):
		
		temp[0] = current
		temp = sorted(temp,key=lambda process: process.get_arrival_time())

for process in final:
	print(process.get_name(),"   ",process.get_arrival_time(),"----",process.get_burst_time())



