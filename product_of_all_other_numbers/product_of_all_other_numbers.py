import numpy
'''
Input: a List of integers
Returns: a List of integers
'''
# def product_of_all_other_numbers(arr):
#     # Your code here
#     new_array = []
#     for i in range(len(arr)):
#         if i == 0:
#             prod = numpy.prod(arr[i + 1:])
#             new_array.append(int(prod))
#         else:
#             product = numpy.prod(arr[:i]) * numpy.prod(arr[i + 1:])
#             new_array.append(int(product))
#     return new_array

# Product that doesnt use numpy
def product_of_all_other_numbers(arr):
    new_arr = []
    for i in range(len(arr)):
        copy_arr = arr.copy()
        copy_arr[i] = 1
        total = 1
        for num in copy_arr:
            total = total * num
        
        new_arr.append(total)
    
    return new_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
