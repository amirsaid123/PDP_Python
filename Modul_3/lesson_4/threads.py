import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)  # Simulate a time-consuming task

# Create a new thread
t = threading.Thread(target=print_numbers)

# Start the thread
t.start()

# Main thread continues to execute
print("Main thread is running...")

# Wait for the thread to finish
t.join()
print("Thread finished execution.")
