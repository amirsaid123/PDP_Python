from flask import Flask, render_template
import json
import aiofile
import httpx
from bs4 import BeautifulSoup

app = Flask(__name__)

class Namoz:
    async def get_cities(self):
        async with aiofile.async_open("database/cities.json", "r") as f:
            data = await f.read()
            return json.loads(data)

    async def get_city_times(self, city_url):
        async with httpx.AsyncClient() as client:
            response = await client.get(city_url)

        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        times = soup.find_all("div", class_="ad__item bor")

        namaz_times = []
        for time in times:
            title_element = time.find("h2", class_="nam")
            title = title_element.text.strip() if title_element else "N/A"

            time_element = time.find("p", class_="time")
            namoz_time = time_element.text.strip() if time_element else "N/A"

            namaz_times.append({"namoz": title, "time": namoz_time})

        return namaz_times

@app.route('/')
async def show_cities():
    cities_data = await Namoz().get_cities()
    cities = [{"id": city['id'], "shahar": city['shahar']} for city in cities_data]
    return render_template('cities.html', cities=cities)

@app.route('/city/<int:city_id>/times')
async def show_times(city_id):
    cities_data = await Namoz().get_cities()
    city_url = None
    for city in cities_data:
        if city['id'] == city_id:
            city_url = city['url']
            break

    if city_url:
        namaz_times = await Namoz().get_city_times(city_url)
        return render_template('times.html', city_id=city_id, namaz_times=namaz_times)
    else:
        return f"City with ID {city_id} not found", 404

if __name__ == '__main__':
    app.run(debug=True)
