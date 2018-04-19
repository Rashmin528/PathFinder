import csv

class Node(object):
    def __init__(self, city, state):
        self.city = city
        self.state = state

def List():
     with open('citygps.csv','r') as file:
        reader = csv.reader(file)
        return [Node(city,state) for city, state in reader]

for get in List():
     print(get.city, get.state) 
