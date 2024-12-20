# from multiprocessing import Process
# import time
#
# def worker(name):
#     print(f"Process {name} started.")
#     time.sleep(2)  # Simulate some work
#     print(f"Process {name} finished.")
#
# if __name__ == "__main__":
#     processes = []
#
#     # Create 5 processes
#     for i in range(5):
#         p = Process(target=worker, args=(i,))
#         processes.append(p)
#         p.start()
#
#     # Wait for all processes to complete
#     for p in processes:
#         p.join()
#
#     print("All processes finished.")


from multiprocessing import Pool
import time

def square(n):
    time.sleep(1)  # Simulate some delay
    return n * n

if __name__ == "__main__":
    with Pool(10) as pool:  # Create a pool with 4 processes
        results = pool.map(square, range(10))  # Apply 'square' function to each input

    print(f"Results: {results}")
