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

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None 

def traverseLL(head):

    while head is not None:

        print(head.data, end = " ")

        head = head.next

    print()


# Driver code
def main():

    # Create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    # Example of traversing the node and printing

    traverseLL(head)


if __name__ == "__main__":
    main()

        