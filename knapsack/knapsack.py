#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

# Example Knapsack
# {'Value': 197, 'Chosen': [1, 7, 8]}

def knapsack_solver(items, capacity):
    # Your code here
    returnBag = {
      'Value': 0
      'Chosen': []
    }

    item_weights = [i[1] for i in items]
    item_values = [i[2] for i in items]

    n = len(item_weights)
    W = capacity
    bag = [[0 for w in range(W + 1)] for i in range(n)]

    for i in range(1, n):
      for w in range(1, W + 1):
        wi = item_weights[i]
        vi = item_values[i]

        if wi <= w:
          bag[i][w] = max([bag[i - 1][w -wi] + vi, bag[i - 1][w]])
        else:
          bag[i][w] = bag[i - 1][w]
    
    print(bag)


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')