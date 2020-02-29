from functools import reduce

# flatten
flatten = lambda l: [i for s in l for i in s]

# power set

def powerset(ls):
	x = len(ls)
	for i in range(1 << x):
		print [ls[s] for s in range(x) if (i & (1 << s))]

# all permutation

def permutation(ls): 
    if len(ls) == 0: 
        return [] 

    if len(ls) == 1: 
        return [ls] 
  
    l = [] 

    for i in range(len(ls)): 
       m = ls[i] 

       remLst = ls[:i] + ls[i+1:] 

       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 

# number spiral

# I am sorry Dr. Garcia, I ran out of time for this one.


"""
def numspir(n,end_corner):
	direction_vecs = [(1,0),(0,-1),(0,1),(-1,0)] # corner 1, 2, 3, 4, respectively

	curr_dir_ind = end_corner - 1

	curr_pos = (0,n-1)
	curr_num = n**2 -1

	mat = [] # declare using nested for look

	for i in range(0, n):
		mat.append([])
		for n in range(0,n):
			mat[i].append(-1)

	while curr_num >= 0:
		mat[curr_pos] = curr_num

		if change_dir(mat,curr_pos):
			curr_dir_ind += 1

		curr_pos = curr_pos + direction_vecs[curr_dir_ind%%4]

		curr_num-=1


def change_dir(next_pos,curr_num,mat):
	if mat[next_pos] == -1:

"""