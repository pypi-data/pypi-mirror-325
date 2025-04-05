import matplotlib.pyplot as plt

def showStack(arr):
    if not len(arr):
      print('showStack : This is an empty list.')
      return
      
    fig, node = plt.subplots(figsize=(2, len(arr)/2))
    node.text(0.5, len(arr)/2, 'Top', ha='center')
    for i, item in enumerate(arr._data):
        node.text(0.5, i/2, str(item), ha='center', bbox=dict(facecolor="white", boxstyle="round"))
    node.text(0.5, -0.5, 'Bottom', ha='center')
    node.set_ylim(-0.5, len(arr)/2)
    plt.axis('off')
    plt.show()

def showCircularQueue(arr):
    fig, node = plt.subplots(figsize=(len(arr._data),2))

    for i, item in enumerate(arr._data):
        varColor = 'black' # box color

        # front label
        if i == arr._front:
          varColor = 'royalblue'
          node.text(i, 0.25, 'Front', ha='center', color=varColor)

        # rear label
        if i == arr._rear and i == arr._front:
          varColor = 'indianred'
          node.text(i, 0.15, 'Rear', ha='center', color=varColor)
          varColor = 'black'
        elif i == arr._rear:
          varColor = 'indianred'
          node.text(i, 0.25, 'Rear', ha='center', color=varColor)

        # none
        if arr._data[i] == None:
          varColor = 'lightgray'

        # box element
        node.text(i, 0.5, str(item), ha='center', color=varColor, bbox=dict(facecolor="white", edgecolor=varColor, boxstyle="round"))

    node.set_xlim(0, len(arr._data))
    plt.axis('off')
    plt.show()

def showSinglyLinkedList(arr):
    def tableNode(color, name, next):
      table = node.table(cellText=[[name, next]] , 
                          cellLoc='center', 
                          colWidths=[3, 1], 
                          cellColours=[['white', color]],
                          bbox=[index/arr._count, 0.2, 0.75/arr._count, 0.4])

    if arr._head is None:
      print("showLinkedList : This is an empty list.")
      return
    else:  
      #setup
      fig, node = plt.subplots(figsize=(arr._count*1.25, 1))
      current = None
      index = 0

      #root node
      tableNode('lightblue', arr._count, '')
      node.annotate('', xytext=(index+0.65, 0.4) , xy=(index+1, 0.4),va='center', arrowprops=dict(arrowstyle='->'))
      current = arr._head
      index += 1

    #data node
    count = 0
    while current != None:
      count += 1
      if current._next != None:
        tableNode('pink', current._name, '')
        node.annotate('', xytext=(index+0.65, 0.4) , xy=(index+1, 0.4),va='center', arrowprops=dict(arrowstyle='->'))
      else:
        tableNode('pink', current._name, 'X')

      current = current._next
      index += 1

    node.set_xlim(0, arr._count)
    plt.axis('off')
    plt.show()

    if(count != arr._count):
      print(f"VisualDSA WARNING: Node count mismatch. Expected {arr._count}, found {count}.")
  

# Sorting -----------------------------------------------------------

def bubbleTableRow(arr,currentPos, sortedPos, isExchange, isHideArrow):
  fig, ax = plt.subplots(figsize=(len(arr)/2, 1))

  nextPos = currentPos-1
  faceColor = []
  edgeColor = []
  for i in range(len(arr)):
    if i == currentPos:
      faceColor.append('aliceblue')
      edgeColor.append('cornflowerblue')
    elif i <= sortedPos:
      faceColor.append('honeydew')
      edgeColor.append('darkseagreen')
    elif i == nextPos:
      faceColor.append('mistyrose')
      edgeColor.append('salmon')
    else:
      faceColor.append('white')
      edgeColor.append('lightgray')

  table = ax.table(cellText=[arr] ,
                          cellLoc='center',
                          cellColours=[faceColor],
                          bbox=[0, 0.5, 1, 0.5]
                     )

  for i in range(len(arr)):
    cell = table[(0, i)]  # Access cell at row=0, column=i
    cell.set_edgecolor(edgeColor[i])  # Set edge color

  # arrow compare
  if not isHideArrow:
    if isExchange:
      col = 'teal'
      sym = "⇄"
    else:
      col = 'indianred'
      sym = "⨯"

    ax.annotate('',
                    xytext=(currentPos+0.5, 0.5) ,
                    xy=(nextPos+0.5, 0.5),
                    ha="center",
                    va='bottom',
                    arrowprops=dict(arrowstyle="<->",
                                    connectionstyle="bar,fraction=-0.5",
                                    ec='k'
                                    ))

    ax.text(currentPos, 0.1, sym, ha="center", va="center", fontsize=14, color=col)

  ax.set_xlim(0, len(arr))
  ax.set_ylim(0, 1)

  plt.axis('off')
  plt.show()

def selectionTableRow(arr,currentPos, comparePos, sortedPos, minPos,isExchange, isHideArrow):
  fig, ax = plt.subplots(figsize=(len(arr)/2, 1))

  faceColor = []
  edgeColor = []
  for i in range(len(arr)):
    if i <= sortedPos:
      faceColor.append('honeydew')
      edgeColor.append('darkseagreen')
    elif i == currentPos:
      faceColor.append('aliceblue')
      edgeColor.append('cornflowerblue')
    elif i == comparePos:
      faceColor.append('mistyrose')
      edgeColor.append('salmon')
    else:
      faceColor.append('white')
      edgeColor.append('lightgray')

  table = ax.table(cellText=[arr] ,
                          cellLoc='center',
                          cellColours=[faceColor],
                          bbox=[0, 0.5, 1, 0.5]
                     )

  for i in range(len(arr)):
    cell = table[(0, i)]  # Access cell at row=0, column=i
    cell.set_edgecolor(edgeColor[i])  # Set edge color

  # arrow
  if not isHideArrow:
    if isExchange:
      col = 'teal'
      sym = "⇄"
      indent = (currentPos+comparePos)/2+0.5
    else:
      col = 'black'
      sym = "min"
      indent = minPos+0.5

    # calculate bar fraction
    cal = comparePos-currentPos
    if cal > 3:
      cal = 3.5
    connect = "bar,fraction="+str(1 / (2 ** cal ))

    #adjust gap if current == campare
    if currentPos == comparePos:
      currentPos -= 0.2
      comparePos += 0.2

    ax.annotate('',
                    xytext=(currentPos+0.5, 0.5) ,
                    xy=(comparePos+0.5, 0.5),
                    ha="center",
                    va='bottom',
                    arrowprops=dict(arrowstyle="<->",
                                    connectionstyle=connect,
                                    ec=col,
                                    ))

    ax.text(indent, 0.1, sym, ha="center", va="center", fontsize=10, color=col)

  ax.set_xlim(0, len(arr))
  ax.set_ylim(0, 1)

  plt.axis('off')
  plt.show()

def bubbleSort(alist):
    # print("Original list: ", alist, "\n")
    no_compare = 0
    no_exchange = 0

    n = len(alist)
    for round in range(0, n-1):
      print("Round ", round+1)

      for i in range(n-1, round, -1):

        no_compare += 1
        if alist[i-1] > alist[i]:
          bubbleTableRow(alist, i, round-1, True, False)  # visualize

          no_exchange += 1
          buff = alist[i-1]
          alist[i-1] = alist[i]
          alist[i] = buff
        else:
          bubbleTableRow(alist, i, round-1, False, False) # visualize

      # print("Current list: ", alist, "\n")
      bubbleTableRow(alist, -1, round, False, True)       # visualize

    print("Result")
    bubbleTableRow(alist, -1, n, False, True)       # visualize
    # print("Number of Comparisons: ", no_compare)
    # print("Number of Exchanges: ", no_exchange)

def selectionSort(alist):
    # print("Original list: ", alist, "\n")
    no_compare = 0
    no_exchange = 0

    n = len(alist)
    for round in range(n-1):
      print('Round ', round+1)
      # print('Position to insert: ', round)

      min = round
      for i in range(round+1,n):
        no_compare += 1
        curr = min
        comp = i
        if alist[i] < alist[min]:
          min = i

        # print(curr, comp, min)
        selectionTableRow(alist,curr,comp,round-1,min,False,False)

      #exchange
      selectionTableRow(alist,round,min,round-1,min,True,False)

      buff = alist[round]
      alist[round] = alist[min]
      alist[min] = buff

      no_exchange += 1
      
      # print('Position of min value: ', min)
      # print("Current list: ", alist, "\n")
      selectionTableRow(alist,-1,-1,round,-1,False,True)

    print("Result")
    selectionTableRow(alist,-1,-1,n,-1,False,True)

    # print("Number of Comparisons: ", no_compare)
    # print("Number of Exchanges: ", no_exchange)

def insertionSort(alist):

    #my version
    # print("Original list: ", alist, "\n")
    no_compare = 0
    no_exchange = 0

    n = len(alist)
    for round in range(1, n):
      print('Round ', round)
      pos = round
      num = alist[pos]
      
      while pos != 0 and num < alist[pos-1]:
        bubbleTableRow(alist, pos, round, True, False)

        swap = alist[pos-1]
        alist[pos] = swap
        alist[pos-1] = num

        no_compare += 1
        no_exchange += 1
        pos -= 1

      # stop by num > alist[pos-1]
      if pos != 0:
        bubbleTableRow(alist, pos, round, False, False)
        no_compare += 1

      bubbleTableRow(alist, -1, round, False, True)

    print('Result')
    bubbleTableRow(alist, -1, n, False, True) 
    # print("Number of Comparisons: ", no_compare)
    # print("Number of Exchanges: ", no_exchange)

class DataNode:
  def __init__(self, name, next):
    self._name = name     # The value stored within the node
    self._next = next     # A reference to the next node in the list (None if it's the last node)

class SinglyLinkedList():
  def __init__(self):
    self._count = 0       # The number of nodes in the list
    self._head = None     # A reference to the first node of the list 

  # ... (class methods)

# Sample linked list data
my_list = SinglyLinkedList()
my_node1 = DataNode("John", None)
my_node2 = DataNode("Adam", my_node1)
my_list._head = my_node2
my_list._count += 1

# Visualize the linked list
showSinglyLinkedList(my_list)