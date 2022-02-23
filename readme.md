<div align="center">

# algo & data structures

[Info](#info) •
[Lab1](#lab1)

</div>

## Info

<div align="right">

```
Aleksey Kuchkin
		LA-11mn
			 V1
	   		ICF
```

</div>

<div align="center">
Kyiv
KPI
2022
</div>

## Lab1

### Run

```
git clone https://github.com/KuchkinAleksey/algo.git
cd algo/
python -m unittest -v lab1/test.py
python lab1/demo.py
```

### Results

`python -m unittest -v lab1/test.py`

```
test_linked_list_append (lab1.test.TestSinglyLinkedList) ... ok
test_linked_list_arr (lab1.test.TestSinglyLinkedList) ... ok
test_linked_list_delete (lab1.test.TestSinglyLinkedList) ... ok
test_linked_list_find (lab1.test.TestSinglyLinkedList) ... ok
test_linked_list_format (lab1.test.TestSinglyLinkedList) ... ok
test_linked_list_prepend (lab1.test.TestSinglyLinkedList) ... ok
test_linked_list_reverse (lab1.test.TestSinglyLinkedList) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.007s

OK    
```

`python lab1/demo.py`

```
{}
default fmt:
   (-99, 99) --> (3, 4) --> (-1, 0) --> (1, 2) --> (3, 4)
set of complex numbers fmt:
   { (-99+99j), (3+4j), (-1+0j), (1+2j), (3+4j) }

to_arr:
   [(-99, 99), (3, 4), (-1, 0), (1, 2), (3, 4)]
from_arr:
   { (-99+99j), (3+4j), (-1+0j), (1+2j), (3+4j), (5+6j), (-1+7j), (-2+8j), (3+4j), (1+2j), (3+4j), (3+4j), (123-123j) }

node (-1+7j) at 6 pos
node not found EMPTY so idx is -1

head node (-99+99j) deleted:
   { (3+4j), (-1+0j), (1+2j), (3+4j), (5+6j), (-1+7j), (-2+8j), (3+4j), (1+2j), (3+4j), (3+4j), (123-123j) }
tail node (123-123j) deleted:
   { (3+4j), (-1+0j), (1+2j), (3+4j), (5+6j), (-1+7j), (-2+8j), (3+4j), (1+2j), (3+4j), (3+4j) }

all (3+4j) nodes deleted, last one was in position 10:
   { (-1+0j), (1+2j), (5+6j), (-1+7j), (-2+8j), (1+2j) }

reverse:
   { (1+2j), (-2+8j), (-1+7j), (5+6j), (1+2j), (-1+0j) }
reverse:
   { (-1+0j), (1+2j), (5+6j), (-1+7j), (-2+8j), (1+2j) }
```