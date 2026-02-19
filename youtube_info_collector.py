import json
from yt_dlp import YoutubeDL


def make_key_from_title(title: str) -> str:
    # Take the YouTube video title, run it through the title() function and bring the resulting title words together
    return title.title().replace(" ", "")


def get_youtube_info(url):
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False) # get all the info about the YouTube video using the url

    title = info.get("title")  # get the YouTUbe video title from the pool of information

    # Return a JSON object containing selected video information
    return {
        "key": make_key_from_title(title),
        "name": title,
        "summary": info.get("description"),
        "youtube_link": info.get("webpage_url"),
    }


# Example usage
one = ""

two = ""

three = ""

four = ""

five = ""

six = ""


url_list = [one, two, three]

videos = {}

# For loop that goes through a list of YouTube urls and prepares a JSON object collection containing video info
for url in url_list:
    info = get_youtube_info(url)
    videos[info["key"]] = {
        "name": info["name"],
        "summary": info["summary"],
        "youtube_link": info["youtube_link"],
    }

# Pretty-print valid JSON
print(json.dumps(videos, indent=2, ensure_ascii=False))
