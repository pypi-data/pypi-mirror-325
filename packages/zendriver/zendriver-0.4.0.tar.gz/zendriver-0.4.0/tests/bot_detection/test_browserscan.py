import zendriver as zd


async def test_browserscan(browser: zd.Browser):
    page = await browser.get("https://www.browserscan.net/bot-detection")

    element = await page.find_element_by_text("Test Results:")
    assert (
        element is not None
        and element.parent is not None
        and isinstance(element.parent.children[-1], zd.Element)
    )
    assert element.parent.children[-1].text == "Normal"
