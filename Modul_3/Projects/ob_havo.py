import asyncio, json, aiofile, httpx
from bs4 import BeautifulSoup
from tabulate import tabulate




class Weather:
    async def write_cities(self, url):
        name = url.split('/')[-1]
        d = {"City": name, "url": url}
        async with aiofile.async_open("database/cities_weather.json", "r") as f:
            data = await f.read()
            data = json.loads(data)

        d['id'] = data[-1].get('id') + 1 if data else 1


        data.append(d)

        async with aiofile.async_open("database/cities_weather.json", "w") as f:
            data = json.dumps(data, indent=4)
            await f.write(data)


    async def show_cities(self):
        async with aiofile.async_open("database/cities_weather.json", "r") as f:
            data = await f.read()
            data = json.loads(data)

        cities = []

        for city in data:
            temp = [city['id'], city['City'].capitalize()]
            cities.append(temp)

        print(tabulate(cities, tablefmt='fancy_grid'))


    async def show_city(self, city_url):

        async with httpx.AsyncClient() as client:
           res = await client.get(city_url)


        html = res.text
        soup = BeautifulSoup(html, 'html.parser')

        weathers = []
        first_day = soup.find("div", class_="current-day")
        numbers = soup.find_all("p", class_="forecast")
        morning = numbers[0].text
        night = numbers[2].text
        first_description = soup.find("div", class_="current-forecast-desc")


        current_day = {
            "Kun": first_day.text.strip(),
            "Ertalab": morning.strip(),
            "Kechqurun": night.strip(),
            "Ob-xavo": first_description.text.strip(),
            "Yog`ingarchilik": "0%"
        }
        weathers.append(current_day)



        days = soup.find_all("td", class_="weather-row-day")
        mornings = soup.find_all("span", class_="forecast-day")
        nights = soup.find_all("span", class_="forecast-night")
        descriptions = soup.find_all("td", class_="weather-row-desc")
        rains = soup.find_all("td", class_="weather-row-pop")

        for i in range(len(days)):
            d = {"Kun": days[i].text.strip(),
                 "Ertalab": mornings[i].text,
                 "Kechqurun": nights[i].text,
                 "Ob-xavo": descriptions[i].text.strip().capitalize(),
                 "Yog`ingarchilik": rains[i].text}
            weathers.append(d)


        return weathers






class Main:
    async def main(self):
        print("Welcome to Weather App")
        await Weather().show_cities()
        key = int(input("Choose a city:"))

        async with aiofile.async_open("database/cities_weather.json", "r") as f:
            data = await f.read()
            data = json.loads(data)

        url = ""
        for city in data:
            if city['id'] == key:
                url = city['url']
                break

        weathers = await Weather().show_city(url)
        table = tabulate(weathers, headers="keys", tablefmt="fancy_grid")
        print(table)






asyncio.run(Main().main())