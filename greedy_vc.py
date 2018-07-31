def find_vc(input_graph):
	#'''This function finds the vertex cover '''
    cover = []
    valid, num_edge = valid_cover(input_graph, cover)
    
    while not valid:
        m = [x for x in range(0, len(num_edge)) if num_edge[x] == max(num_edge)][0]
        cover.append(m)
        valid, num_edge = valid_cover(input_graph, cover)
        
    return cover

def valid_cover(graph, cover):
	##'''Goes through the upper right triangle of the matrix finding the edges '''
    valid = True
    num_edge = [0] * len(graph)
    for i in range(0, len(graph)):
        for j in range(i, len(graph)): #Just check the upper right triangle of the matrix
            if graph[i][j] == 1:
                if (i not in cover) and (j not in cover):
                    valid = False
                    num_edge[i] += 1
                    num_edge[j] += 1
    return valid, num_edge


def vcCondition(vertexCover,k):
	#'''Checks the condition whehter or not vertex cover is less thank or equal to k. it returns true for the first case, and false for the latter'''
	if len(vertexCover) <= k:
	    return True
	else:
		return False

def run():
	#''' The main part '''
	k = int(raw_input('Enter a value for k: '))

	#Self defined graph here. Feel free to change it to your liking. This is using an adjacency matrix to represent the graph. 
	graph = [[0, 1, 1, 1, 1],
	         [1, 0, 0, 0, 0],
	         [1, 0, 0, 1, 1],
	         [1, 0, 1, 0, 1],
	         [1, 0, 1, 1, 0]]
	cover = find_vc(graph)

	#The output
	if (vcCondition(cover,k)):
		print("There is a vertex cover of size less than or equal to k, and it is: ")
		print cover
		print 'For the graph (Represented as an adjacency matrix): '
		print graph
	else:
		print('Oooohhhps...Size of vertex cover is larger than k')

run() # Used to run the file
