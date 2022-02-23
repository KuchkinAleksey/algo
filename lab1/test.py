import unittest
from lab1.linkedlist import SinglyLinkedList as SLL

class TestSinglyLinkedList(unittest.TestCase):
  def test_linked_list_prepend(self):
    sll = SLL()
    sll.prepend('B')
    sll.prepend('A')
    self.assertEqual(sll.to_str(), "A --> B")

  def test_linked_list_append(self):
    sll = SLL()
    sll.append('A')
    sll.append('B')
    self.assertEqual(sll.to_str(), "A --> B")

  def test_linked_list_arr(self):
    sll = SLL()
    sll.from_arr(['A','B','C'])
    self.assertEqual(str(sll.to_arr()), "['A', 'B', 'C']")

  def test_linked_list_delete(self):
    sll = SLL()
    sll.from_arr(['A','A','B','C','C','D'])
    head_node = sll.delete_head()
    tail_node = sll.delete_tail()
    # A --> B --> C --> C, last C idx = 3
    c_idx, c_node = sll.delete('C')
    none_idx, none_node = sll.delete('X')
    self.assertEqual(sll.to_str(), "A --> B")
    self.assertEqual(head_node.to_str(), "A")
    self.assertEqual(tail_node.to_str(), "D")
    self.assertEqual(f"{c_idx}: {c_node.to_str()}", "3: C")
    self.assertEqual(f"{none_idx}: {none_node.to_str()}", "-1: None")

  def test_linked_list_find(self):
    sll = SLL()
    sll.from_arr(['A','B','C','C']) # first C idx = 2
    c_idx, c_node = sll.find('C')
    none_idx, none_node = sll.find('X')
    self.assertEqual(f"{c_idx}: {c_node.to_str()}", "2: C")
    self.assertEqual(f"{none_idx}: {none_node.to_str()}", "-1: None")

  def test_linked_list_reverse(self):
    sll = SLL()
    sll.from_arr(['A','B','C'])
    sll.reverse()
    self.assertEqual(sll.to_str(), "C --> B --> A")

  def test_linked_list_format(self):
    fmt_node = lambda x: f"[{x}]" if x else "[]"
    fmt_list = lambda x: ",".join(x) if len(x) else "empty list"
    sll = SLL()
    self.assertEqual(sll.to_str(fmt_list), "empty list")
    sll.from_arr(['A','B','C'])
    self.assertEqual(sll.to_str(fmt_list), "A,B,C")
    self.assertEqual(sll.to_str(fmt_list,fmt_node), "[A],[B],[C]")

if __name__ == "__main__":
  unittest.main()