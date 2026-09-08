def fibonacci_recursive(n):
    print(n)
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Example: print the first 10 terms

print(fibonacci_recursive(5), end=" ")
