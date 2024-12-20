import httpx, aiofile, asyncio



url = "https://kun.uz/"
# response = httpx.get(url)
# print(response.status_code)
# print(response.text)





async def get_html(url):
    async with httpx.AsyncClient() as client:
        client = httpx.get(url)
    return client





response = asyncio.run(get_html(url))
print(response.text)
