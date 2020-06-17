'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    # Your code here
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    elif cache and cache[n]:
        return cache[n]
    else:
        if cache is None:
            cache = {}
        result = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
        cache[n] = result
        return result

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
