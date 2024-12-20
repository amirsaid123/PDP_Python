# import threading
# import time
#
#
# def send_email(receiver_email):
#     time.sleep(2.5)
#     print("Finish")
#
#
# start = time.time()
# threads = []
#
# for email in range(100000):
#     t = threading.Thread(target=send_email, args=(email,))
#     t.start()
#     threads.append(t)
#
#
# for thread in threads:
#     thread.join()
#
#
#
#
# print(time.time() - start)


from concurrent.futures import ThreadPoolExecutor
import time

def send_email(receiver_email):
    time.sleep(2.5)  # Simulate sending email
    print(f"Email sent to: {receiver_email}")

start = time.time()

# Use a thread pool with 10 threads to send emails concurrently
with ThreadPoolExecutor(max_workers=100) as executor:
    # Submit email sending tasks to the pool
    executor.map(send_email, range(100000))  # Simulate 100 emails

print(f"Total time: {time.time() - start:.2f} seconds")
