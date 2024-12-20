import threading
import time
from multiprocessing import Pool

start = time.time()
def send_email(receiver):
    time.sleep(2)
    print(f"Sent to {receiver}")

def split_tasks(emails: list):
    threads = []
    for email in emails:
        t = threading.Thread(target=send_email, args=(email,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    emails = list(range(1, 1001))
    tasks_list = []

    for i in range(0, len(emails), 10):
        tasks_list.append(emails[i:i + 10])

    with Pool(10) as p:
        p.map(split_tasks, tasks_list)


    print(time.time() - start)