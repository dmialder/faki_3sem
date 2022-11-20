import threading
import time


def thread_job(i, arr):
    with lock:
        global sum_array
        sum_array += sum(arr)


def run_threads(N):
    cuts = N
    if N >= len(array):
        cuts = len(array)
    threads = [
        threading.Thread(target=thread_job, args=(i, array[i*cuts : (i + 1)*cuts]))
        for i in range(N)
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

array = [73, 29, 1, 98, 3, 56, 72, 17, 83, 83, 23]
sum_array = 0
N = 5
start = time.time()

lock = threading.Lock()
run_threads(N)

print(time.time() - start)
print(sum_array)