class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_term_input = page.locator("[placeholder=\"Search\"]")
        self.search_result_count = page.locator(".heading-counter")

    async def navigate(self):
        await self.page.goto("http://automationpractice.com/index.php")

    async def search(self, text):
        await self.search_term_input.fill(text)
        await self.search_term_input.press("Enter")
        await self.search_term_input.click()
        
