import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def selection_sort(values):
  """
  Better than bogo sort but still takes a long time for big values.
  A test with a list with 10000 values takes ~6s 
  Another test with a list with 1000000 values doesn`t even complete.
  O(n^2) run time
  """
  sorted_list = []
  print("%-25s %-25s" % (values, sorted_list))
  for i in range(0, len(values)):
    index_to_move = index_of_min(values)
    sorted_list.append(values.pop(index_to_move))
    print("%-25s %-25s" % (values, sorted_list))
  return sorted_list

def index_of_min(values):
  min_index = 0
  for i in range(1, len(values)):
    if values[i] < values[min_index]:
      min_index = i
  return min_index

print(selection_sort(numbers))