
# API doc: https://dev.bitly.com/api-reference#createBitlink

# Usage: <cmd> full_long_url
# Output: Shortened URL: https://bit.ly/short_name

import requests
import sys

print ("--- 命令行参数:", sys.argv)
# pass in the URL you want to shorten
if len(sys.argv) < 2:
    # expect 2 or 3 arguments: cmd, url, [short name]
    print(f"用法: {sys.argv[0]} full_long_url")
    exit(1)

url = sys.argv[1]

# account credentials
username = "cs1948"
password = "G6odl8ck"

# get the access token
auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))
if auth_res.status_code == 200:
    # if response is OK, get the access token
    access_token = auth_res.content.decode()
    print("--- Got access token:", access_token)
else:
    print(f"[!] Cannot get access token. code: {auth_res.status_code}, reason: {auth_res.reason}. Now exiting... ")
    exit()

# construct the request headers with authorization
headers = {"Authorization": f"Bearer {access_token}"}

# get the group UID associated with your account
groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
if groups_res.status_code == 200:
    # if response is OK, get the GUID
    groups_data = groups_res.json()['groups'][0]
    guid = groups_data['guid']
else:
    print(f"[!] Cannot get GUID. code: {groups_res.status_code}, reason: {groups_res.reason}. Now exiting... ")
    exit()

print("--- groups_res:", groups_res.json())
print("--- guid:", guid)

# make the POST request to get shortened URL for `url`
shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url}, headers=headers)
if shorten_res.status_code == 200 or shorten_res.status_code == 201 :
    # if response is OK, get the shortened URL
    link = shorten_res.json().get("link")
    print("--- Shortened URL:", link)
else:
    print(f"[!] Cannot shorten URL: {url} for GUID: {guid}, code: {shorten_res.status_code}, reason: {shorten_res.reason}. Now exiting... ")
    exit()
