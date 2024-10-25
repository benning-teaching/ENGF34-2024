# Using return
def return_example():
    return [1, 2, 3] #The function ends here

# Using yield
def yield_example():
    yield 1 #The function does not end here
    yield 2
    yield 3

# Subfunction using yield
def subgenerator():
    yield 'a'
    yield 'b'
    yield 'c'

# Using yield from with a subfunction
def yield_from_example():
    yield 1
    yield from subgenerator() #This yields from the subfunction
    yield 2

if __name__ == "__main__":
    # Using return
    print("Using return:")
    result = return_example()
    print(result)  # Output: [1, 2, 3]

    # Using yield
    print("\nUsing yield:")
    for value in yield_example():
        print(value)  # Output: 1 2 3

    # Using yield from with a subfunction
    print("\nUsing yield from:")
    for value in yield_from_example():
        print(value)  # Output: 1 a b c 2