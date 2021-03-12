
# Site: hhttps://sina.lt/
#
# Usage: <cmd> full_long_url shorten_site
# Output: Shortened URL: https://shorten_site/***

import requests
import sys
import base64
import random
import re

print("--- 命令行参数:", sys.argv)
# print(len(sys.argv) )
if len(sys.argv) < 3:
    # expect 3 arguments: cmd, url, shorten_site
    print(f"用法: {sys.argv[0]} full_long_url shorten_site")
    exit(1)

# get the URL you want to shorten from cmd line
url = sys.argv[1]
site = sys.argv[2]

# get cookie -- Note: cookie is set in response from https://sina.lt/images/transparent.gif
# need to fake a random user-agent ip to avoid the detection of repeated requests from the same user
ramdon_ip = f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
#ramdon_ip = "89.0.1.0"
request_headers = {"User-Agent": f"Chrome/{ramdon_ip}"}

response_headers = requests.get("https://sina.lt/images/transparent.gif", headers=request_headers).headers
print ("--- response headers: ", response_headers )

cookies = response_headers["Set-Cookie"]
print ("--- response cookies: ", cookies)
# -- cookie:  __cfduid=ddab0dc31dc293bd1c220b19e3f45e3b41615278040; expires=Thu, 08-Apr-21 08:20:40 GMT; path=/; domain=.sina.lt; HttpOnly; SameSite=Lax, PHPSESSID=gg3q810h2biu3k6pmo3c6h83p2; path=/
# need to remove expires or just extract PHPSESSID out by split the string with ";" and ","
for cookie in re.split('; |, ', cookies):
    # print(cookie)
    if cookie.startswith("PHPSESSID"):
        break

# set cookie (PHPSESSID is significant) and user-agent in request headers
# e.g. cookie = 'PHPSESSID=iqc5s5fkvnv9lrooog58ho3lk5'
request_headers2 = {"cookie": f"{cookie}", "User-Agent": f"Chrome/{ramdon_ip}"}
print ("--- request headers: ", request_headers2)

# construct the API URL to call
# based64 encode long_url
base64encoded = base64.b64encode(url.encode())
base64encoded_url = base64encoded.decode()

api_url = f"https://sina.lt/api.php?from=w&url={base64encoded_url}&site={site}"
print("--- api_url: ", api_url)

# make the request
response = requests.get(api_url, headers=request_headers2).json()

print ("--- data: ", response)

if response["result"] == "ok":
    # OK, get shortened URL
    shortened_url = response["data"]["short_url"]
    print("--- Shortened URL:", shortened_url)
else:
    print("[!] Error Shortening URL:", response)
