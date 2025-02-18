# def most_frequent(lst):
#     return  max(set(lst), key=lst.count)

# print(most_frequent([1, 3, 3, 2, 1, 3, 2, 2, 2, 2]))  # Output: 2 >>o(n^2)

def most_frequent(lst):
    freq_map = {}  # Dictionary to store frequency counts

    # Count occurrences
    for num in lst:
        freq_map[num] = freq_map.get(num, 0) + 1  # Increment count

    # Find the most frequent number
    most_common = max(freq_map, key=freq_map.get)  # Get key with max value
    return most_common, freq_map[most_common]  # Return the number and its count

# Example usage
print(most_frequent([1, 3, 3, 2, 1, 3, 2, 2, 2, 2]))  



# def mostFrequent(num):

#     num_store = []
#     counter = 0

#     num = list(num)

#     for n in num:
#         if n not in num_store:
#             num_store.append(n)
#         else:
#             counter += 1

#     return counter 

# print(mostFrequent([1,2,1,3,4,4,1,1,1,1,1,4,4,4,4,4,4,4]))
