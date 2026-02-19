import yt_dlp

def search_youtube(query, max_results=5):
    # Set yt-dlp options for search-only (no download)
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,  # Get metadata without downloading videos
        "force_generic_extractor": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Use the ytsearch feature with the number of results
        search_result = ydl.extract_info(f"ytsearch{max_results}:{query}", download=False)

    # Loop through search results and print title + URL
    for entry in search_result["entries"]:
        title = entry.get("title")
        url = entry.get("url")
        full_url = f"{url}"
        print(f"{title}\n{full_url}\n")


# Example usage
topic = "karate news story stops crime"
search_youtube(topic, max_results=15)
