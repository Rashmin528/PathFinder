def calculate_distance(graph, path):
	Total = 0
	for x in range(0,len(path)-1):
		segment_list = graph[path[x]] 
	for neighbor in segment_list: 
		if neighbor.end_city == path[x+1]:
		Total = Total + neighbor.distance
	return Total
