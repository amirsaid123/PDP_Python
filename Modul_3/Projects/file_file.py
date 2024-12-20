import httpx
from bs4 import BeautifulSoup
import asyncio










city_url = "https://obhavo.uz/tashkent"
async def get_html(url):
    async with httpx.AsyncClient() as client:
        res = await client.get(city_url)

    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    weathers = []

    days = soup.find_all("td", class_="weather-row-day")
    mornings = soup.find_all("span", class_="forecast-day")
    nights = soup.find_all("span", class_="forecast-night")
    descriptions = soup.find_all("td", class_="weather-row-desc")
    rains = soup.find_all("td", class_="weather-row-pop")

    for i, day in enumerate(days):
        print(f"{i}, {day.text}")



asyncio.run(get_html(city_url))