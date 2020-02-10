"""
Dynamic programming is breaking down a problem into smaller sub-problems, 
solving each sub-problem and storing the solutions to each of these 
sub-problems in an array (or similar data structure) 
so each sub-problem is only calculated once.
"""

class Job: 
	def __init__(self, start, finish, profit): 
		self.start = start 
		self.finish = finish 
		self.profit = profit 



def binarySearch(job, start_index): 
	lo = 0
	hi = start_index - 1
	while lo <= hi: 
		mid = (lo + hi) // 2
		if job[mid].finish <= job[start_index].start: 
			if job[mid + 1].finish <= job[start_index].start: 
				lo = mid + 1
			else: 
				return mid 
		else: 
			hi = mid - 1
	return -1

# The main function that returns the maximum possible 
# profit from given array of jobs 
def schedule(job): 
	job = sorted(job, key = lambda j: j.start) 
	n = len(job) 
	table = [0 for _ in range(n)] 
	table[0] = job[0].profit; 
	for i in range(1, n): 
		inclProf = job[i].profit 
		l = binarySearch(job, i) 
		if (l != -1): 
			inclProf += table[l]; 
		table[i] = max(inclProf, table[i - 1]) 
	return table[n-1] 

# Driver code to test above function 
job = [Job(1, 2, 50), Job(3, 5, 20), Job(6, 19, 100), Job(2, 100, 200)] 
print("Optimal profit is"), 
print(schedule(job))