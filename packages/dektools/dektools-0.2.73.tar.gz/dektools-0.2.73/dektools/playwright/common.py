import playwright
import patchright
from playwright.sync_api import sync_playwright as sync_playwright_default
from patchright.sync_api import sync_playwright as sync_playwright_stealth
from playwright.async_api import async_playwright as async_playwright_default
from patchright.async_api import async_playwright as async_playwright_stealth
from ..ext.image import image_extensions
from ..ext.font import font_extensions
from ..ext.audio import audio_extensions
from ..ext.video import video_extensions
from ..web.url import get_url_ext
from .errors import async_safe_process, async_raise, sync_safe_process, sync_raise


def sync_playwright(stealth=True):
    if stealth:
        return sync_playwright_stealth()
    else:
        return sync_playwright_default()


def async_playwright(stealth=True):
    if stealth:
        return async_playwright_stealth()
    else:
        return async_playwright_default()


def is_stealth(obj):
    if isinstance(obj, type):
        cls = obj
    else:
        cls = obj.__class__
    return cls.__module__.startswith(patchright.__name__)


def get_playwright_name(stealth: bool):
    return patchright.__name__ if stealth else playwright.__name__


def get_resource_type(request):
    default = request.resource_type
    if default == 'other':
        ext = get_url_ext(request.url)
        if ext == '.css':
            return 'stylesheet'
        elif ext == 'js':
            return 'script'
        elif ext in audio_extensions or ext in video_extensions:
            return 'media'
        if ext in image_extensions:
            return 'image'
        elif ext in font_extensions:
            return 'font'
    return request.resource_type


page_content_messages = [
    "Page.content: Unable to retrieve content because the page is navigating and changing the content."
]


async def async_page_content(page):
    async def main():
        return await page.content()

    return await async_safe_process(main, others=async_raise, stealth=is_stealth(page), messages=page_content_messages)


def sync_page_content(page):
    def main():
        return page.content()

    return sync_safe_process(main, others=sync_raise, stealth=is_stealth(page), messages=page_content_messages)


class _PlaywrightResponse:
    def __init__(self, url, status, headers, body):
        self.url = url
        self.status = status
        self.headers = headers
        self._body = body

    def fulfill_kwargs(self):
        return dict(
            status=self.status,
            headers=self.headers,
            body=self._body
        )


class SyncPlaywrightResponse(_PlaywrightResponse):
    @property
    def body(self):
        return self._body


class AsyncPlaywrightResponse(_PlaywrightResponse):
    async def body(self):
        return self._body
