def factorial(n):
    """
    Calculate the factorial of a number recursively.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n (n!)
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_iterative(n):
    """
    Calculate the factorial of a number iteratively.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n (n!)
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
if __name__ == "__main__":
    num = 5
    print(f"The factorial of {num} is: {factorial(num)}")
    print(f"The factorial of {num} using iterative method is: {factorial_iterative(num)}")
    
    # Testing with a few more numbers
    for test_num in range(6, 11):
        print(f"{test_num}! = {factorial(test_num)}")
