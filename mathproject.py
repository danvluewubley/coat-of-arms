import numpy as np

table = ''
name = "Daniel Wu"
name = name.replace(" ", "").lower()
name = name + name + name[0] + name[1]
table = table + name
table = list(table)
table_of_converted_letters = []
table_of_coordinates = []

matrix= np.arange(0,len(name)).reshape((len(name)//2, 2))

def letter_handle(x):
  return {
      'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14,'o': 15,'p': 16,'q': 17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26
  }.get(x)

def coordinate_handle(x):
  return {
      '1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, '11': 10, '12': 0, '13': 1, '14': 2, '15': 3, '16': 4, '17': 5, '18': 6, '19': 7, '20': 8, '21': 9, '22': 10, '23': 0, '24': 1, '25': 2, '26': 3
  }.get(str(x))

def original_coordinates():
  for x in range(len(name)):
    table_of_converted_letters.append(letter_handle(name[x]))
    table_of_coordinates.append(coordinate_handle(table_of_converted_letters[x]))

  for x in range(len(name)//2):
    matrix[x, 0] = table_of_coordinates[x]
    matrix[x, 1] = table_of_coordinates[x+len(name)//2]

  print("Original Coordinates: ")
  print(matrix)
  return matrix

def reflection_y_coordinates(matrix):
  for x in range(len(name)//2):
    matrix[x, 0] = table_of_coordinates[x] * -1
    matrix[x, 1] = table_of_coordinates[x+len(name)//2]

  print("Coordinates after a reflection over the y-axis:")
  print(matrix)

def reflection_x_coordinates(matrix):
  for x in range(len(name)//2):
    matrix[x, 0] = table_of_coordinates[x]
    matrix[x, 1] = table_of_coordinates[x+len(name)//2] * -1

  print("Coordinates after a reflection over the x-axis: ")
  print(matrix)

def reflection_origin_coordinates(matrix):
  for x in range(len(name)//2):
    matrix[x, 0] = table_of_coordinates[x] * -1
    matrix[x, 1] = table_of_coordinates[x+len(name)//2] * -1

  print("Coordinates after a reflection over the origin: ")
  print(matrix)

matrix = original_coordinates()
reflection_y_coordinates(matrix)
reflection_x_coordinates(matrix)
reflection_origin_coordinates(matrix)