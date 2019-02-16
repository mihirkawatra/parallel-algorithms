import multiprocessing
import random
import time
main_array = random.sample(range(1000000), 1000000)

def find_string(start_index, end_index, thread_num):
    elem_to_search = 12312
    start_time = time.time()
    for i in range(int(start_index), int(end_index)):
        if main_array[i] == elem_to_search:
            end_time = time.time()
            print("Found in " + str(thread_num) + " at index " + str(i))
            print("Time taken:", str(end_time - start_time))

if __name__ == "__main__":
    # creating thread, divided input string into 3
    print("Multiple threads(4)\n")
    array_length = len(main_array)
    # The input string is divided in terms of length among the threads created
    t1 = multiprocessing.Process(target=find_string, args=(0, array_length/4, "thread 1"))
    t2 = multiprocessing.Process(target=find_string, args=(array_length/4, array_length/2, "thread 2"))
    t3 = multiprocessing.Process(target=find_string, args=(array_length/2, 3*(array_length)/4, "thread 3"))
    t4 = multiprocessing.Process(target=find_string, args=(3*array_length/4, array_length, "thread 4"))
    # start threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    time.sleep(1)
    print("\n\nExplicit Single thread\n")
    t1 = multiprocessing.Process( target=find_string, args=(0, array_length, "single thread") )
    t1.start()
    t1.join()
    time.sleep(1)
    print("\n\n Default function call\n")
    find_string(0, array_length, "no thread")
