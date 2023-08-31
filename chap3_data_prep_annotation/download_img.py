#%%
from tqdm import tqdm
from simple_image_download import simple_image_download as Downloader


def _download(keyword, limit):
    downloader = Downloader.simple_image_download
    downloader().download(keywords=keyword, limit=limit)
    urls = downloader().urls(keywords=keyword, limit=limit)
    return urls

def download(keywords, limit):
    for keyword in tqdm(keywords):
        urls = _download(keyword=keyword,limit=limit)
        with open(f"simple_images/{keyword}.txt", "w") as f:
            f.writelines("\n".join(urls))





# %%
download(keywords=["brain tumors x-ray", "heart tumors x-ray"], limit=10)



# %%
from simple_image_download.simple_image_download import simple_image_download as Downloader
from tqdm import tqdm
def _download(keyword, limit):
  downloader = Downloader()
  # download images
  downloader.download(keywords=keyword, limit=limit)
  # return the urls
  urls = downloader.urls(keywords=keyword, limit=limit)
  return urls

def download(keywords, limit):
  for keyword in tqdm(keywords):
    urls = _download(keyword=keyword, limit=limit)
    with open(f"simple_images/{keyword}.txt", "w") as f:
      f.writelines('\n'.join(urls))
  



# %%
