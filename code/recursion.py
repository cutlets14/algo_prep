# ## Recursive Santa
# houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house", "Satvik's house"]

# def deliver_presents_iteratively():
#     for house in houses:
#         print(f"Delivering presents to: {house}.")

# def deliver_presents_recursively(houses):
#     # Worker elf doing his work
#     if len(houses) == 1:
#         house = houses[0]
#         print(f"Delivering presents to: {house}.")
#     else:
#         # Splitting the work
#         # Using // to split the houses implicitly takes care of non-even number of houses
#         midpoint = len(houses) // 2
#         first_array = houses[:midpoint]
#         second_array = houses[midpoint:]

#         # Deliver presents recursively for each array
#         deliver_presents_recursively(first_array)
#         deliver_presents_recursively(second_array)


# def main():
#     # deliver_presents_iteratively()
#     deliver_presents_recursively(houses)

# if __name__ == "__main__":
#     main()

# def factorial(n):
#     # Base case
#     if n == 1:
#         return 1

#     # return condition
#     return n * factorial(n-1)

# print(factorial(6))

# def iter_factorial(n):
#     # Initialize the product
#     product = 1

#     while n > 0:
#         product *= n
#         n -= 1
    
#     return product

# print(iter_factorial(6))

# Print numbers from 1 to 10 recursively
# def ptn(n):
#     if n != 1:
#         ptn(n-1)
#     print(n)

def countup(n):
    if n > 0:
        countup(n-1)
        print(n)



# Print numbers from 1 to 10 iteratively
# def print_from_to(n, N):
#     while n <= N:
#         print(n)
#         n += 1

# print_from_to(1, 10)
# ptn(10)
        
countup(3)