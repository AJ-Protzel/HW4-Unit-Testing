#---------------------------------------------------------------cubeVol
# Write code to calculate the volume of a cube
# Use 3 unit tests
# Consider: negative, type error, complex numbers
def cubeVol(num):
  if(type(num) not in [int, float]):
    raise TypeError('Input must be int or float')
  return num**3

#---------------------------------------------------------------aveElem
# Calculate average of elements in a list
# Use 3 unit tests
# Consider: empty lists, divide by zero
def aveElem(arr):
  if(len(arr) <= 0):
    return 0
    
  total = 0
  for i in range(len(arr)):
    total += arr[i]
  return total/len(arr)

#---------------------------------------------------------------fullName
# Generate full name when you provide first and last name as inputs
# Use 3 unit tests
def fullName(first, last):
  name = ("{} {}".format(first, last))
  return str(name)