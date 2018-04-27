import csv

class Node(object):
    def __init__(self, start_city,end_city,state,distance,maxspeed,highway):
        self.start_city = start_city
        self.end_city = end_city
        self.state = state
        self.distance = distance
        self.maxspeed = maxspeed
        self.highway = highway

def read_file(file_name='roadsegment.csv'):
        result = {}
        with open(file_name, 'r') as file:
                reader = csv.reader(file)
                for start_city, end_city, details in reader:
                        state, distance, maxspeed, highway = details.split(' ')
                        result[start_city] = Node(start_city,end_city, state, distance,maxspeed,highway)
        return result

if __name__ == "__main__":
        input_data = read_file()
        input_city = 'Bayfield'
        print(input_data[input_city].start_city)
        print(input_data[input_city].end_city)
        print(input_data[input_city].state)
        print(input_data[input_city].distance)
        print(input_data[input_city].maxspeed)
        print(input_data[input_city].highway)