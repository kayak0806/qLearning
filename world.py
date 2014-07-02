

class world(object):
	def __init__(self,start):
		self.pos = start%6 # init pos forced to 0-5
		self.values = [4,6,8,6,4,2]

	def display(self):
		print self.pos

	def actions(self):
		if (self.pos==0):
			return [0,1]
		if (self.pos==5):
			return [-1,0]
		return [-1,0,1]

	def move(self, dir):
		self.pos += dir

	def reward(self, dir):
		if (dir==0):
			if (self.pos==2):
				return -1
			return 0
		newPos = self.pos+dir
		if (newPos==7 or newPos==0):
			return -10
		return (newPos - self.pos)


Q = dict() #Q(action,state) = value
y = .5
alpha = .5

# Q(a,s) = (1-alpha)*Q(a,s)+alpha*[ reward(a,s)+y*maxQ(b,s') ]
# Q(a,s) = reward(a,s)+maxQ(b,s')

olin = world(0)

'''each step'''
current = olin.pos
if current == 




# if __name__ == '__main__':
# 	olin = world(10)
# 	olin.display()
# 	olin.move(0)
# 	olin.display()
