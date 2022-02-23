class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

  def to_str(self, fmt=None):
    if fmt == None:
      fmt = lambda x: str(x) 
    return fmt(self.data)


class SinglyLinkedList:

  def __init__(self):
    self.head = None

  def __iter__(self):
    node = self.head
    while node != None:
      yield node
      node = node.next

  def prepend(self, data):
    self.head = Node(data, self.head)

  def append(self, data):
    try:
      *_, last_node = self.__iter__()
      last_node.next = Node(data)
    except:
      self.head = Node(data)

  def to_str(self, fmt_list=None, fmt_node=None):
    if fmt_list == None:
      fmt_list = lambda x: " --> ".join(x) if len(x) else "empty"
    fmt_nodes = [node.to_str(fmt_node) for node in self.__iter__()]
    return fmt_list(fmt_nodes)

  def to_arr(self):
    return [node.data for node in self.__iter__()]

  def from_arr(self, arr):
    if self.head:
      *_, last_node = self.__iter__()
    else:
      last_node = Node(None)
    for item in arr:
      last_node.next = Node(item)
      last_node = last_node.next
      if not self.head:
        self.head = last_node

  def delete_tail(self):
    try:
      *_, n1_node, _ = self.__iter__()
      res = n1_node.next
      n1_node.next = None
    except:
      if self.head:
        res = self.head
        self.head = None
      else:
        return Node(None)
    return res

  def delete_head(self):
    if self.head:
      res = self.head
      self.head = self.head.next 
      return res
    return Node(None)

  def find(self, data):
    for idx,node in enumerate(self.__iter__()):
      if node.data == data:
        return idx,node
    return -1, Node(None)

  def delete(self, data):
    last_ne = None
    head = None
    res = -1,Node(None)
    for idx,node in enumerate(self.__iter__()):
      if node.data != data:
        if not head:
          head = node
        if last_ne:
          last_ne.next = node
        last_ne = node
      else:
      	res = idx,node
    self.head = head
    last_ne.next = None
    return res

  def reverse(self):
    prev = None
    for node in self.__iter__():
      prev = Node(node.data, prev)
      node = None
    self.head = prev
