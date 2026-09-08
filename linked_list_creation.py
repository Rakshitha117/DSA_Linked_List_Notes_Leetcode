"""
============================================================
        FINDING THE MIDDLE NODE OF A LINKED LIST
============================================================

Linked List Example:

    10 → 20 → 30 → 40 → 50 → None

A linked list consists of Nodes.

Each Node contains:
    1. data  -> stores the value
    2. next  -> stores a reference to the next Node

Example Node:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


HEAD:
    - 'head' stores a reference to the first node.
    - It normally remains at the beginning of the list.

TAIL:
    - 'tail' stores a reference to the last node.
    - When a new node is added, tail moves to the new node.

NEW NODE:
    - new_node = Node(value)
    - Creates a new Node object and stores its reference in
      the variable 'new_node'.

CONNECTING NODES:
    - tail.next = new_node
    - The 'next' attribute of the current last node is updated
      to point/reference to the new node.

    Example:

        tail → [10 | next] → [20 | None]


============================================================
APPROACH 1: BRUTE FORCE
============================================================

Idea:

    1. Traverse the complete linked list and count the nodes.
    2. Calculate the middle index using:

           middleIndex = count // 2

    3. Start again from head.
    4. Move to the middle index.
    5. Return the middle node.

Example:

    Linked List:
        10 → 20 → 30 → 40 → 50

    Number of nodes = 5

    Middle index:
        5 // 2 = 2

    Index:
        10    20    30    40    50
         0     1     2     3     4
                     ↑
                   middle

    Result:
        30

Time Complexity:
    O(n)

Space Complexity:
    O(1)

Note:
    The list is traversed twice:
        1. Once to count the nodes.
        2. Once to reach the middle node.


============================================================
APPROACH 2: HARE / SLOW AND FAST POINTER
============================================================

Idea:

    Use two pointers:

        slow → moves one node at a time
        fast → moves two nodes at a time

    Both start from head:

        slow = head
        fast = head

    During every iteration:

        slow = slow.next
        fast = fast.next.next

    When fast reaches the end of the linked list,
    slow will be pointing to the middle node.

Example:

    10 → 20 → 30 → 40 → 50

    Initially:

        slow
         ↓
        10 → 20 → 30 → 40 → 50
         ↑
        fast

    After first iteration:

             slow
              ↓
        10 → 20 → 30 → 40 → 50
                    ↑
                   fast

    After second iteration:

                    slow
                     ↓
        10 → 20 → 30 → 40 → 50
                              ↑
                             fast

    fast reaches the end, so slow points to:

        30

Time Complexity:
    O(n)

Space Complexity:
    O(1)

Advantage:
    Only one traversal is required.


============================================================
IMPORTANT PYTHON CONCEPT
============================================================

When we write:

    currentNode = head

    while currentNode is not None:
        currentNode = currentNode.next

'currentNode' is a reference to a Node object.

'currentNode.next' accesses the next attribute of that Node.

Do NOT confuse:

    currentNode
        -> reference to the current Node

    currentNode.next
        -> reference to the next Node


Example:

    currentNode
         ↓
       [10 | next] → [20 | next] → [30 | None]


After:

    currentNode = currentNode.next

we get:

       [10] → currentNode → [20] → [30]
                    ↑


IMPORTANT:
    If currentNode becomes None, the loop must stop.

    Therefore:

        while currentNode is not None:

    is used when currentNode is the pointer being moved.


============================================================
HEAD vs TAIL
============================================================

When the list is empty:

    head = None
    tail = None

After creating the first node:

    head = new_node
    tail = new_node

Both point to the same node because the first node is
both the beginning and the end of the list.

    head
     ↓
    [10 | None]
     ↑
    tail

After adding more nodes:

    head                         tail
     ↓                            ↓
    [10] → [20] → [30] → [40] → [50] → None

    head stays at the first node.
    tail moves to the last node.


============================================================
KEY DSA TAKEAWAY
============================================================

A linked list is basically a collection of Node objects
connected using the 'next' reference.

    Node → Node → Node → None

The most important operations are:

    Node(value)
        → creates a new node

    node.data
        → gets the value

    node.next
        → gets the reference to the next node

    node.next = another_node
        → connects two nodes

    current = current.next
        → moves the pointer to the next node

For finding the middle:

    Brute Force:
        Count → Calculate middle → Traverse again

    Hare Method:
        slow = 1 step
        fast = 2 steps

============================================================
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def create_linked_list(values):
    head=None
    tail=None

    for value in values:
        new_node=Node(value)

        if head is None:
            head=new_node
            tail=new_node
        else:
            tail.next=new_node
            tail=new_node
    return head

def printing_linked_list(head):
    current=head
    while current is not None:
        print(current.data,end="=>")
        current=current.next
    print("None")

####finding the middel of the linkedList using the brute Force
def middle_node_bruteForce(head):
    count=0
    currentNode=head
    while currentNode is not None:
        count+=1
        currentNode=currentNode.next
    middleIndex=count//2
    current=head
    for i in range(middleIndex):
        current=current.next
    return current


### finding middle node using Hare/slow-fast

def middle_node_Hare(head):
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next

    return slow

# 1. Create the linked list
head = create_linked_list([10, 20, 30, 40, 50])
printing_linked_list(head)

middle_Node_value_brute=middle_node_bruteForce(head)
print("Middle node value using brute",middle_Node_value_brute.data)

middle_node_value_hare=middle_node_Hare(head)
print("Middle Vlaue using Hare:",middle_node_value_hare.data)