#!/usr/bin/env python3

import requests
import json
import subprocess

r = requests.get("http://a1.phobos.apple.com/us/r1000/000/Features/atv/AutumnResources/videos/entries.json")
data = r.json()
for vid_group in data:
	for video in vid_group["assets"]:
		movie_url = video["url"]
		print("showing move from : %s" % video["accessibilityLabel"])
		subprocess.call(["omxplayer", movie_url])
