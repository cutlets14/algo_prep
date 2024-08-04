## Recursive factorial

def recursive_factorial(n):
    # Base case
    if n == 1:
        return 1
    else: 
        # Recursively compute the factorial
        return n * recursive_factorial(n-1)

def main():
    recursive_factorial(10)

if __name__ == "__main__":
    main()