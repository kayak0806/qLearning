import random

rooms = 8
goal = 2

gamma = 0.5
alpha = 0.5


reward = {
(0,0):-1,(0,3):0,(0,7):-10,
(1,1):-1,(1,2):0,(1,7):-10,
(2,1):0,(2,2):-1,(2,4):0,
(3,0):0,(3,1):0,(3,3):-1,(3,4):0,(3,5):0,
(4,2):0,(4,3):0,(4,4):-1,(4,5):0,(4,6):10,(4,7):-10,
(5,3):0,(5,4):0,(5,5):-1,
(6,4):0,(6,6):10,
(7,0):0,(7,1):0,(7,4):0,(7,7):-10}

def getActions(room):
	actions = []
	for r in range(rooms):
		if (room,r) in reward:
			actions.append( r )
	return actions

Q = dict()

for i in range(5):
	# make a move
	# pos = random.randint(0,rooms-1)
	pos = 0
	lenth = 0
	while (pos != 6):
		lenth+=1
		print pos
		actions = getActions(pos)
		best = []
		qbest = None
		for r in actions:
			rq = Q.setdefault((pos,r),0)
			if rq>qbest:
				qbest = rq
				best = [r]
			elif rq==qbest:
				best.append(r)
		next = random.choice(best)

		'''
		in real life, this is where you'd move.
		next would be where you actually ended up.
		reward would be a measured reward, not from a table.
		'''

		nextActions = getActions(next)
		nqbest = None
		for r in nextActions:
			rq = Q.setdefault( (next,r), 0 )
			nqbest = max(nqbest,rq)

		Q[(pos,next)] = Q[(pos,next)]+alpha*(reward[(pos,next)]+gamma*nqbest-Q[(pos,next)])

		pos = next
	print 'trial',i,' done in ', lenth
	

