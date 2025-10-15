import time

def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"function {func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper



@decorator

def example_function(n):
    print( f"the sum is  {sum(range(n))}")


example_function(100000000)
