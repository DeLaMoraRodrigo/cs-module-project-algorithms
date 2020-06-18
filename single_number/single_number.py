'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    lone_number = []
    for i in range(len(arr)):
        if lone_number.__contains__(arr[i]):
            lone_number.remove(arr[i])
        else:
            lone_number.append(arr[i])
    return lone_number[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")