import asyncio
import json
import os

import yt_dlp

takeout_file = "path to your file"

with open(takeout_file, "rb") as f:
    takeout_json = json.load(f)

parsed_json = []

failed = []

no_url = []


class FakeLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass


async def extract(data):
    url = data.get("titleUrl")
    if not url:
        no_url.append(data)
        return
    yt_obj = yt_dlp.YoutubeDL(
        {
            "quiet": True,
            "logger": FakeLogger(),
            "ignoreerrors": True,
            "ignore_no_formats_error": True,
        }
    )
    request = await asyncio.to_thread(yt_obj.extract_info, url, download=False)
    if not request:
        failed.append(data)
    else:
        new_data = {}
        new_data["trackName"] = request.get("title")
        new_data["albumName"] = request.get("album")
        new_data["artistName"] = request.get("artist", request.get("album"))
        new_data["datetime"] = data.get("time")
        parsed_json.append(new_data)


async def start():
    await asyncio.gather(
        *[extract(data) for data in takeout_json if data["header"] == "YouTube Music"]
    )


asyncio.run(start())


def writer(file_name, jdata):
    count = 0
    while os.path.isfile(f"{file_name}{count}.json"):
        count += 1
    file_name = f"{file_name}{count}.json"
    with open(file_name, "w+") as nj:
        json.dump(jdata, nj, indent=4)


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


for chunk in chunks(parsed_json, 2600):
    writer(f"new_json", chunk)

if failed:
    writer("failed", failed)

print(f"Processed: {len(parsed_json)} out of {len(takeout_json)}")
print(f"Failed: {len(failed)}, check failed.json")
print(f"Not processed: {len(no_url)}")
