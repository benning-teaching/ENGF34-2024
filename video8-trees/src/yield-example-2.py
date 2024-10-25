import time

# Using return
def return_example():
    result = []
    for i in range(1, 4):
        time.sleep(1)  # Simulate a time-consuming operation
        result.append(i)
    return result

# Using yield
def yield_example():
    for i in range(1, 4):
        time.sleep(1)  # Simulate a time-consuming operation
        yield i

if __name__ == "__main__":
    # Using return
    print("Using return:")
    start_time = time.time()
    result = return_example()
    end_time = time.time()
    print(result)  # Output: [1, 2, 3]
    print(f"Time taken with return: {end_time - start_time:.2f} seconds")

    # Using yield
    print("\nUsing yield:")
    start_time = time.time()
    for value in yield_example():
        print(value)  # Output: 1 2 3
    end_time = time.time()
    print(f"Time taken with yield: {end_time - start_time:.2f} seconds")