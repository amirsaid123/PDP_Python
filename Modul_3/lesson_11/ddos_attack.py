import time
import requests
import threading

from bs4 import BeautifulSoup


def request():
    url = "https://kun.uz/"
    # response = requests.get(url , data=data)
    # cookies = response.cookies
    # html_code = response.text
    # soup = BeautifulSoup(html_code , "html.parser")
    # _csrf = soup.find("meta" , {"name" : "csrf-token"})["content"]
    # print(_csrf)
    # data["_csrf"] = _csrf
    response = requests.get(url)
    print(response)



threads = []
for i in range(1, 10000):
    # d = {
    #     "_csrf" : "lIraw1guIbwq5Uij9-q6VIhaFqY8Kob1Ir5w2bznC6Lg3eOzbmxnhH2_C-GDtfsN7zgm00lf4Z1FjwLg74Z85Q==",
    #     "SignupForm[username]" : f"Annatar"+"_"+str(i),
    #     "SignupForm[email]" : f"Annatar"+"_"+str(i)+"@gmail.com",
    #     "SignupForm[password]" : "Qwer123*!"
    # }
    thread = threading.Thread(target=request)
    thread.start()
    time.sleep(0.05)
    threads.append(thread)

for thread in threads:
    thread.join()



