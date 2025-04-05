
This Python library provides functions for visualizing various data structures, including linked lists, queue, stack, and more. It utilizes Matplotlib for creating interactive and informative visualizations.

This library was developed for the Data Structures and Algorithms course at King Mongkut's Institute of Technology Ladkrabang (KMITL) to enhance student understanding of these fundamental concepts.
## Table of Contents  
Data Visualization
- [Stack](#stack)
- [Queue](#Queue)
- [Singly Linked List](#Singly-Linked-List) 


Sorting Visualization
- [Bubble Sort](#Bubble-Sort) 
- [Selection Sort](#Selection-Sort) 
- [Insertion Sort](#Insertion-Sort) 
## Installation

Install using pip

```bash
pip install visualdsa
```
    


## Stack
#### Context
- A stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle.
- Imagine a stack of plates – you can only add or remove plates from the top of the stack.


#### Sample stack class
```python
class ArrayStack:
  def __init__(self):
    self._data = []

  def __len__(self):
    return len(self._data)
  
  # ... (class methods)
```

#### Visualization
```python
import visualdsa as vd

# Sample stack data
my_stack = ArrayStack()
my_stack._data = [3, 2, 1]

# Visualize the stack
vd.showStack(my_stack)
```
![](https://img2.pic.in.th/pic/Unknown-8-2.png)

## Queue
#### Context
- A circular queue is a linear data structure that follows the First-In, First-Out (FIFO) principle, like a regular queue, but with a circular arrangement.
- The last element of the queue is logically connected to the first element, creating a circular structure. This efficient use of space by avoiding wasted memory at the beginning of the array.
- There are 2 pointers, front and rear, track the positions of the first and last elements in the queue, respectively.
#### Sample circular queue class
```python
class ArrayQueue:
  def __init__(self):
    self._data = [None] * 5   # A list to store the queue elements with capacity of 5
    self._front = 0           # The index of the front of the queue
    self._rear = 0            # he index of the rear of the queue

  def __len__(self):
    return len(self._data)
  
  # ... (class methods)

```

#### Visualization
```python
import visualdsa as vd

# Sample queue data
my_queue = ArrayQueue()
my_queue._data = [3, 2, 1, None, None]
my_queue._front = 0
my_queue._rear = 2

# Visualize the queue
vd.showQueue(my_queue)
```
![](https://img2.pic.in.th/pic/Unknown-9-2.png)

## Singly Linked List
#### Context
- A singly linked list is a linear data structure where each element (node) points to the next element in the sequence.

#### Sample singly linked list class
```python
class DataNode:
  def __init__(self, name, next):
    self._name = name     # The value stored within the node
    self._next = next     # A reference to the next node in the list (None if it's the last node)

class SinglyLinkedList():
  def __init__(self):
    self._count = 0       # The number of nodes in the list
    self._head = None     # A reference to the first node of the list 

  # ... (class methods)

```

#### Visualization
```python
import visualdsa as vd

# Sample linked list data
my_list = SinglyLinkedList()
my_node1 = DataNode("John", None)
my_node2 = DataNode("Adam", my_node1)
my_list._head = my_node2
my_list._count += 2

# Visualize the linked list
vd.showSinglyLinkedList(my_list)
```
![](https://img5.pic.in.th/file/secure-sv1/Unknown-10-2.png)

## Bubble Sort
#### Context
- Compares adjacent elements and swaps them if they are in the wrong order.
- Repeatedly passes through the list until no swaps1 occur in a pass.

#### Visualization
```python
import visualdsa as vd

arr = [12, 90, 53, 63]
vd.bubbleSort(arr)
```

![](https://img5.pic.in.th/file/secure-sv1/bubleac1d0a5ce51496f1.png)


## Selection Sort
#### Context
- Finds the minimum element in the unsorted portion of the list and places it at the beginning.
- Repeats this process until the entire list is sorted.

#### Visualization
```python
import visualdsa as vd

arr = [12, 90, 53, 63]
vd.selectionSort(arr)
```

![](https://img5.pic.in.th/file/secure-sv1/selection45f61e7a5eea5d99.png)


## Insertion Sort
#### Context
- Builds the sorted array one element at a time.
- Inserts each element into its correct position within the already sorted portion of the array.

#### Visualization
```python
import visualdsa as vd

arr = [12, 90, 53, 63]
vd.insertionSort(arr)
```

![](https://img2.pic.in.th/pic/insertion408de62f7f106725.png)