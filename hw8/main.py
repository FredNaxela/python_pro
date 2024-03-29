# Task 1
def sum_func(args):
    if not isinstance(args, list):
        raise ValueError("Args must be a list")

    def mul_func(x):
        if not isinstance(x, int | float):
            raise ValueError("The list must contain only numbers")
        return x * 2

    return sum(mul_func(i) for i in args)

try:
    my_list = [4, 5, 6]
    print(sum_func(my_list))
except ValueError as e:
    print("Error:", e)


#Task 2
def save_file(file_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(file_name, 'w') as file:
                data = func(*args, **kwargs)
                file.write(f"Result: {str(data)}")
                return data
        return wrapper
    return decorator            
  
@save_file("mul_func.txt")        
def mul_func(x):
    if not isinstance(x, int | float):
        raise ValueError("Must be int or float")
    return x * 2

try:
    mul_func(3)
except ValueError as e:
    print("Error:", e)


#Task 3
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Function execution time: {(end - start):.5f}")
        return res
    return wrapper

@measure_time
def mul_func(x):
    time.sleep(2)
    if not isinstance(x, int | float):
        raise ValueError("Must be int or float")
    return x * 2

try:
    mul_func(4)
except ValueError as e:
    print("Error:", e)


#Task 4
def limit_calls(max_calls):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if wrapper.calls >= max_calls:
                raise ValueError("Max 3 function calls")
            wrapper.calls += 1
            return func(*args, **kwargs)
        wrapper.calls = 0
        return wrapper
    return decorator

@limit_calls(3)
def mul_func(x):
    if not isinstance(x, int | float):
        raise ValueError("Must be int or float")
    return x * 2

try:
    print(mul_func(4))
    print(mul_func(5))
    print(mul_func(6))
    print(mul_func(7))
except ValueError as e:
    print("Error:", e)


#Task 5
def cache_results(func):
    cash = {}
    def wrapper(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in cash:
            cash[key] = func(*args, **kwargs)
        return cash[key]
    return wrapper


@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Обчислюється
print(fibonacci(10))  # Використання кешу