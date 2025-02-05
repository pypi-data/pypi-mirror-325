import os
from urllib.parse import unquote
from urllib.parse import urlparse
#====================================================================================================================

class Filename:

    async def get02(url):
        filename01 = urlparse(url).path.split("/")
        filename02 = filename01[-1]
        filename03 = unquote(filename02)
        filename04 = filename03.replace("/", "-")
        return filename04

#====================================================================================================================

    async def get03(moonues):
        filename01 = moonues.index("filename=") + len("filename=")
        filename02 = moonues[filename01:]
        filename03 = unquote(filename02.strip('"'))
        filename04 = filename03.replace("/", "-")
        return filename04

#====================================================================================================================

    async def get04(onames, cnames):
        filenames = os.path.splitext(cnames)[0] if cnames else os.path.splitext(onames)[0]
        extensios = os.path.splitext(cnames)[1] if cnames else os.path.splitext(onames)[1]
        extension = extensios if extensios else os.path.splitext(onames)[1]
        return str(filenames) + str(extension)

#====================================================================================================================

    async def get01(url, headers):
        moones = headers.get("Content-Disposition", None)
        moonus = await Filename.get03(moones) if moones and "filename=" in moones else await Filename.get02(url)
        return moonus

#====================================================================================================================
