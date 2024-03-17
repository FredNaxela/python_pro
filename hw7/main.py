from datetime import timedelta, datetime

#Task 1
def progression(f, r, n):
    for _ in range(n):
        yield f
        f *= r
        
for i in progression (2, 2, 5):
    print(i)


#Task 2
def my_range(*args):
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args
    if step == 0:
        raise ValueError("Step must not be zero")
    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step

for i in my_range(1, 10, 2):
    print(i)


#Task 3
def prime(n):
    for num in range(2, n + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else: 
            yield num

for i in prime(20):
    print(i)


#Task 4
n = int(input("Enter n: "))
cubes_list = (i**3 for i in range(2, n+1))
print(list(cubes_list))


#Task 5
def fibonacci(n):
    p1, p2 = 0, 1
    for _ in range(n):
        p1, p2 = p2, p1 + p2
        yield p1
        
for i in fibonacci(10):
    print(i)


#Task 6
def date_range(start_date, end_date):
    while start_date <= end_date:
        yield start_date
        start_date += timedelta(days=1)

start_date = datetime(2024, 3, 1)
end_date = datetime(2024, 3, 10)

for item in date_range(start_date, end_date):
    print(item.date())