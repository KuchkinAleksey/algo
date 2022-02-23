from linkedlist import SinglyLinkedList as SLL

if __name__ == "__main__":

  fmt_node_complex = lambda x: f"({x[0]}{x[1]:+}j)" if x else "EMPTY"
  fmt_list_set = lambda x: "{ "+", ".join(x)+" }" if len(x) else "{}"


  sll = SLL()
  print(sll.to_str(fmt_list_set, fmt_node_complex))
  sll.append((1,2))
  sll.append((3,4))
  sll.prepend((-1,0))
  sll.prepend((3,4))
  sll.prepend((-99,99))

  print("default fmt:\n  ", sll.to_str())
  print("set of complex numbers fmt:\n  ", sll.to_str(fmt_list_set,
                                                      fmt_node_complex))


  print("\nto_arr:\n  ", sll.to_arr())
  sll.from_arr([(5,6),(-1,7),(-2,8),(3,4),(1,2),(3,4),(3,4),(123,-123)])
  print("from_arr:\n  ", sll.to_str(fmt_list_set,fmt_node_complex))


  idx, node = sll.find((-1,7))
  print(f"\nnode {node.to_str(fmt_node_complex)} at {idx} pos")
  idx, node = sll.find((-12,34))
  print(f"node not found {node.to_str(fmt_node_complex)} so idx is {idx}")


  node = sll.delete_head()
  print(f"\nhead node {node.to_str(fmt_node_complex)} deleted:\n  ",
        sll.to_str(fmt_list_set,fmt_node_complex))
  node = sll.delete_tail()
  print(f"tail node {node.to_str(fmt_node_complex)} deleted:\n  ",
        sll.to_str(fmt_list_set,fmt_node_complex))


  idx, node = sll.delete((3,4))
  print(f"\nall {node.to_str(fmt_node_complex)} nodes deleted, last one was",
        f"in position {idx}:\n  ", sll.to_str(fmt_list_set,fmt_node_complex))


  sll.reverse()
  print("\nreverse:\n  ", sll.to_str(fmt_list_set,fmt_node_complex))
  sll.reverse()
  print("reverse:\n  ", sll.to_str(fmt_list_set,fmt_node_complex))