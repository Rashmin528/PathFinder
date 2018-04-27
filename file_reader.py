import csv


class Node(object):
    def __init__(self, city, state, latitude=0, longitude=0):
        self.city = city
        self.state = state
        self.latitude = latitude
        self.longitude = longitude


def read_file(file_name='citygps.csv'):
	result = {}
	with open(file_name, 'r') as file:
		reader = csv.reader(file)
		for city, details in reader:
			state, latitude, longitude = details.split(' ')
			result[city] = Node(city, state, latitude, longitude)
	return result


if __name__ == "__main__":
	# Reads as City = Node(city, state, latitude, longitude)
	input_data = read_file()
	input_city = 'Seattle'
	print "This Prints City : Node"
	print input_data[input_city]
	print input_data[input_city].state
	print input_data[input_city].latitude
	print input_data[input_city].longitude
