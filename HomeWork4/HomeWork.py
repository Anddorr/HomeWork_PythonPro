from aiohttp import ClientSession
from bs4 import BeautifulSoup
import asyncio
import time

url = 'https://books.toscrape.com/'


async def parser(page: int) -> None:
    result_list = []
    async with ClientSession() as session:
        async with session.get(f'{url}catalogue/page-{page}.html', ssl=False) as responce:
            resp = await responce.text()
            my_bs = BeautifulSoup(resp, 'html.parser')
            response_name = my_bs.findAll('article', {'class': 'product_pod'})
            response_price = my_bs.findAll('p', {'class': 'price_color'})
            response_image = my_bs.findAll('div', {'class': 'image_container'})
            responce_stack = my_bs.findAll('p', {'class': "instock availability"})
            for i in range(len(response_price)):
                print(response_name[i].h3.find('a')['title'])
                print(response_price[i].text)
                print(responce_stack[i].text.replace('\n', '').strip())
                print(f"{url}{response_image[i].a.find('img')['src']} \n")


async def main():
    start_time = time.time()
    async_list = []
    for pages in range(1, 2):
        task = asyncio.create_task(parser(page=pages))
        async_list.append(task)
    await asyncio.gather(*async_list)
    time_diff = time.time() - start_time
    print(f'Asynchronous function completed in {time_diff:.2f} seconds')


asyncio.run(main())
