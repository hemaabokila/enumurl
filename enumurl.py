#!/usr/bin/python3
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
import time
from colorama import Fore, Style
from optparse import OptionParser
def test_url(url):
    parse=urlparse(url)
    return bool(parse.scheme) and bool(parse.netloc)

def intrnal_url(url,url2):
    domain=urlparse(url).netloc
    domain2=urlparse(url2).netloc
    return domain==domain2

def norm_url(url):
    return url.rstrip('/')

def get_links(cur_url,url):
    links=set()
    try:
        response=requests.get(cur_url,timeout=10)
        if response.status_code==200:
            b_suop=BeautifulSoup(response.text,"html.parser")
            for i in b_suop.find_all("a",href=True):
                href=i.get("href")
                full_url=urljoin(cur_url,href)
                normd_url=norm_url(full_url)
                if test_url(normd_url) and intrnal_url(url,normd_url):
                    links.add(normd_url)
            if links:
                print(links)
        return links
    except requests.exceptions.RequestException as erorr:
        print(f"{Fore.RED}Error fetching {cur_url}: {erorr}){Style.RESET_ALL}")
        return  set()
def enum_url(url):
    print(f'''
    {Fore.RED}
     _____ _   _ _   _ __  __ _   _ ____  _     
    | ____| \ | | | | |  \/  | | | |  _ \| |    
    |  _| |  \| | | | | |\/| | | | | |_) | |    
    | |___| |\  | |_| | |  | | |_| |  _ <| |___ 
    |_____|_| \_|\___/|_|  |_|\___/|_| \_\_____|
                                                
    {Style.RESET_ALL}
    ''')
    visited=set()
    to_visit=[(norm_url(url),0)]
    try:
        while to_visit:
            cur_url,depth=to_visit.pop()
            if cur_url not in visited and depth<=2:
                print(cur_url)
                visited.add(cur_url)
                new_link=get_links(cur_url,url)
                for link in  new_link:
                    normd_link=norm_url(link)
                    if normd_link not in visited and normd_link not in [x[0] for x in to_visit]:
                        to_visit.append((link,depth +1))
                time.sleep(1)
    except KeyboardInterrupt:
        print(f"{Fore.RED}Closed {Style.RESET_ALL}")

parser = OptionParser(F"""
{Fore.BLUE}
 _____ _   _ _   _ __  __ _   _ ____  _     
| ____| \ | | | | |  \/  | | | |  _ \| |    
|  _| |  \| | | | | |\/| | | | | |_) | |    
| |___| |\  | |_| | |  | | |_| |  _ <| |___ 
|_____|_| \_|\___/|_|  |_|\___/|_| \_\_____|
                                            
{Style.RESET_ALL}
---------------------------------------------
pscan -u or --url     >>   Target hostname "https://example.com"
---------------------------------------------
Developed by: Ibrahem abo kila
---------------------------------------------
""")
parser.add_option("-u", "--url", dest="url", help="Target hostname")


(options, args) = parser.parse_args()

if not options.url:
    print(parser.usage)
    print(f"{Fore.RED}Please specify a target using -u or --url{Style.RESET_ALL}")
else:
    enum_url(options.url)

    
