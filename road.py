import csv

class Segment(object):
	def __init__(self, start_city, end_city, state, distance, maxspeed, highway):
		self.start_city = start_city
		self.end_city = end_city
		self.state = state
		self.distance = distance
		self.maxspeed = maxspeed
		self.highway = highway

def read_file():
	result = {}
	with open('roadsegment.csv', 'r') as file:
		reader = csv.reader(file)
		for start_city, end_city, details in reader:
			state, distance, maxspeed, highway = details.split(' ')
			if start_city not in result:
				result[start_city] = [Segment(start_city, end_city, state, distance, maxspeed, highway)]
			else:
				result[start_city].append(Segment(start_city, end_city, state, distance, maxspeed, highway))
			if end_city not in result:
				result[end_city] = [Segment(start_city, end_city, state, distance, maxspeed, highway)]
			else:
				result[end_city].append(Segment(start_city, end_city, state, distance, maxspeed, highway))

	return result

if __name__ == "__main__":
	result = read_file()
	input_city = 'Okolona'
	for value in result[input_city]:
		print(value.start_city)
		print(value.end_city)
		print(value.state)
		print(value.distance)
		print(value.maxspeed)
		print(value.highway)
