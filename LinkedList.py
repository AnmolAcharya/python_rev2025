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


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# # Given the head of a list and an int, appends
# # a new node at the end and returns the head.
# def append(head, new_data):

#     # Create a new node
#     new_node = Node(new_data)

#     # If the Linked List is empty, make the 
#     # new node as the head and return
#     if head is None:
#         return new_node

#     # Store the head reference in a temporary variable
#     last = head

#     # Traverse till the last node
#     while last.next:
#         last = last.next

#     # Change the next pointer of the last 
#     # node to point to the new node
#     last.next = new_node

#     # Return the head of the list
#     return head


# # This function prints the contents of the 
# # linked list starting from the head
# def print_list(node):

#     while node:
#         print(node.data, end=" ")
#         node = node.next


# # Driver code
# if __name__ == "__main__":

#     # Create a hard-coded linked list: 
#     # 2 -> 3 -> 4 -> 5 -> 6
#     head = Node(2)
#     head.next = Node(3)
#     head.next.next = Node(4)
#     head.next.next.next = Node(5)
#     head.next.next.next.next = Node(6)

#     print("Created Linked list is: ", end="")
#     print_list(head)

#     # Example of appending a node at the end
#     head = append(head, 1)

#     print("\nAfter inserting 1 at the end: ", end="")
#     print_list(head)

#########################################################

# # Node class representing a single element in the linked list
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # Function to insert a new node at a specific position
# def insert_at_position(head, new_data, position):
#     # Create a new node with the given data
#     new_node = Node(new_data)

#     # If inserting at the beginning (position 0)
#     if position == 0:
#         new_node.next = head
#         return new_node  # The new node becomes the head

#     # Start traversal from head
#     current = head
#     count = 0

#     # Traverse to the node before the desired position
#     while current is not None and count < position - 1:
#         current = current.next
#         count += 1

#     # If the position is greater than the length of the list, return head (invalid position)
#     if current is None:
#         print("Position out of bounds")
#         return head

#     # Insert the new node in between
#     new_node.next = current.next
#     current.next = new_node

#     return head

# # Function to print the linked list
# def print_list(node):
#     while node:
#         print(node.data, end=" -> ")
#         node = node.next
#     print("None")  # Indicating end of the list

# # Driver code
# if __name__ == "__main__":
#     # Creating a linked list: 2 -> 3 -> 4 -> 5 -> 6
#     head = Node(2)
#     head.next = Node(3)
#     head.next.next = Node(4)
#     head.next.next.next = Node(5)
#     head.next.next.next.next = Node(6)

#     print("Original Linked List:")
#     print_list(head)

#     # Insert a node with value 1 at position 3 (between 4 and 5)
#     head = insert_at_position(head, 1, 3)

#     print("After inserting 1 at position 3:")
#     print_list(head)

#     # Insert at the beginning (position 0)
#     head = insert_at_position(head, 9, 0)

#     print("After inserting 9 at the beginning:")
#     print_list(head)

#     # Insert at an invalid position
#     head = insert_at_position(head, 99, 10)  # Should print "Position out of bounds"



#############Reversing a linked list##########

# prev = None
# curr = head
# next_node = None 

# while curr:
#     next_node = curr.next
#     curr.next = prev 
#     prev = curr 
#     curr = next_node 

# return prev  

################################################

#Technique of solving leetcode problems -> 
#Slow and Fast Pointers

