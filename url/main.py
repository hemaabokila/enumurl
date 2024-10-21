from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
import time
from colorama import Fore, Style
import os
import argparse

class URLEnumeration:
    def __init__(self, base_url=None, url_file=None, max_depth=2):
        self.base_url = base_url
        self.url_file = url_file
        self.max_depth = max_depth
        self.visited = set()
        self.to_visit = []

        if self.url_file:
            self.load_external_links()
        elif self.base_url:
            self.to_visit.append((self.norm_url(base_url), 0))

    def load_external_links(self):
        try:
            with open(self.url_file, "r") as file:
                links = file.read().splitlines()
                for link in links:
                    normed_link = self.norm_url(link)
                    if self.test_url(normed_link):
                        self.to_visit.append((normed_link, 0))
                    else:
                        print(f"{Fore.RED}[!] Invalid URL: {link}{Style.RESET_ALL}")
        except FileNotFoundError:
            print(f"{Fore.RED}[!] URL file not found!{Style.RESET_ALL}")

    def test_url(self, url):
        parse = urlparse(url)
        return bool(parse.scheme) and bool(parse.netloc)

    def internal_url(self, url, url2):
        domain = urlparse(url).netloc
        domain2 = urlparse(url2).netloc
        return domain == domain2

    def norm_url(self, url):
        url = url.rstrip('/')
        if not urlparse(url).scheme:
            url = 'http://' + url
        elif urlparse(url).scheme not in ['http', 'https']:
            url = 'http://' + url 
        return url

    def get_links(self, cur_url):
        links = set()
        try:
            response = requests.get(cur_url, timeout=10)
            if response.status_code == 200:
                b_soup = BeautifulSoup(response.text, "html.parser")
                for i in b_soup.find_all("a", href=True):
                    href = i.get("href")
                    full_url = urljoin(cur_url, href)
                    normed_url = self.norm_url(full_url)
                    if self.test_url(normed_url):
                        links.add(normed_url)
                if links:
                    print(f"{Fore.GREEN}[*] Discovered links from {cur_url}:{Style.RESET_ALL}")
                    for link in links:
                        print(f"{link}")
            return links
        except requests.exceptions.RequestException as error:
            print(f"{Fore.RED}Error fetching {cur_url} {Style.RESET_ALL}")
            return set()

    def run(self):
        print(f'''
        {Fore.BLUE}
         _____ _   _ _   _ __  __ _   _ ____  _     
        | ____| \\ | | | | |  \\/  | | | |  _ \\| |    
        |  _| |  \\| | | | | |\\/| | | | | |_) | |    
        | |___| |\\  | |_| | |  | | |_| |  _ <| |___ 
        |_____|_| \\_|\\___/|_|  |_|\\___/|_| \\_\\_____|
                Developed by: Ibrahem abo kila                          
        {Style.RESET_ALL}
        ''')
        try:
            while self.to_visit:
                cur_url, depth = self.to_visit.pop(0) 
                if cur_url not in self.visited and depth <= self.max_depth:
                    print(f"Visiting: {cur_url}")
                    self.visited.add(cur_url)
                    new_links = self.get_links(cur_url)
                    for link in new_links:
                        normd_link = self.norm_url(link)
                        if normd_link not in self.visited and normd_link not in [x[0] for x in self.to_visit]:
                            self.to_visit.append((normd_link, depth + 1))
                    time.sleep(1)

            print(f"{Fore.GREEN}[*] Finished enumeration.{Style.RESET_ALL}")
            print(f"{Fore.BLUE}[*] Discovered links:{Style.RESET_ALL}")
            for link in self.visited:
                print(f" - {link}")
            print(f"{Fore.GREEN}[*] Total links discovered: {len(self.visited)}{Style.RESET_ALL}")

        except KeyboardInterrupt:
            print(f"{Fore.RED}Closed by user{Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description="URL enumeration tool")
    parser.add_argument("target", nargs='?', help="Target hostname")
    parser.add_argument("-u", "--urlfile", type=str, help="Path to the file containing URLs")
    
    args = parser.parse_args()
    if (args.target is None and args.urlfile is None) or (args.target is not None and args.urlfile is not None):
        print(f"{Fore.RED}[!] Please provide either a target URL or a URL file, not both.{Style.RESET_ALL}")
        return

    url_enum = URLEnumeration(base_url=args.target, url_file=args.urlfile)
    url_enum.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Fore.BLUE}[*] Exiting...{Style.RESET_ALL}")
        os._exit(0)
