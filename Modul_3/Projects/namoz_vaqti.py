import asyncio, json, aiofile, httpx
from bs4 import BeautifulSoup
from tabulate import tabulate




class Namoz:
    async def write_cities(self, url):
        name = url.split('/')[-1]
        d = {"shahar": f"{name}", "url": f"{url}"}
        async with aiofile.async_open("database/cities.json", "r") as f:
            data = await f.read()
            data = json.loads(data)

        d['id'] = data[-1].get("id") + 1 if data else 1

        data.append(d)

        async with aiofile.async_open("database/cities.json", "w") as f:
            data = json.dumps(data, indent=4)
            await f.write(data)


    async def show_cities(self):
        async with aiofile.async_open("database/cities.json", "r") as f:
            data = await f.read()
            data = json.loads(data)

        cities = []
        for city in data:
            temp = [city['id'], city['shahar'].capitalize()]
            cities.append(temp)

        print(tabulate(cities, tablefmt="fancy_grid"))


    async def show_city(self, city_url):
        async with httpx.AsyncClient() as client:
            response = await client.get(city_url)

        html = response.text
        soup = BeautifulSoup(html, "html.parser")


        times = soup.find_all("div", class_="ad__item bor")

        namaz_times = []
        for time in times:

            title_element = time.find("h2", class_="nam")
            if title_element:
                title = title_element.text.strip()
            else:
                title = "N/A"


            time_element = time.find("p", class_="time")
            if time_element:
                namoz_time = time_element.text.strip()
            else:
                namoz_time = "N/A"


            namaz_times.append({"namoz": title, "time": namoz_time})

        return namaz_times


class Main:
    async def main(self):
        print("Namoz vaqti ilovasiga Xush Kelibsiz!")
        await Namoz().show_cities()
        key = int(input("Shaharni tanlang:"))
        async with aiofile.async_open("database/cities.json", "r") as f:
            data = await f.read()
            data = json.loads(data)

        url = ""
        for city in data:
            if city["id"] == key:
                url = city["url"]
                break

        times = await Namoz().show_city(url)
        table = tabulate(times, tablefmt="fancy_grid")
        print(table)

asyncio.run(Main().main())


