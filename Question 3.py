import math
import time
from concurrent.futures import ThreadPoolExecutor

def factorial_part(start, end):
    result = 1
    for i in range(start, end):
        result *= i
    return result

def threaded_factorial(n, num_threads):
    chunk_size = n // num_threads
    ranges = [(i * chunk_size + 1, (i + 1) * chunk_size + 1) for i in range(num_threads)]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = executor.map(lambda r: factorial_part(*r), ranges)

    total = 1
    for result in results:
        total *= result
    
    return total

def single_threaded_factorial(n):
    return math.factorial(n)

def first_ten_digits(n):
    return str(n)[:10]

def main(n, num_threads):

    start_time = time.time()
    single_result = single_threaded_factorial(n)
    single_duration = time.time() - start_time
    print(f"Single-threaded result: {first_ten_digits(single_result)} (Time: {single_duration:.6f}s)")

    start_time = time.time()
    threaded_result = threaded_factorial(n, num_threads)
    threaded_duration = time.time() - start_time
    print(f"Multithreaded result: {first_ten_digits(threaded_result)} (Time: {threaded_duration:.6f}s)")

    assert single_result == threaded_result, "Results do not match!"

if __name__ == "__main__":
    n = 1000
    num_threads = 4
    main(n, num_threads)
