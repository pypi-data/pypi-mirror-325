import os

class Location:
    async def get01(filename, location):
        return os.path.join(location, filename) if location else filename

#============================================================================
