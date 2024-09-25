import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} seconds')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)


# threads = []
# for _ in range(5):
#     t = Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f'Finishesd in {round(finish-start, 2)} second(s)')