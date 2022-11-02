import re
import requests
import sys
import json


def beacon():
    webhook = "https://webhook.site/a9faeec9-8efd-46f4-a2fb-90daf003a408"

    print("[+] Sending request...")

    r = requests.get(str(webhook))

    if r.status_code == 200:
        print("[+] "+str(r.status_code))
        print("[+] Done")

    else:
        print("[+] Failed to send request...Run")


def apiIP():

    ip = sys.argv[1]
    api = str("https://ipinfo.io/"+ip+"?token=88607959947c24")
    make_req = requests.get(api)
    print(make_req.text)
    info = open(ip+"information.json", "a+")
    info.write(make_req.text)


apiIP()
