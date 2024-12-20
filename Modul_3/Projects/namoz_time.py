from enum import Enum
import asyncio

import httpx
from bs4 import BeautifulSoup


class Lang(Enum):
    uz = "1"
    oz = "2"
    ru = "3"
    en = "4"

class NamazTime:
    base_url = "https://namozvaqti.uz"
    def __init__(self, lang:str = "uz"):
        self.lang = lang


    async def requests(self, url):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        return response.content

    async def region_list(self):
        region_url = f"{self.base_url}/{self.lang}/viloyat"
        html_code = await self.requests(region_url)
        soup = BeautifulSoup(html_code, "html.parser")
        cards = soup.find_all("div", {"class": "col-xl-4 col-xs-12 py-1"})
        result = []
        for card in cards:
            d = {
                "href": card.find("a")["href"],
                "name": card.text,
            }
            result.append(d)
        return result

    async def districts_list(self, region_url):
        html_code = await self.requests(region_url)
        soup = BeautifulSoup(html_code, "html.parser")
        cards = soup.find_all("div", {"class": "col-xl-4 col-xs-12 py-1"})
        result = []
        for card in cards:
            d = {
                "href": card.find("a")["href"],
                "name": card.text,
            }
            result.append(d)

        return result

    async def namoz_time_list(self, district_url):
        html_code = await self.requests(district_url)
        soup = BeautifulSoup(html_code, "html.parser")
        cards = soup.find_all("div", {"class": "ad__item bor"})
        d  = {}
        for card in cards:
            d[card.find("h2").text] = card.find("p", class_="time").text

        return d


class UI:
    session_lang = "uz"
    async def lang(self):
        menu = """
        Tilni tanlang
        1) Uz
        2) O`z
        3) Ru
        4) En
        """
        print(menu)

        key = input("Tilni tanlang:")
        choice = Lang(key).name
        self.session_lang = choice
        print("\n" * 100)
        await self.region_ui()

    async def region_ui(self):
        self.obj = NamazTime(self.session_lang)
        regions_data = await self.obj.region_list()
        for i, region in enumerate(regions_data):
            print(f"{i+1}. {region['name']}")

        key = input("Viloyatni tanlang:")
        print("0.Back")
        if key == "0":
            print("\n" * 100)
            await self.lang()
        index = int(key) - 1
        region_url = regions_data[index].get("href")
        print("\n" * 100)
        await self.district_ui(region_url)

    async def district_ui(self, region_url):
        distric_data:list[dict] = await self.obj.districts_list(region_url)
        for i, district in enumerate(distric_data):
            print(f"{i+1}. {district['name'].strip()}")
        print("0.Back <--")
        key = input("Tumanni tanlang:")
        if key == "0":
            print("\n" * 100)
            await self.region_ui()
        index = int(key) - 1
        district_url = distric_data[index].get("href")
        print("\n" * 100)
        await self.namoz_time_url(district_url, region_url)

    async def namoz_time_url(self, district_url, region_url):
        namoz_time:dict = await self.obj.namoz_time_list(district_url)
        for name, time in namoz_time.items():
            print(f"{name}: {time}")
        input("Press Enter to go back:")
        print("\n" * 100)
        await self.district_ui(region_url)





asyncio.run(UI().lang())




