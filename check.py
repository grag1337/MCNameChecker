import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from art import *
from os import system, name
from time import sleep
import ctypes
import re
from tqdm import tqdm
from tqdm import tqdm_gui

linecounter = 0
with open("words.txt",'r') as f:
    for line in f:
        linecounter = linecounter + 1



def clear():
    if name == 'nt':
        system('cls')

    else:
        system('clear')

wordappend = open("available.txt", "a")
words = open("words.txt", "r")
url = "https://namemc.com/search?q="
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
counter = 0
availablele = 0
availablesoon = 0
myCoolTitle = "[+] STARTING | COMPLETED " + str(counter) + "/" + str(linecounter) + "|"
ctypes.windll.kernel32.SetConsoleTitleW(myCoolTitle)

pbar = tqdm_gui(total=linecounter)

for line in words:
    try:
        clear()
        counter = counter + 1
        pbar.set_description("Available: " + str(availablele) + " | " + "Available Soon: " + str(availablesoon) + " |")
        pbar.update(+1)
        myCoolTitle = "RUNNING | COMPLETED " + str(counter) + \
                    "/" + str(linecounter) + " | " + "Available: " + str(availablele) + \
                    " | " + "Available Soon: " + str(availablesoon) + " |"
        ctypes.windll.kernel32.SetConsoleTitleW(myCoolTitle)
        sleep(2)
        url2 = url + line
        req = Request(url2, headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, "html.parser")
        soup2 = str(soup)
        if "Unavailable" in soup2:
            print("[+]" + str(line) + " is unavailable")
            clear()
        elif "Available Later" in soup2:
            availablesoon = availablesoon + 1
            print("[+]" + line + " is available later!!!")
            availabledate = soup.find("meta", {"name": "og:description"})
            cumsock = str(availabledate)
            cumsock2 = cumsock.split("t=\"")[1]
            wordappend.write("\n [+]"+ line + " Is available later " + cumsock2.split("Z,")[0])
            clear()
            continue
        elif "Available" in soup2:
            availablele = availablele + 1
            print("[+]" + line + " is available!!!")
            wordappend.write("\n [+]" + line + " Is available!")    
            clear()
            continue

    except KeyboardInterrupt:
        clear()
        print("Exiting...")
        sleep(2)
        quit
    except:
        clear()
        print("error " + str(IOError))
        print("Requesting too frequently, waiting 60 seconds.")
        pbar.set_description("[+] SLEEPING FOR 60 SECONDS")
        sleep(60)
        continue

pbar.close()
words.close()
wordappend.close()
