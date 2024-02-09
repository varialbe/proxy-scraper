![Screenshot_3](https://github.com/varialbe/proxy-scraper/assets/142154418/a141ac2c-d573-4c7a-8d50-3c5d3ac2b61b)
# Proxy Scraper Script

This Python script is designed to scrape and combine proxy lists from multiple sources. It's useful for developers and researchers who need a reliable list of proxies for web scraping, anonymity, or bypassing geo-restrictions.

## Features

- Scrapes proxies from multiple sources.
- Combines proxies into a single list.
- Prints execution time.
- Colorful debugging output for HTTP status codes.

## Sources

The script scrapes proxies from the following sources:
- [Free Proxy List](https://free-proxy-list.net/)
- [ProxyScrape](https://api.proxyscrape.com/v3/free-proxy-list/get?request=getproxies&proxy_format=ipport&format=text)
- [GeoNode Proxy List](https://proxylist.geonode.com/api/proxy-list)
- [Netzwelt](https://www.netzwelt.de/proxy/index.html)
- [OpenProxyList](https://api.openproxylist.xyz/http.txt)

## Usage

The script is straightforward to use and can be executed as a standalone Python script. Ensure you have Python installed on your system!

### Installation

First, clone the repository to your local machine:
```bash
git clone https://github.com/varialbe/proxy-scraper.py
cd proxy-scraper-script
```

Then, install the required packages using pip:

```bash
pip install requests beautifulsoup4 colorama
```

### Running the Script

Execute the script with Python:

```bash
python proxy_scraper.py
```

## Disclaimer

This script is for educational purposes only. Scraping proxies may violate the terms of service of some websites. It is the end user's responsibility to ensure that their actions comply with local laws and website terms of use. The author of this script is not responsible for any misuse or damage that may arise from its use.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
