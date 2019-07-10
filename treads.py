import time
import threading


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 10000:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
# for i in range(3):
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


# start_time = time.time()
# executor = ThreadPoolExecutor(max_workers=4)
# task_list = [executor.submit(fib, n) for n in range(3, 35)]
# thread_results = [task.result() for task in as_completed(task_list)]
# print(thread_results)
# print("ThreadPoolExecutor time is: {}".format(time.time() - start_time))