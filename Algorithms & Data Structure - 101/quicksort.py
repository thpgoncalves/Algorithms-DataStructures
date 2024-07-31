def quicksort(values):
  """
  In best case the run time is O(log n) - Using the pivote as a random pick
  In the worst case the run time is O(n^2)
  """
  if len(values) <= 1:
    return values
  less_than_pivot = []
  greater_than_pivot = []
  pivot = values[0]
  for value in values[1:]:
    if value <= pivot:
      less_than_pivot.append(value)
    else:
      greater_than_pivot.append(value)
  print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
  return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

numbers = [78, 94, 23, 56, 1, 5, 0 , -4, 1043]
print(numbers)
sorted_numbers = quicksort(numbers)
print(sorted_numbers)