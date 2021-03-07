
# API doc: https://cutt.ly/api-documentation/cuttly-links-api
# API Key: https://cutt.ly/edit
#
# Usage: <cmd> full_long_url [short_name]
# Output: Shortened URL: https://cutt.ly/short_name

import requests
import sys

print("--- 命令行参数:", sys.argv)
# print(len(sys.argv) )
if len(sys.argv) < 2:
    # expect 2 or 3 arguments: cmd, url, [short name]
    print(f"用法: {sys.argv[0]} full_long_url [short_name]")
    exit(1)

# get the URL you want to shorten from cmd line
url = sys.argv[1]

api_key = "e77a2e10762f46d8be84d47974d4703310301"

# construct the API URL to call
if len(sys.argv) >= 3:
    # user provided the preferred short name
    short_name = sys.argv[2]
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}&name={short_name}"
else:
    # user didnot provide the short name. 
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"

print("--- api_url: ", api_url)

# make the request
data = requests.get(api_url).json()["url"]

print ("--- data: ", data)

if data["status"] == 7:
    # OK, get shortened URL
    shortened_url = data["shortLink"]
    print("--- Shortened URL:", shortened_url)
else:
    print("[!] Error Shortening URL:", data)
