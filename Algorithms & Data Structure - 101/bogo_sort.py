import random
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def is_sorted(values):
  for index in range(len(values) - 1):
    if values[index] > values[index + 1]:
      return False
  return True

def bogo_sort(values):
  """
  Is a random algorithm that can take much time to sort a small list.
  For example a list of 8 numbers took over 13000 attempts to get sorted.
  For a medium list it could not even get sorted for hours.
  """
  attempts = 0
  while not is_sorted(values):
    print(attempts)
    random.shuffle(values)
    attempts += 1
  return values

print(bogo_sort(numbers))