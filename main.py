import praw
import os
import tempfile
import download
import image
import env
import list
import re
import sys


def subreddit(download_directory, subreddit, limit):
    reddit = praw.Reddit(client_id=env.client_id, client_secret=env.client_secret, user_agent=env.user_agent)

    subreddit = reddit.subreddit(subreddit)
    sub_id = re.sub(r'[^a-zA-Z0-9\s]', '', subreddit.title)
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)
    os.chdir(download_directory)
    if not os.path.exists(sub_id):
        os.makedirs(sub_id)

    url_file = f"{sub_id}\_downloaded.json"
    urls = list.get_url_list(url_file)
    
    hot = subreddit.hot(limit=limit)
    tmp = tempfile.gettempdir()

    for post in hot:
        if post.url in urls:
            print("Image already downloaded, skipping...", flush = True)
            continue
        if post.url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_name = post.url.split('/')[-1]
            new_name = image_name[:image_name.rfind(".")]
            tmpfile = f"{tmp}\{new_name}.png"
            print(f"Downloading {image_name} ", end = "", flush = True)        
            download.download_universal(post.url, tmpfile)         
            print(f"✓ ", end = "", flush = True)
            if os.path.exists(tmpfile):
                png = image.convert_to_png(tmpfile)
                with open(f"{sub_id}/{new_name}.png", 'wb') as f:
                    f.write(png.read())
                    print(f"\t-> {sub_id}/{new_name}.png", flush = True)
                    urls.append(post.url)
            else:
                print("Download failed!")
        else:
            print("Not an image, skipping...", flush = True)
    list.write_url_list(url_file, urls)


if __name__ == '__main__':
    _download_directory = 'downloaded_images'
    _limit = 50
    _subreddit = sys.argv[1]
    subreddit(_download_directory, _subreddit, _limit)