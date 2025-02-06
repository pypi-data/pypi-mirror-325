import aiohttp
from ..scripts import Scripted
from ..functions import Filename
from ..functions import Filesize
from ..functions import Location
#=============================================================================================

class Cores:

    async def get01(self, url, session):
        async with session.get(url, **self.kwords) as response:
            return dict(response.headers)

    async def get02(self, url, session=None):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, **self.kwords) as response:
                return dict(response.headers)

#=============================================================================================

    async def start(self, url, filename, location, progress, proargs, dsizes=0, tsizes=0):
        async with aiohttp.ClientSession() as session:
            dlsession = await self.get01(url, session)
            dfilesize = await Filesize.get01(dlsession)
            dfilenamo = await Filename.get01(url, dlsession)
            dfilename = await Filename.get04(dfilenamo, filename)
            dlocation = await Location.get01(dfilename, location)
            async with session.get(url, **self.kwords) as response:
                with open(dlocation, Scripted.READ01) as handlexo:
                    tsizes += dfilesize
                    while True:
                        moones = await response.content.read(self.chunks)
                        if not moones:
                            break
                        handlexo.write(moones)
                        dsizes += self.chunks
                        await self.display(dsizes, tsizes, progress, proargs)

                await response.release()
                return dlocation if dlocation else None

#=============================================================================================
