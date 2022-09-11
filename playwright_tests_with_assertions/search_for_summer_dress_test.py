import asyncio
import re

from playwright.async_api import Playwright, async_playwright, expect
from models.search import SearchPage 


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    search_page = SearchPage(page)

    await search_page.navigate()
    await expect(page).to_have_title("My Store") 
    await search_page.search("summer dress")
    await expect(search_page.search_result_count)\
            .to_have_text(re.compile(r".*\d+ results have been found\.*"))

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())

