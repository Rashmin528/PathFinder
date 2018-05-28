class Segment(object):
	def __init__(self, start_city, end_city, distance, maxspeed, highway):
		self.start_city = start_city
		self.end_city = end_city
		self.distance = distance
		self.maxspeed = maxspeed
		self.highway = highway

def read_segment_file():
	result = {}
	with open('roadsegments.txt','r') as file:
		for line in file.readlines():
			# details = line.split(' ')
	  # Abbot_Village,_Maine Bingham,_Maine 24 45 ME_16
			start_city, end_city, distance, maxspeed, highway = line.split(' ')
	  # result[Start_city] = [Segment(start to end)]
			if start_city not in result:
				result[start_city] = [Segment(start_city, end_city, distance, maxspeed, highway)]
			else:
				result[start_city].append(Segment(start_city, end_city, distance, maxspeed, highway))
	  # result[End_city] = [Segment(end to start)]
			if end_city not in result:
				result[end_city] = [Segment(end_city, start_city, distance, maxspeed, highway)]
			else:
				result[end_city].append(Segment(end_city, start_city, distance, maxspeed, highway))	

	return result

def dfs_iterative(graph, start, destination):
	stack = [start]
	path = []

	while stack: # while stack is not empty
		vertex = stack.pop() # get the first city to vertex
		if vertex in path:  # if city already in path
			continue # skip
		if vertex == destination: # if city is destination
			path.append(destination) # finally add destination at the end
			return path # return path
		path.append(vertex) # if city is not destination, city not in path then only add to path
		for segment_object in graph[vertex]:
			stack.append(segment_object.end_city)


def bfs_iterative(graph, start, destination):
	queue =  [start]
	visited = []

	while queue:
		vertex = queue.pop(0)
		if vertex in visited:
			continue
		if vertex == destination:
			visited.append(destination)
			return visited
		visited.append(vertex)
		for segment_object in graph[vertex]:
			queue.append(segment_object.end_city)
  
def calculate_distance(path, graph):
	pass

graph = read_segment_file()
print("------DFS PATH--------")
dfs_path = dfs_iterative(graph,"Bloomington,_Indiana", "Indianapolis,_Indiana") # dfs_path = [A, B, C, D] 
print(dfs_path)

print("------BFS PATH--------")
bfs_path = bfs_iterative(graph,"Bloomington,_Indiana", "Indianapolis,_Indiana") # bfs_path = [C, E, F, G, D] 
print(bfs_path)
