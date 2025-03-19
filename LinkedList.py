# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None 

# def traverseLL(head):

#     while head is not None:

#         print(head.data, end = " ")

#         head = head.next

#     print()


# # Driver code
# def main():

#     # Create a hard-coded linked list:
#     # 10 -> 20 -> 30 -> 40
#     head = Node(10)
#     head.next = Node(20)
#     head.next.next = Node(30)
#     head.next.next.next = Node(40)

#     # Example of traversing the node and printing

#     traverseLL(head)


# if __name__ == "__main__":
#     main()

#################################################################

# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def search_key(head, key):

#     length = 0

#     curr = head 

#     while curr is not None:

#         if curr.data == key:
#             return True
        
#         length += 1

#         curr = curr.next


#     return False

# # Driver code
# if __name__ == "__main__":

#     # Create a hard-coded linked list:
#     # 14 -> 21 -> 13 -> 30 -> 10
#     head = Node(14)
#     head.next = Node(21)
#     head.next.next = Node(13)
#     head.next.next.next = Node(30)
#     head.next.next.next.next = Node(10)

#     # Key to search in the linked list
#     key = 17

#     if search_key(head, key):
#         print("Yes")
#     else:
#         print("No")

#################################################

# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None 

# def countLL(head):

#     length = 0

#     curr = head

#     while curr is not None:

#         curr = curr.next
#         length += 1

#     return length


# # Driver code
# def main():

#     # Create a hard-coded linked list:
#     # 10 -> 20 -> 30 -> 40
#     head = Node(10)
#     head.next = Node(20)
#     head.next.next = Node(30)
#     head.next.next.next = Node(40)

#     # Example of traversing the node and printing

#     print(countLL(head))


# if __name__ == "__main__":
#     main()

##########

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_start(head, new_data):

    #creating a new node with the given data 
    new_node = Node(new_data)

    # new_node.next = head #make the next of the new node point to the current head 

    return new_node

def print_list(head):

    curr = head

    while curr is not None:

        print(f"{curr.data}", end=  " ")

        curr = curr.next


    print()

# Driver code to test the functions
if __name__ == "__main__":
    # Create the linked list 2->3->4->5
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)

    # Print the original list
    print("Original Linked List:", end="")
    print_list(head)

    # Insert a new node at the front of the list
    print("After inserting Nodes at the front:", end="")
    data = 1
    head = insert_at_start(head, data)

    # Print the updated list
    print_list(head)





        

        