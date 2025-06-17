import asyncio
from pyppeteer import launch

async def get_data():

        pageName = 'https://wyniki.datasport.pl/results5441/indexnew.php'
        browser = await launch()
        page = await browser.newPage()
        await page.goto(pageName)

        await asyncio.sleep(5)
        await (await page.querySelector('#start1'))._scrollIntoViewIfNeeded()
        await asyncio.sleep(2)
        await page.evaluate('''window.open = () => ({document: window.document})''')
        await (await page.querySelector('#start1')).click()
        await asyncio.sleep(5)
        print('done')

        results = await page.evaluate('''() => {
            return [...document.querySelectorAll('tr')].slice(0).map((tr) => [...tr.querySelectorAll('td,th')].map(td => td.innerText))
        }''')

        name  = 'results_wro.json'
        with open(name, 'w') as f:
            f.write(str(results))  

        await browser.close()

asyncio.get_event_loop().run_until_complete(get_data())
