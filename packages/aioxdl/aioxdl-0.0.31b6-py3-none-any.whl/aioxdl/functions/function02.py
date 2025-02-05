class Filesize:
    async def get01(response):
        return int(response.get("Content-Length", 1))
