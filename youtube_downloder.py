#!/usr/bin/env python
"""
Download youtube videos

"""

# !pip install pytube

import pytube
link = input("Paste your link here: ")
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()