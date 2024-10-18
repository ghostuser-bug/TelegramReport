import os
import requests
from time import sleep
from configparser import ConfigParser
from threading import Thread
from re import compile

THREADS = 500
PROXIES_TYPES = ('http', 'socks4', 'socks5')
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
REGEX = compile(r"(?:^|\D)?((?:[1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
                r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
                r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
                r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
                r"):" + (r"(?:\d|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}"
                r"|65[0-4]\d{2}|655[0-2]\d|6553[0-5])"
                r")(?:\D|$)")

# Use a context manager for error logging
def log_error(message):
    with open('errors.txt', 'a+') as errors:
        errors.write(f'{message}\n')

cfg = ConfigParser(interpolation=None)
if not os.path.exists("config.ini"):
    log_error("config.ini file not found. Please ensure the file is in the same directory!")
    exit()

cfg.read("config.ini", encoding="utf-8")
http, socks4, socks5 = '', '', ''
try:
    socks4, socks5, http = cfg["SOCKS4"], cfg["SOCKS5"], cfg["HTTP"]
except KeyError:
    log_error("Error reading proxy types from config.ini.")
    exit()

http_proxies, socks4_proxies, socks5_proxies = [], [], []
time_out = 15

def save_proxies(proxies, proxy_type):
    with open(f"{proxy_type}_proxies.txt", 'w') as file:
        for proxy in proxies:
            file.write(proxy + '\n')

def scrap(sources, _proxy_type):
    proxies = []
    for source in sources:
        if source:
            try:
                response = requests.get(source, timeout=time_out)
                if REGEX.findall(response.text):
                    proxies.extend(proxy.group(1) for proxy in REGEX.finditer(response.text))
            except Exception as e:
                log_error(str(e))

    if _proxy_type == 'socks4':
        save_proxies(proxies, 'socks4')        
    elif _proxy_type == 'socks5':
        save_proxies(proxies, 'socks5')             
    elif _proxy_type == 'http':
        save_proxies(proxies, 'http')

def start_scrap():
    threads = []
    for i in (http_proxies, socks4_proxies, socks5_proxies):
        i.clear()
    sources = [
        (socks4.get("Sources").splitlines(), 'socks4'),
        (socks5.get("Sources").splitlines(), 'socks5'),
        (http.get("Sources").splitlines(), 'http')
    ]
    for source in sources:
        thread = Thread(target=scrap, args=(source[0], source[1]))
        threads.append(thread)
        thread.start()
    for t in threads:
        t.join()

def start_view():
    start_scrap()

Thread(target=start_view).start()
