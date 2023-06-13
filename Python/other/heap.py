import heapq

list = [6, 7, 9, 4, 3, 5, 8, 10, 1]

heapq.heapify(list)

print(list)

# print 3 largest numbers
print(heapq.nlargest(3, list))

# print 3 smallest numbers
print(heapq.nsmallest(3, list))

heapq.heappush(list, 6)

# Print the updated heap
print("Heap after push:", list)

# Remove and return the smallest element from the heap
smallest = heapq.heappop(list)

# Print the smallest element and the updated heap
print("Smallest element:", smallest)


