import re
import requests
import sys
import json


def beacon():
    webhook = "your_site_or_webhook."

    print("[+] Sending request...")

    r = requests.get(str(webhook))

    if r.status_code == 200:
        print("[+] "+str(r.status_code))
        print("[+] Done")

    else:
        print("[+] Failed to send request...Run")


def apiIP():

    ip = sys.argv[1]
    api = str("https://ipinfo.io/"+ip+"?token=token")
    make_req = requests.get(api)
    print(make_req.text)
    info = open(ip+"information.json", "a+")
    info.write(make_req.text)


apiIP()
