import threading
import time

# Indicates some tast being done
def func(seconds):
    print(f'Sleeping for {seconds} seconds:')
    for i in range(seconds,0,-1):
        time.sleep(1)
        print(f'\t{i}')

#count time:
timer_start = time.perf_counter()   

#Normal Code:  
# func(4)
# func(2)
# func(1)

# Same code using Threads:
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[3])
t3 = threading.Thread(target=func, args=[2])

t1.start()
t2.start()
t3.start()


#waiting for their end:
t1.join()
t2.join()
t3.join()
timer_final = time.perf_counter() 
print(timer_final-timer_start)