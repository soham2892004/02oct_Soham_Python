print("hello world")

range_start = int(input("Enter the starting range: "))
range_end = int(input("Enter the ending range: "))


fib_series = [0, 1]


for i in range(2, range_end + 1):
  fib_series.append(fib_series[i - 1] + fib_series[i - 2])


result = fib_series[range_start:range_end + 1]


print("The Fibonacci series within the given range is:", result)