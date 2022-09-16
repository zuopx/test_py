from aiohttp import web
from datetime import datetime


async def handle(request):
    return web.Response(text=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

app = web.Application()
app.add_routes([
    web.get('/', handle),
])

if __name__ == '__main__':
    web.run_app(app)
