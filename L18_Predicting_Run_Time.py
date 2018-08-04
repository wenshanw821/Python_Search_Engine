import time

def time_execution(code):
    start = time.perf_counter()
    result = eval(code)
    run_time = time.perf_counter() - start

    # print(result)
    return result, run_time

def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1
    # return i


print(time_execution('spin_loop(10 ** 8)')[1])
