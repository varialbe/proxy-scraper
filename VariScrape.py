import requests
from bs4 import BeautifulSoup
import time
from colorama import init, Fore, Style
import os
import fade

banner = r"""

█░█ ▄▀█ █▀█ █ ▄▄ █▀ █▀▀ █▀█ ▄▀█ █▀█ █▀▀
▀▄▀ █▀█ █▀▄ █ ░░ ▄█ █▄▄ █▀▄ █▀█ █▀▀ ██▄

https://varialbe.xyz | https://github.com/varialbe"""
faded_banner = fade.purpleblue(banner)

init(autoreset=True)

print(faded_banner)

def fetch_and_combine_proxies():
    response_free_proxy_list = requests.get("https://free-proxy-list.net/")
    print(Fore.MAGENTA + f"free-proxy-list.net: {response_free_proxy_list.status_code}" if response_free_proxy_list.status_code == 200 else Fore.BLUE + f"free-proxy-list.net: {response_free_proxy_list.status_code}")
    soup_free_proxy_list = BeautifulSoup(response_free_proxy_list.text, 'html.parser')
    proxies_free_proxy_list = [line.strip() for line in soup_free_proxy_list.select_one('#raw > div > div > div.modal-body > textarea').text.split('\n')[3:] if line.strip()]

    response_proxyscrape = requests.get("https://api.proxyscrape.com/v3/free-proxy-list/get?request=getproxies&proxy_format=ipport&format=text")
    print(Fore.MAGENTA + f"proxyscrape.com: {response_proxyscrape.status_code}" if response_proxyscrape.status_code == 200 else Fore.BLUE + f"proxyscrape.com: {response_proxyscrape.status_code}")
    proxies_proxyscrape = [proxy.strip() for proxy in response_proxyscrape.text.strip().split('\n') if proxy.strip()]

    response_geonode = requests.get("https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc")
    print(Fore.MAGENTA + f"geonode.com: {response_geonode.status_code}" if response_geonode.status_code == 200 else Fore.BLUE + f"geonode.com: {response_geonode.status_code}")
    proxies_geonode = [f"{proxy['ip']}:{proxy['port']}" for proxy in response_geonode.json()['data']]

    response_netzwelt = requests.get("https://www.netzwelt.de/proxy/index.html")
    print(Fore.MAGENTA + f"netzwelt.de: {response_netzwelt.status_code}" if response_netzwelt.status_code == 200 else Fore.BLUE + f"netzwelt.de: {response_netzwelt.status_code}")
    soup_netzwelt = BeautifulSoup(response_netzwelt.text, 'html.parser')
    rows_netzwelt = soup_netzwelt.select('#article > div.tblc > table > tbody > tr')
    proxies_netzwelt = [f"{row.find('td').find('a').text.strip()}:{row.find_all('td')[1].text.strip()}" for row in rows_netzwelt]

    response_openproxylist = requests.get("https://api.openproxylist.xyz/http.txt")
    print(Fore.MAGENTA + f"openproxylist.xyz: {response_openproxylist.status_code}" if response_openproxylist.status_code == 200 else Fore.BLUE + f"openproxylist.xyz: {response_openproxylist.status_code}")
    proxies_openproxylist = response_openproxylist.text.strip().split('\n')

    all_proxies = proxies_free_proxy_list + proxies_proxyscrape + proxies_geonode + proxies_netzwelt + proxies_openproxylist

    return all_proxies

input = input("Start Scraping? (y/n): ")
if input.lower() == "y":
    print(f"{Fore.CYAN} Started Scraping..")
    start_time = time.time()
    combined_proxies = fetch_and_combine_proxies()
    elapsed_time = time.time() - start_time
    print(f"{Fore.CYAN}Execution time: {elapsed_time:.2f} seconds")
else:
    os._exit()