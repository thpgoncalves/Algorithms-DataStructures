"""
- in liked list we call a node where the value/object is `saved`.
- the first node we call it the Head and the las we call the Tail.
- each node has 2 pieces of information, the item that we want to store and the reference to the next node on the list. 
- 
"""

class Node:
  """
  An object for storing a single node of a linked list.
  Models two attributes - data and the link to the next node in the list.
  """

  data = None
  next_node = None

  def __init__(self, data) -> None:
    self.data = data

  def __repr__(self) -> str:
    return "<Node data: %s>" % self.data
  
class LinkedList:
  """
  Singly linked list
  """

  def __init__(self) -> None:
    self.head = None

  def is_empty(self):
    return self.head == None
  
  def size(self):
    """
    Returns the number of nodes in the list.
    Takes O(n) run time
    """
    current = self.head
    count = 0 

    while current != None:
      count += 1
      current = current.next_node

    return count
  
  def add(self, data):
    """
    Adds a new node containing data at the head of the list.
    Takes O(1) run time - constant
    """
    new_node = Node(data)
    new_node.next_node = self.head
    self.head = new_node

  def search(self, key):
    """
    Serch for the first node containing data that matches the key.
    Returns the node or `None` if not found
    Takes O(n) - linear time
    """
    current = self.head

    while current != None:
      if current.data == key:
        return current
      else:
        current = current.next_node
    return None     

  def insert(self, data, index):
    """
    Insert a new Node containing data at index position
    Insertion takes constant O(1) time, but finding the node at the
    insertion point takes linear O(n) time 

    Takes overall O(n) runtime
    """

    if index == 0:
      self.add(data)
    
    if index > 0:
      new = Node(data)
      position = index
      current = self.head

      while position > 1:
        current = Node.next_node
        position -= 1

      prev_node = current
      next_node = current.next_node

      prev_node.next_node = new
      new.next_node = next_node

  def remove(self, key):
    """
    Removes Node containing data that matches the key
    Returns the node or None if key doesn`t exist
    Takes O(n) run time
    """
    current = self.head
    previous = None
    found = False

    while current != None and not found:
      if current.data == key and current == self.head:
        found = True
        self.head = current.next_node
      elif current.data == key:
        found = True
        previous.next_node = current.next_node
      else: 
        previous = current
        current = current.next_node
    
    return current
  
  def node_at_index(self, index):
    if index == 0:
      return self.head
    else:
      current = self.head
      position = 0

      while position < index:
        current = current.next_node
        position += 1

      return current    

  def __repr__(self) -> str:
    """
    Return a string representation of the list
    Takes O(n) run time - linear
    """
    nodes = []
    current = self.head

    while current != None:
      if current is self.head:
        nodes.append("[Head: %s]" % current.data)
      elif current.next_node is None:
        nodes.append("[Tail: %s]" % current.data)
      else:
        nodes.append("[%s]" % current.data)

      current = current.next_node
    return '->'.join(nodes)