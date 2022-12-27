import numpy as np

table = ''
name = ["Daniel Wu", "Zahin Islam"]
edited_name = []
num = 0


for x in range(len(name)):
  name[x] = name[x].replace(" ", "").lower()
  name[x] = list(name[x])


for x in range(len(name)):
  join = ""
  edited_name.append(join.join(name[x]) + join.join(name[x]) + name[x][0] + name[x][1])

def letter_handle(x):
  return {
      'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14,'o': 15,'p': 16,'q': 17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26
  }.get(x)

def coordinate_handle(x):
  return {
      '1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, '11': 10, '12': 0, '13': 1, '14': 2, '15': 3, '16': 4, '17': 5, '18': 6, '19': 7, '20': 8, '21': 9, '22': 10, '23': 0, '24': 1, '25': 2, '26': 3
  }.get(str(x))


def original_coordinates(name1, num):
  join = ""
  matrix = np.arange(0,len(name1)).reshape((len(name1)//2, 2))
  table_of_converted_letters = []
  table_of_coordinates = []

  for x in range(len(name1)):
    table_of_converted_letters.append(letter_handle(name1[x]))
    table_of_coordinates.append(coordinate_handle(table_of_converted_letters[x]))

  for x in range(len(name1)//2):
    matrix[x, 0] = table_of_coordinates[x]
    matrix[x, 1] = table_of_coordinates[x+len(name)//2]

  print(join.join(name[num]) + "'s Original Coordinates: ")
  print(matrix)
  return matrix, table_of_coordinates


def reflection_y_coordinates(name1, matrix, table_of_coordinates, num):
  join = ""
  for x in range(len(name1)//2):
    matrix[x, 0] = table_of_coordinates[x] * -1
    matrix[x, 1] = table_of_coordinates[x+len(name)//2]

  print("Coordinates after a reflection over the y-axis:")
  print(matrix)
  with open("info.txt", "a") as f:
    f.write(join.join(name[num]) + "'s Coordinates after a reflection over the y-axis\n")
    f.write(np.array_str(matrix) + '\n')
  f.close()


def reflection_x_coordinates(name1, matrix, table_of_coordinates, num):
  for x in range(len(name1)//2):
    matrix[x, 0] = table_of_coordinates[x]
    matrix[x, 1] = table_of_coordinates[x+len(name1)//2] * -1

  print("Coordinates after a reflection over the x-axis: ")
  print(matrix)

  with open("info.txt", "a") as f:
    f.write(join.join(name[num]) + "'s Coordinates after a reflection over the x-axis\n")
    f.write(np.array_str(matrix) + '\n')
  f.close()


def reflection_origin_coordinates(name1, matrix, table_of_coordinates, num):
  for x in range(len(name1)//2):
    matrix[x, 0] = table_of_coordinates[x] * -1
    matrix[x, 1] = table_of_coordinates[x+len(name1)//2] * -1

  print("Coordinates after a reflection over the origin: ")
  print(matrix)

  with open("info.txt", "a") as f:
    f.write(join.join(name[num]) + "'s Coordinates after a reflection over the origin\n")
    f.write(np.array_str(matrix) + '\n')
  f.close()

f = open("info.txt", "r+") 
f.seek(0) 
f.truncate() 
for x in range(len(edited_name)):
  matrix, table_of_coordinates = original_coordinates(edited_name[x], num)
  reflection_y_coordinates(edited_name[x], matrix, table_of_coordinates, num)
  reflection_x_coordinates(edited_name[x], matrix, table_of_coordinates, num)
  reflection_origin_coordinates(edited_name[x], matrix, table_of_coordinates, num)
  num += 1
