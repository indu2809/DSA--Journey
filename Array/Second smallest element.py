a = [3, 5, 2, 9, 1]
smallest = float('inf')
second_smallest = float('inf')
for num in a:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num
print(second_smallest)
