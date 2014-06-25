include math

# possible states: range(0,100)
# possible actions: -1,0,1

tempStart = 90
tempGoal  = 50
tempNow   = tempStart

y = .5
alpha = .5

Q = dict() #Q(action,state) = value

def reward(a,s):
	return -(tempGoal - (s+a))

def transition(a,s):
	return s+a

def actions(s):
	if s<=0:
		return {0,1}
	if s>=100:
		return {-1,0}
	return {-1,0,1}

def randomize(a):
	return math.random()

def step(s):
	next = []
	for b in actions(s):
		next.append((Q.get((b,transition(b,s)),0),b))
	return max(next)[1]		

action = 0
for i in range(100):
	'''update'''
	# Q(a,s) = (1-alpha)*Q(a,s)+alpha*[ reward(a,s)+y*maxQ(b,s') ]
	# Q(a,s) = reward(a,s)+maxQ(b,s')
	old = Q.get((action,tempNow),0)
	new = reward(action,tempNow) + y*step(tempNow)
	Q[(action,tempNow)] =  (1-alpha)*old + alpha*new

	tempNow = transition(action,tempNow)
	print tempNow
	action = step(tempNow)



