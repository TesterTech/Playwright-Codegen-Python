import asyncio

from playwright.async_api import Playwright, async_playwright, expect
from models.search import SearchPage 


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    search_page = SearchPage(page)

    await search_page.navigate()
    await search_page.search("summer dress")

    #await page.goto("http://automationpractice.com/index.php")
    #await page.locator("img[alt=\"My Store\"]").click()
    #await page.locator("[placeholder=\"Search\"]").click()
    #await page.locator("[placeholder=\"Search\"]").fill("summer dress")
    #await page.locator("button:has-text(\"Search\")").click()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())

