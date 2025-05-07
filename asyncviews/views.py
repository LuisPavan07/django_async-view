import asyncio
import httpx
from django.http import HttpResponse


async def http_call_async():
    for num in range(1, 10):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("http://httpbin.org")
        print(r)

async def async_view(request):
    await http_call_async()
    return HttpResponse("Hello World, welcome!")