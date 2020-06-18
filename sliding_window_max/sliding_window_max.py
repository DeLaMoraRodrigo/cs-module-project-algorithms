from collections import deque
'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# def sliding_window_max(nums, k):
#     if len(nums) == 0:
#         return []
#     max_arr = []
#     for i in range(len(nums) - k + 1):
#         window = nums[i: i + k]
#         max_arr.append(max(window))

#     return max_arr

def sliding_window_max(nums, k):
    n = len(nums)
    Qi = deque()
    max_arr = []

    for i in range(k):
        while Qi and nums[i] >= nums[Qi[-1]]:
            Qi.pop()
        
        Qi.append(i)
    
    for i in range(k, n):
        max_arr.append(nums[Qi[0]])

        while Qi and Qi[0] <= i - k:
            Qi.popleft()
        
        while Qi and nums[i] >= nums[Qi[-1]]:
            Qi.pop()
        
        Qi.append(i)
    
    max_arr.append(nums[Qi[0]])

    return max_arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
