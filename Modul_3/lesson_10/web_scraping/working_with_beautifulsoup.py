from bs4 import BeautifulSoup
import httpx

code = """
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <div>
        hello world
    </div>
    <h2 class="title is-5">Senior Python Developer</h2>
    <h2 class="title is-5">Senior Python Developer</h2>
    <h2 class="title is-5">Senior Python Developer</h2>
    <h3 class="subtitle is-6 company">Payne, Roberts and Davis</h3>
    <p class="location">Stewartbury, AA</p>
    <p class="location1">Stewartbury, AAA</p>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" alt="" style="width: 20px">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" alt="" style="width: 20px">
    <img class="tmp" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" alt="" style="width: 20px">


    </body>
    </html>
"""
#
# soup = BeautifulSoup(code, 'html.parser')
#
# # print(soup.find("p", {"class": "location1"}).text)
#
# print(soup.find("img")["src"])


url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDEvJyUjkex89qzPfmjQxAiNZsVRD2IWcctg&s"
response = httpx.get(url)
data = response.read()

with open("image.jpg", "wb") as f:
    f.write(data)